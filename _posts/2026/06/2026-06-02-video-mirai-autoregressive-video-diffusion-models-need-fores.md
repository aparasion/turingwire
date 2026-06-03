---
title: "Video-Mirai: Autoregressive Video Diffusion Models Need Foresight"
date: 2026-06-02 17:55:13 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2606.03971v1"
arxiv_id: "2606.03971"
authors: ["Yonghao Yu", "Lang Huang", "Runyi Li", "Zerun Wang", "Toshihiko Yamasaki"]
slug: video-mirai-autoregressive-video-diffusion-models-need-fores
summary_word_count: 431
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces Video-Mirai, a method that enhances autoregressive video diffusion models by incorporating foresight to improve future frame consistency."
---

**Problem**  
The paper addresses a critical gap in the training of causal video generators, specifically the representation-level planning gap. Existing autoregressive video diffusion models typically rely solely on past frames for generating future content, which can lead to inconsistencies in identity, layout, and motion across generated segments. This work is particularly relevant as it is a preprint and has not undergone peer review, indicating that the findings should be interpreted with caution.

**Method**  
Video-Mirai proposes a novel training paradigm that integrates foresight into the autoregressive generation process without altering the causal inference mechanism. The method involves three key components: a frozen foresight encoder that processes the completed rollout non-causally, a lightweight predictor that distills the foresight encoder's output into causal states, and the original generator architecture that remains unchanged during inference. The training process utilizes future frames to supervise the representations, ensuring that the generated segments maintain consistency with future content. The authors do not disclose specific training compute details, but the method is designed to preserve per-step FLOPs and KV-cache behavior of the original model.

**Results**  
Video-Mirai demonstrates significant improvements over a strong Causal-Forcing baseline on the VBench benchmark. The Total Score for 5-second video rollouts increases from 83.8 to 84.6. For 30-second rollouts, subject consistency improves from 84.9 to 88.5, while background consistency rises from 90.2 to 91.9. These results indicate that the incorporation of future-conditioned targets is a crucial factor in enhancing the model's performance, as confirmed by ablation studies. The improvements are statistically significant, showcasing the effectiveness of the proposed method in addressing the identified planning gap.

**Limitations**  
The authors acknowledge that their approach is limited to the training phase and does not modify the inference process, which may restrict its applicability in scenarios requiring real-time generation. Additionally, the reliance on a frozen foresight encoder may limit the adaptability of the model to dynamic environments where future frames are highly variable. The paper does not explore the potential computational overhead introduced during the training phase, which could be a concern for large-scale applications.

**Why it matters**  
The findings of this study have significant implications for the development of more robust video generation models that can maintain consistency over longer sequences. By demonstrating that visual autoregressive models can benefit from foresight, this work paves the way for future research into integrating predictive capabilities into generative models. This approach could enhance applications in video synthesis, animation, and other domains requiring coherent temporal continuity. The insights presented in this paper contribute to the ongoing discourse on improving causal inference in generative models, as discussed in related works available on [arXiv](https://arxiv.org/abs/2606.03971v1).
