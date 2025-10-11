---
layout: post
title: "Information Compression, Neural Networks, and AI for Science: Toward a Unified Theory"
date: 2025-10-11 14:00:00 +0900
description: Exploring the deep connections between information compression theory, neural network approximation, and the future of scientific discovery through AI
tags: artificial-intelligence information-theory neural-networks quantum-computing scientific-discovery compression english
categories: research
toc:
  sidebar: left
lang: en
---

## Introduction

When learning introductory information science, one encounters Huffman coding as the most representative compression algorithm. Huffman coding is a lossless compression technique that minimizes string length without loss of information by eliminating repetition from the string representing the information. In other words, "it achieves the purpose of compression by representing more frequently repeated characters with fewer bits."

Meanwhile, JPEG compression achieves its purpose by removing high-frequency signals through Fourier transformation and eliminating information in areas that humans cannot properly perceive. Therefore, unlike Huffman coding, JPEG compression is a lossy compression technique where information is lost.

It is well known that neural networks with sufficient depth can approximate arbitrary continuous functions. Let's twist this idea slightly. Could the number of weights needed in a neural network to approximate a function within a certain error provide a good foundation for exploring the minimum amount of information needed to represent that function?

One of the key concepts in linear algebra—the one-to-one correspondence between matrices and linear transformations—reveals that all linear functions are merely arrangements of numbers on a grid. If this fact could be extended to nonlinear functions, that is, if nonlinear functions are also nothing more than arrangements of numbers, there is ample room to apply information compression theory to neural network approximation theory. Furthermore, we cannot exclude the possibility that these two fields could be unified under the shadow of a grand theory.

## The Concept of condensed expression

One of the main functions of intelligence, as I define here, is the generation of condensed expressions. We experience various phenomena occurring in the world directly, but we can also indirectly experience the world through condensed expressions that represent it—such as sentences, images, and videos. Moreover, humans have the ability to generate and share condensed expressions based on their direct experiences.

The generation of condensed expressions is closely connected with pattern discovery. In particular, patterns that commonly appear and are repeated multiple times are commonly subject to condensation. For example, in Huffman Coding, the basic principle behind creating compressed files like .zip, the goal of condensation (compression, in this case) is achieved by representing more frequently repeated characters with fewer bits (binary numbers of 0 or 1). Just as it is more efficient to say "repeat a 20 times" rather than typing "aaaaaaaaaaaaaaaaaaaa" to someone, the removal of repetition is undoubtedly the most essential element in generating condensed expressions.

### Shared Knowledge and Communication

We can also eliminate repetition between 'you' and 'me'. When communicating with condensed expressions, we can omit information that the other person and I already share. This is the fundamental principle that allows humans to transmit vast amounts of information with sentences of limited word count. Therefore, to convey information to someone, it is desirable to generate condensed expressions by distinguishing between what the other person and I share and what we do not share. The reason communication is difficult between two people with different temporal and cultural contexts, and the reason why shared knowledge among team members directly translates into comprehensive performance in sports, are all related to the use of condensed expressions.

### Context-Dependent Information

Additionally, "unimportant" information can be omitted. Information that is not useful in context should be omitted for efficient communication. For a waiter working in a restaurant, the contextually important information is the type and quantity of menu items ordered at each table, so unlike in general situations, the customer omits their name (which is usually important) and only mentions the menu they want to order. As another example, in .jpg format compressed image files we use daily, information at high frequencies that cannot be properly distinguished by the human eye is removed to achieve a compression ratio of approximately 10:1. This too is possible because information that does not need to be conveyed in the context of human visual perception is boldly omitted.

### Representation of Reality

