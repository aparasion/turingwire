---
title: "Confidence-Guided Diffusion Augmentation for Enhanced Bangla Compound Character Recognition"
date: 2026-05-11 17:51:46 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.10916v1"
arxiv_id: "2605.10916"
authors: ["Md. Sultan Al Rayhan", "Maheen Islam"]
slug: confidence-guided-diffusion-augmentation-for-enhanced-bangla
summary_word_count: 415
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of recognizing handwritten Bangla compound characters, which are characterized by complex structures, significant intra-class variation, and a scarcity of high-quality annotated datasets. Existing systems struggle with generalization across diverse writing styles, particularly for compound characters that include intricate ligatures and diacritical marks. The authors identify a gap in effective data augmentation techniques that can enhance model robustness in low-resource settings.

**Method**  
The authors propose a confidence-guided diffusion augmentation framework that integrates class-conditional diffusion modeling with classifier guidance. This framework synthesizes high-quality handwritten compound character samples. Key technical contributions include the incorporation of Squeeze-and-Excitation enhanced residual blocks within the U-Net backbone of the diffusion model, which improves feature extraction and representation. A confidence-based filtering mechanism is introduced, where pre-trained classifiers serve as quality gates to retain only the most class-consistent synthetic samples. The filtered synthetic images are then fused with the original training dataset to retrain multiple classification architectures, including ResNet50, DenseNet121, VGG16, and Vision Transformer. The training compute details are not disclosed, but the approach emphasizes quality-aware augmentation to enhance model performance.

**Results**  
The proposed method demonstrates significant performance improvements on the AIBangla compound character dataset. The best-performing model achieves a classification accuracy of 89.2%, which is a notable enhancement over the previous benchmark for AIBangla. The results indicate consistent improvements across various architectures: ResNet50, DenseNet121, VGG16, and Vision Transformer, although specific accuracy metrics for each architecture are not provided. The effect size is substantial, indicating that the confidence-guided diffusion augmentation framework effectively addresses the limitations of existing recognition systems.

**Limitations**  
The authors acknowledge that their approach relies on the availability of pre-trained classifiers for the confidence-based filtering mechanism, which may not be feasible in all scenarios. Additionally, the study is limited to the AIBangla dataset, which may not fully represent the diversity of handwritten Bangla characters in real-world applications. The authors do not discuss the computational efficiency of the proposed method, which could be a concern for deployment in resource-constrained environments.

**Why it matters**  
This work has significant implications for the field of handwritten character recognition, particularly in low-resource languages and scripts. By demonstrating that quality-aware diffusion augmentation can enhance model performance, the findings encourage further exploration of generative models in data-scarce scenarios. The proposed framework could be adapted to other languages and character sets facing similar challenges, potentially leading to broader advancements in the field of optical character recognition (OCR) and machine learning applications in linguistics.

Authors: Md. Sultan Al Rayhan, Maheen Islam  
Source: arXiv:2605.10916  
URL: https://arxiv.org/abs/2605.10916v1
