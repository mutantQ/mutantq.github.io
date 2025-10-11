---
layout: post
title: "보충 자료 : 최대공약수와 최소공배수"
date: 2021-07-20 10:00:00 +0900
description: 수학 교육 자료
tags: education tutoring mathematics korean
categories: education
unlisted: true
---

*본 자료는 인공지능을 활용하지 않고 작성되었음을 알립니다.*

## GCD and LCM

![](/assets/img/blog/tutoring/untitled__161f0f24f931802cbe25e788d3d23.png)

![](/assets/img/blog/tutoring/untitled_1__161f0f24f931802cbe25e788d3d23.png)

위의 그림을 이용하여 최대공약수와 최소공배수의 성질들을 설명해보자.

## Prove: $A=Ga$, $B=Gb$이면 $a, b$는 서로소

### 상황에 대한 이해

$A$와 $B$가 모두 자연수라고 하자.

$A$와 $B$의 최대공약수(Greatest Common Divisor, GCD)를 $G$라고 하면,

$G$는 ($A$와 $B$의 최대공약수이기 전에) $A$와 $B$의 공약수(Common Divisor, CD)이므로

$$
\begin{align*}
A=Ga \;\;(a는\;자연수) \\ B=Gb\;\;(b는\;자연수) \tag{1}
\end{align*}
$$

이다. 여기서 **$a$와 $b$가 서로소, 즉 $\textrm{gcd}(a, b)=1$임을 보이고자 한다.**

### Proof by Contradiction

귀류법(Proof by Contradiction)을 사용하자. 결론을 부정하여

$$
\textrm{gcd}(a, b)=k\;(k는 \;1보다 \;큰\;자연수)
$$

라고 하자. 그러면 또 다시

$$
\begin{align*}
a=ka'\;\;(a'은\;자연수) \\ b=kb'\;\;(b'은\;자연수) \tag{2}
\end{align*}
$$

와 같이 나타낼 수 있다. 식 $(2)$의 결과를 식 $(1)$에 대입하면

$$
\begin{align*}
A=(Gk)a'\;\;(a'는\;자연수) \\ B=(Gk)b'\;\;(b'는\;자연수) \tag{3}
\end{align*}
$$

따라서 $Gk=G'$는 $A$와 $B$의 공약수이다.

$G'>G$이므로 $G$보다 더 큰 공약수 $G'$이 존재한다. 하지만 이것은 $G$가 $A$와 $B$의 **'최대'**공약수라는 가정과 모순이다. 결론을 부정했을 때 모순이 발생하므로, 결론은 참이다.

## Prove: $L=Gab$

### 상황에 대한 이해

$A$와 $B$의 최소공배수(Least Common Multiple, LCM)를 $L$이라고 하자.

우선 $Gab=(Ga)b=(Gb)a$이므로, $Ga=A,\;Gb=B$임을 생각하면 $Gab$가 $A$와 $B$의 공배수(Common Multiplier, CM)임을 알 수 있다. 이제 $Gab$가 공배수 중에서도 **'최소'**공배수임을 보여야 한다.

### Proof by Contradiction

결론을 부정하여 $L<Gab$, 즉 $Gab$보다도 더 작은 최소공배수가 존재한다고 하자. 그렇다면 모든 공배수는 최소공배수의 배수이므로

$$
Gab=Lm\;\;(m은\;1보다\;큰\;자연수) \tag{4}
$$

을 만족하는 $m$이 존재한다. 이때, $L$은 $A$와 $B$의 공배수이기 때문에 다음이 성립한다.

$$
\begin{align*}
L=Ak_1 = (Ga)k_1\;\;(k_1은\;자연수)\\ L=Bk_2 = (Gb)k_2\;\;(k_2는\;자연수)\tag{5}
\end{align*}
$$

식 $(5)$의 결과를 식 $(4)$에 대입하면 다음을 얻는다.

$$
\begin{aligned} Gab&=Lm\\ &=Gak_1 m \\&=Gbk_2m\;\;(m은\;1보다\;큰\;자연수) \end{aligned} \tag{6}
$$

이를 정리하면

$$
\begin{aligned} b&=k_1m \\ a&=k_2m\;\;(m은\;1보다\;큰\;자연수) \end{aligned} \tag{7}
$$

따라서 $a$와 $b$는 공약수 $m$을 가진다. 이는 $a,b$가 서로소라는 가정에 모순이다. 결론을 부정했을 때 모순이 발생하므로, 결론은 참이다.

## Prove: $AB=GL$

### 상황에 대한 이해

앞서 $A=Ga$, $B=Gb$라 하면 $a,b$가 서로소이고 $L=Gab$가 됨을 보였다.

### Proof

앞서 증명한 사실들을 조합하면 다음을 얻는다.

$$
\begin{aligned} AB&=(Ga)(Gb)=G^2ab \\ GL&=G(Gab)=G^2ab \end{aligned} \tag{8}
$$

$$
\therefore \; AB=G^2ab=GL \tag{9}
$$
