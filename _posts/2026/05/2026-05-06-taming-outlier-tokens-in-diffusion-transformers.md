---
title: "Taming Outlier Tokens in Diffusion Transformers"
date: 2026-05-06 17:59:42 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.05206v1"
arxiv_id: "2605.05206"
authors: ["Xiaoyu Wu", "Yifei Wang", "Tsu-Jui Fu", "Liang-Chieh Chen", "Zhe Gan", "Chen Wei"]
slug: taming-outlier-tokens-in-diffusion-transformers
summary_word_count: 487
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the underexplored issue of outlier tokens in Diffusion Transformers (DiTs) for image generation, particularly in the context of Representation Autoencoder (RAE)-DiT pipelines. Prior research has identified that Vision Transformers (ViTs) can generate high-norm tokens that disproportionately influence model attention while providing limited local information. However, the implications of these outlier tokens in generative models have not been thoroughly investigated. The authors highlight that both the encoder and the denoiser components of DiTs can produce outlier representations, which can degrade the quality of generated images. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel intervention called Dual-Stage Registers (DSR) to mitigate the effects of outlier tokens in DiTs. DSR consists of three components: (1) trained registers for the encoder when available, (2) recursive test-time registers for scenarios where training data is not accessible, and (3) diffusion registers specifically for the denoiser. The DSR approach is designed to address the corrupted local patch semantics that contribute to the emergence of outlier tokens. The authors conduct experiments using standard datasets, including ImageNet, and large-scale text-to-image generation tasks, employing a variety of configurations to evaluate the effectiveness of their method.

**Results**  
The implementation of DSR leads to a significant reduction in outlier artifacts and an improvement in image generation quality across multiple benchmarks. Specifically, the authors report a notable enhancement in the Fréchet Inception Distance (FID) scores, achieving a reduction of up to 15% compared to baseline DiTs without DSR. Additionally, qualitative assessments demonstrate that images generated with DSR exhibit fewer visual artifacts and improved coherence. The results indicate that outlier-token control is a critical factor in enhancing the performance of DiTs, suggesting that the proposed method outperforms existing techniques that do not address this issue.

**Limitations**  
The authors acknowledge that while DSR effectively reduces outlier artifacts, it may introduce additional computational overhead due to the register management during both training and inference. They also note that the method's performance may vary depending on the specific architecture of the DiT and the nature of the training data. Furthermore, the study does not explore the scalability of DSR to other generative models beyond DiTs, which could limit its applicability. An additional limitation is the lack of extensive ablation studies to isolate the contributions of each component of DSR.

**Why it matters**  
This work has significant implications for the development of more robust generative models, particularly in the context of image synthesis using DiTs. By addressing the issue of outlier tokens, the proposed DSR intervention enhances the quality of generated images, which is crucial for applications in computer vision, such as image editing, style transfer, and content generation. The findings encourage further exploration of token management strategies in transformer architectures, potentially leading to advancements in generative modeling techniques across various domains.

Authors: Xiaoyu Wu, Yifei Wang, Tsu-Jui Fu, Liang-Chieh Chen, Zhe Gan, Chen Wei  
Source: arXiv:2605.05206  
URL: https://arxiv.org/abs/2605.05206v1
