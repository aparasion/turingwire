---
title: "Masked Generative Transformer Is What You Need for Image Editing"
date: 2026-05-11 17:05:52 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: major
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.10859v1"
arxiv_id: "2605.10859"
authors: ["Wei Chow", "Linfeng Li", "Xian Sun", "Lingdong Kong", "Zefeng Li", "Qi Xu"]
slug: masked-generative-transformer-is-what-you-need-for-image-edi
summary_word_count: 408
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of diffusion models in image editing, particularly their global denoising mechanism, which inadvertently causes modifications to propagate into surrounding areas that should remain unchanged. The authors propose a novel approach using Masked Generative Transformers (MGTs) to confine edits to specific regions, thereby mitigating the issue of unintended alterations. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the EditMGT framework, which utilizes MGTs for localized token prediction. The architecture incorporates multi-layer attention consolidation to aggregate cross-attention maps, generating precise localization signals for edits. Additionally, the method employs region-hold sampling to prevent token flipping in non-target areas, ensuring that only the intended regions are modified. The authors introduce a new dataset, CrispEdit-2M, consisting of 2 million high-resolution samples (>1024 pixels) across seven categories, which supports the training of the model. EditMGT is designed with 960 million parameters, optimizing both performance and computational efficiency.

**Results**  
EditMGT achieves state-of-the-art performance in image similarity metrics across multiple benchmarks, outperforming existing diffusion-based methods. The authors report a 6x increase in editing speed compared to these baselines, highlighting the efficiency of their approach. Specific performance metrics are not disclosed in the abstract, but the results indicate a significant improvement in both speed and accuracy, suggesting a robust capability for localized image editing.

**Limitations**  
The authors acknowledge that while EditMGT excels in localized editing, it may still face challenges in handling complex scenes where multiple edits are required simultaneously. Additionally, the reliance on a large dataset (CrispEdit-2M) may limit the model's generalizability to domains with less available data. The paper does not discuss potential biases in the dataset or the implications of training on high-resolution images, which could affect the model's performance in lower-resolution contexts.

**Why it matters**  
The introduction of MGTs for image editing represents a significant shift in methodology, offering a viable alternative to diffusion models that have dominated the field. By enabling precise control over localized edits, this work opens avenues for more sophisticated image manipulation techniques in various applications, including graphic design, content creation, and augmented reality. The efficiency gains also suggest potential for real-time editing applications, which could enhance user experience in interactive environments. Overall, this research lays the groundwork for future explorations into transformer-based architectures in image processing tasks.

Authors: Wei Chow, Linfeng Li, Xian Sun, Lingdong Kong, Zefeng Li, Qi Xu, Hang Song, Tian Ye et al.  
Source: arXiv:2605.10859  
URL: [https://arxiv.org/abs/2605.10859v1](https://arxiv.org/abs/2605.10859v1)
