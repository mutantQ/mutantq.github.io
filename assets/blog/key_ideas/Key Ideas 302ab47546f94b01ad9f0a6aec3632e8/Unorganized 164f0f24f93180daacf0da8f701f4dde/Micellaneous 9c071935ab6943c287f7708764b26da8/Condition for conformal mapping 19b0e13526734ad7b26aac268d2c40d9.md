# Condition for conformal mapping

$$
\begin{aligned}&\text{If }\;\;\mathbf{F}(\mathbf{r})=\sum_{i=1}^nF_i(\mathbf{r})\mathbf{e}_i \\&\text{and }\braket{\nabla F_i(\mathbf{r})|\nabla F_j(\mathbf{r})}=f(\mathbf{r})\delta_{ij} \\&\text{for some} \;f:\R^n \rightarrow \R \text{ such that } f(\mathbf{r})\ne0\text{ for all }\mathbf{r} \in \R^n, \\& \text{is }\mathbf{F}:\R^n\rightarrow\R^n \text{ conformal?}\end{aligned}
$$

Let $n=2$, and define the set $\mathcal{C}$ as the following:

$$
\mathcal{C}=\{t\mathbf{e}_1+t^2\mathbf{e}_2\,|\,t \in \R\}
$$

 Then, define $F_1$ and $F_2$ as follows:

$$
\begin{aligned}F_1(\mathbf{r})&= \begin{cases}
          \braket{\mathbf{e}_1|\mathbf{r}}  &\text{if} \; \mathbf{r} \notin \mathcal{C} \\0&\text{if} \; \mathbf{r} \in \mathcal{C}\end{cases}\\ F_2(\mathbf{r})&=   \braket{\mathbf{e}_2|\mathbf{r}}  \end{aligned}
$$

$\braket{\nabla F_i(\mathbf{r})|\nabla F_j(\mathbf{r})}=1 \cdot\delta_{ij}$, since $\nabla F_i(\mathbf{r})=\mathbf{e}_i$. However, $F$ is not conformal, since at the point $\mathbf{0}$ the angle between the curve $\mathcal{C}$ and the y-axis is not preserved.