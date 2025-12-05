---
layout: post
title: "Introducing mutual"
date: 2025-12-05 10:00:00 +0900
description: Building trust infrastructure for the post-AI era
tags: startup mutual content-authenticity hardware-security
categories: announcement
lang: en
---

## The Problem

AI-generated images and videos are now virtually indistinguishable from reality. Disinformation, fraud, defamation—the problems are escalating.

Many approaches focus on software-based detection, but the fundamental vulnerability lies in hardware. In most systems, camera modules transmit unencrypted raw data to the processor. This path is vulnerable. A simple adapter can intercept the feed or inject entirely synthetic data, and the system has no way of knowing.

## The Solution: SRA (Signing Right Away)

mutual authenticates content at the source, at the hardware level.

The SRA architecture has two core components:

1. **Encrypted Camera-to-Processor Link**: The camera module and processor perform mutual authentication. All subsequent data is protected by authenticated encryption schemes like AES-GCM/CCM.

2. **Immediate Signing in TEE**: The encrypted feed is sent directly to the processor's Trusted Execution Environment (TEE). Inside the TEE, data is decrypted and cryptographically signed along with its metadata. Private signing keys never leave the TEE.

The result is a standard image file with embedded C2PA Content Credentials. By the time a user accesses the image, it has already been signed within a hardware-secured environment.

## Background

In spring 2024, I formalized the initial SRA concept. The project paused during my military service, and after discharge, I reassembled a team to begin prototyping.

Our goal was ambitious: reverse-engineer and implement a secure transport layer for the MIPI CSI-2 protocol without official documentation. It failed. FPGA memory limitations, the limits of undocumented reverse engineering—we understood the problems clearly, but lacked the resources to solve them.

Then Kay Kyungsik Woo, founder and CEO of MVL Foundation, held a seminar for student entrepreneurs. MVL operates TADA, a blockchain-based ride-hailing platform with 2 million users, 200,000 drivers, over $30M raised, 250 employees globally, and profitability achieved in 2022.

I pitched SRA. We received angel investment.

## Why "mutual"

In economics, a "lemon market" describes how information asymmetry—when buyers can't distinguish good products from bad—causes markets to collapse. Digital media is in that situation now.

mutual's mission is to **provide technical trust where information asymmetry exists, restoring mutual trust between parties.**

We're not building another AI detector. We're building infrastructure that makes authentic content provably authentic.

## Market Validation

Qualcomm's Snapdragon 8 Gen 3 introduced hardware support for C2PA, signaling that hardware-based content authentication is entering commercialization. Truepic has already implemented a similar architecture using the Qualcomm TEE with their Foresight system.

mutual's strategy is not proprietary hardware or closed solutions. We aim to provide an **open, interoperable reference architecture** implementable on any SoC with the necessary trusted hardware components. The business model follows ARM's IP licensing approach.

## The Team

We're a small team from Seoul National University. One prototyping failure taught us exactly what works and what doesn't. We're now recruiting a hardware engineer co-founder.

If you're interested, check out the [job posting](/blog/2025/mutual-cofounder-hardware/).

---

**Contact**: [jangyejun@snu.ac.kr](mailto:jangyejun@snu.ac.kr)
