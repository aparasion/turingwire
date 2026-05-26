---
title: "InstructSAM: Segment Any Instance with Any Instructions"
date: 2026-05-25 17:58:03 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.26102v1"
arxiv_id: "2605.26102"
authors: ["Yuqian Yuan", "Wentong Li", "Zhaocheng Li", "Yutong Lin", "Juncheng Li", "Siliang Tang"]
slug: instructsam-segment-any-instance-with-any-instructions
summary_word_count: 410
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in multi-instance segmentation capabilities under arbitrary instructions, a challenge that has not been adequately tackled in existing literature. The authors propose InstructSAM, a unified framework that integrates instruction-driven instance segmentation with a vision-language model (VLM) and the Segment Anything Model (SAM3). This work is presented as a preprint and has not yet undergone peer review.

**Method**  
InstructSAM formulates the problem of instruction-driven instance segmentation as a set-structured query prediction task. The architecture incorporates a bank of learnable instance queries that are contextualized with both visual and instruction-based information. This is achieved through a hybrid-attention mechanism that enhances interaction among instance queries, visual tokens, and instruction tokens, thereby improving instance enumeration and minimizing duplicate predictions. The LLM-conditioned queries are then projected into SAM3's detector query space, facilitating accurate multi-instance segmentation in a single forward pass. The authors also introduce Inst2Seg, a large-scale dataset that pairs free-form instructions with instance-level masks, which is crucial for training and evaluation.

**Results**  
InstructSAM demonstrates significant performance improvements over existing methods. Specifically, it achieves state-of-the-art results on complex instruction-driven and phrase-level referring segmentation benchmarks, outperforming prior end-to-end methods and the baseline SAM3's agentic pipeline. The authors report that InstructSAM, with a model size of 2 billion parameters, achieves a notable increase in accuracy and efficiency, enabling effective single-pass multi-instance predictions. However, specific numerical results and comparisons to named baselines are not detailed in the abstract.

**Limitations**  
The authors acknowledge that while InstructSAM enhances instruction understanding and compositional reasoning, it still relies on the underlying architecture of SAM3, which may limit its adaptability to other segmentation tasks. Additionally, the reliance on a large-scale dataset (Inst2Seg) may pose challenges in terms of generalizability to other domains or less structured instruction sets. The paper does not address potential computational overhead introduced by the hybrid-attention mechanism or the scalability of the model to larger datasets.

**Why it matters**  
The introduction of InstructSAM has significant implications for the field of instance segmentation, particularly in scenarios requiring nuanced instruction interpretation. By bridging the gap between vision-language models and segmentation tasks, this work paves the way for more sophisticated applications in areas such as robotics, autonomous navigation, and interactive AI systems. The ability to process arbitrary instructions for segmentation tasks could enhance user interaction and expand the applicability of segmentation models in real-world scenarios.

Authors: Yuqian Yuan, Wentong Li, Zhaocheng Li, Yutong Lin, Juncheng Li, Siliang Tang, Jun Xiao, Yueting Zhuang et al.  
Source: arXiv:2605.26102  
URL: [https://arxiv.org/abs/2605.26102v1](https://arxiv.org/abs/2605.26102v1)
