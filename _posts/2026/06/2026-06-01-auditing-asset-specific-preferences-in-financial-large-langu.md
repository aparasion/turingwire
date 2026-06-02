---
title: "Auditing Asset-Specific Preferences in Financial Large Language Models: Evidence from Bitcoin Representations and Portfolio Allocation"
date: 2026-06-01 17:36:06 +0000
category: research
subcategory: agents_robotics
company: "ServiceNow"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2606.02528v1"
arxiv_id: "2606.02528"
authors: ["Wenbin Wu"]
slug: auditing-asset-specific-preferences-in-financial-large-langu
summary_word_count: 415
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper investigates biases in financial large language models (LLMs) towards Bitcoin, revealing internal representations that influence portfolio decisions."
---

**Problem**  
This work addresses the untested hypothesis that large language models (LLMs) exhibit systematic biases towards specific financial instruments, particularly Bitcoin. Despite the increasing use of LLMs in robo-advisory and trading applications, there is a lack of empirical evidence regarding their asset-specific preferences. The authors propose a three-level audit protocol to explore these biases, focusing on the implications for financial decision-making. This research is presented as a preprint, indicating that it has not yet undergone peer review.

**Method**  
The authors develop a three-level audit protocol to assess the preferences of eight frontier LLMs regarding Bitcoin. The first level involves a behavioral audit, where the models' rankings of Bitcoin among money-like instruments are evaluated under different frames (e.g., crisis vs. autonomous-agent). The second level involves an internal analysis using a sparse-autoencoder feature search in the Gemma 3 model, identifying a dominant feature that selectively influences Bitcoin representation. The third level tests the financial consequences of manipulating this feature, measuring the impact on Bitcoin's portfolio share. The authors employ random controls to validate their findings and establish mechanism boundaries.

**Results**  
The behavioral audit reveals that Bitcoin's ranking varies significantly based on the framing context, with a rank of 5 out of 8 under normal conditions but near the top during crisis scenarios. The attribute-swap experiment confirms that the rankings are influenced by functional properties rather than mere nomenclature. The internal feature analysis identifies a Bitcoin-selective feature, which, when amplified, increases Bitcoin's portfolio share by 5.2 percentage points, while suppression decreases it by 4.6 percentage points. This demonstrates a causal influence of internal representations on financial decisions, characterized as bounded behavioral leverage.

**Limitations**  
The authors acknowledge that their findings are limited to the specific context of Bitcoin and the selected LLMs, which may not generalize to other financial instruments or models. Additionally, the study does not explore the long-term implications of these biases on market behavior or the potential for manipulation. The reliance on a single model (Gemma 3) for internal representation analysis may also limit the robustness of the conclusions drawn.

**Why it matters**  
This research has significant implications for the development of autonomous financial agents and the establishment of know-your-agent (KYA) standards. By identifying and quantifying the internal biases of LLMs, the study provides a foundational framework for understanding how these biases can influence financial recommendations and decisions. As LLMs become increasingly integrated into financial systems, understanding their asset-specific preferences is crucial for ensuring transparency and accountability in automated financial decision-making, as published in [arXiv cs.LG](https://arxiv.org/abs/2606.02528v1).
