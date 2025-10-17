---
layout: post
title: "Signing Right Away"
date: 2025-10-05 20:00:00 +0900
description: A Hardware-Rooted Trust Architecture for Verifiable Digital Provenance
tags: digital-signature c2pa content-provenance fake-news ai-generated-images
categories: whitepaper
lang: en
---

*This work contains AI-generated paragraphs and sentences. The original whitepaper of this work has been written by myself in English. The original experiment notes (undisclosed) were written in Korean by myself and my teammates, Wonbeen Yoon and Minjun Yi from Seoul National University. Gemini Deep Research was used to organize the work into the full whitepaper. Each work was fully reviewed and revised by myself. Special thanks to Hrvoje (Harvey) Puh for his valuable feedback in the original whitepaper.*


You can find the full whitepaper here: **[PDF](/assets/pdf/SRA-2025-10-05.pdf)** \
The original whitepaper can be viewed here: **[PDF](/assets/pdf/SRA-2024-05-26.pdf)**

## A Brief Motivation

The proliferation of generative AI has made it trivial to create hyper-realistic fake images and videos, posing a serious threat to information integrity. This raises significant concerns over disinformation and fraud. While many approaches try to solve this with software classifiers, the root of the problem is arguably in hardware. 

In most current systems, the camera module sends an unencrypted, raw bitstream to the main processor over an interface like MIPI CSI-2. This link is vulnerable; a simple adapter can be used to intercept the feed or inject entirely synthetic data, and the system would have no way of knowing.

This suggests that a robust solution requires securing content provenance at the source.

## An Early Attempt and a Hard Reset

The initial idea for SRA was formalized back in the spring of 2024. Shortly after, I began my mandatory military service, which put the project on hold. After being discharged recently, I gathered a few friends to reboot the project with fresh energy.

Our goal was ambitious: to reverse-engineer and replicate a secure transport layer for the MIPI CSI-2 protocol without official documentation. To put it mildly, it was a failure. Our attempts to build on an unknown, undocumented foundation resulted in glitchy, unparseable camera feeds. The custom parsing logic we wrote would fail intermittently, and the entire pipeline was fundamentally unstable. It was a disaster.

But the experience, while painful, was incredibly valuable. It taught us two critical lessons:

1. **Hardware limitations are real.** Our FPGA platform needed significantly more memory to buffer and process full image frames in real-time.

2. **Reverse engineering has its limits.** To build a stable image processing pipeline, we couldn't rely on guesswork alone. We needed access to at least some confidential documentation or, failing that, a far more powerful and flexible hardware platform to allow for rapid, iterative testing.

<!-- We had reached a deadlock. We knew exactly what the problems were and what we needed to solve them, but we lacked the resources.

It was at this point that a fortuitous opportunity arose. A successful founder, Kay Kyungsik Woo, held a seminar and offered to provide angel investment (approx. $70,000 in total) to three student teams. This was the catalyst we desperately needed to move forward, armed with the hard-won lessons from our initial failure. -->

## The SRA Architecture

The core architecture of SRA was established in our original 2024 whitepaper, based on fundamental cryptographic principles of confidentiality, integrity, authentication, and replay protection. We initially designed our system around authenticated encryption schemes like ChaCha20-Poly1305. During development, we discovered that the MIPI Alliance's Camera Security Framework had independently standardized similar approaches, which validated our architectural choices. While the prototyping experience taught us crucial lessons about implementation strategy—particularly the need for hardware-accelerated cryptography and better development platforms—the fundamental architectural design remained consistent.

The architecture involves two main components:

### 1. Authenticated & Encrypted Camera-to-Processor Link

The first step is to secure the physical data path. The camera module and processor would first perform a mutual authentication handshake. Once trust is established, all data transmitted over the CSI-2 interface would be protected by an authenticated encryption (AEAD) scheme, like AES-GCM. This ensures both confidentiality and integrity, as any modification would be detected via MAC verification.

### 2. Immediate Signing in a Trusted Execution Environment (TEE)

The encrypted feed is sent directly to a TEE, an isolated, secure enclave on the processor. Inside the TEE, the data is decrypted, processed, and cryptographically signed along with its metadata (e.g., timestamp, device ID). The private signing keys never leave the TEE, protecting them from a compromised OS. The final output is a standard image file with an embedded, verifiable C2PA Content Credential. This design ensures that by the time an application or user has access to an image, it has already been signed within a secure hardware environment.

<!-- The investment would allow us to acquire the necessary next-generation FPGA to properly implement and test this more robust architecture. -->

## Aligning with the Broader Ecosystem

Our prototyping experience led to a critical strategic insight: the most effective path to widespread adoption is not to reinvent the wheel, but to align with and build upon the secure hardware capabilities that are already being integrated into commercial System-on-Chips (SoCs).

Mobile SoC vendors like Qualcomm have already integrated the necessary hardware primitives—such as secure Image Signal Processors (ISPs), hardware crypto accelerators, and robust Trusted Execution Environments (TEEs)—into their platforms. The emergence of the Qualcomm Snapdragon 8 Gen 3 as the first C2PA-compliant mobile platform validates this trend.

### Our Strategy: Open and Interoperable

Rather than pursuing custom silicon or proprietary solutions, SRA's strategy is to position itself as an **open, interoperable reference architecture** that can be implemented on any SoC that provides the necessary trusted hardware components. By leveraging existing secure camera APIs and TEE SDKs, SRA can be deployed as a firmware or software solution that "lights up" the latent security capabilities of modern devices.

This approach dramatically reduces cost and time-to-market compared to a custom silicon strategy, and it fosters a competitive, multi-vendor ecosystem rather than a single proprietary solution. The initial plan to design custom ASICs was abandoned in favor of this more pragmatic path that builds on the industry's existing investments in secure hardware.

Industry pioneers like Truepic have already demonstrated similar architectures in practice with their Foresight system, which leverages the Qualcomm TEE and secure hardware pipeline. This serves as proof-of-concept for our model and demonstrates a clear path to market through ecosystem collaboration.

## Conclusion

The goal of SRA is to help create a digital ecosystem where the authenticity of content can be programmatically verified. The problem is challenging and involves navigating hardware, cryptography, and industry standards, but we believe it's a critical step toward rebuilding trust in digital media.

