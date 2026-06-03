---
title: "AlignAtt4LLM: Fast AlignAtt for Decoder-Only LLMs at IWSLT 2026 Simultaneous Speech Translation Task"
date: 2026-06-02 17:52:18 +0000
category: research
subcategory: efficiency_inference
company: "Google DeepMind"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.03967v1"
arxiv_id: "2606.03967"
authors: ["Quentin Fuxa", "Dominik Mach\u00e1\u010dek"]
slug: alignatt4llm-fast-alignatt-for-decoder-only-llms-at-iwslt-20
summary_word_count: 398
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces AlignAtt4LLM, a novel approach for simultaneous speech translation using decoder-only LLMs, achieving significant performance improvements."
---

**Problem**  
This work addresses the gap in simultaneous speech translation systems utilizing decoder-only large language models (LLMs), specifically for the IWSLT 2026 task. Prior implementations of AlignAtt have relied on encoder-decoder architectures, which are not applicable here. The authors present AlignAtt4LLM as a pioneering solution for this context, highlighting the need for effective alignment strategies in the absence of cross-attention mechanisms.

**Method**  
AlignAtt4LLM employs a synchronous cascade architecture, integrating Qwen3-ASR for forced alignment to generate an incrementally updated source transcript. The translation is performed by Gemma-4 E4B-it, which utilizes a modified AlignAtt policy tailored for decoder-only LLMs. Key innovations include: 
1. An explicit source span included in the prompt to guide translation.
2. Offline selection of translation-specific alignment heads to optimize performance.
3. Selective qk-fast replay of the draft-to-source attention block to enhance efficiency.
4. Runtime query/key capture that ensures bit-identical preservation of model outputs. 

The system is designed to operate effectively in both low-latency (around 2 seconds) and high-latency (below 4 seconds) regimes, making it suitable for real-time applications.

**Results**  
On the IWSLT 2026 development set, AlignAtt4LLM demonstrates superior performance compared to baseline systems for English to German and English to Italian translations. Specifically, it achieves a notable improvement in translation quality metrics, although exact numerical results are not disclosed in the abstract. For English to Chinese, results are less consistent, indicating potential limitations in the method's applicability across diverse language pairs. The authors emphasize that AlignAtt4LLM's architecture is not inherently tied to Gemma-4, allowing for future adaptations with more robust translation-focused decoder-only models.

**Limitations**  
The authors acknowledge that while AlignAtt4LLM shows promise, its performance for English to Chinese translations is mixed, suggesting that further optimization may be necessary for non-European languages. Additionally, the reliance on a deterministic prompt layout and calibrated attention heads may limit flexibility in diverse translation scenarios. The work is a preprint and has not undergone peer review, which may affect the reliability of the findings.

**Why it matters**  
The introduction of AlignAtt4LLM represents a significant advancement in the field of simultaneous speech translation, particularly for decoder-only LLMs. Its innovative approach to alignment and translation can inform future research and applications in real-time translation systems, potentially enhancing user experience in multilingual communication. The findings and methodologies presented in this paper could serve as a foundation for subsequent studies aiming to improve translation accuracy and efficiency in various language pairs, as published in [arXiv](https://arxiv.org/abs/2606.03967v1).
