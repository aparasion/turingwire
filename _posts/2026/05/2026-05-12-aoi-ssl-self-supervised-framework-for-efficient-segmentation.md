---
title: "AOI-SSL: Self-Supervised Framework for Efficient Segmentation of Wire-bonded Semiconductors In Optical Inspection"
date: 2026-05-12 17:27:25 +0000
category: research
subcategory: efficiency_inference
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.12430v1"
arxiv_id: "2605.12430"
authors: ["Joaqu\u00edn Figueira", "Rob Van Gastel", "Giacomo D'Amicantonio", "Zhuoran Liu", "Ioan Gabriel Bucur", "Faysal Boughorbel"]
slug: aoi-ssl-self-supervised-framework-for-efficient-segmentation
summary_word_count: 422
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of segmentation in automated optical inspection (AOI) of wire-bonded semiconductors, which typically requires device-specific models that necessitate retraining with new devices or under distribution shifts. The authors propose AOI-SSL, a self-supervised learning framework that aims to reduce the reliance on labeled data and improve training efficiency. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of AOI-SSL is the integration of small-domain self-supervised pre-training of vision transformers with in-context inference techniques. The authors pre-train state-of-the-art self-supervised algorithms, specifically focusing on Masked Autoencoders, on a small industrial inspection dataset. This pre-training is designed to enhance downstream segmentation tasks while minimizing the need for extensive labeled fine-tuning. The framework employs patch-level retrieval methods that predict segmentation masks directly from dense encoder embeddings, which allows for efficient inference with minimal additional training. Notably, the authors demonstrate that a simple similarity-based retrieval method achieves performance comparable to more complex attention-based aggregation techniques currently prevalent in the literature.

**Results**  
The experimental results indicate that self-supervised pre-training significantly enhances segmentation quality compared to both training from scratch and using ImageNet-pretrained backbones, all while adhering to a fixed fine-tuning computational budget. Specifically, the retrieval-based segmentation approach outperforms traditional fine-tuning methods when applied to single device images, facilitating rapid adaptation to challenging samples. The paper reports that the proposed method achieves a notable improvement in segmentation accuracy, although specific numerical results and comparisons to named baselines are not detailed in the abstract.

**Limitations**  
The authors acknowledge that the effectiveness of AOI-SSL is contingent on the availability of a small industrial inspection dataset for pre-training. They also note that while the method excels in single-device scenarios, its performance in multi-device contexts or under more diverse distribution shifts remains to be evaluated. Additionally, the reliance on self-supervised pre-training may not generalize across all types of semiconductor devices, which could limit the framework's applicability.

**Why it matters**  
The implications of this work are significant for the field of automated optical inspection and machine learning in industrial applications. By reducing the need for extensive labeled datasets and enabling rapid adaptation to new devices, AOI-SSL could streamline the deployment of segmentation models in real-world settings. This approach not only enhances the efficiency of model training but also opens avenues for further research into self-supervised learning techniques in other domains where labeled data is scarce or expensive to obtain.

Authors: Joaquín Figueira, Rob Van Gastel, Giacomo D'Amicantonio, Zhuoran Liu, Ioan Gabriel Bucur, Faysal Boughorbel, Egor Bondarev  
Source: arXiv:2605.12430  
URL: [https://arxiv.org/abs/2605.12430v1](https://arxiv.org/abs/2605.12430v1)
