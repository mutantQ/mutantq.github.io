#!/usr/bin/env python3
r"""
Script to export Jekyll-compatible LaTeX equations back to standard markdown format.
This is the reverse operation of fix_latex.py.

- Inline equations ($...$): unescape special characters, replace \\\\ with \newline, replace \\: with \:
- Block equations ($$...$$): unwrap align* environments, replace \\ with \newline
- Replace ° (degree symbol) back to \degree
- Idempotent operation

Unescaping rules:
- Unescape: \_, \|, \*, \{, \} back to _, |, *, {, }
- Keep LaTeX command arguments as-is (e.g., \mathcal{D})
"""

import re
import sys
import os
import argparse
from pathlib import Path

def is_latex_command_at(equation, pos):
    """Check if position pos is the start of a LaTeX command (backslash followed by letters)."""
    if pos < 0 or pos >= len(equation) or equation[pos] != '\\':
        return False, 0
    
    i = pos + 1
    while i < len(equation) and equation[i].isalpha():
        i += 1
    
    if i > pos + 1:  # Found at least one letter after backslash
        return True, i
    return False, 0

def count_preceding_backslashes(text, pos):
    """Count consecutive backslashes immediately before position pos."""
    count = 0
    i = pos - 1
    while i >= 0 and text[i] == '\\':
        count += 1
        i -= 1
    return count

def unescape_inline(equation):
    """Unescape special characters in inline equations."""
    # First, handle special replacements (idempotent protection)
    equation = equation.replace(r'\\\\', '<<<NEWLINE>>>')
    equation = equation.replace(r'\operatorname{argmax}', r'\argmax')
    equation = equation.replace(r'\operatorname{argmin}', r'\argmin')
    equation = equation.replace('°', r'\degree')
    
    # Handle \\: → \: (idempotent: protect existing \:)
    equation = equation.replace(r'\:', '<<<SINGLE_COLON>>>')
    equation = equation.replace(r'\\:', r'\:')
    equation = equation.replace('<<<SINGLE_COLON>>>', r'\:')
    
    # Parse equation and identify LaTeX command braces
    result = []
    i = 0
    latex_brace_stack = []  # Stack to track which braces belong to LaTeX commands
    
    while i < len(equation):
        char = equation[i]
        
        # Check for LaTeX command
        is_cmd, cmd_end = is_latex_command_at(equation, i)
        if is_cmd:
            # Add the command to result
            result.append(equation[i:cmd_end])
            i = cmd_end
            
            # Skip whitespace
            while i < len(equation) and equation[i] in [' ', '\t']:
                result.append(equation[i])
                i += 1
            
            # If followed by {, mark it as LaTeX command brace
            if i < len(equation) and equation[i] == '{':
                latex_brace_stack.append(len(latex_brace_stack))  # Push marker
                result.append('{')
                i += 1
            continue
        
        # Check for escaped character
        if char == '\\' and i + 1 < len(equation):
            next_char = equation[i + 1]
            
            # Check if this is a LaTeX command (already handled above)
            if next_char.isalpha():
                result.append(char)
                i += 1
                continue
            
            # Unescape special characters (but only if they're not part of LaTeX commands)
            if next_char in ['_', '{', '}', '*', '|']:
                # Check if this brace is part of LaTeX command context
                if next_char in ['{', '}'] and latex_brace_stack:
                    # Keep the backslash for LaTeX command braces? No, remove it
                    pass
                
                # Skip the backslash, append the character
                result.append(next_char)
                i += 2
                
                # Track braces for LaTeX command context
                if next_char == '{':
                    if i > 2 and equation[i-3:i-2] in ['_', '^']:
                        # This was a subscript/superscript brace, don't track
                        pass
                    else:
                        # Check if preceded by a LaTeX command
                        # For now, we'll track all unescaped braces
                        pass
                elif next_char == '}':
                    pass
                
                continue
        
        # Handle braces (tracking for LaTeX commands)
        if char == '{':
            # Check if this opens a LaTeX command argument
            if latex_brace_stack or (i > 0 and result and result[-1].isalpha()):
                latex_brace_stack.append(len(latex_brace_stack))
            result.append('{')
            i += 1
        
        elif char == '}':
            # Check if this closes a LaTeX command brace
            if latex_brace_stack:
                latex_brace_stack.pop()
                result.append('}')
                
                # Check if next non-whitespace char is '{' (multi-argument command)
                j = i + 1
                while j < len(equation) and equation[j] in [' ', '\t']:
                    j += 1
                if j < len(equation) and equation[j] == '{':
                    latex_brace_stack.append(len(latex_brace_stack))
            else:
                result.append('}')
            i += 1
        
        else:
            result.append(char)
            i += 1
    
    # Restore newline (add space to prevent concatenation with next character)
    result_str = ''.join(result)
    result_str = result_str.replace('<<<NEWLINE>>>', r'\newline ')
    
    return result_str