Finally, we represent the world through condensed expressions. The universe is very complex, and our brains cannot simulate all of it. Therefore, from the perspective of survival, we need to express and store only the most important information as condensed expressions. From an evolutionary perspective, self-consciousness is presumed to have developed through the process of organisms craving food, and particularly the ability to effectively represent and remember the world helps us imagine and seek out prey that is outside our detection range (i.e., cannot be seen). Furthermore, humans not only represent the world in an effective way but also share condensed information in the form of language with those similar to themselves, thereby achieving common goals.

## The Connection to Neural Network Theory

Examples of diagonalization and SVD (Singular Value Decomposition) correspond well to examples of lossless compression and lossy compression, respectively. In the sense that a matrix diagonalized by finding an appropriate basis completely represents the linear transformation only with the components of a diagonal matrix, and that a similar linear transformation can be made approximately by omitting singular values of small magnitude, approximation using diagonalization and SVD are similar to the concepts of lossless compression and lossy compression, respectively.

SVD makes most terms zero through basis transformation and even arranges the bases in order of importance. This makes us imagine something that is an extension of SVD into a nonlinear version. If we define information compression as finding an appropriate "nonlinear basis," might neural networks already be performing that role?

### Research Directions in Information Compression Theory

Research applying the perspective of information compression to linear algebra should precede. Drawing ideas from rate-distortion theory, for a matrix $X$ sampled from a distribution $\mathcal{D}$ and $\tilde{X}$ a list of nonzero singular values calculated from $X$ (which have been subsequently quantized via storing in low resolution floating point number representations, e.g., float16):

$$
\begin{aligned}
&\underset{p(\tilde{x}|x)}{\text{minimize}}\;I(X;\tilde{X})\\
&\text{subject to} \; \left< d(x,\tilde{x}) \right>_{p(x,\tilde{x})}\le D
\end{aligned}
$$

The problem is that $p(\tilde{x}\|x)$ is deterministic for the case of SVD. What if we can allow for some randomness when applying SVD, so that we can further compress the representation? Note that $I(X; \tilde{X})=H(\tilde{X})-H(\tilde{X}\|X)$ and that $H(\tilde{X}\|X)=0$ when $\tilde{X}$ is deterministic given $X$. So we're basically left with the minimization of $H(\tilde{X})$.

### Optimal Basis for Task Distributions

If you are to perform different but related tasks, how would you construct and train your model? By related, I mean that there are similarities for some parts in the task, just as if sipping coffee and watering a plant both involve "grabbing."

Given a distribution of tasks $\mathcal{D}$, where each sampled task $F \sim \mathcal{D}$ is a Lebesgue-integrable function from $\mathbb{R}^n$ to $\mathbb{R}^m$, and given the norm $\|\cdot\|$ defined by the inner product $\left<f,g\right>=\int\_\{\mathbb{R}^n\}w(\mathbf{x})\{f(\mathbf{x})\cdot g(\mathbf{x})\} d\mathbf{x}$, what is the most efficient parametrized basis $\mathcal{B}\_\theta = \{f\_1(\theta), f\_2(\theta), \cdots,f\_d(\theta) \}$, i.e.,

$$
\begin{align*}
\underset{\theta \in \mathbb{R}^p} {\textrm{minimize}} \;\;\mathbb{E}_{F \sim \mathcal{D}} \left[ \left\| \sum_{i=1}^dC_i(\theta)f_i(\theta) - F \right\|^2 \right]
\end{align*}
$$

where $C\_i(\theta):=\left<f\_i(\theta), F\right>$.

### Connections to Perturbation Theory

We use the original eigenstates of the Hamiltonian, even after the perturbation. **Why not make corrections to the basis state itself?**

Why do you have to use the original energy eigenstates to approximate the perturbed state? Is it actually a good basis, in the sense of minimizing the amount of data needed to describe the full system?

What if the reason we need to solve the Schrödinger equation is actually because language has not developed sufficiently? There might be a mathematical language where the basis is naturally found from information about the potential. The language of computers is remarkably rich. Therefore, the attempt to simulate—that is, to analyze in the language of computers—is quite reasonable.

