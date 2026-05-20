---
title: "X-Ray cardiac angiographic vessel segmentation based on pixel classification using machine learning and region growing"
date: 2026-05-19 16:27:45 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.20073v1"
arxiv_id: "2605.20073"
authors: ["E O Rodrigues", "L O Rodrigues", "J J Lima", "D Casanova", "F Favarim", "E R Dosciatti"]
slug: x-ray-cardiac-angiographic-vessel-segmentation-based-on-pixe
summary_word_count: 449
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of accurate vessel segmentation in X-ray angiographic images, a critical task in medical imaging that impacts diagnosis and treatment planning. Existing methods, particularly unsupervised approaches, have limitations in accuracy and robustness, necessitating improved techniques that leverage pixel-level classification.

**Method**  
The authors propose a novel pixel-classification framework for vessel segmentation that integrates multiple textural features. Key components include:

- **Feature Extraction**: The method employs anisotropic diffusion, Hessian matrix-based features, mathematical morphology, and statistical measures derived from the pixel neighborhood to enhance the representation of vascular structures.
- **ELEMENT Methodology**: This innovative approach combines pixel classification with region-growing techniques, where the classification outcome of one pixel influences the classification of adjacent pixels, promoting spatial coherence in segmentation.
- **Classifier**: A Random Forests classifier is utilized to determine the likelihood of each pixel belonging to the vessel structure based on the extracted features.

The training process and specific computational resources used are not disclosed, but the methodology emphasizes a structured approach to pixel classification that enhances segmentation accuracy.

**Results**  
The proposed method achieves a segmentation accuracy of 95.48%, which is reported as the highest in the literature for this task. This performance surpasses that of existing unsupervised state-of-the-art methods, although specific baseline models and their respective accuracy metrics are not detailed in the paper. The effect size indicates a significant improvement, suggesting that the integration of advanced feature extraction and the ELEMENT methodology contributes substantially to the accuracy gains.

**Limitations**  
The authors acknowledge several limitations, including:

- **Generalizability**: The method's performance may vary across different datasets or imaging conditions not represented in the training set.
- **Computational Complexity**: The reliance on multiple feature extraction techniques and the Random Forests classifier may lead to increased computational demands, which could limit real-time application in clinical settings.
- **Lack of Comparison with Other Classifiers**: The study does not compare the Random Forests classifier with other potential classifiers, such as deep learning models, which may offer competitive or superior performance.

Additionally, the paper does not address the potential impact of noise and artifacts commonly present in X-ray angiograms on segmentation accuracy.

**Why it matters**  
This work has significant implications for the field of medical imaging, particularly in enhancing the precision of vessel segmentation in X-ray angiography. Improved segmentation accuracy can lead to better diagnostic outcomes and more effective treatment planning in cardiovascular medicine. Furthermore, the integration of pixel classification with region-growing techniques may inspire future research in other imaging modalities and applications, potentially leading to advancements in automated image analysis and interpretation.

Authors: E O Rodrigues, L O Rodrigues, J J Lima, D Casanova, F Favarim, E R Dosciatti, V Pegorini, L S N Oliveira et al.  
Source: arXiv:2605.20073  
[https://arxiv.org/abs/2605.20073v1](https://arxiv.org/abs/2605.20073v1)
