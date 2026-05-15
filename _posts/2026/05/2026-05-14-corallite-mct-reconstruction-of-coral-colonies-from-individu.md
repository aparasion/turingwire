---
title: "CoralLite: μCT Reconstruction of Coral Colonies from Individual Corallites"
date: 2026-05-14 17:12:59 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.15093v1"
arxiv_id: "2605.15093"
authors: ["Jess Jones", "Leonardo Bertini", "Kenneth Johnson", "Erica Hendy", "Tilo Burghardt"]
slug: corallite-mct-reconstruction-of-coral-colonies-from-individu
summary_word_count: 416
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the capability to reconstruct individual corallites from μCT scans of coral colonies, which is crucial for understanding the growth dynamics of coral reefs. Existing methods lack a robust framework for segmenting and modeling the intricate structures of coral skeletons, particularly at the level of individual polyps. The authors present CoralLite, a novel dataset and baseline method for this task, filling a significant void in the literature regarding coral skeletal analysis.

**Method**  
The core technical contribution is the hybrid V-Trans-UNet architecture designed for segmenting μCT virtual slabs of coral colonies, specifically targeting the segmentation of corallites. The model is pre-trained on weakly annotated data and subsequently fine-tuned using fully annotated slice sections, which include over 8,000 manual annotations of corallite regions. The training process leverages topology-aware techniques to enhance the model's ability to maintain structural integrity during segmentation. The dataset comprises 697 μCT slices and 37 partial or full slice annotations, which are made publicly available alongside the model weights and source code to facilitate reproducibility and further research.

**Results**  
The proposed model achieves a topological accuracy of 0.94 and mean Dice scores of 0.77 on unseen slices from the same colony and projection axis. When tested on a different, biologically unrelated specimen, the model still performs with a mean Dice score of 0.63. These results demonstrate a significant improvement over existing segmentation methods, establishing a new baseline for corallite reconstruction from μCT data.

**Limitations**  
The authors acknowledge that their experiments are limited in scale and context, which may affect the generalizability of the results. The dataset is confined to specific coral species (\emph{Porites} sp.), and the model's performance on other coral types remains untested. Additionally, the reliance on manual annotations, while extensive, may introduce bias or variability in the training data. The authors do not discuss potential computational resource requirements for training the model, which could be a barrier for some researchers.

**Why it matters**  
The implications of this work are significant for marine biology and ecological research, as it provides a foundational tool for studying coral growth patterns and health. By enabling detailed 3D modeling of individual corallites, researchers can better understand the dynamics of coral colonies, including responses to environmental stressors and the impacts of climate change. The availability of the CoralLite dataset and model also paves the way for future advancements in coral research and machine learning applications in biological imaging.

Authors: Jess Jones, Leonardo Bertini, Kenneth Johnson, Erica Hendy, Tilo Burghardt  
Source: arXiv:2605.15093  
URL: https://arxiv.org/abs/2605.15093v1
