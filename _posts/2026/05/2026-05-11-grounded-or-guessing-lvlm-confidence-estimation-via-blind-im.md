---
title: "Grounded or Guessing? LVLM Confidence Estimation via Blind-Image Contrastive Ranking"
date: 2026-05-11 17:35:10 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.10893v1"
arxiv_id: "2605.10893"
authors: ["Reza Khanmohammadi", "Erfan Miahi", "Simerjot Kaur", "Charese H. Smiley", "Ivan Brugere", "Kundan Thind"]
slug: grounded-or-guessing-lvlm-confidence-estimation-via-blind-im
summary_word_count: 467
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the issue of visual ungroundedness in large vision-language models (LVLMs), where models can generate confident responses based solely on language priors, neglecting the visual input. Existing confidence estimation methods fail to discern whether a prediction is influenced by the image or is merely a product of textual cues. This gap in capability highlights the need for a robust mechanism to evaluate the reliability of predictions in LVLMs, particularly in applications requiring high-stakes decision-making.

**Method**  
The authors propose a novel confidence estimation framework called Blind-Image Contrastive Ranking (BICR). This model-agnostic approach involves extracting hidden states from a frozen LVLM in two scenarios: with the actual image-question pair and with the image blacked out while keeping the question constant. A lightweight probe is then trained on the hidden states from the real image, utilizing a ranking loss that penalizes higher confidence scores associated with the blacked-out view. This method effectively teaches the model to associate visual grounding with prediction reliability without incurring additional inference costs. The training process leverages contrastive learning principles to enhance the model's ability to discern when visual information is genuinely contributing to the prediction.

**Results**  
BICR was evaluated across five contemporary LVLMs and compared against seven baseline methods on a comprehensive benchmark that includes tasks such as visual question answering, object hallucination detection, medical imaging, and financial document understanding. The results indicate that BICR achieves the best average performance across all LVLMs in terms of both calibration and discrimination. Specifically, it demonstrates statistically significant improvements in discrimination capabilities, with effect sizes robust to cluster-aware analysis, achieving these results with 4-18 times fewer parameters than the most effective probing baseline.

**Limitations**  
The authors acknowledge that while BICR improves confidence estimation, it may not fully eliminate the risk of visual ungroundedness in all contexts. The reliance on a frozen LVLM could limit the adaptability of the probe to different model architectures or tasks. Additionally, the framework's performance may vary depending on the quality and diversity of the training data used for the probe. The authors do not discuss potential biases in the training data or the implications of deploying BICR in real-world applications, which could affect its generalizability.

**Why it matters**  
The introduction of BICR has significant implications for the development of more reliable LVLMs, particularly in critical domains such as healthcare and finance, where the consequences of ungrounded predictions can be severe. By providing a mechanism to assess the reliability of model outputs based on visual grounding, this work paves the way for enhanced interpretability and trustworthiness in AI systems. Future research can build on this framework to further refine confidence estimation techniques and explore their integration into existing LVLM architectures.

Authors: Reza Khanmohammadi, Erfan Miahi, Simerjot Kaur, Charese H. Smiley, Ivan Brugere, Kundan Thind, Mohammad M. Ghassemi  
Source: arXiv:2605.10893  
URL: https://arxiv.org/abs/2605.10893v1
