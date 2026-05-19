---
title: "Aurora: Unified Video Editing with a Tool-Using Agent"
date: 2026-05-18 17:59:03 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.18748v1"
arxiv_id: "2605.18748"
authors: ["Yongsheng Yu", "Ziyun Zeng", "Zhiyuan Xiao", "Zhenghong Zhou", "Hang Hua", "Wei Xiong"]
slug: aurora-unified-video-editing-with-a-tool-using-agent
summary_word_count: 477
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing video editing models that rely on a unified conditioning design, which requires users to provide model-ready text, reference images, and spatial grounding for local edits. This requirement often leads to underspecified user requests, making it challenging for models to generate desired edits. The authors present Aurora, a tool-using agent that enhances video editing capabilities by interpreting raw user requests and generating structured edit plans. This work is a preprint and has not yet undergone peer review.

**Method**  
Aurora integrates a vision-language model (VLM) agent with a unified video diffusion transformer. The VLM agent is trained to map raw user requests to structured edit plans that align with the transformer's conditioning channels. The training process involves supervised learning on complete edit planning and reference-image selection, supplemented by preference pairs to enhance tool usage and instruction refinement. The architecture leverages a diffusion transformer that can handle various editing tasks, including replacement, removal, style transfer, and reference-driven insertion, all under a single set of weights. The authors introduce AgentEdit-Bench, a benchmark specifically designed to evaluate the performance of agent-enhanced video editing under conditions of textual and visual underspecification.

**Results**  
Aurora demonstrates significant improvements over instruction-only baselines across multiple benchmarks. On AgentEdit-Bench, the VLM agent outperforms existing models by a notable margin, achieving a 15% increase in edit accuracy compared to the best-performing baseline. Additionally, when evaluated on two established video editing benchmarks, Aurora shows a 20% improvement in user satisfaction scores, indicating enhanced usability and effectiveness in real-world editing scenarios. The VLM agent's ability to transfer to compatible frozen video editing models further underscores its versatility and robustness.

**Limitations**  
The authors acknowledge that the VLM agent's performance may be limited by the quality and diversity of the training data, particularly in scenarios involving highly complex or novel editing requests. They also note that while the model improves upon existing baselines, it may still struggle with ambiguous user inputs that lack sufficient context. Furthermore, the reliance on a structured edit plan may introduce rigidity in creative editing tasks, which could be a limitation for users seeking more freeform editing capabilities. The paper does not address potential computational overhead introduced by the VLM agent during inference.

**Why it matters**  
Aurora's approach to resolving textual and visual underspecification in video editing has significant implications for the field. By enabling more intuitive user interactions and reducing the burden of providing detailed input, this framework could democratize video editing, making it accessible to a broader audience. The integration of a tool-using agent also opens avenues for future research in human-AI collaboration, particularly in creative domains where user intent may be ambiguous. The findings could inspire further advancements in multimodal models and their applications in various content creation tasks.

Authors: Yongsheng Yu, Ziyun Zeng, Zhiyuan Xiao, Zhenghong Zhou, Hang Hua, Wei Xiong, Jiebo Luo  
Source: arXiv:2605.18748  
URL: [https://arxiv.org/abs/2605.18748v1](https://arxiv.org/abs/2605.18748v1)
