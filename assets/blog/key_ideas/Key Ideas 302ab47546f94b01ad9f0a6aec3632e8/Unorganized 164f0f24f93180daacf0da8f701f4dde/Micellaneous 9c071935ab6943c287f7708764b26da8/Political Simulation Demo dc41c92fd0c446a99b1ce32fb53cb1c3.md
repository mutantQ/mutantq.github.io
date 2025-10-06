# Political Simulation Demo

Let’s say there are three countries, $0, 1,2$. These countries will receive **initial rewards** $r_0,\:r_1,\:r_2$ at each time step. The reward $r_0$ is centered around $1$, and the rewards $r_1$ and $r_2$ is centered around $0$. Therefore, country $0$ is rewarded with reward $1$ **on average,** and country $1$ and $2$ is rewarded nothing **on average**.

However, when two countries become **‘friends’,** they can benefit each other. Two countries can become friends by increasing the **affinity** (=closeness) between them - if one country sends an **invitation** to another country, and the receiving country accepts the invitation, the affinity is increased by $\delta =0.05$. The affinity between countries starts from $0$ and never decreases, and is accumulated until it reaches the maximum affinity of $1$.

For example, let’s say that the affinity between countries $0$ and $1$ has increased by $\delta =0.05$, once. Then the **final rewards** $R_0,\:R_1,\:R_2$ that each country gets would become:

$$
\begin{aligned} R_0&=\bold{1.00}\,r_0+\bold{0.10}\,r_1+0.05\,r_2 \\ R_1&=\bold{0.10}\,r_0+\bold{1.00}\,r_1+0.00\,r_2 \\ R_2&=0.05\,r_0+0.00\,r_1+\bold{1.00}\,r_2 \end{aligned}
$$

We will call the above mechanism reward sharing. A more precise description can be found below:

$$
R_i = \sum_{j=0}^{N-1} a_{ij}r_j
$$

$N$: number of countries.
$a_{ij}$: Affinity between countries $i$ and $j$, where $a_{ii}=1$ for all $i \in \{0, \cdots,N-1\}$.
$r_k$: initial reward of country $k$.
$R_k$: final reward of country $k$ (after reward sharing).