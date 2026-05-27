---
title: "How and What to Imagine? Visual Thinking in Unified Multimodal Models for Cross-View Spatial Reasoning"
date: 2026-05-26 17:20:05 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.27310v1"
arxiv_id: "2605.27310"
authors: ["Qian Yang", "Ankur Sikarwar", "Huy Le", "Le Zhang", "Zhuan Shi", "Perouz Taslakian"]
slug: how-and-what-to-imagine-visual-thinking-in-unified-multimoda
summary_word_count: 435
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of vision-language models (VLMs) in cross-view spatial reasoning, where models often fail to leverage fine-grained geometric information due to an over-reliance on language. The authors identify a gap in the effective integration of visual thinking—specifically, the generation of intermediate thinking images—into the reasoning process. Previous approaches have shown that models frequently neglect visual evidence in these generated traces, prompting the need for a more effective method of visual reasoning in unified multimodal models (UMMs).

**Method**  
The authors introduce a novel training intervention called View Dropout (VDrop), which selectively occludes parts of one input view during training while allowing these occluded parts to remain visible to the generated thinking-image tokens. This mechanism encourages the model to utilize the thinking image for answer prediction rather than solely depending on the input views. To evaluate the effectiveness of different types of visual thinking, the authors explore three variants of thinking images: top-down, panoramic, and point-matching renderings. The models are trained on synthetic scenes, and the evaluation is conducted across five real-world out-of-domain benchmarks, focusing on the learnability-informativeness tradeoff of the different visual thinking approaches.

**Results**  
The results indicate that the panoramic visual thinking variant, when combined with VDrop, significantly outperforms other configurations in terms of both informativeness and learnability. Specifically, this configuration achieves the highest out-of-domain generalization performance across the evaluated benchmarks. The authors report that panoramic visual thinking with VDrop leads to a marked improvement in reasoning accuracy, although specific numerical performance metrics against baseline models are not disclosed in the abstract.

**Limitations**  
The authors acknowledge that their approach relies on synthetic scenes for training, which may not fully capture the complexities of real-world scenarios. Additionally, while VDrop enhances the model's reliance on visual thinking, the specific mechanisms by which different types of visual thinking contribute to performance improvements are not exhaustively analyzed. The paper does not address potential computational overhead introduced by the VDrop mechanism or the scalability of the proposed methods to larger datasets or more complex reasoning tasks.

**Why it matters**  
This work has significant implications for the development of more robust VLMs capable of effective cross-view spatial reasoning. By demonstrating the importance of visual thinking and introducing a method to enhance its utility, the authors pave the way for future research that could further refine multimodal reasoning capabilities. The findings suggest that integrating visual reasoning strategies can lead to improved generalization in real-world applications, which is critical for tasks such as autonomous navigation, robotic manipulation, and augmented reality.

Authors: Qian Yang, Ankur Sikarwar, Huy Le, Le Zhang, Zhuan Shi, Perouz Taslakian, Aishwarya Agrawal  
Source: arXiv:2605.27310  
URL: https://arxiv.org/abs/2605.27310v1
