#!/usr/bin/env python3
r"""
Script to fix LaTeX equations in markdown files for Jekyll compatibility.
- Inline equations ($...$): escape special characters, replace \newline with \\\\, replace \: with \\:
- Block equations ($$...$$): replace \newline with \\, wrap in align* if needed
- Replace \degree with ° (degree symbol) in both inline and block equations
- Idempotent operation

Escaping rules:
- Escape: _, |, *, and {} when used for subscripts/superscripts (e.g., a_{ij} -> a\_\{ij\})
- DON'T escape: ^ (caret) and {} when they're arguments to LaTeX commands (e.g., \mathcal{D})
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

def double_escape_inline(equation):
    """Double escape special characters in inline equations."""
    # First, handle special replacements
    equation = equation.replace(r'\newline', '<<<NEWLINE>>>')
    equation = equation.replace(r'\argmax', r'\operatorname{argmax}')
    equation = equation.replace(r'\argmin', r'\operatorname{argmin}')
    equation = equation.replace(r'\degree', '°')
    
    # Handle \: → \\: (idempotent: protect existing \\:)
    equation = equation.replace(r'\\:', '<<<ESCAPED_COLON>>>')
    equation = equation.replace(r'\:', r'\\:')
    equation = equation.replace('<<<ESCAPED_COLON>>>', r'\\:')
    
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
        
        # Handle special characters
        if char == '{':
            # Check if this opens a LaTeX command argument (we just handled this above)
            # Or if it's a subscript/superscript brace
            # If preceded by _ or ^, it needs escaping
            if i > 0 and equation[i-1] in ['_', '^']:
                # This is a subscript/superscript brace - needs escaping
                num_backslashes = count_preceding_backslashes(equation, i)
                if num_backslashes == 0:
                    result.append('\\')
                result.append('{')
                # Don't push to stack - these braces need their matching } escaped too
            elif latex_brace_stack:
                # We're inside a LaTeX command, check if this is a nested brace
                result.append('{')
                latex_brace_stack.append(len(latex_brace_stack))
            else:
                # Standalone brace - escape it
                num_backslashes = count_preceding_backslashes(equation, i)
                if num_backslashes == 0:
                    result.append('\\')
                result.append('{')
            i += 1
        
        elif char == '}':
            # Check if this closes a LaTeX command brace
            if latex_brace_stack:
                latex_brace_stack.pop()
                result.append('}')
                
                # Check if next non-whitespace char is '{' (multi-argument command like \frac{a}{b})
                # If so, push back to stack to keep the LaTeX command context
                j = i + 1
                while j < len(equation) and equation[j] in [' ', '\t']:
                    j += 1
                if j < len(equation) and equation[j] == '{':
                    # This is another argument to the same command
                    latex_brace_stack.append(len(latex_brace_stack))
            else:
                # This is a subscript/superscript brace or standalone - needs escaping
                num_backslashes = count_preceding_backslashes(equation, i)
                if num_backslashes == 0:
                    result.append('\\')
                result.append('}')
            i += 1
        
        elif char == '_':
            # Escape underscore (single escape: \_)
            num_backslashes = count_preceding_backslashes(equation, i)
            if num_backslashes == 0:
                result.append('\\')
            result.append(char)
            i += 1
        
        elif char == '^':
            # Caret doesn't need escaping, just append
            result.append(char)
            i += 1
        
        elif char == '*':
            # Escape asterisk (single escape: \*)
            num_backslashes = count_preceding_backslashes(equation, i)
            if num_backslashes == 0:
                result.append('\\')
            result.append(char)
            i += 1
        
        elif char == '|':
            # Escape pipe character (single escape: \|)
            num_backslashes = count_preceding_backslashes(equation, i)
            if num_backslashes == 0:
                result.append('\\')
            result.append(char)
            i += 1
        
        else:
            result.append(char)
            i += 1
    
    # Restore newline
    result_str = ''.join(result)
    result_str = result_str.replace('<<<NEWLINE>>>', r'\\\\')
    
    return result_str

def process_block_equation(equation):
    """Process block equations: replace \newline with \\, wrap in align* if needed."""
    equation = equation.strip()
    
    if equation.startswith(r'\begin{align'):
        equation = equation.replace(r'\newline', r'\\')
        equation = equation.replace(r'\degree', '°')
        return equation
    
    equation = equation.replace(r'\newline', r'\\')
    equation = equation.replace(r'\argmax', r'\operatorname{argmax}')
    equation = equation.replace(r'\argmin', r'\operatorname{argmin}')
    equation = equation.replace(r'\degree', '°')
    
    if ('\\\\' in equation or '&' in equation):
        if not (r'\begin{aligned}' in equation or r'\begin{align*}' in equation):
            equation = r'\begin{align*}' + '\n' + equation + '\n' + r'\end{align*}'
    
    return equation

def fix_latex_equations(content):
    """Fix all LaTeX equations in the markdown content."""
    result = []
    i = 0
    
    while i < len(content):
        # Check for block equation ($$)
        if i < len(content) - 1 and content[i:i+2] == '$$':
            j = i + 2
            while j < len(content) - 1:
                if content[j:j+2] == '$$':
                    equation = content[i+2:j]
                    processed = process_block_equation(equation)
                    result.append('$$')
                    result.append('\n')
                    result.append(processed)
                    result.append('\n')
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
                    processed = double_escape_inline(equation)
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

def process_file(filepath):
    """Process a single markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        fixed_content = fix_latex_equations(content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"✓ Fixed LaTeX equations in {filepath}")
        return True
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
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
        description='Fix LaTeX equations in markdown files for Jekyll compatibility.'
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
        
        # Find all .md files in _posts
        md_files = sorted(posts_dir.glob('*.md'))
        if not md_files:
            print(f"No markdown files found in {posts_dir}")
            sys.exit(0)
        
        print(f"Processing {len(md_files)} markdown file(s) in {posts_dir}")
        success_count = 0
        for filepath in md_files:
            if process_file(filepath):
                success_count += 1
        
        print(f"\nProcessed {success_count}/{len(md_files)} files successfully")
    
    elif args.files:
        # Process specified files
        success_count = 0
        for filepath in args.files:
            if process_file(filepath):
                success_count += 1
        
        print(f"\nProcessed {success_count}/{len(args.files)} files successfully")
    
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
