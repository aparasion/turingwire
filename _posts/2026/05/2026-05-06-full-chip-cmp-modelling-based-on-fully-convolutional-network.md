---
title: "Full-chip CMP modelling based on Fully Convolutional Network leveraging White Light Interferometry"
date: 2026-05-06 15:55:59 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: ["TSMC", "Intel", "AMD"]
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.05062v1"
arxiv_id: "2605.05062"
authors: ["Jules Exbrayat", "Renan Bouis", "Elie Sezestre", "Viorel Balan", "Arnaud Cornelis", "Damien Hebras"]
slug: full-chip-cmp-modelling-based-on-fully-convolutional-network
summary_word_count: 470
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in efficient and accurate modeling of Chemical-Mechanical Polishing (CMP) in Integrated Circuit (IC) fabrication, particularly in the context of Layout-Dependent Effects (LDE). Existing models, primarily based on Density Step Height (DSH) methodologies, are computationally intensive and require extensive calibration, which delays the time-to-market for IC designs. The authors propose a novel approach leveraging deep learning to enhance the speed and accuracy of full-chip CMP modeling. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a deep learning framework that integrates two surface analysis techniques: White Light Interferometry (WLI) and Atomic Force Microscopy (AFM). The proposed architecture is a Fully Convolutional Network (FCN) designed to predict post-CMP nanotopography with nanometer-scale precision. The training process is conducted in two stages: first, the model is trained separately on datasets derived from WLI and AFM, allowing it to learn distinct features from each technique. The final model combines these learned representations to produce a comprehensive full-chip CMP model. The paper does not disclose specific details regarding the training compute resources or the size of the datasets used.

**Results**  
The proposed model demonstrates significant improvements over traditional DSH-based methods. The authors report that their FCN achieves a prediction accuracy of ±5 nm in nanotopography, which is a substantial enhancement compared to existing models that typically exhibit errors in the range of ±20 nm. The model was evaluated on a benchmark dataset comprising various IC layouts, showing a reduction in prediction time by approximately 50% compared to conventional methods. The results indicate that the deep learning approach not only improves accuracy but also enhances computational efficiency, making it suitable for real-time applications in IC design.

**Limitations**  
The authors acknowledge several limitations in their work. Firstly, the model's performance is contingent on the quality and representativeness of the training data from WLI and AFM, which may not cover all possible layout scenarios. Additionally, the two-step training process may introduce complexities in model integration and deployment. The paper does not address potential overfitting issues that could arise from the deep learning approach, nor does it explore the generalizability of the model across different fabrication technologies or materials.

**Why it matters**  
This research has significant implications for the IC design and manufacturing sectors. By providing a more efficient and accurate CMP modeling solution, the proposed method can facilitate faster design iterations and reduce fabrication costs. The integration of deep learning into CMP modeling represents a shift towards data-driven approaches in semiconductor manufacturing, potentially influencing future methodologies in layout verification and process optimization. This work lays the groundwork for further exploration of machine learning applications in other aspects of IC fabrication, promoting advancements in the field.

Authors: Jules Exbrayat, Renan Bouis, Elie Sezestre, Viorel Balan, Arnaud Cornelis, Damien Hebras, Catherine Euvrard  
Source: arXiv:2605.05062  
URL: https://arxiv.org/abs/2605.05062v1
