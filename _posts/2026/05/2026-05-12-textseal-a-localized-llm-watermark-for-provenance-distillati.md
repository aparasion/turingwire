---
title: "TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection"
date: 2026-05-12 17:44:41 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.12456v1"
arxiv_id: "2605.12456"
authors: ["Tom Sander", "Hongyan Chang", "Tom\u00e1\u0161 Sou\u010dek", "Tuan Tran", "Valeriu Lacatusu", "Sylvestre-Alvise Rebuffi"]
slug: textseal-a-localized-llm-watermark-for-provenance-distillati
summary_word_count: 435
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the need for robust watermarking techniques in large language models (LLMs) to ensure provenance and protect against unauthorized model distillation. The authors identify a gap in existing watermarking methods, particularly in their ability to maintain output diversity and detection strength in mixed human/AI content. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this work is the introduction of TextSeal, a watermarking framework that leverages Gumbel-max sampling for dual-key generation. This approach enhances output diversity while employing entropy-weighted scoring to optimize watermark detection. TextSeal incorporates multi-region localization, allowing for precise identification of the watermark within the generated text. The framework is designed to be computationally efficient, supporting speculative decoding and multi-token prediction without introducing inference overhead. The authors claim that TextSeal is theoretically distortion-free, ensuring that the watermark does not degrade the quality of the generated text.

**Results**  
TextSeal demonstrates superior performance compared to the baseline method SynthID-text, achieving a significantly higher detection strength. The evaluation metrics indicate that TextSeal maintains robust detection capabilities even when the watermark is diluted in documents containing a mix of human and AI-generated text. In a multilingual human evaluation involving 6000 A/B comparisons across five languages, no perceptible quality differences were reported, suggesting that the watermarking process does not adversely affect the model's output. Additionally, the framework's "radioactive" property allows the watermark signal to persist through model distillation, enabling the detection of unauthorized use of the model.

**Limitations**  
The authors acknowledge that while TextSeal shows strong performance in detection and preservation of output quality, the evaluation is limited to specific benchmarks and may not generalize across all potential use cases. They do not address potential vulnerabilities to adversarial attacks aimed at watermark removal or the implications of watermarking in highly sensitive applications. Furthermore, the scalability of the method in extremely large models or diverse application domains remains untested.

**Why it matters**  
The implications of TextSeal are significant for the field of AI and LLMs, particularly in contexts where provenance and intellectual property protection are critical. By providing a robust watermarking solution that does not compromise model performance, this work paves the way for more secure deployment of LLMs in commercial and research settings. The ability to detect unauthorized use through model distillation also raises important considerations for ethical AI usage and compliance with intellectual property laws. This research could influence future work on watermarking techniques and their integration into LLM architectures.

Authors: Tom Sander, Hongyan Chang, Tomáš Souček, Tuan Tran, Valeriu Lacatusu, Sylvestre-Alvise Rebuffi, Alexandre Mourachko, Surya Parimi et al.  
Source: arXiv:2605.12456  
URL: [https://arxiv.org/abs/2605.12456v1](https://arxiv.org/abs/2605.12456v1)
