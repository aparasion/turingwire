---
title: "Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning"
date: 2026-05-05 16:51:28 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.03968v1"
arxiv_id: "2605.03968"
authors: ["Zakarya Elmimouni", "Fares Fourati", "Mohamed-Slim Alouini"]
slug: label-efficient-school-detection-from-aerial-imagery-via-wea
summary_word_count: 392
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of school detection from aerial imagery in regions with limited or outdated official records, which hampers educational infrastructure planning and connectivity initiatives. The authors highlight the gap in existing literature regarding scalable, automated methods for school detection that require minimal human annotations. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a weakly supervised framework that consists of two main stages: an automatic labeling pipeline and a fine-tuning process. The automatic labeling pipeline utilizes sparse location points to generate semantic segmentation masks, which are then converted into bounding boxes for training. The initial training stage employs these automatically labeled images to learn representations of school structures. Subsequently, a small set of 50 manually labeled images is used for fine-tuning the model, enhancing its performance on a clean dataset. The architecture specifics are not disclosed, but the method emphasizes efficiency in low-data regimes, minimizing the reliance on extensive human annotations.

**Results**  
The proposed framework demonstrates strong object detection performance, particularly in low-data scenarios. The models achieve significant detection accuracy using only 50 manually labeled images, outperforming traditional methods that require larger annotated datasets. While specific metrics (e.g., mAP, precision, recall) are not detailed in the abstract, the authors claim that their approach significantly reduces the need for costly annotations, thus enabling scalable school mapping efforts.

**Limitations**  
The authors acknowledge that their method relies on the quality of the automatically generated labels, which may introduce noise and affect detection accuracy. Additionally, the framework's performance in diverse geographic and environmental conditions is not thoroughly evaluated. The reliance on a small number of manually labeled images may also limit the generalizability of the model across different regions. Furthermore, the paper does not discuss potential biases in the automatically generated labels or the implications of using aerial imagery in various contexts.

**Why it matters**  
This research has significant implications for educational infrastructure development and connectivity initiatives, particularly in underserved areas. By providing a scalable and efficient method for school detection, the framework can facilitate better resource allocation and planning for educational services. The public release of models, training code, and auto-labeled data is expected to foster further research and real-world applications, potentially influencing policy decisions and investment in education-related infrastructure globally.

Authors: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini  
Source: arXiv:2605.03968  
URL: [https://arxiv.org/abs/2605.03968v1](https://arxiv.org/abs/2605.03968v1)
