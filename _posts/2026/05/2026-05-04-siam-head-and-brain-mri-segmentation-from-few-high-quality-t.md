---
title: "SIAM: Head and Brain MRI Segmentation from Few High-Quality Templates via Synthetic Training"
date: 2026-05-04 15:37:12 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.02737v1"
arxiv_id: "2605.02737"
authors: ["Romain Valabregue", "Ines Khemir", "Eric Badinet", "Fran\u00e7ois Rousseau", "Guillaume Auzias", "Reuben Dorent"]
slug: siam-head-and-brain-mri-segmentation-from-few-high-quality-t
summary_word_count: 434
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing synthetic training methods for brain MRI segmentation, which typically rely on large datasets of automatically labeled templates. These methods introduce systematic biases and lack flexibility in accommodating new anatomical structures. The authors propose the Segment It All Model (SIAM), which is trained using only six high-quality, manually annotated templates, thereby filling a gap in the literature regarding efficient and flexible segmentation of both brain and extra-cerebral tissues.

**Method**  
SIAM is a 3D segmentation framework designed to segment 16 anatomical structures, including both brain and extra-cerebral tissues such as cerebrospinal fluid, vessels, dura mater, skull, and skin. The model employs an innovative approach that extends domain randomization to both intensity and shape domains. This involves generating synthetic images that ensure contrast variability and applying high-resolution spatial transformations to model anatomical differences, such as cortical thickness and deep nuclei morphology. The training process leverages only six manually annotated templates, significantly reducing the dependency on large labeled datasets. The architecture specifics, loss functions, and training compute details are not disclosed in the abstract.

**Results**  
SIAM was evaluated across eight heterogeneous datasets comprising 301 subjects, which included various MRI contrasts (T1-weighted, T2-weighted, CT) and a wide age range. The results indicate that SIAM matches or outperforms state-of-the-art segmentation methods for brain structures. Notably, it also extends automated segmentation capabilities to non-brain structures. The model demonstrates superior consistency across different imaging contrasts and repeated acquisitions, with improved sensitivity to subtle gray matter atrophy. Specific quantitative results, such as Dice coefficients or Hausdorff distances, are not provided in the abstract but are expected to be detailed in the full paper.

**Limitations**  
The authors acknowledge that the reliance on only six high-quality templates may limit the model's generalizability to anatomical variations not represented in the training set. Additionally, while the model shows improved performance across various contrasts, the potential for overfitting to the specific templates used is a concern. The abstract does not discuss computational efficiency or the time required for training and inference, which are critical for clinical applications.

**Why it matters**  
The development of SIAM has significant implications for the field of medical imaging, particularly in enhancing the automation of MRI segmentation tasks. By reducing the need for extensive labeled datasets, SIAM can facilitate the integration of new anatomical structures and improve the adaptability of segmentation models in clinical settings. This work may pave the way for future research focused on synthetic training methodologies and their application in other imaging modalities or anatomical regions.

Authors: Romain Valabregue, Ines Khemir, Eric Badinet, François Rousseau, Guillaume Auzias, Reuben Dorent  
Source: arXiv:2605.02737  
URL: https://arxiv.org/abs/2605.02737v1
