---
title: "Improving Combined Detection and Classification of TEM Defects via Mask-Conditioned Latent Diffusion Augmentation"
date: 2026-06-01 17:38:47 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2606.02532v1"
arxiv_id: "2606.02532"
authors: ["Ni Li", "Nuohao Liu", "Ryan Jacobs", "Ajay Annamareddy", "Maciej P. Polak", "Kevin Field"]
slug: improving-combined-detection-and-classification-of-tem-defec
summary_word_count: 425
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper presents a mask-conditioned latent diffusion model for augmenting TEM image datasets, enhancing defect detection and classification performance."
---

**Problem**  
The paper addresses the challenge of limited high-quality labeled data in the analysis of microstructural defects in transmission electron microscopy (TEM) images, particularly for irradiated metal alloys. The authors note that existing methods often rely on manual annotations, which are time-consuming and may not scale effectively. This work is a preprint and has not undergone peer review, indicating that the findings should be interpreted with caution.

**Method**  
The authors propose a generative data augmentation technique utilizing a mask-conditioned latent diffusion model (LDM). This model synthesizes realistic TEM images along with automatically generated multi-class defect masks, eliminating the need for manual labeling. The LDM is trained on distributions derived from experimental masks, allowing for the generation of synthetic image-mask pairs. The generated data is then used to augment small experimental datasets containing 10, 50, and 100 labeled images. A Mask Regional Convolutional Neural Network (R-CNN) is employed for defect detection and classification, leveraging the augmented datasets to improve model performance.

**Results**  
The results indicate that the generative augmentation approach leads to modest improvements in model performance. Specifically, the harmonic mean of the detection and classification F1 scores shows an increase of up to 0.02 when compared to baseline models trained solely on the original datasets. The authors observe that the extent of improvement varies depending on the specific train/test data split, suggesting that the effectiveness of the augmentation may be context-dependent. The paper does not provide extensive quantitative comparisons against other augmentation techniques or state-of-the-art methods, which could further contextualize the results.

**Limitations**  
The authors acknowledge that the performance gains from the proposed method are relatively small, which may limit its practical applicability in scenarios requiring significant improvements. Additionally, the reliance on the quality of the learned distributions from experimental masks could introduce biases if the training data is not representative. The paper does not explore the scalability of the method to larger datasets or its performance across different microscopy techniques, which could be critical for broader adoption.

**Why it matters**  
This work highlights the potential of generative models to address data scarcity in microscopy-based image quantification tasks, particularly in materials science. By enabling the synthesis of labeled data without manual intervention, the proposed method could facilitate more robust training of deep learning models in similar domains. The findings suggest avenues for future research into targeted generative approaches that could further enhance model performance in defect detection and classification tasks. This is particularly relevant as the field continues to explore automated analysis techniques for complex imaging data, as discussed in related literature (see [arXiv cs.CV](https://arxiv.org/abs/2606.02532v1)).
