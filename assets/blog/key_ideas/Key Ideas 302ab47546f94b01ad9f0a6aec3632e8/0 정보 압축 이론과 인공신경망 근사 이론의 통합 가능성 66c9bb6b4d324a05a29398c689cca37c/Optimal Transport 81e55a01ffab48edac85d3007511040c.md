# Optimal Transport

From now on, let $X$ be a Polish space, i.e., a completely metrizable and separable topological space. Honestly, I find it cumbersome to restate what $X$ represents in every definition or theorem. Since assuming $X$ is [Polish](https://en.wikipedia.org/wiki/Polish_space) should not cause any issues, I will maintain this assumption throughout the text.

- Review (Mathematics)
    
    **Definition**
    
    > A function $f:X \to \mathbb{R}$ is said to be **lower semi-continuous** (lsc) if for every $x_0 \in X$, we have:
    > 
    > 
    > $\liminf_{x \to x_0} f(x) \geq f(x_0).$
    > 
    > Equivalently, If is lower semi-continuous if for every $\alpha \in \mathbb{R}$, the **sublevel set**
    > 
    > $\{ x \in X \mid f(x) \leq \alpha \}$
    > 
    > is a closed set in $X$.
    > 
    
    An **important example** of a **lower semi-continuous (lsc) function** is the **cumulative distribution function (CDF) of a random variable**.
    
    물론, upper semi continuous도 같은 방식으로 정의할 수 있음. 
    
    **Example**
    
    ![image.png](Optimal%20Transport%2081e55a01ffab48edac85d3007511040c/image.png)
    
    **Theorem: Minimum Attainment for LSC Functions**  
    
    > If $f: X \to \mathbb{R}$ is **lower semi-continuous** and $X$ is **compact (and polish)**, then it **attains its minimum**, i.e., there exists some $x^* \in X$  such that:
    > 
    > 
    > $f(x^*) = \min_{x \in X} f(x).$
    > 
    
    This is similar to the **Weierstrass extreme value theorem**, which states that a **continuous real function** attains both its **minimum** and **maximum** on a compact domain. However, for lower semi-continuous functions, we **only** guarantee the **existence of a minimum**, not necessarily a maximum.
    
    **If I do not mention compactness, the function may not necessarily attain its minimum.**
    
    - Proof sketch
        1. **Define a Minimizing Sequence**
            - Let $m = \inf_{x \in X} f(x).$
            - Take a sequence $(x_n)$ such that
                
                $m \le f(x_n) < m + \frac{1}{n}$   
                
        2. **Use [Compactness via Sequential Compactness](https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem)**
            - Since a **compact metric space is sequentially compact**, the sequence $(x_n)$ has a **convergent subsequence**  $x_{n_k} \to x^*$ for some  $x^* \in X .$
        3. **Apply Lower Semi-Continuity**
            - First you should check that
            
            $m=\liminf_{k} f(x_{n_k})$ and apply the definition of lower semi continuouity.