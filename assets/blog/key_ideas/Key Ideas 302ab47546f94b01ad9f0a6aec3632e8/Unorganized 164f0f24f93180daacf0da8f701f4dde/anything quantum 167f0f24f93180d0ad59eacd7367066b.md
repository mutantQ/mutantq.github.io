# anything quantum

큐비트 vs 비트

만약 상자 안에 비트가 여러 개 있고
또 다른 상자 안에 큐비트가 여러 개 있는데,

첫번째 상자에서는 0과 1의 개수가 같고
두번째 상자에서는 벨 상태에 놓인 큐비트만 들어 있다.

두 상자에서 큐비트와 비트를 구분할 수 있는 방법을 고안하시오.

#Ideas

- 편광판: 구멍이 작아지는데 통과하는 빛의 양이 많아진다
- 초전도체의 경제적 효율을 높일 수 있는 방법

**Quantum computing**

- Quantum Computing for the Environment
- Quantum Card (QPU)
- Quantum computing for weather forcast
- Quantum computer graphics
- Quantum computing and art
- Quantum computers lack story
- **Quantum phenomenon and entropy**
- **Quantum assisted telescope**

#Ideas

양자컴퓨터로 최적의 양자컴퓨터 설계가 가능할까

#Ideas

거의 대부분의 양자컴퓨터 알고리즘은 0 상태, 1 상태,  + 상태나 - 상태에 놓여있다

이들만을 이용해서 연산을 하기로 제약 조건을 걸고 노이즈를 감소시킬 수는 없을까?
용수철 같은 느낌으로 고정되는 그런 큐비트

#Ideas

Connectivity, partially quantum, classical on big scale

#Ideas

BQP = BP?

Casework:
BQP ?= BP
QC is possible
Deep learning is plausible

#Ideas

Fully quantum 대신 partially quantum?

#Ideas

고전역학은 양자역학의 근사 (n>>1)
양자물리학

#Ideas

Openfermion

#Ideas

Deep learning to help scientists formulate quantum problems and build algorithms

#Ideas

Solovey-Kitaev Theorem

#Ideas

QC vs AI

어떤 시기에 어떤 것을 사용해야 하는가?

#Ideas

Quantum and Classical Operations Simultaneously

#Ideas

Google Proving Quantum Supremacy

#Ideas

QM9 database

#Ideas

Tox21 Program

Toxicity testing in the 21st century
In vivo ~ animal testing
In vitro ~ non-animal lab testing
In silico ~ using only computers
sdf format - chemical compound

12 toxic effects
⁃	stress response effects (SR)
⁃	such as : heat shock response effect (SR-HSE)
⁃	lead to liver injury or cancer
⁃	nuclear receptor effects (NR)
⁃	such as : activation of the estrogen receptor (NR-ER)
⁃	can disrupt the endocrine system

DeepTox using Tox21 10K compound library
⁃	Used basic DNNs for multiclass classification & cross entropy loss
⁃	Generated a large number of correlated features using off-the-shelf software for chemical descriptors
⁃	used known toxicophores but later removed them from the model
⁃	Have standardized real-valued/count features and applied tanh nonlinearity before training
⁃	Median imputation performed to substitute missing value
⁃	Removed sparse features before training

#Ideas

Can Quantum Computers be replicated by a Neural Network?

If so, does the parameter required to learn a quantum circuit rise exponentially or polynomially?
What would be the best toy model to start with?

#Ideas

Roger Penrose - Quantum Physics of Consciousness
 
Neurophysiology
 
Computational part – electrical
The gap between quantum and classical
Noncomputational activity
Environmental decoherence –
The emperor’s new mind –
Microtubules
Strength of the synapses
Mass displacement
Consciousness involves many neurons
Many microtubules in concert acting in a certain way
It has to expressed in the neuronal impulse

Quantum Mind

#Ideas

Maybe, if the quantum effects inside the warm body becomes well formulated, we can make high-temperature superconducting materials?

#Ideas

Can you enhance DFT method using machine learning? Can you learn the error terms with machine learning?

#Ideas

**Bose Einstein condenstate**

**Material science with quantum tech**

**Biological sensing transition metal**

perovskite nickelates

**Superconducting = fermionic?**

달성 방법: 양자컴퓨팅 알고리즘을 이용한 신촉매 개발

비판적 관점

