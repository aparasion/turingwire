---
title: "Detecting overfitting in Neural Networks during long-horizon grokking using Random Matrix Theory"
date: 2026-05-12 16:57:48 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.12394v1"
arxiv_id: "2605.12394"
authors: ["Hari K. Prakash", "Charles H Martin"]
slug: detecting-overfitting-in-neural-networks-during-long-horizon
summary_word_count: 484
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of detecting overfitting in neural networks (NNs) during long-horizon grokking, a phenomenon where models achieve high training accuracy while test accuracy declines. Existing methods for overfitting detection typically require access to training or test data, which limits their applicability. The authors propose a novel approach using Random Matrix Theory (RMT) to identify overfitting without direct data access, filling a critical gap in the literature regarding the detection of overfitting dynamics in deep learning models.

**Method**  
The core technical contribution is the introduction of a method based on RMT to detect overfitting through the analysis of the spectral properties of weight matrices in neural network layers. The authors randomize each weight matrix element-wise, transforming it from \(\mathbf{W}\) to \(\mathbf{W}_{\mathrm{rand}}\). They then fit the empirical spectral distribution of the randomized weights to a Marchenko-Pastur distribution, identifying outliers that indicate deviations from self-averaging behavior. These outliers, termed "Correlation Traps," signal the onset of overfitting. The authors also propose an empirical method to differentiate between benign and harmful Correlation Traps by evaluating the Jensen-Shannon (JS) divergence of output logits when random data is passed through the trained model. This approach allows for the detection of the "anti-grokking" phase, characterized by high training accuracy coupled with declining test accuracy.

**Results**  
The authors demonstrate that during the anti-grokking phase, the number and scale of Correlation Traps increase as test accuracy decreases, while training accuracy remains high. They provide empirical evidence that some foundation-scale large language models (LLMs) exhibit similar Correlation Traps, suggesting potential overfitting issues. While specific numerical results and comparisons to baseline models are not detailed in the abstract, the findings indicate a structural distinction between the anti-grokking phase and the pre-grokking phase, highlighting the importance of monitoring these metrics during training.

**Limitations**  
The authors acknowledge that their method relies on the assumption that the spectral properties of weight matrices can effectively indicate overfitting, which may not hold for all architectures or training regimes. Additionally, the empirical approach to distinguishing between benign and harmful Correlation Traps may introduce variability based on the random data used. The study does not address the computational overhead associated with the RMT analysis, which could limit its practicality in large-scale applications. Furthermore, the implications of Correlation Traps on model interpretability and robustness are not fully explored.

**Why it matters**  
This work has significant implications for the development of more robust training methodologies in deep learning. By providing a method to detect overfitting without requiring access to training or test data, the authors enable practitioners to monitor model performance more effectively during training. The identification of Correlation Traps could lead to improved generalization in neural networks, particularly in long-horizon tasks where overfitting is prevalent. This research opens avenues for further exploration of RMT applications in machine learning and may influence future architectures and training strategies to mitigate overfitting.

Authors: Hari K. Prakash, Charles H Martin  
Source: arXiv:2605.12394  
URL: https://arxiv.org/abs/2605.12394v1