When we see the symbol $\ket{\psi}$, we automatically associate the linear algebraic structure contained within it (Hilbert space, linearity, commutative law, ...), but actually, looking at the symbol itself, it carries no information. When a complex but ordered pattern repeats, replacing it with the same symbol makes the notation easier to understand and simpler. What would we need to do to create an artificial intelligence model that can introduce new notation as needed?

Physics formulas are a way of expression used by people to implicitly describe patterns of natural phenomena (obtained from observational data). However, while this thing called a formula may seem to contain a great deal of information, in reality, the amount of information actually contained is very small because it assumes the reader's background knowledge. For example, when seeing the formula $\mathbf{F}=m\mathbf{a}$, if you don't know the meaning of the equals sign, you won't know that the left side and right side are the same, and if you don't know that $\mathbf{F}$ means force, $m$ means mass, and $\mathbf{a}$ means acceleration—that is, the second derivative of position with respect to time—it's all for naught. In other words, specific information about the formula is stored in the human brain, and **the reality of the formula is merely the first spark to retrieve information stored in the brain.** The system of knowledge created by humans ultimately represents nothing more than the connection relationships between different vectors.

## AI for Science: The Revolution of Simulation

### The Economics of Experimentation

Trial and error inherently involves pain. While some people enjoy this pain, continued repetitive work is generally only a source of fatigue. Laboratory work where people manually transfer solutions with pipettes, observe, and record results is extremely expensive considering labor costs. Even when automated with robots for High Throughput Screening (HTS), the cost ranges from a few tens of cents to as much as one dollar per pipetting action.

The total budget invested in gravitational wave experiments, the enormous budget invested in CERN's super-large particle accelerator—in these large experimental facilities, the situation where additional huge amounts are incurred because initial setting errors were not caught due to the absence of simulation is dizzying just to imagine. However, thanks to the dramatic development of computing, researchers have been able to conduct experiments without directly interacting with the physical world, which has brought tremendous cost savings—as if everyone gained the ability to conduct thought experiments like Einstein.

### Beyond Cost Savings

To summarize the preceding story, computing is cheap and convenient while real-world experiments are expensive and tiring, and this is why simulation-based research has been activated since the 2000s. However, expecting simulation to merely reduce the trial and error and labor of experiments is extremely shortsighted. 

Empowered by improvements in parallel computing performance and developments in neural network theory, scientists have become able to solve differential equations that could not possibly be calculated in time, and have even reached the stage of autonomously exploring new circuit designs and proposing optimal circuit structures. Now artificial intelligence has reached the stage where it directly reasons in simulations, establishes theories, and formulates them, and groups that actively utilize this to conduct research are likely to gain the upper hand. Indeed, an era of new automation has opened where research is also conducted with artificial intelligence.

### Quantifying Knowledge

How can we quantify the total amount of knowledge about a certain topic?

Consider an AI chemist example: If there were an AI chemist conducting various experiments in a state connected with experimental equipment, it should conduct experiments in the direction that maximizes Knowledge most quickly. That is the essential role of a "chemist."

How do people know that they don't know something? What makes them pursue new knowledge? Where does the sense of KNOWLEDGE come from? Can you make that into a loss function?

### Cloning vs. Simulation

Quantum computers "clone" a system. There exists a direct one-to-one correspondence of all physical properties between the original system and the cloned system. Neural networks "approximate" a system. They do not fully capture the physics of the original system, but describe the system accurately to a certain extent—this is what it means to "simulate."

### Collaborative Learning

Can inducing collaboration between agents yield better quality results with the same resources? Imagine a learning model like a group of researchers who write equations on a blackboard, playing a modeling game while reinforcement learning, growing while communicating.

## AI for Quantum Mechanics

### Can Machines Discover the Schrödinger Equation?

**On Observation, Pattern Finding, and Formulation**

