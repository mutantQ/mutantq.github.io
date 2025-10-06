# Weakly equivariant neural networks

### Introduction

How many degrees of freedom do we need to train a neural network? [Li et. al.](https://arxiv.org/pdf/1804.08838) introduced Random Subspace Training as a method for measuring the intrinsic dimension of objective landscapes. Leveraging tools from Random Matrix Theory (most notably, Gordon's Escape Theorem), [Larsen et. al.](https://arxiv.org/pdf/2107.05802) attempted to explain the sharp phase transition in the success probability of hitting a loss sub-level set during random subspace training.

Much earlier than that came the Convolution Neural Network (CNN). It is known that CNNs leverage translational equivariance in data structures. This notion of equivariance has been generalized to arbitrary group transformations, including the rotation group $SO(n)$, symmetric group $S_n$, and so on. These layers that satisfy the group equivariance property may be represented as Group Convolutional Neural Networks (G-CNNs).

Larsen et. al. compared the learning success probability between three cases of Random Subspace Training: using (a) the random affine subspace (b) the burn-in subspace or (c) the lottery subspace. For (b) specifically, they trained the neural network using two distinct phases:

- **Phase I** trains the weights on the full parameter space.
- **Phase II** trains the weights on the random subspace.

Since it is known that a linear layer that satisfies some equivariance constraint lies on a **subspace** of the original space of weights, can we leverage this fact to prove some generalization bound for equivariant weights? Also, one downside of the Random Subspace Training method is that it does not serve as a practical method for reducing training compute. On the other hand, G-CNNs have been empirically proven to provide a good inductive bias, most notably in vision tasks. The question is then: can we get the best of both worlds?

### The Linear Subspace of Equivariant Weights

Let $W \in \R^{m\times n}$ be a weight matrix and omit biases for the sake of simplification. For some group $G$, define a representation $\rho: G \rightarrow GL(\R^{m\times n})$ as:

$$
\rho(g)(W)=K_gWL_g^{-1}
$$

Where $K: G \rightarrow GL(\R^n)$ and $L: G \rightarrow GL(\R^m)$ are representations of the input space and the output space, respectively. We can prove that $\rho$ is a homomorphism:

$$
\begin{aligned}
\rho(g_1 g_2)&=K_{g_1 g_2} W L_{g_1 g_2}^{-1} \\
&= K_{g_1}K_{g_2} W L_{g_2}^{-1}L_{g_1}^{-1}\\
&= K_{g_1}(K_{g_2} W L_{g_2}^{-1})L_{g_1}^{-1}\\
&= \rho(g_1) \circ \rho(g_2)
\end{aligned}
$$

We can also show $\rho(g) \in GL(\R^{m\times n})\;\forall g \in G$, by proving that it is both (a) linear and (b) injective (hence bijective). For finite groups, Van der Pol et. al. constructed the symmetrizer $S(W)$ as the following average;

$$
S(W)=\frac{1}{|G|}\sum_{g\in G}\rho(g)(W)=\frac{1}{|G|}\sum_{g\in G}K_gWL_g^{-1}
$$

and has proven some of its properties. Defining $\mathcal{W}:=\{W\in \R^{m\times n}: WL_g=K_g W,\; \forall g\in G\}$ as the set of equivariant weights, the following holds:

$$
\begin{aligned} \text{The symmetric propety}&: S(W)L_g=K_gS(W) \\ 
\text{The fixing property}&: W \in \mathcal{W} \rightarrow S(W)=W \\ \text{The idempotence property}&:S(S(W))=S(W),\;\forall W\in \R^{m\times n} \end{aligned}
$$

**Most importantly, $\mathcal{W}$ forms a subspace of the original space of weights $\R^{m\times n}$.** 

### Multi-Phase Symmetric Learning

Imagine a symmetric learning algorithm consisting of two phases, Phase I and Phase II:

- **Phase I** trains the weights on the equivariant subspace $\mathcal{W}$.
- **Phase II** trains the weights on either one of the following spaces:
    1. The full parameter space $\R^{m\times n}$, or
    2. A random subspace $\{A\theta + w_t: \theta \in \R^d\}$ obtained by pruning some overparametrized weight that need not be equivariant.

The fact that it consists of two phases is similar, in a sense, to the Burn-in Random Subspace Training. Since equivariance is a good inductive bias, **but only upto the point where the constraint hinders further learning**, the resulting combination of the two training phases may be superior: it only makes use of the equivariance during the beginning, while the resulting neural network is not constrained to exact equivariance.

The following diagram summarizes the discussion:

![1000000291.jpg](Weakly%20equivariant%20neural%20networks%20198f0f24f93180ae93d9d4be37fff35f/1000000291.jpg)

### Implementation Idea: Incorporating Positional Encodings

The self-attention mechanism is permutation invariant to the position of the tokens. Therefore, the transformer architecture would not have been able to comprehend the token’s positional information if it weren't for the sinusoidal positional encoding. The question is then: Can this assumption be extended to other symmetry groups? For example, we might attempt to encode rotations with a quaternion and provide it as input to a rotationally invariant neural network.

In fact, the idea of positional encoding has already been studied through the lens of group representation theory. [Derek Lim et. al.](https://openreview.net/pdf?id=18f4nhMJ33) proposed a framework to view a positional encoding $\gamma: \mathcal{X} \rightarrow \R^d$ as a group representation $\rho: G \rightarrow \text{GL}(V)$, by representing existing instances of positional encoding in the form $\gamma(x)=\textrm{vec}(\rho(x))$. They prove that the transformer architecture exhibit translational equivariance provided that the weights are of the form $W_V = b_1 I, W_K = b_2 I, W_Q = b_3 I$ for some $b_1, b_2,b_3 \in \R$. The author hence describes transformers as being “equivariantly biased”.

Therefore, we propose restricting weights to diagonal matrices during **phase I**. We believe this approach - achieving approximate equivariance using positional encodings - has three potential advantages over existing methods:

1.  **Computational efficiency.** We can leverage parameter efficient equivariant neural networks to non-equivariant problems. In fact, the transformer architecture is already an example of this - Although the positional encoding breaks the permutation invariance of the self-attention mechanism, the increase in the required training cost is negligible (or minimal, at most).
2. **Flexibility to Symmetry Breaking.** Existing group equivariant deep learning methods tend to suffer performance loss whenever symmetry is broken. There are many instances of such symmetry breaking - to give one such example, in a hydrogen atom, rotational symmetry may be broken by the exertion of magnetic or electric field. Approximate invariance & equivariance, achieved using group representation positional encoding, will allow the neural network to explore parameters that lie outside of the equivariant parameter subspace.
3. **Flexibility in the Choice of Symmetry.** According to Derek Lim et. al., most existing positional encodings can be viewed as group representions. For example, the sinusoidal positional encoding $\gamma(x)=\text{vec}(e^{i\alpha x})$ is used in the original transformer architecture. Conversely, by choosing a different group irrep $\rho$ instead of $e^{i\alpha x}$, one can choose the desired inductive bias freely.
4. **Generalization Capabilities.** If you are to perform different but related tasks, what would the optimal construction and training method of the model be? There are many tasks which exhibit the same or similar symmetry, and we may consider these tasks as, in a sense, “relevant”. Soft / approximate symmetry may enable enhanced generalization between these relevant tasks. For example, sipping coffee and watering a plant both involves "grabbing and moving an object,” which may share the same underlying roto-translational symmetry $\text{SE}(3)$.