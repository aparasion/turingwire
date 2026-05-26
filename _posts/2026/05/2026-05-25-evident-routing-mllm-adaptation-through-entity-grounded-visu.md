---
title: "EVIDENT: Routing MLLM Adaptation through Entity-Grounded Visual Evidence for Cross-Domain Video Temporal Grounding"
date: 2026-05-25 17:58:11 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.26104v1"
arxiv_id: "2605.26104"
authors: ["Geo Ahn", "Jiwook Han", "Youngrae Kim", "Joonseok Lee", "Jinwoo Choi"]
slug: evident-routing-mllm-adaptation-through-entity-grounded-visu
summary_word_count: 451
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of fine-tuning Multimodal Large Language Models (MLLMs) for Video Temporal Grounding (VTG), particularly under domain shifts. The authors identify that existing methods often lead to performance degradation when faced with unseen query concepts and visual domain shifts. This gap in the literature highlights the need for a robust adaptation framework that can maintain performance across varying domains. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose EVIDENT, a parameter-efficient adaptation framework designed to enhance VTG by leveraging entity-grounded visual evidence. EVIDENT comprises three main components:  
1. **Entity Bottleneck Adapter**: This component transforms dense visual tokens into compact entity-level slots, effectively reducing the complexity of visual information while retaining essential semantic content.  
2. **Entity-Binding Distillation Loss**: This loss function instills objectness priors into the MLLM's visual space, guiding the model to associate each slot with a coherent entity. This process helps to structure the previously unstructured visual data.  
3. **Entity-to-eVidence Gating Mechanism**: This mechanism utilizes the identified entities as evidence to direct the model's attention towards moments that contain query-relevant entities, thereby enhancing temporal localization capabilities.  

The training process involves fine-tuning the MLLM with these components, which collectively enable the model to rely on entity-grounded evidence rather than potentially misleading dataset shortcuts.

**Results**  
EVIDENT was evaluated on cross-domain VTG benchmarks, demonstrating significant improvements in out-of-domain robustness compared to baseline models. The authors report that EVIDENT achieves a performance increase of up to 15% in mean Average Precision (mAP) on the ActivityNet and Charades datasets when compared to standard fine-tuning methods. Importantly, it maintains competitive in-domain performance with only a modest increase in parameter overhead, indicating its efficiency and effectiveness.

**Limitations**  
The authors acknowledge that while EVIDENT improves robustness to domain shifts, it may still struggle with highly complex or ambiguous visual contexts where entity grounding is less clear. Additionally, the reliance on pre-trained MLLMs may limit the adaptability of EVIDENT to entirely novel tasks or domains not represented in the pre-training phase. The paper does not address the computational cost associated with the additional components, which could be a concern for deployment in resource-constrained environments.

**Why it matters**  
The implications of this work are significant for future research in VTG and related fields. By establishing entity-level grounding as a viable inductive bias for generalizable temporal localization, EVIDENT opens avenues for more robust MLLM adaptations across diverse domains. This approach could enhance the performance of various applications, including video understanding, action recognition, and human-computer interaction, where accurate temporal grounding is critical. The findings encourage further exploration of entity-based methodologies in multimodal learning contexts.

Authors: Geo Ahn, Jiwook Han, Youngrae Kim, Joonseok Lee, Jinwoo Choi  
Source: arXiv:2605.26104  
URL: [https://arxiv.org/abs/2605.26104v1](https://arxiv.org/abs/2605.26104v1)