기사를 상당히 흥미롭게 읽었습니다. 기자 분께서 많은 제약 기업의 연구 계획을 조사하고 투자 유치 과정에 대해 잘 요약해주신 것 같습니다.
하지만, 양자역학이나 양자컴퓨팅 분야를 완전히 이해하고 쓰신 글이 아니다보니 몇 가지 오류와 설명 방식의 문제점을 발견할 수 있었습니다. 물론, 저 역시도 양자역학을 제대로 이해하고 있다고 볼 수 없으니 기술의 실현 가능성에 대해서 완전히 부정하고 싶지는 않습니다.
기사에서는 양자컴퓨팅 분야가 머신러닝 분야와 결합하여 조만간 큰 시너지를 낼 것이라 점치고 있습니다. 아마 양자 머신러닝(quantum machine learning) 분야를 염두에 두고 기사를 작성한 것으로 보입니다.
그러나, 양자컴퓨팅은 아직 먼 미래의 기술로 성능 면에서 기존 기술에 우위를 점하기에는 턱없이 부족합니다. 컴퓨터 성능 향상에서 가장 중요한 것은 바로 scalability입니다. 양자컴퓨팅은 고전컴퓨팅과는 달리 scalable한 시스템의 설계 가능성을 보장할 수 없습니다.
Scalability란, 컴퓨팅 플랫폼에서 기본 구조를 반복적으로 쌓아올릴 때 문제 발생 없이 성능 향상을 이룰 수 있는지를 말합니다. 불 대수와 튜링 머신에 기반한 고전 컴퓨터의 경우 집적도를 올리면서도 구조적인 문제가 일어나지 않도록 설계하는 것이 가능했기 때문에 무어의 법칙에 따라 높은 성능을 달성하였습니다. 즉, 구조의 반복이 시스템의 정확도나 설계 안정성을 해치지 않았기 때문에 비약적인 성능 향상이 가능했습니다.
양자컴퓨팅의 경우 큐비트의 개수를 늘릴 때마다 (즉, 구조가 반복될 때마다) 얽힘 상태를 유지하기 어려워지기 때문에 외부 노이즈의 영향을 심하게 받게 됩니다. 이를 보완하기 위해 양자 오류 정정 기술이 연구되고 있지만, 성능 저하를 발생시키 때문에 현재 기술로는 큐비트를 늘려도 유의미한 성능 향상이 일어나지 않습니다. 아직까지 scalable한 양자컴퓨터의 가능성에 대해서는 불확실성이 큽니다. 이런 상황에서 곧바로 응용을 논하는 기사는 독자들에게 양자컴퓨팅에 대한 지나친 환상을 심어 줄 확률이 높습니다.
양자컴퓨팅에 대한 개념 설명은 꽤나 정확하다고 느꼈습니다. 그러나 반드시 양자+머신러닝, 또는 양자역학에 기반한 머신러닝에 국한해서 기사를 작성한 점은 아쉽게 다가왔습니다. 실제로 딥마인드의 경우 양자역학에 기반한 계산은 학습 데이터를 생성하는 일부 경우를 제외하곤 규칙을 전부 머신러닝 모델이 학습하도록 설계되었습니다. 즉, 풀고자하는 문제의 범위를 어느 정도 한정하고 나면 패턴을 학습하기만 하면 그만이기 때문에 양자역학의 개념들을 반드시 학습할 필요성은 없기 때문입니다.

옹호하는 관점

옹호하는 관점입니다. 실제로 저는 해당 기사가 굉장히 잘 작성되었고 꽤나 유익한 정보를 제공한다는 점에 동의합니다. 특히 구체적으로 어느 제약 회사가 인공지능을 적극적으로 활용하고 있는지 알 수 있어서 좋았습니다. 제약 업계에 문외안인 저에게 대웅 제약과 크리스탈파이의 협업, SK케미칼과 인세리브로의 협업 등은 모두 처음 들어보는 내용이었습니다. 관련 지식을 제대로 갖추고 있다면 큰 오해 없이 내용 전달이 가능한 것으로 보였습니다. 다만, 제가 투자 업계에 대해서 잘 알지 못하게 때문에 구체적으로 투자와 협업이 어떤 것을 의미하는지, 단순히 이슈 메이킹을 통해 주가를 올리기 위한 목적은 없는지는 알기 힘들 것 같습니다. 양자컴퓨팅에 대해서 한 문단으로 잘 요약해서 설명한 것은 맞습니다.

Journal of Chemical Theory and Computation

#Ideas

Ad-hoc mathematical expressions such as the Lennard-Jones Potential, can be just as accurate even though it does not perform quantum calculations.

#Ideas

Small quantum fluctuations/uncertainty, leading to macroscopically observable BIG phenomena

In July 2020, scientists reported that quantum vacuum fluctuations can influence the motion of macroscopic, human-scale objects by measuring correlations below the standard quantum limit between the position/momentum uncertainty of the mirrors of LIGO and the photon number/phase uncertainty of light that they reflect.[6][7][8]

**Preskill Quantum Computing**

RBM states, entanglement entropy, entanglement area law

#Ideas

VQE 오차함수 만들기

#Ideas