def process_block_equation_export(equation):
    """Process block equations: keep align*/aligned if & is present, otherwise unwrap and replace \\ with \newline."""
    equation = equation.strip()
    
    # Replace degree symbol
    equation = equation.replace('°', r'\degree')
    equation = equation.replace(r'\operatorname{argmax}', r'\argmax')
    equation = equation.replace(r'\operatorname{argmin}', r'\argmin')
    
    # Check if equation uses alignment character (&)
    has_alignment = '&' in equation
    
    # If equation has alignment, keep the align*/aligned environment
    if has_alignment:
        # Keep align* or aligned as-is, just replace \\ with \newline
        equation = equation.replace(r'\\\\', '<<<QUAD_BACKSLASH>>>')
        equation = equation.replace(r'\\', r'\newline ')
        equation = equation.replace('<<<QUAD_BACKSLASH>>>', r'\newline ')
        return equation
    
    # Otherwise, unwrap align* environment if present
    if equation.startswith(r'\begin{align*}') and equation.endswith(r'\end{align*}'):
        # Remove the align* wrapper
        equation = equation[len(r'\begin{align*}'):-(len(r'\end{align*}'))]
        equation = equation.strip()
    
    # Similar for aligned
    if equation.startswith(r'\begin{aligned}') and equation.endswith(r'\end{aligned}'):
        equation = equation[len(r'\begin{aligned}'):-(len(r'\end{aligned}'))]
        equation = equation.strip()
    
    # Replace \\ with \newline (but be careful with \\\\)
    # First protect \\\\ (quad backslash)
    equation = equation.replace(r'\\\\', '<<<QUAD_BACKSLASH>>>')
    # Then replace remaining \\ with \newline (add space to prevent concatenation)
    equation = equation.replace(r'\\', r'\newline ')
    # Restore quad backslash as \newline (since \\\\ was used for line breaks in inline)
    equation = equation.replace('<<<QUAD_BACKSLASH>>>', r'\newline ')
    
    return equation

def remove_html_tags(content):
    """Remove HTML block tags like <aside>, <div>, etc. but keep their content."""
    # Remove common block-level HTML tags
    block_tags = ['aside', 'div', 'section', 'article', 'blockquote', 'details', 'summary']
    
    for tag in block_tags:
        # Remove opening tags with attributes: <tag ...>
        content = re.sub(rf'<{tag}[^>]*>\s*', '', content)
        # Remove closing tags: </tag>
        content = re.sub(rf'</{tag}>\s*', '', content)
    
    return content

def is_in_list_context(content, pos):
    """Check if position is within a list item by looking at indentation pattern."""
    # Find the start of current line
    line_start = pos
    while line_start > 0 and content[line_start - 1] not in ['\n', '\r']:
        line_start -= 1
    
    # Check indentation of current line
    indent = content[line_start:pos]
    if not indent or indent.strip() != '':  # No indentation or has non-whitespace
        return False
    
    # Look back through previous lines to find list marker
    search_pos = line_start - 1
    lines_checked = 0
    max_lines = 20  # Limit search to avoid performance issues
    
    while search_pos >= 0 and lines_checked < max_lines:
        # Find start of previous line
        prev_line_start = search_pos
        while prev_line_start > 0 and content[prev_line_start - 1] not in ['\n', '\r']:
            prev_line_start -= 1
        
        # Get the line content
        line_content = content[prev_line_start:search_pos + 1].lstrip()
        
        # Empty line check
        if not line_content.strip():
            lines_checked += 1
            search_pos = prev_line_start - 1
            continue
        
        # Check for numbered list marker (e.g., "1. ", "2. ")
        if line_content and line_content[0].isdigit():
            match = re.match(r'^\d+\.\s', line_content)
            if match:
                return True
        
        # Check for bullet list marker (e.g., "- ", "* ", "+ ")
        if line_content and line_content[0] in ['-', '*', '+']:
            if len(line_content) > 1 and line_content[1] == ' ':
                return True
        
        # If we found non-empty, non-list content, stop
        if line_content and line_content[0] not in ['-', '*', '+'] and not line_content[0].isdigit():
            break
        
        lines_checked += 1
        search_pos = prev_line_start - 1
    
    return False