In my sophomore year, curious about quantum mechanics, I took the advanced course "Applications of Quantum Mechanics" one year early. From the first class, the professor expressed the opinion that even machine learning could not discover the Schrödinger equation, the first law of quantum mechanics. This question greatly attracted me—what exactly is quantum mechanics that even artificial intelligence cannot grasp its principles?

To define "discovering the Schrödinger equation" more specifically means "discovering patterns of quantum wave phenomena from experimental data and presenting them in a form that can communicate with other physicists." If machines could perform such work, it would be sufficient to recognize it as "formula discovery." Can artificial intelligence discover the Schrödinger equation from data?

### Symbolic Regression

The most representative example of a methodology where machines autonomously establish formulas and verify them with data is symbolic regression. Symbolic regression deals with methodology where machines autonomously generate equations to fit given experimental data. It was initiated by economist John Koza in the early 1990s and became formalized in the 2000s. Initially, solutions using genetic algorithms were mainstream, but with the recent development of deep learning, deep neural network-based algorithms such as AIFeynman have begun to appear.

For example, suppose we want to "rediscover" Newton's second law $\mathbf{F}=m\mathbf{a}$ from experimental data, but we don't know that the equation we're looking for is $\mathbf{F}=m\mathbf{a}$. Can machines, like Newton, discover natural laws on their own? For convenience, let's assume that the force $\mathbf{F}$ applied to an object and position $\mathbf{x}$ are given as functions of time, and the object's mass $m$ is also given. If an appropriate algorithm operates on the given variables and functions to derive a quantity that doesn't change—that is, an invariant—we can say we have found a "law." For example, if we figured out that $\mathbf{F}-md^2\mathbf{x}/dt^2=\mathbf{0}$ always holds, we can interpret this as having discovered the force-acceleration law.

Therefore, symbolic regression can be thought of as minimizing the following loss function:

$$
\mathcal{L}(f_\text{expr}):=\|f_\text{expr}( \mathbf{F},\mathbf{x}, m)\|^2
$$

When $\mathcal{F} := \{ \mathbf{v}: [t\_i, t\_f] \rightarrow \mathbb{R}^3 \}$, $\mathbf{F},\mathbf{x}\in\mathcal{F}$ are functions of time $t\in [t\_i,t\_f]$ and can be differentiated as much as desired, and $f\_\{\text{expr}\}:\mathcal{F}\times\mathcal{F}\times\mathbb{R}^+ \rightarrow \mathcal{F}$ is a well-formed expression made using operators we know such as addition, multiplication, and differentiation.

### Complexity and Overfitting

If experimental data is fitted with an overly complex equation, measurement errors will be reflected in the equation, so to prevent overfitting, $f\_\text{expr}$ should be 'simple'. Here we obtain several points to consider:

1. What methods exist for measuring the complexity of equations?
2. What methods exist for structurally incorporating the concept of well-formed expressions into deep neural networks?
   - Can a good large language model be constrained to generate only equations that "make sense mathematically"?
3. Does there exist an appropriate embedding that embodies the meaning of equations? If so, how should it be learned?

By answering questions like these, we can open new possibilities for developing artificial intelligence that establishes hypotheses (well-formed expressions) and autonomously verifies them with data.

### Quantum Computers as AI 'Playgrounds'

Just as humans revealed quantum mechanics through experiments, if we provide quantum computers as 'playgrounds' for artificial intelligence, very interesting discoveries will emerge. Having artificial intelligence spontaneously comprehend quantum phenomena with little experimental data is like trying to make people completely understand quantum mechanics with just a few cases. If humans could not interact with and experiment in their surrounding environment, humans might never have known about quantum phenomena. Therefore, a device that can freely experiment with quantum phenomena at high speed—that is, a quantum computer—will be a very attractive auxiliary device for artificial intelligence to understand quantum mechanics.

