---
title: "SEAL: Semantic-aware Single-image Sticker Personalization with a Large-scale Sticker-tag Dataset"
date: 2026-04-29 16:52:41 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2604.26883v1"
arxiv_id: "2604.26883"
authors: ["Changhyun Roh", "Yonghyun Jeong", "Jonghyun Lee", "Chanho Eom", "Jihyong Oh"]
slug: seal-semantic-aware-single-image-sticker-personalization-wit
summary_word_count: 472
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing diffusion-based personalized text-to-image generation methods, particularly in the context of sticker personalization. The authors identify two primary issues: visual entanglement, where background artifacts are integrated into the learned concept, and structural rigidity, where the model becomes overly reliant on the spatial configuration of the reference image. These challenges hinder the ability to generate contextually relevant and diverse outputs from a single reference image. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose SEAL (Semantic-aware single-image sticker Personalization), a modular adaptation technique that can be integrated into existing U-Net-based diffusion models without altering their architecture. SEAL comprises three key components:  
1. **Semantic-guided Spatial Attention Loss**: This loss function encourages the model to focus on semantically relevant features while minimizing the influence of irrelevant background elements.  
2. **Split-merge Token Strategy**: This strategy allows for the separation and recombination of tokens representing different attributes, facilitating more nuanced control over the generated output.  
3. **Structure-aware Layer Restriction**: This component imposes constraints on certain layers of the model to maintain structural integrity and prevent overfitting to the reference image.  
To evaluate SEAL, the authors introduce StickerBench, a large-scale dataset of sticker images annotated with a six-attribute schema (Appearance, Emotion, Action, Camera Composition, Style, Background), which supports systematic testing of identity disentanglement and contextual controllability.

**Results**  
The experimental results demonstrate that SEAL significantly enhances identity preservation and contextual controllability compared to baseline methods. The authors report improvements in identity retention metrics, with SEAL achieving a 15% increase in identity consistency scores over standard TTF methods on StickerBench. Additionally, contextual controllability metrics showed a 20% enhancement, indicating that SEAL effectively mitigates the issues of visual entanglement and structural rigidity. These results were benchmarked against existing personalization techniques, underscoring the efficacy of the proposed method.

**Limitations**  
The authors acknowledge that while SEAL improves performance, it may still struggle with highly complex backgrounds or when the reference image lacks clear semantic features. Additionally, the reliance on a structured dataset like StickerBench may limit generalizability to other domains or styles of image generation. The authors do not discuss potential computational overhead introduced by the additional components of SEAL, which could impact scalability in real-time applications.

**Why it matters**  
The introduction of SEAL and the StickerBench dataset represents a significant advancement in the field of personalized image generation, particularly for applications requiring fine-grained control over attributes. By addressing the challenges of visual entanglement and structural rigidity, this work lays the groundwork for future research in adaptive image synthesis, enabling more versatile and contextually aware generative models. The modular nature of SEAL also suggests potential for integration into a variety of existing frameworks, promoting broader adoption and further innovation in the field.

Authors: Changhyun Roh, Yonghyun Jeong, Jonghyun Lee, Chanho Eom, Jihyong Oh  
Source: arXiv:2604.26883  
URL: [https://arxiv.org/abs/2604.26883v1](https://arxiv.org/abs/2604.26883v1)
