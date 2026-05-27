---
title: "Detectability in Diversity: Improved Canary Crafting for Privacy Auditing in One Run"
date: 2026-05-26 17:06:14 +0000
category: research
subcategory: privacy_auditing
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.27292v1"
arxiv_id: "2605.27292"
authors: ["Mathieu Dagr\u00e9ou", "Aur\u00e9lien Bellet"]
slug: detectability-in-diversity-improved-canary-crafting-for-priv
summary_word_count: 405
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in privacy auditing methodologies, specifically focusing on the efficiency of crafting "canary" points for membership inference attacks (MIAs) in machine learning models. The authors highlight the limitations of existing one-run auditing methods, which typically suffer from high computational costs and suboptimal leakage estimates due to interference among canaries. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel approach to canary crafting that optimizes for both detectability and minimal interference. The method begins with a greedy initialization based on influence functions, which helps identify canaries that are likely to be detectable. This is followed by a bilevel optimization procedure that aims to maximize the distinguishability of the canaries while ensuring diversity in the embedding space. The optimization process is computationally efficient, allowing for the use of bilevel algorithms that can handle the dual objectives effectively. The paper does not disclose specific training compute requirements but emphasizes the reduced computational burden compared to traditional methods.

**Results**  
The proposed method demonstrates significant improvements in privacy leakage estimates when evaluated against established baselines in the context of one-run privacy auditing. The authors report that their approach yields stronger leakage estimates with lower computational costs compared to previous canary crafting techniques. While specific numerical results and effect sizes are not detailed in the abstract, the implication is that the method outperforms existing approaches in both accuracy and efficiency.

**Limitations**  
The authors acknowledge that their method may still be susceptible to certain types of adversarial attacks that exploit the underlying assumptions of the canary crafting process. Additionally, the reliance on influence functions for initialization may introduce biases depending on the model architecture and dataset used. The paper does not address the scalability of the method to larger datasets or more complex models, which could be a potential limitation in practical applications.

**Why it matters**  
This work has significant implications for the field of privacy auditing in machine learning, particularly in enhancing the efficiency and effectiveness of one-run auditing methods. By improving the detectability of canaries while minimizing interference, the proposed approach could lead to more accurate assessments of privacy leakage, thereby informing the design of differential privacy mechanisms. This advancement is crucial for researchers and practitioners aiming to ensure robust privacy guarantees in machine learning applications, especially in sensitive domains such as healthcare and finance.

Authors: Mathieu Dagréou, Aurélien Bellet  
Source: arXiv:2605.27292  
URL: https://arxiv.org/abs/2605.27292v1
