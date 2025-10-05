---
layout: post
title: "Signing Right Away"
date: 2025-10-05 20:00:00 +0900
description: A Hardware-Rooted Trust Architecture for Verifiable Digital Provenance
tags: digital-signature c2pa content-provenance fake-news ai-generated-images
categories: ideas
lang: en
---

You can find the full whitepaper here: **[PDF](/assets/pdf/SRA-2025-10-05.pdf)**

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

We had reached a deadlock. We knew exactly what the problems were and what we needed to solve them, but we lacked the resources.

It was at this point that a fortuitous opportunity arose. A successful founder, Kay Kyungsik Woo, held a seminar and offered to provide angel investment (approx. $70,000 in total) to three student teams. This was the catalyst we desperately needed to move forward, armed with the hard-won lessons from our initial failure.

## A More Mature Architecture

That failure forced us to take a step back and refine our approach, leading to the more structured architecture we are pursuing now. The plan is heavily inspired by the MIPI Alliance's Camera Security Framework, which outlines pillars of confidentiality, integrity, authentication, and replay protection.

Our revised architecture involves two main components:

### 1. Authenticated & Encrypted Camera-to-Processor Link

The first step is to secure the physical data path. The camera module and processor would first perform a mutual authentication handshake. Once trust is established, all data transmitted over the CSI-2 interface would be protected by an authenticated encryption (AEAD) scheme, like AES-GCM. This ensures both confidentiality and integrity, as any modification would be detected via MAC verification.

### 2. Immediate Signing in a Trusted Execution Environment (TEE)

The encrypted feed is sent directly to a TEE, an isolated, secure enclave on the processor. Inside the TEE, the data is decrypted, processed, and cryptographically signed along with its metadata (e.g., timestamp, device ID). The private signing keys never leave the TEE, protecting them from a compromised OS. The final output is a standard image file with an embedded, verifiable C2PA Content Credential.

This design ensures that by the time an application or user has access to an image, it has already been signed within a secure hardware environment. The investment would allow us to acquire the necessary next-generation FPGA to properly implement and test this more robust architecture.

## Thoughts on Long-Term Viability and IP

Looking ahead, we recognize that working around closed industry standards isn't a sustainable strategy. This prototyping effort is a means to an end, and we have a three-stage plan for addressing the intellectual property (IP) challenges:

### 1. Develop Proprietary Technology

The primary goal is to use the experience gained to develop our own unique, efficient, and patentable method for secure camera data transmission.

### 2. Contribute to Standardization

Once we have a robust proprietary solution, one path is to contribute it to open standards bodies like C2PA. This could help create a more open, interoperable ecosystem for secure media capture.

### 3. Build a Defensive Patent Portfolio

We would also patent our innovations to create a defensive IP portfolio, allowing us to operate and protect our work as we aim for broader adoption, potentially through licensing to device and chip manufacturers.

## Conclusion

The goal of SRA is to help create a digital ecosystem where the authenticity of content can be programmatically verified. The problem is challenging and involves navigating hardware, cryptography, and industry standards, but we believe it's a critical step toward rebuilding trust in digital media.

