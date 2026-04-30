---
title: "KAYRA: A Microservice Architecture for AI-Assisted Karyotyping with Cloud and On-Premise Deployment"
date: 2026-04-29 16:35:31 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2604.26869v1"
arxiv_id: "2604.26869"
authors: ["Attila Pint\u00e9r", "Javier Rico", "Attila R\u00e9pai", "Jalal Al-Afandi", "Adrienn \u00c9va Borsy", "Andr\u00e1s Kozma"]
slug: kayra-a-microservice-architecture-for-ai-assisted-karyotypin
summary_word_count: 416
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the deployment of AI-assisted karyotyping systems within clinical cytogenetic laboratories, particularly focusing on the operational constraints that limit patient data egress. The authors present KAYRA, a microservice architecture designed to function effectively in both cloud and on-premise environments. This work is a preprint and has not yet undergone peer review.

**Method**  
KAYRA employs a multi-model architecture that integrates several state-of-the-art deep learning components: an EfficientNet-B5 combined with a U-Net for semantic segmentation, a Mask R-CNN (utilizing ResNet-50 with Feature Pyramid Networks) for instance detection, and a ResNet-18 for classification tasks. The architecture is orchestrated through a cascaded Region of Interest (ROI) narrowing strategy, which optimizes the focus of downstream models on chromosome-bearing regions. The system is containerized, allowing for seamless deployment in both cloud and on-premise settings. The training compute details are not disclosed, but the architecture is designed to meet the requirements of clinical environments.

**Results**  
In a pilot clinical evaluation involving 459 chromosomes from 10 metaphase spreads, KAYRA demonstrated a segmentation accuracy of 98.91%, significantly outperforming two commercial reference systems (78.21% and 40.52%). For classification, KAYRA achieved an accuracy of 89.1%, compared to 86.9% and 54.5% for the references. The rotation accuracy was recorded at 89.76%, against 94.55% and 78.43% for the competitors. Statistical significance was established for segmentation and classification improvements over the older density-thresholding reference (p < 0.0001), while the difference in classification accuracy against a modern AI-supported reference was not statistically significant (p = 0.34) at the current test-set size.

**Limitations**  
The authors acknowledge that the pilot study's sample size may limit the generalizability of the classification results against the modern AI reference. Additionally, the paper does not discuss the potential computational overhead associated with the microservice architecture or the implications of deploying in resource-constrained environments. The lack of peer review may also raise concerns regarding the robustness of the findings.

**Why it matters**  
KAYRA's architecture represents a significant advancement in the integration of AI into clinical cytogenetics, providing a flexible deployment model that can adapt to varying regulatory environments. The strong empirical performance on segmentation and classification tasks suggests that KAYRA could enhance diagnostic workflows in cytogenetic laboratories, potentially leading to improved patient outcomes. This work lays the groundwork for future research into scalable AI solutions in clinical settings, emphasizing the importance of human-in-the-loop systems for expert review in diagnostic processes.

Authors: Attila Pintér, Javier Rico, Attila Répai, Jalal Al-Afandi, Adrienn Éva Borsy, András Kozma, Hajnalka Andrikovics, György Cserey  
Source: arXiv:2604.26869  
URL: https://arxiv.org/abs/2604.26869v1
