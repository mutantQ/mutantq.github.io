---
layout: post
title: "Introducing mutual"
date: 2025-12-05 10:00:00 +0900
description: Building trust infrastructure for the post-AI era
tags: startup mutual content-authenticity hardware-security
categories: announcement
lang: en
---

![mutual logo](/assets/img/mutual-logo.jpg)

{% include video.liquid path="https://www.youtube.com/embed/Ev9knl_Zbsg" class="img-fluid rounded z-depth-1" controls=true %}

Smartphone cameras capture billions of photos and videos every day. Between the moment light hits the sensor and the moment a file is stored or uploaded, that data passes through a long chain of hardware and software. mutual focuses on the earliest part of this pipeline, where physical signals are first converted into digital data.

Over the coming years, a growing share of the media we consume will be generated or heavily modified by AI systems. At that scale, **human perception alone is no longer enough to reliably distinguish authentic content from fabricated content.**

mutual exists to answer a practical question: how do we build infrastructure that makes it possible to trust what we see again?

### Following the breadcrumbs

Over the last few years, a group of companies in the US and Europe has converged on a particular answer. Adobe, together with Google, Sony, OpenAI and others, is leading a technical coalition called **C2PA (Coalition for Content Provenance and Authenticity)**.

The idea behind C2PA is simple to state and hard to implement: record the entire lifecycle of a piece of content, protect that record cryptographically, and make it transparently verifiable to anyone who consumes it later. In other words, give every piece of media a **provenance trail**.

If you follow that logic, a natural question appears:

> If we want a trustworthy record of how content was created, **where should that record start?**

In a photo editor? In a video export step? On a cloud server?

Our answer is: it should start at the **sensor**—at the point where the physical world first becomes digital.

Once a signal has left the sensor, it can, in principle, be copied and modified arbitrarily. The inverse is also true: if we can **lock down and sign the signal at the moment it leaves the sensor and enters the camera pipeline**, every later step can be checked against that original commitment.

mutual is a company built around that belief.

## The problem we see

The internet today behaves like a kind of lemon market. High-quality and low-quality information, real and fake media, all sit side by side. As the information asymmetry grows, trust erodes, and everyone ends up paying for it.

Most current efforts attack the problem at the end of the pipeline: they try to classify already-generated content as real or fake. As generative models improve, this becomes a losing game. If you only ever see the final pixels, the detector is always chasing the generator.

So we decided to change the question:

> What if, instead of trying to detect fakes, we could **prove the origin** of genuine content?

## mutual's approach: Signing Right Away

Our core architecture is called **SRA (Signing Right Away)**. As the name suggests, the goal is to **sign content at the moment it is created**.

Conceptually, the flow is straightforward:

1. A signal comes off the image sensor and enters the camera pipeline.
2. That path is protected at the hardware level using authenticated encryption (AES-GCM/CCM).
3. Only inside a secure enclave (TEE) is the data decrypted and combined with metadata for signing.
4. The final file is produced with C2PA-compliant content credentials attached.

This way, when someone opens an image later, they can ask: \"Did this really originate from a physical sensor? Was it tampered with along the way?\"—and get a cryptographically grounded answer. The root of trust sits in **hardware**, not just in software that can be bypassed.

For a deeper dive into the architecture, you can read the whitepaper (PDF): [Signing Right Away](/assets/pdf/SRA-2025-10-05.pdf).

## How we got here

In spring 2024, I wrote up the first version of SRA as a kind of whitepaper. Around that time I also benefited a lot from guidance by Prof. Soojean Han at KAIST ACSS Lab, who encouraged me to formalize the work in this format and generously provided the first Trion T20 FPGA board that made our early prototyping possible. Then I left for mandatory military service. When I came back, I gathered a few friends, and we tried to turn the idea into a prototype.

We aimed high: without official documentation, we tried to reverse-engineer the MIPI CSI-2 camera interface and bolt a secure transport layer on top. It mostly failed. Our FPGA board didn't have enough memory. Our best-effort understanding of the protocol led to streams that would randomly break. We learned exactly what was wrong and what we needed—but we didn't have the resources to get there.

Around that time, I met **Kay Kyungsik Woo**, founder and CEO of MVL Foundation. MVL runs TADA, a mobility service used by 2 million riders and hundreds of thousands of drivers in Southeast Asia. It's a team that has actually built and scaled a blockchain-based mobility ecosystem.

I walked him through SRA: why the sensor matters, why the timing is right, why this has to live in hardware.

At the end of that conversation, mutual got its first angel investment.

## The name

When I started thinking about what kind of company I wanted to build, one word kept coming back: trust. But the kind of trust we care about isn't one-sided. It's not \"just trust us\"; it's creating the **conditions** under which two sides can rationally trust each other.

That's what \"mutual\" is about.

> Our mission is to provide technical trust wherever information asymmetry exists, so that mutual trust can be restored.

We are still refining that sentence, but it captures the direction of the company.

## Looking ahead

Qualcomm's Snapdragon 8 Gen 3 already supports C2PA at the hardware level. Companies like Truepic are shipping systems built on top of secure camera pipelines. To us, these are strong signals that the ecosystem is moving in the right direction.

mutual's goal is to build a **reference architecture** that is not tied to any single chip or vendor. If a System-on-Chip exposes the right security primitives, our design should be able to run on top of it. On the business side, we are thinking in terms of an ARM-like IP licensing model.

For now, we're a small team based in Seoul. Our days are filled with reading specs, building prototypes, and translating standards into running code. We're looking forward to adding a a hardware engineer co-founder to the team.

If any of this resonates with you, you might enjoy reading the [co-founder role description](/blog/2025/mutual-cofounder-hardware/).

---

**Contact**: [jangyejun@gmail.com](mailto:jangyejun@gmail.com)