At least so far, quantum mechanical phenomena do not appear to play an important role in the human brain. Meanwhile, AI systems including AlphaFold have already shown excellent performance in predicting and simulating the structure of complex molecules such as proteins without considering quantum phenomena. However, there was the disadvantage of having to use a very good (million-dollar) computer, and there was the limitation that the types of molecules that could be simulated were restricted to proteins.

If symbolic regression can show that machines can autonomously devise core equations like the Schrödinger equation when given a quantum mechanics experimental dataset, it will provide new insights into the relationship between quantum mechanics and intelligence.

### Neural Networks for Quantum Eigenvalue Problems

Let's devise a simple symbolic regression methodology that uses machine learning for quantum computation. First, writing the Schrödinger equation:

$$
\hat{H} \Psi (\mathbf{r}, t) = i\hbar \frac{\partial}{\partial t} \Psi(\mathbf{r}, t)
$$

When the Hamiltonian is invariant with respect to time, we find solutions to the eigenvalue problem $\hat{H}\psi(\mathbf{r})= E\psi(\mathbf{r})$ and multiply by the phase factor $e^\{-iEt/\hbar\}$ to evolve them—game over.

The action of an operator on a wave function can be interpreted as a linear transformation acting on a vector. And the eigenvalue problem can be thought of as finding the axis of symmetry whose direction is invariant before and after applying the transformation. Can we approximate and obtain these "axes of symmetry," i.e., eigenfunctions, with neural networks?

Replace the wave function $\psi:\mathbb{R}^n\rightarrow\mathbb{C}$ satisfying the eigenvalue equation $\hat{H}\psi = E\psi$ with the neural network $\psi\_\theta$. Then the loss function can be expressed as follows for some norm $\|\cdot\|$:

$$
\mathcal{L}(\theta, E)=\|\hat{H}\psi_\theta - E\psi_\theta\|^2
$$

There are still some unresolved problems with the above approach. For example, how do we define the above norm? One possibility is to define the norm of function $f$ as $\|f\|=\sqrt{\mathbb{E}\left[\|f(X)\|^2\right]},\;\;X \sim \mathcal{N}(\mathbf{0}, I\_\{n\times n\})$. However, the wave function $\psi\_\theta$ defined by a neural network is extremely complex, and considerable computational resources are consumed to calculate the expectation value used in the norm.

Additionally, a method has not been prepared for calculating the action of the Hamiltonian on the (neural network-defined) wave function. Suppose we approximate the Hamiltonian again with a neural network. When the dimension of $\theta$ is $N$, we need to newly define an operator $\hat{H}\_\Theta: \mathbb{R}^N \rightarrow \mathbb{R}^N$ defined by a neural network.

We can confirm that computational complexity increases exponentially according to the complexity of the system being simulated. What does this mean? If we utilize artificial intelligence, physics at the level of small molecules can be simulated without much difficulty. However, it does not seem possible to simulate the dynamics of larger quantum systems of ~10,000 level without compromising on accuracy.

### The Paradox of Quantum Computing for AI

If we can sufficiently describe quantum mechanics just by obtaining the simulation function, there is no need to insist on quantum computers. However, paradoxically, the cheapest way to obtain large-scale quantum experimental data is quantum computing. We must explore whether quantum parallelism can provide practically significant help, and if so, how much.

According to what has been revealed so far about neural networks, through training, they can learn patterns and structures embedded in multidimensional data, and can compressively represent revealed information through dimensionality reduction techniques. And it is also quite possible to map information stored as vectors this way into formulas that humans can see by using natural language processing.

The fact that machines cannot discover quantum phenomena on their own seems rather implausible given the speed of AI development, but considering the characteristic of quantum phenomena where computational complexity increases exponentially according to the complexity of the system, the professor's statement may not be so wrong after all.

## Research Questions and Future Directions

### Gordon's Escape Theorem and Dataset Intrinsic Dimension

