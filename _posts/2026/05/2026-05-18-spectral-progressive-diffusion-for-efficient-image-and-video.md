---
title: "Spectral Progressive Diffusion for Efficient Image and Video Generation"
date: 2026-05-18 17:55:39 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.18736v1"
arxiv_id: "2605.18736"
authors: ["Howard Xiao", "Brian Chao", "Lior Yariv", "Gordon Wetzstein"]
slug: spectral-progressive-diffusion-for-efficient-image-and-video
summary_word_count: 444
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiencies in the generation of high-resolution images and videos using diffusion models, which typically generate content autoregressively in the frequency domain. The authors identify a gap in the literature regarding the redundancy of high-resolution computations on noise-dominated frequencies during the denoising process. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce Spectral Progressive Diffusion, a framework that progressively increases the resolution of generated content along the denoising trajectory of pretrained diffusion models. The core technical contributions include:

1. **Spectral Noise Expansion Mechanism**: This mechanism allows for the manipulation of noise in the frequency domain, enabling the model to focus on generating low-frequency components first, followed by high-frequency details.
   
2. **Optimal Resolution Schedule**: The authors derive a resolution schedule based on the model's power spectrum, which dictates how and when to increase the resolution during the denoising process.

3. **Training-Free Acceleration**: The framework allows for significant speedups without the need for retraining the model, making it applicable to existing pretrained models.

4. **Fine-Tuning Recipe**: A novel fine-tuning approach is proposed to further enhance both the efficiency and quality of the generated outputs.

**Results**  
The proposed method demonstrates substantial improvements in generation speed while maintaining visual fidelity. Specifically, the authors report speedups of up to 4x on state-of-the-art pretrained image generation models and 3x on video generation models compared to traditional diffusion approaches. The visual quality is preserved, with no significant degradation noted in qualitative assessments against baseline models. The benchmarks used for evaluation include standard datasets for image and video generation, although specific datasets and baseline models are not explicitly named in the summary.

**Limitations**  
The authors acknowledge that their method may not generalize to all types of diffusion models, particularly those that do not conform to the assumptions made regarding frequency domain behavior. Additionally, the reliance on pretrained models may limit the applicability of the framework to scenarios where such models are not available. The paper does not address potential issues related to the scalability of the method to extremely high-resolution outputs or the computational overhead associated with the initial spectral noise expansion.

**Why it matters**  
The implications of this work are significant for the field of generative modeling, particularly in applications requiring high-resolution outputs, such as image synthesis, video generation, and potentially real-time applications. By providing a method that accelerates the generation process while preserving quality, this framework could facilitate broader adoption of diffusion models in practical applications. Furthermore, the insights into frequency domain behavior may inspire future research into more efficient generative techniques and architectures.

Authors: Howard Xiao, Brian Chao, Lior Yariv, Gordon Wetzstein  
Source: arXiv:2605.18736  
URL: [https://arxiv.org/abs/2605.18736v1](https://arxiv.org/abs/2605.18736v1)
