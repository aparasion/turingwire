---
title: "Virtual Scanning for NSCLC Histology: Investigating the Discriminatory Power of Synthetic PET"
date: 2026-05-04 15:46:53 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02746v1"
arxiv_id: "2605.02746"
authors: ["Fatih Aksu", "Laura Ciuffetti", "Francesco Di Feola", "Filippo Ruffini", "Giulia Romoli", "Fabrizia Gelardi"]
slug: virtual-scanning-for-nsclc-histology-investigating-the-discr
summary_word_count: 437
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the capability of accurately differentiating between adenocarcinoma (ADC) and squamous cell carcinoma (SCC) in non-small cell lung cancer (NSCLC) using standard imaging techniques. While [$^{18}$F]FDG PET/CT is a conventional diagnostic tool, its application is hindered by high costs and radiation exposure. The authors propose a novel approach to enhance histological subtype classification by utilizing synthetic PET data to supplement anatomical CT scans, thereby potentially improving diagnostic accuracy without the drawbacks of traditional PET imaging.

**Method**  
The authors introduce a framework that employs a 3D Pix2Pix Generative Adversarial Network (GAN) to synthesize pseudo-PET volumes from anatomical CT scans. The GAN is pretrained on the FDG-PET/CT Lesions dataset, ensuring that the synthetic outputs retain relevant metabolic features. These synthetic PET volumes are then integrated with structural CT data using the MINT framework, which is a multi-stage intermediate fusion architecture designed to facilitate the combination of multimodal data. The training process and specific hyperparameters are not disclosed, but the architecture's design aims to enhance the feature representation for improved classification performance.

**Results**  
The proposed multimodal approach was evaluated on a multi-center dataset comprising 714 subjects. The integration of synthetic PET features led to a statistically significant improvement in classification performance compared to a CT-only baseline. Specifically, the Area Under the Curve (AUC) increased from 0.489 to 0.591, and the Geometric Mean (GMean) improved from 0.305 to 0.524. These results indicate that the synthetic PET scans provide valuable metabolic cues that enhance the model's ability to differentiate between histological subtypes, demonstrating the effectiveness of the proposed feature-enhancement strategy.

**Limitations**  
The authors acknowledge that the study is limited by the reliance on synthetic data, which may not fully capture the complexities of real PET scans. Additionally, the generalizability of the results to other datasets or clinical settings remains to be validated. The paper does not discuss potential biases in the training data or the implications of using synthetic data in clinical practice, which could affect the robustness of the findings.

**Why it matters**  
This work has significant implications for the field of medical imaging and cancer diagnosis. By demonstrating that synthetic PET data can enhance the classification of NSCLC histological subtypes, the study opens avenues for further research into virtual imaging techniques that could mitigate the limitations of traditional imaging modalities. The approach could lead to more accessible diagnostic tools, particularly in settings where physical PET scans are impractical or unavailable, ultimately contributing to personalized treatment strategies for lung cancer patients.

Authors: Fatih Aksu, Laura Ciuffetti, Francesco Di Feola, Filippo Ruffini, Giulia Romoli, Fabrizia Gelardi, Arturo Chiti, Valerio Guarrasi et al.  
Source: arXiv:2605.02746  
URL: https://arxiv.org/abs/2605.02746v1
