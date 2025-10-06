# Variational AI - Informational Meeting

## Reading material found @variational.ai

[Variational-AI-Generative-AI-Technology.pdf](Variational%20AI%20-%20Informational%20Meeting%204666e85ee90f49d9b61e56abcc78463d/Variational-AI-Generative-AI-Technology.pdf)

## Vocabularies

- ligand
- potency
- ADMET
- excretion
- binding affinity
- protein-ligand intections
- VHTS
- pharmacophore
- conformer
- make-on-demand libraries
- QSAR
- BindingDB
- holo structure

Please note that I’m mostly unfamiliar with the biology/chemistry part

# Questions for todays meeting

- I have 5 questions that lead to the **key question** that I want to ask you today
- Please share opinions for each question
- I would love to hear more about the last question!

## 5-Questions

### Q1. The article is leaving out reinforcement learning - The number of possible configurations in the Game of Go is $10^{170}$ whereas the size of the chemical space is only $10^{60}$ (using only elements $\text{H, C, O, N, S}$ and molecular weight $<500$). It seems plausible to apply RL to navigate the chemical space. Can we combine generative AI with RL?

An article by Pyzer-Knapp et. al.:

Another approach is a **combination of VAE and reinforcement learning (RL)**[61](https://www.nature.com/articles/s41524-022-00765-z#ref-CR61),[62](https://www.nature.com/articles/s41524-022-00765-z#ref-CR62), where drug molecules’ SMILES and target proteins are both encoded on a common latent space. Reinforcement learning explores this space, guided by a model to predict the efficacy of the generated drug to target cancer proteins[61](https://www.nature.com/articles/s41524-022-00765-z#ref-CR61). 

Pyzer-Knapp, E.O., Pitera, J.W., Staar, P.W.J. *et al.* Accelerating materials discovery using artificial intelligence, high performance computing and robotics. *npj Comput Mater* **8**, 84 (2022). https://doi.org/10.1038/s41524-022-00765-z

### Q2. How does the VAE - RL combination work?

An article by Born J. et. al.:

We present a novel framework for molecule generation based on deep generative models and reinforcement learning that, for the first time, enables the generation of molecules while **taking into account the disease context** encoded in the form of gene expression profile (GEP) data (for a graphical illustration see Figure 1A). … The training procedure is split into two stages. In the first stage, the models are trained independently; one VAE is trained on **gene expression data** (in the following called profile VAE or just PVAE) from TCGA (Weinstein et al., 2013), and another VAE (in the following called SMILES VAE or just SVAE) is trained on **bioactive small molecules** from ChEMBL (Bento et al., 2013) (see Figure 1C). As a critic, we use PaccMann, a **multimodal drug sensitivity prediction model** developed and validated in our previous work (Manica et al., 2019; Cadow et al., 2020). In the second stage, the encoder of the profile VAE is combined with the decoder of the molecule VAE and exposed to a joint retraining that is optimized using a **policy gradient** regime with a reward coming from the critic module.

Born J, Manica M, Oskooei A, Cadow J, Markert G, Rodríguez Martínez M. PaccMannRL: De novo generation of hit-like anticancer molecules from transcriptomic data via reinforcement learning. iScience. 2021 Mar 5;24(4):102269. doi: 10.1016/j.isci.2021.102269. PMID: 33851095; PMCID: PMC8022157.

> Basically, what we do is create two VAEs each for generating gene expression & small molecules and use a multimodal critic to evalute the performance & use policy gradient methods to optimize the outputs.
> 

**RL is used in an interesting way**, to tailor the molecules’ performance towards the given GEP (Gene Expression Profile), but it’s not the use in the way I was thinking

### Q3. We should always take into account that neural networks are only as good as the data it is provided with - if the datasets used to train VAEs are biased towards popular structures, we are not fully exploring the chemical space (ChEMBL has 1,576,904 compounds which are manually curated). We should utilize reinforcement learning to generate data in wet-lab environments, and use them to train the generative models. Can we do that?

Supporting evidence from Julien Horwood and Emmanuel Noutahi:

Following advances in generative modeling for domains such as computer vision and natural language processing, there has been **increased interest in applying generative methods to drug discovery**. … these approaches **bias the generation of molecules toward the data distribution over which they were trained**, restricting their ability to discover truly novel compounds. Previous work1,2 has attempted to address these issues by framing molecular design as a Reinforcement Learning (RL) problem3 in which an agent **learns a mapping from a given molecular state to atoms that can be added to the molecule in a stepwise manner.**

… **our framework treats synthesizability as a feature rather than as a constraint.** … the REACTOR framework is **able to efficiently explore synthetically accessible chemical space in a goal-directed manner**, while also providing a theoretically valid synthetic route for each generated compound.

Julien Horwood and Emmanuel Noutahi, Molecular Design in Synthetically Accessible Chemical Space via Deep Reinforcement Learning, ACS Omega **2020** *5* (51), 32984-32994 DOI: 10.1021/acsomega.0c04153

### Q4. What would be the action space & state space if we were to directly apply RL to lab environments, and its how should we reward the agent?

- 3.2.1.1. State Space $S=\{f(m) | m ∈ M\}$  with $f$ being a **feature extraction function** and $M$ being the space of molecules reachable given a set of chemical reactions, initialization molecules, and available reactants.
- 3.2.1.2. Action Space $A$. We define a set of higher- level actions $A_o$ as a curated list of **chemical reaction templates**
$R=r_1+r_2+\cdots+r_k \rightarrow (p_1, \cdots, p_m)$
Each $r_i$ corresponds to a reactant, while each $p_j$ is a product of this reaction. (+terminal action) …  Set of primitive actions, $*A_i*$, corresponding to a **list of reactants derived from the reaction templates**, which we also refer to as chemical building blocks. …
- 3.2.1.3. Reward Distribution $R$. … We use a deterministic reward function based on the property to be optimized. In Table 1, this corresponds to the binary prediction of compounds binding to the D2 dopamine receptor (DRD2). In Table S1, these are the penalized calculated octanol−water partition coefficient (cLogP) and quantitative estimate of drug-likeness (QED).20

Julien Horwood and Emmanuel Noutahi, Molecular Design in Synthetically Accessible Chemical Space via Deep Reinforcement Learning, ACS Omega **2020** *5* (51), 32984-32994 DOI: 10.1021/acsomega.0c04153

### Q5. However, this paper does not focus on wet lab applications. Can we control HTS (High Throughput Screening) devices with RL? → Key question for today

![Untitled](Variational%20AI%20-%20Informational%20Meeting%204666e85ee90f49d9b61e56abcc78463d/Untitled.png)

I**BM Research** has been working on the RoboRXN platform, which combines machine learning with a cloud-based robotic laboratory to automate chemical synthesis. → Something like this, but couldn’t find paper.

Searched for: reinforcement learning + high throughput screening

Could not find any related papers. What would be your search keyword?