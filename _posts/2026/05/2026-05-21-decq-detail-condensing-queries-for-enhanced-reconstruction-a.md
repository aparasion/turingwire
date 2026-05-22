---
title: "DecQ: Detail-Condensing Queries for Enhanced Reconstruction and Generation in Representation Autoencoders"
date: 2026-05-21 17:34:04 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.22777v1"
arxiv_id: "2605.22777"
authors: ["Tianhang Wang", "Yitong Chen", "Wei Song", "Zuxuan Wu", "Min Li", "Jiaqi Wang"]
slug: decq-detail-condensing-queries-for-enhanced-reconstruction-a
summary_word_count: 405
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of Representation Autoencoders (RAEs) that utilize frozen vision foundation models (VFMs) as tokenizers. While these RAEs benefit from robust high-level representations, the freezing of VFMs restricts their spatial reconstruction capabilities, which hampers fine-grained generation and image editing. The authors note that fine-tuning the VFM to enhance reconstruction can disrupt the pretrained semantic space, leading to a degradation in generative fidelity. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose DecQ, a framework designed to enhance RAEs by introducing lightweight detail-condensing queries. These queries extract fine-grained information from intermediate features of the VFM through condenser modules. The architecture integrates these queries into the decoder, allowing them to work in conjunction with patch tokens during generative modeling. This dual approach aggregates information from both shallow and deep layers of the VFM, effectively addressing the trade-off between reconstruction quality and generative performance. The implementation requires only 8 additional queries and incurs a computational overhead of 3.9%.

**Results**  
DecQ demonstrates significant improvements over the baseline frozen DINOv2-based RAE. Specifically, the Peak Signal-to-Noise Ratio (PSNR) for reconstruction increases from 19.13 dB to 22.76 dB, indicating a substantial enhancement in reconstruction quality. For generative modeling, DecQ achieves a 3.3× faster convergence rate compared to the RAE, with a Fréchet Inception Distance (FID) of 1.41 without guidance and 1.05 with guidance. These results suggest that DecQ not only improves reconstruction fidelity but also accelerates the generative process.

**Limitations**  
The authors acknowledge that the proposed method relies on the architecture of the DINOv2 model, which may limit its generalizability to other VFMs. Additionally, while the computational overhead is minimal, the introduction of extra queries may still pose challenges in resource-constrained environments. The paper does not address potential issues related to the scalability of the approach or its performance on diverse datasets beyond those tested.

**Why it matters**  
The implications of this work are significant for the fields of image generation and editing, particularly in scenarios where high fidelity and fine-grained control are essential. By effectively balancing the trade-off between reconstruction and generation, DecQ opens avenues for further research into hybrid models that leverage both frozen and fine-tuned representations. This could lead to advancements in applications such as interactive image editing, content creation, and other domains where high-quality visual outputs are critical.

Authors: Tianhang Wang, Yitong Chen, Wei Song, Zuxuan Wu, Min Li, Jiaqi Wang  
Source: arXiv:2605.22777  
URL: [https://arxiv.org/abs/2605.22777v1](https://arxiv.org/abs/2605.22777v1)
