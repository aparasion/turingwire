---
title: "OphMAE: Bridging Volumetric and Planar Imaging with a Foundation Model for Adaptive Ophthalmological Diagnosis"
date: 2026-05-04 15:18:06 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02714v1"
arxiv_id: "2605.02714"
authors: ["Tienyu Chang", "Zhen Chen", "Renjie Liang", "Jinyu Ding", "Jie Xu", "Sunu Mathew"]
slug: ophmae-bridging-volumetric-and-planar-imaging-with-a-foundat
summary_word_count: 432
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing ophthalmic AI systems that primarily focus on single-modality inference, which does not align with clinical practices that utilize multiple imaging modalities for diagnosis. The authors highlight the need for a model that can integrate volumetric data from 3D Optical Coherence Tomography (OCT) with planar data from 2D en face OCT, particularly in resource-limited settings where advanced imaging hardware may not be available.

**Method**  
The core technical contribution is the Ophthalmic multimodal Masked Autoencoder (OphMAE), which employs a novel cross-modal fusion architecture and an adaptive inference mechanism. The model was pre-trained on a substantial dataset comprising 183,875 paired OCT images from 32,765 patients. The architecture leverages masked autoencoding techniques to learn generalizable representations across modalities. The training process and compute resources are not explicitly disclosed, but the scale of the dataset suggests significant computational requirements. The model's design allows it to adaptively maintain high diagnostic accuracy even when limited to single-modality inputs.

**Results**  
OphMAE was evaluated on 17 diverse diagnostic tasks using a benchmark dataset of 48,340 paired OCT images from 8,191 patients. It achieved an Area Under the Curve (AUC) of 96.9% for Age-related Macular Degeneration (AMD) and 97.2% for Diabetic Macular Edema (DME), outperforming both existing single-modal and multimodal foundation models. Notably, when restricted to single-modality 2D inputs, the model still achieved a high AUC of 93.7% for AMD. Furthermore, it demonstrated exceptional data efficiency, retaining 95.7% AUC with only 500 labeled samples, indicating its robustness in scenarios with limited labeled data.

**Limitations**  
The authors acknowledge that while OphMAE shows strong performance across various tasks, the reliance on a large pre-training dataset may limit its applicability in settings where such data is scarce. Additionally, the model's performance in real-world clinical environments remains to be validated, as the study is based on retrospective data. The paper does not address potential biases in the dataset or the generalizability of the model across different populations or imaging devices.

**Why it matters**  
OphMAE represents a significant advancement in ophthalmic AI by bridging the gap between volumetric and planar imaging modalities, thus enhancing diagnostic capabilities in clinical practice. Its adaptability and data efficiency make it a promising tool for deployment in resource-limited settings, potentially democratizing access to advanced diagnostic technologies. This work lays the groundwork for future research into multimodal AI applications in ophthalmology and other medical fields, encouraging the development of models that can integrate diverse data sources for improved patient outcomes.

Authors: Tienyu Chang, Zhen Chen, Renjie Liang, Jinyu Ding, Jie Xu, Sunu Mathew, Amir Reza Hajrasouliha, Andrew J. Saykin et al.  
Source: arXiv:2605.02714  
URL: https://arxiv.org/abs/2605.02714v1
