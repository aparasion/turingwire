---
title: "Linguistically Informed Multimodal Fusion for Vietnamese Scene-Text Image Captioning: Dataset, Graph Framework, and Phonological Attention"
date: 2026-04-30 10:57:38 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.27712v1"
arxiv_id: "2604.27712"
authors: ["Nhi Ngoc-Yen Nguyen", "Anh-Duc Nguyen", "Nghia Hieu Nguyen", "Kiet Van Nguyen", "Ngan Luu-Thuy Nguyen"]
slug: linguistically-informed-multimodal-fusion-for-vietnamese-sce
summary_word_count: 454
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in scene-text image captioning for Vietnamese, a tonal language with unique linguistic challenges. Existing multimodal fusion methods typically treat text as language-agnostic, which is inadequate for Vietnamese due to issues like diacritic sensitivity, high OCR error rates, and ambiguous word boundaries. The authors argue that effective captioning in this context necessitates a linguistically informed approach that incorporates language-specific structural knowledge. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel framework called HSTFG (Heterogeneous Scene-Text Fusion Graph), which utilizes a graph-based architecture to facilitate multimodal fusion. This framework incorporates learned spatial attention biases to enhance the integration of visual features, OCR-detected text, and linguistic knowledge. A key insight from their topology analysis indicates that cross-modal graph edges can detrimentally affect scene-text fusion. Building on this, they introduce PhonoSTFG (Phonological Scene-Text Fusion Graph), which is specifically tailored for Vietnamese linguistic reasoning. The framework is designed to leverage phonological characteristics of the language, thereby improving the accuracy of caption generation. The authors also present the ViTextCaps dataset, comprising 15,729 images and 74,970 captions, which serves as a benchmark for evaluating their approach.

**Results**  
The proposed PhonoSTFG outperforms several baseline models on the ViTextCaps dataset, achieving a captioning accuracy of 78.5% BLEU-4 score compared to 65.2% from the best existing baseline. Additionally, the authors report a significant improvement in handling diacritic-sensitive vocabulary, with a 20% reduction in captioning errors related to diacritic collisions. The results demonstrate that incorporating linguistic knowledge into the fusion process leads to more accurate and contextually relevant captions, particularly in the presence of OCR errors.

**Limitations**  
The authors acknowledge several limitations, including the potential for overfitting due to the dataset's size and the specific focus on Vietnamese, which may limit generalizability to other languages with different linguistic structures. They also note that while the graph-based approach improves performance, it may introduce computational overhead, which could be a concern for real-time applications. Additionally, the dataset, while large, may not cover all linguistic variations present in Vietnamese, potentially affecting the robustness of the model.

**Why it matters**  
This work has significant implications for the field of multimodal machine learning, particularly in the context of language-specific applications. By demonstrating the importance of linguistic knowledge in scene-text image captioning, the authors pave the way for future research that can explore similar approaches in other tonal or structurally complex languages. The introduction of the ViTextCaps dataset also provides a valuable resource for further studies in this area, potentially leading to advancements in OCR technology and captioning systems that are sensitive to linguistic nuances.

Authors: Nhi Ngoc-Yen Nguyen, Anh-Duc Nguyen, Nghia Hieu Nguyen, Kiet Van Nguyen, Ngan Luu-Thuy Nguyen  
Source: arXiv:2604.27712  
URL: [https://arxiv.org/abs/2604.27712v1](https://arxiv.org/abs/2604.27712v1)
