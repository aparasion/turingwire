---
title: "Pixel-Level Pavement Distress Assessment Using Instance Segmentation"
date: 2026-05-25 17:53:23 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.26095v1"
arxiv_id: "2605.26095"
authors: ["Logan Dewick", "Bibesh Pyakurel", "Kong Pheng Yang", "Nazim Choudhury", "M. G. Sarwar Murshed"]
slug: pixel-level-pavement-distress-assessment-using-instance-segm
summary_word_count: 415
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in automated pavement distress assessment, which has traditionally relied on image-level classification or coarse bounding box detection. The authors argue that these methods lack the geometric precision required for effective maintenance quantification, particularly for thin, branching, and irregular cracks. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a vision-based pavement distress analysis system utilizing Mask R-CNN for instance segmentation. They evaluate their approach on the UWGB-StreetCrack dataset, which consists of field-collected roadway images annotated with polygon labels for various crack types, including longitudinal, transverse, alligator cracks, and potholes. The study employs five variants of the Detectron2-based Mask R-CNN architecture, with a consistent fine-tuning protocol across models. The best-performing model is identified as Mask R-CNN with a ResNet-101 Feature Pyramid Network (FPN) backbone. The training process and compute resources are not explicitly detailed, but the model's performance is benchmarked against a YOLO detector adapted from CSPDarknet53, which serves as a comparative baseline.

**Results**  
The Mask R-CNN model with ResNet-101 FPN achieved notable performance metrics: 84.23% precision, 90.04% recall, and an F1 score of 87.04% using a project-specific bounding-box matching protocol. Additionally, the model estimated an aggregate predicted crack-area fraction of 2.164%, closely aligning with the ground-truth value of 2.170%. In contrast, the YOLO detector reached significantly lower performance metrics, with 27.5% precision and 20.7% recall on the same validation protocol. These results underscore the effectiveness of instance segmentation for detailed pavement distress analysis compared to traditional detection methods.

**Limitations**  
The authors acknowledge several limitations, including challenges related to annotation consistency, class imbalance, confounder rejection, and the need for robust mask-level benchmarking. They do not address potential issues such as the generalizability of the model to different pavement types or conditions, the computational efficiency of the instance segmentation approach in real-time applications, or the scalability of the dataset for broader deployment.

**Why it matters**  
This work has significant implications for the field of automated infrastructure monitoring, particularly in enhancing the precision of pavement distress assessments. By demonstrating the efficacy of instance segmentation over traditional detection methods, the study paves the way for more accurate and efficient maintenance strategies in civil engineering. The findings may also inform future research on improving annotation practices and addressing class imbalance in similar datasets, ultimately contributing to the development of more robust machine learning models for infrastructure analysis.

Authors: Logan Dewick, Bibesh Pyakurel, Kong Pheng Yang, Nazim Choudhury, M. G. Sarwar Murshed  
Source: arXiv:2605.26095v1  
URL: [https://arxiv.org/abs/2605.26095v1](https://arxiv.org/abs/2605.26095v1)
