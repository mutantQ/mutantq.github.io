# 0c. AI for Science

## 컴퓨팅의 발전과 시뮬레이션

시행착오는 본질적으로 고통을 수반한다. 이 고통을 즐기는 사람들도 있지만, 계속되는 반복 작업은 대개 피로의 원인이 될 뿐이다. 실험실에서 피펫으로 사람이 직접 용액을 옮겨담고, 관찰하고, 또 결과를 기록하는 일은 인건비를 고려하면 대단히 비싼 작업이며, 이를 로봇으로 자동화하여 고속 스크리닝(HTS, High Throughput Screening)으로 실험을 진행하더라도 피펫팅 1회에 몇십 센트에서 많게는 1달러의 비용이 소모된다. 중력파 실험에 투입된 총 예산은 XX달러, CERN의 초대형 입자가속기에 투입된 예산은 XX달러로 가희 천문학적인데, 이런 대형 실험 시설에서 시뮬레이션의 부재로 초기 설정 오류를 잡아내지 못해 추가적인 거대 금액이 발생하는 상황은 상상만해도 아찔하다. 그러나 컴퓨팅의 비약적인 발전 덕에 연구자들은 직접 물리 세계와 상호작용하지 않고도 실험을 수행할 수 있게 되었으며, 이는 엄청난 비용 절감 효과를 가져다주었다 - 마치 모두에게 아인슈타인처럼 사고 실험하는 능력이 생긴 것처럼 말이다.

앞선 이야기를 요약하자면, 컴퓨팅은 싸고 편리한 반면 현실 세계의 실험은 비싸고 피곤하며, 이것이 2000년대 이후 시뮬레이션 기반 연구가 활성화될 수밖에 없었던 이유이다. 하지만 시뮬레이션이 단순히 실험의 시행착오와 노고를 줄이는 역할만을 할 것으로 기대하는 것은 대단히 근시안적이다. 병렬 컴퓨팅의 성능 향상과 인공신경망 이론의 발전에 힘입어, 과학자들은 도저히 시간 안에 계산할 수 없었던 미분방정식을 풀 수 있게 되었으며[[ARINT7]](https://www.notion.so/ARINT7-DNN-approximations-of-operators-neural-operators-are-being-introduced-456cf90774ec44c88491cc226c02f72b?pvs=21), 심지어는 새로운 회로 설계를 스스로 탐색하고 최적의 회로 구조를 제안할 수 있게 되었다. 이제는 인공지능이 시뮬레이션 속에서 직접 추론하며 이론을 세우고 수식화하는 단계에 이르렀으며, 이를 적극 활용하여 연구를 수행하는 집단이 우위를 점할 것으로 보인다. 바야흐로, 연구도 인공지능으로 수행하는 신-자동화 시대가 열린 것이다.

### Misc

- **어떤 주제에 대한 지식의 총량을 정량화할 수 있는 방법은?**
    - AI 화학자 예시
        
        만약에 AI 화학자가 있어서 실험 장비들과 연계된 상태로 다양한 실험을 수행하고 있다고 하면 가장 빠르게 Knowledge를 최대화할 수 있는 방향으로 실험을 수행해야 한다. 그것이 ‘화학자’의 본질적인 역할이다.
        
    - 사람은 자신이 무엇인가를 모른다는 사실을 어떻게 알까? 새로운 지식을 추구하게하는 방법은 무엇인가?
        
        Where does the sense of KNOWLEDGE come from? Can you make that into a loss function?
        
- **복제와 시뮬레이션은 다르다.**
    - Quantum computers “clone" a system. There exists a direct one-to-one correspondence of all physical properties, between the original system and the cloned system.
    - Neural networks “approximate” a system. It does not fully capture the physics of the original system, but it describes the system accurately to a certain extent - this is what it means to “simulate".
- **에이전트끼리 협업을 유도하면 같은 리소스로 더 양질의 결과를 얻을 수 있을까?**
    - 칠판에 여러 학생이 수식을 적으면서 모델링 게임을 하듯 강화학습하는 모델
    - 소통하면서 성장해나가는 연구자 그룹과 같은 학습 모델
- **가르치는 행위가 학습을 가속화할 수 있지 않을까?**
    - Giving a proof is similar to teaching math in general, in the sense that you are logically listing why some statement is true.
    - If math is hard, why can't we make machines teach non-experts mathematical concepts, so that it knows what it doesn't know?
- **특정 과목을 인공지능이 마스터하기 위해서는 어떻게 접근해야 할까?**
    - "물리학을 잘한다"의 loss landscape가 있다고 하자
    - 만약 그런게 있다고 하면 일반물리학 같은걸로 대략적인 위치를 잡고, 구체적인 과목들을 더 수강하면서 더 잘하도록 추가학습할 수도 있을 것이다.
    - 반대로 loss landscape를 물리학 평가 문제의 집합으로 역변환하는 매핑을 생각할 수 있다면, 물리학을 잘하도록 유도하는 문제를 난이도와 순서를 고려하여 제시할 수도 있지 않을까?