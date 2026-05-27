---
title: "PlayClass: Automated Play Behaviour Classification in Poultry"
date: 2026-05-26 17:13:36 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.27304v1"
arxiv_id: "2605.27304"
authors: ["Prince Ravi Leow", "Neil Scheidwasser", "Rebecca Oscarsson", "Per Jensen", "Samir Bhatt", "David Alejandro Duch\u00eane"]
slug: playclass-automated-play-behaviour-classification-in-poultry
summary_word_count: 465
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the underexplored area of positive welfare behaviors in poultry, specifically focusing on play behavior classification. Existing automated monitoring systems have predominantly concentrated on negative welfare indicators, creating a significant gap in the literature regarding the detection and analysis of positive behaviors such as play. The authors aim to fill this gap by developing a robust pipeline for classifying play behaviors from video data.

**Method**  
The proposed system, PlayClass, employs a multi-faceted approach to classify play behaviors in poultry using top-down video footage. The architecture integrates long-duration tracking facilitated by the Segment Anything Model (SAM) 3, which is guided by YOLO (You Only Look Once) for establishing chunk boundaries. This method minimizes identity errors during point-based prompting. For the classification of play actions, the pipeline utilizes frozen embeddings from both image and video foundation models. Notably, the authors found that while handcrafted motion features derived from tracked masks yielded competitive accuracy, the V-JEPA 2.1 model consistently outperformed other backbone architectures across various model scales. When combined with handcrafted features, V-JEPA 2.1 achieved a macro-averaged F$_1$ score of 77.0, indicating its effectiveness in distinguishing play behaviors.

**Results**  
The PlayClass pipeline demonstrated a macro-averaged F$_1$ score of 77.0 when utilizing the V-JEPA 2.1 model in conjunction with handcrafted features. This performance was benchmarked against various other models, with V-JEPA 2.1 showing superior results across different scales. The authors note that the dataset presents challenges, particularly due to the similarity in kinematic profiles between play sub-types and non-play behaviors, as well as issues related to inter-bird occlusion. These factors complicate the classification task, yet the results indicate a promising direction for automated play behavior detection.

**Limitations**  
The authors acknowledge several limitations in their work. The dataset remains challenging due to the overlap in kinematic profiles of play and non-play behaviors, which can lead to misclassification. Additionally, inter-bird occlusion poses a significant challenge in accurately tracking individual birds during play. The reliance on frozen embeddings may also limit the adaptability of the model to new or unseen behaviors. Furthermore, as this is a preprint, the findings have not yet undergone peer review, which may affect the robustness of the conclusions drawn.

**Why it matters**  
The development of PlayClass has significant implications for the field of animal welfare monitoring, particularly in poultry. By enabling the automated classification of positive behaviors such as play, this work contributes to a more comprehensive understanding of animal welfare. It opens avenues for further research into the relationship between play and overall well-being in poultry, potentially influencing husbandry practices and welfare assessments. The methodologies employed could also be adapted for similar applications in other animal species, thereby broadening the impact of this research.

Authors: Prince Ravi Leow, Neil Scheidwasser, Rebecca Oscarsson, Per Jensen, Samir Bhatt, David Alejandro Duchêne  
Source: arXiv:2605.27304  
URL: [https://arxiv.org/abs/2605.27304v1](https://arxiv.org/abs/2605.27304v1)
