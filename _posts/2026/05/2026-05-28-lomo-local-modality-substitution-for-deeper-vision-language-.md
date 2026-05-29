---
title: "LoMo: Local Modality Substitution for Deeper Vision-Language Fusion"
date: 2026-05-28 17:27:55 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.30265v1"
arxiv_id: "2605.30265"
authors: ["Feng Han", "Zhixiong Zhang", "Zheming Liang", "Yibin Wang", "Jiaqi Wang"]
slug: lomo-local-modality-substitution-for-deeper-vision-language-
summary_word_count: 390
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in Vision-Language Models (VLMs) related to "carrier sensitivity," where substituting textual queries with their visual counterparts leads to significant performance degradation. The authors identify a bias in existing training datasets, where text and images are asymmetrically organized, resulting in VLMs that struggle to align representations of semantically equivalent content across modalities. This issue hampers the robustness of VLMs in reasoning tasks when faced with modality substitution.

**Method**  
The authors propose Local Modality Substitution (LoMo), a lightweight and architecture-agnostic data curation paradigm aimed at enhancing cross-modal representational invariance. LoMo reformulates single-modality prompts into interleaved multimodal sequences, dynamically selecting target text spans and converting them into rendered images. This approach preserves semantic consistency across the "text, visual, text" format, thereby providing supervision for VLMs to better align representations across modalities. The method does not require extensive changes to existing architectures, making it broadly applicable across various VLMs.

**Results**  
LoMo was evaluated across 13 diverse multimodal benchmarks, demonstrating substantial improvements in multimodal reasoning capabilities. Notably, it achieved a 2.67-point increase over standard supervised fine-tuning (SFT) on the LLaVA-OneVision-1.5-8B model and a 2.82-point increase on the Qwen3.5-9B model. These results indicate that LoMo not only enhances performance but also facilitates deeper cross-modal fusion, outperforming baseline methods in a consistent manner across multiple tasks.

**Limitations**  
The authors acknowledge that while LoMo improves cross-modal alignment, it may not fully eliminate the inherent biases present in training datasets. Additionally, the method's effectiveness may vary depending on the specific architecture of the VLMs employed. The paper does not address the computational overhead introduced by the dynamic selection process, which could impact training efficiency. Furthermore, the generalizability of LoMo to unseen datasets or tasks remains untested.

**Why it matters**  
The implications of this work are significant for the development of more robust VLMs capable of handling modality substitutions without performance loss. By addressing the carrier sensitivity issue, LoMo paves the way for improved multimodal reasoning and representation alignment, which is crucial for applications in areas such as visual question answering, image captioning, and other tasks requiring seamless integration of text and images. This research could inspire further exploration into data curation techniques that enhance the robustness of VLMs against modality biases, ultimately leading to more reliable AI systems.

Authors: Feng Han, Zhixiong Zhang, Zheming Liang, Yibin Wang, Jiaqi Wang  
Source: arXiv:2605.30265  
URL: [https://arxiv.org/abs/2605.30265v1](https://arxiv.org/abs/2605.30265v1)