def export_latex_equations(content):
    """Export all LaTeX equations from Jekyll format to standard markdown."""
    # First, remove HTML block tags
    content = remove_html_tags(content)
    
    result = []
    i = 0
    
    while i < len(content):
        # Check for block equation ($$)
        if i < len(content) - 1 and content[i:i+2] == '$$':
            # Detect indentation of opening $$
            line_start = i
            while line_start > 0 and content[line_start - 1] not in ['\n', '\r']:
                line_start -= 1
            indent = content[line_start:i]
            
            # Check if we're in a list context
            in_list = is_in_list_context(content, i)
            
            # Only remove indentation if not in a list
            if not in_list and indent and indent.strip() == '':
                for _ in range(len(indent)):
                    if result and result[-1] in [' ', '\t']:
                        result.pop()
            
            j = i + 2
            while j < len(content) - 1:
                if content[j:j+2] == '$$':
                    equation = content[i+2:j]
                    processed = process_block_equation_export(equation)
                    result.append('$$')
                    result.append('\n')
                    
                    # If in list, add indentation to each line of the equation
                    if in_list and indent:
                        # Split equation into lines and add indentation
                        equation_lines = processed.split('\n')
                        for idx, line in enumerate(equation_lines):
                            if idx > 0:
                                result.append('\n')
                            if line.strip():  # Only indent non-empty lines
                                result.append(indent)
                            result.append(line)
                    else:
                        result.append(processed)
                    
                    result.append('\n')
                    # Keep indentation for closing $$ if in list
                    if in_list and indent:
                        result.append(indent)
                    result.append('$$')
                    i = j + 2
                    break
                j += 1
            else:
                result.append(content[i])
                i += 1
        
        # Check for inline equation (single $)
        elif content[i] == '$':
            if (i > 0 and content[i-1] == '$') or (i < len(content) - 1 and content[i+1] == '$'):
                result.append(content[i])
                i += 1
                continue
            
            j = i + 1
            while j < len(content):
                if content[j] == '$':
                    if j < len(content) - 1 and content[j+1] == '$':
                        j += 1
                        continue
                    equation = content[i+1:j]
                    processed = unescape_inline(equation)
                    result.append('$')
                    result.append(processed)
                    result.append('$')
                    i = j + 1
                    break
                j += 1
            else:
                result.append(content[i])
                i += 1
        else:
            result.append(content[i])
            i += 1
    
    return ''.join(result)

def process_file(input_filepath, output_filepath):
    """Process a single markdown file."""
    try:
        with open(input_filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        exported_content = export_latex_equations(content)
        
        # Create output directory if it doesn't exist
        output_filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(exported_content)
        
        print(f"✓ Exported {input_filepath.name} → {output_filepath}")
        return True
    except Exception as e:
        print(f"✗ Error processing {input_filepath}: {e}")
        import traceback
        traceback.print_exc()
        return False

def find_posts_directory():
    """Find the _posts directory relative to script location or current working directory."""
    script_dir = Path(__file__).parent
    
    # Check if script is in _posts directory
    if script_dir.name == '_posts':
        return script_dir
    
    # Check if _posts exists relative to current directory
    cwd_posts = Path.cwd() / '_posts'
    if cwd_posts.exists() and cwd_posts.is_dir():
        return cwd_posts
    
    # Check if _posts exists relative to script directory
    script_posts = script_dir / '_posts'
    if script_posts.exists() and script_posts.is_dir():
        return script_posts
    
    return None

def main():
    parser = argparse.ArgumentParser(
        description='Export Jekyll-compatible LaTeX equations back to standard markdown format.'
    )
    parser.add_argument(
        'files',
        nargs='*',
        help='Markdown file(s) to process'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Process all markdown files in _posts directory'
    )
    
    args = parser.parse_args()
    
    if args.all:
        # Find _posts directory
        posts_dir = find_posts_directory()
        if not posts_dir:
            print("Error: Could not find _posts directory")
            sys.exit(1)
        
        # Create exported_posts directory at same level as _posts
        exported_dir = posts_dir.parent / 'exported_posts'
        
        # Find all .md files in _posts
        md_files = sorted(posts_dir.glob('*.md'))
        if not md_files:
            print(f"No markdown files found in {posts_dir}")
            sys.exit(0)
        
        print(f"Processing {len(md_files)} markdown file(s) from {posts_dir}")
        print(f"Output directory: {exported_dir}")
        success_count = 0
        for filepath in md_files:
            output_path = exported_dir / filepath.name
            if process_file(filepath, output_path):
                success_count += 1
        
        print(f"\nExported {success_count}/{len(md_files)} files successfully")
    
    elif args.files:
        # Find posts and exported directories
        posts_dir = find_posts_directory()
        if not posts_dir:
            print("Error: Could not find _posts directory")
            sys.exit(1)
        
        exported_dir = posts_dir.parent / 'exported_posts'
        
        # Process specified files
        success_count = 0
        for filepath_str in args.files:
            filepath = Path(filepath_str)
            # If relative path, make it relative to posts_dir
            if not filepath.is_absolute():
                if posts_dir.name == '_posts' and filepath.parent.name != '_posts':
                    filepath = posts_dir / filepath.name
                else:
                    filepath = Path(filepath_str)
            
            output_path = exported_dir / filepath.name
            if process_file(filepath, output_path):
                success_count += 1
        
        print(f"\nExported {success_count}/{len(args.files)} files successfully")
    
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()