Our current research direction focuses on Gordon's escape theorem combined with incorporating dataset intrinsic dimension. We need practical estimation algorithms for the dataset's intrinsic dimension (e.g., PCA). **We need to give researchers a tool that can estimate the minimum amount of parameters needed to train for a certain task.**

Gordon's escape theorem states that in high-dimensional spaces, a random subspace of sufficient dimension will "escape" through any mesh of low complexity with high probability. This theorem provides a powerful tool for understanding the behavior of random projections and has important applications in compressed sensing and dimensionality reduction.

### Information Bottleneck and Optimal Transport

The Information Bottleneck Method introduces the bottleneck $\tilde{X}$ to form the Markov chain $X \rightarrow \tilde{X} \rightarrow Y$, and drawing ideas from rate-distortion theory we obtain:

$$
\underset{p(\tilde{x}|x)}{\text{minimize}}\;I(X;\tilde{X})-\beta I(X;Y)
$$

An alternative approach is exploring "optimal transport." If a data measure exists on a manifold, it can be represented by manifold structure, and we can find the optimal transport that moves it. This has significance in that it explicitly incorporates the manifold hypothesis into generalization. However, there is little discussion about predicting neural network parameters.

### Fractal Structures and Compression

Complex structures like the Mandelbrot Set or Bifurcation Diagram are embedded in extremely simple formulas. Can we devise information compression algorithms that borrow such structures? Can we analyze fractal structures or bifurcation diagrams with neural networks to derive insights into chaotic systems? Fractal compression and the collage theorem are worth exploring.

### Connection to Complexity Theory

There are $O(n^2)$ and $O(n\log n)$ algorithms which all perform the same task—sorting. Can we argue that one is a lossless compression of the other, since it uses less computation?

## Conclusion: Toward a Unified Framework

The question originally posed—"Can the integration of information compression theory and neural network approximation theory be achieved?"—reveals itself to be not just a technical question but a profound inquiry into the nature of representation, learning, and scientific discovery itself.

We have seen that:

1. **Compression and intelligence are deeply related**: The generation of condensed expressions, the removal of redundancy, and the efficient encoding of patterns are central to both information theory and intelligence.

2. **Neural networks may be nonlinear basis finders**: Just as SVD finds optimal linear bases for compression, neural networks may be discovering optimal nonlinear bases for representing complex functions.

3. **AI is transforming scientific practice**: The ability to simulate, discover patterns, and even formulate theories autonomously represents a fundamental shift in how science can be conducted.

4. **Quantum mechanics presents unique challenges**: The exponential scaling of quantum systems means that even advanced AI requires quantum computers as "playgrounds" to truly understand quantum phenomena.

In summary, the question originally posed—"Can artificial intelligence discover the Schrödinger equation from data?"—and the broader question "Can the integration of information compression theory and neural network approximation theory be achieved?" lead us to new insights about intelligence, learning, and scientific discovery. With the same question, we conclude this essay: Can artificial intelligence truly understand quantum phenomena? And more broadly, can we develop a unified theory that connects information compression, neural network approximation, and the fundamental laws of nature?

The answers may not only revolutionize AI and science but also deepen our understanding of what it means to know, to understand, and to discover.

## Acknowledgments

This essay synthesizes ideas from ongoing research on information compression theory, neural network approximation, and AI for science. Special thanks to 홍철, 록기, 승환, and other collaborators for discussions on Gordon's escape theorem, information bottleneck, and optimal transport approaches.

## References

Key papers and resources mentioned:
- How many degrees of freedom do we need to train deep networks: a loss landscape perspective (arXiv:2107.05802)
- The information bottleneck method (arXiv:physics/0004057)
- Deep Learning and the Information Bottleneck Principle (arXiv:1503.02406)
- Intrinsic dimension of data representations in deep neural networks (arXiv:1905.12784)
- Gordon's escape theorem and related work on high-dimensional geometry
- Symbolic regression literature including AIFeynman
- Generalization bounds for deep learning (arXiv:2012.04115)

