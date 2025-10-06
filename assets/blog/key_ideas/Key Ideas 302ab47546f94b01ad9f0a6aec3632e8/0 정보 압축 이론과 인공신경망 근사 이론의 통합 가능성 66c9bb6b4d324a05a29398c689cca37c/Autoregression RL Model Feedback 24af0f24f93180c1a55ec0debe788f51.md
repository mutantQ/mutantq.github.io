# Autoregression RL Model Feedback

- I was a bit confused with the notation at first, but now that I’m used to it I really like the notation.
    - $h_t$ used for history/hidden state, right? Though you haven’t mentioned I think it could mean both ways, and that’s a good thing.
    - However, you should **make it clear to the reader that $h_t$ is variable length, unlike the fixed-length vector $h_t$ usually appearing in the RNN formulation.** I was a bit confused at first.
- Great that you’re thinking of extending it to inverse dynamics & model based planning.
    - However, I don’t think we should consider inverse dynamics from the outset because it complicates stuff, especially the codebase.
        - We need to implement a “planner” to make use of this learned, inverse dynamics. Building it is already a lot of work, imo. **How are you going to “generate a sequence of optimal future states” which satisfy the constraint of the environment?**
        - TBH, I’m not used to inverse dynamics learning. I have to study a whole new field if I want to work on it, and even if I do learn it I won’t be as confident.
- About part 3 and onwards, there’s a lot of question marks for me, personally.
    - **You’re not making a clear distinction between 1) the Optimal Q-value function and 2) the Q-value function of your current policy. Plus, your’s won’t work for continuous action spaces well because you don’t keep a policy network.**
        - If you haven’t heard about these two concepts, 
        [DeepMind X UCL | 4. Theoretical Fundamentals of Dynamic Programming](https://www.notion.so/DeepMind-X-UCL-4-Theoretical-Fundamentals-of-Dynamic-Programming-7478da99308c409ebe009bf4f8209c13?pvs=21)
        - As you know, the **Q-value function** $Q^\pi(s,a)$ of a policy $\pi$ is the expected, cumulative, discounted reward, given that you’re starting from state $s$ and right after that taking action $a$. In the original DQN literature, you learn the **optimal** Q-value function directly, or $Q^*(s, a)$, which is the Q-value function of the **optimal policy** $\pi^*$.
        - In general, you approximate the value function to either
            1. **assess the performance of your current policy $\pi_\theta$ to inform the policy iteration procedure how well your learned policy is doing, or**
            2. **directly learn the optimal value function $Q^*$ or $V^*$ by minimizing the Bellman error $||\mathcal{T}^*Q_\phi-Q_\phi||$ or $||\mathcal{T}^*V_\phi-V_\phi||$ to values close to zero, and utilizing the resulting, learned value function as your policy. (=the original DQN paper)**
            - e.g., when the action space $\mathcal{A}$ is finite, you can choose the optimal action $a^*=\pi^*(s)=\argmax_{a\in\mathcal{A}} Q^*(s, a)$ and that automatically becomes your optimal policy of your MDP.
        - In 5., you mention **Augmented Value Estimation:** $Q(h_t, a_t) \leftarrow Q(h_t, a_t) + \alpha (r_t + \gamma \max_{a'} Q(h_{t+1}, a') - Q(h_t, a_t))$
            - You’re implying **case 2. directly learn the optimal value function $Q^*$ or $V^*$** here, because you’re using the Bellman Optimality Operator for Q-value functions. So you want something like DQN.
        - The problem is, this approach does not generalize well for infinite action spaces - how are you going to do the $\max$ operation if there are infinite number of actions you can choose amongst?
        - This is why we keep a separate policy(=actor) network $\pi_\theta$, in most cases.
            - even if people use the term “Q-learning” in their paper, you’ll realize they’re mostly Actor-Critic algorithms if you look closely enough.
            - I guess people use the naming because DQN is famous and they want people come up as related, although it’s completely different…