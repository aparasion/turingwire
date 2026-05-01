---
title: "Learning from Disagreement: Clinician Overrides as Implicit Preference Signals for Clinical AI in Value-Based Care"
date: 2026-04-30 15:30:47 +0000
category: research
subcategory: alignment_safety
company: "Anthropic"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.28010v1"
arxiv_id: "2604.28010"
authors: ["Prabhjot Singh", "Abhishek Gupta", "Chris Betz", "Abe Flansburg", "Brett Ives", "Sudeep Lama"]
slug: learning-from-disagreement-clinician-overrides-as-implicit-p
summary_word_count: 471
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in leveraging clinician overrides of clinical AI recommendations as implicit preference signals for improving clinical AI systems in value-based care. Existing literature primarily focuses on explicit feedback mechanisms, such as reinforcement learning from human feedback (RLHF), which may not fully capture the nuanced decision-making processes of domain experts. The authors propose a novel framework that utilizes override data, which is rich in contextual information and observable outcomes, to enhance the alignment of AI systems with clinical realities.

**Method**  
The authors introduce a formal framework that extends standard preference learning through three key contributions:  
1. **Override Taxonomy**: A five-category taxonomy that classifies override types, linking them to distinct model update targets. This categorization allows for more granular learning from clinician decisions.
2. **Preference Formulation**: A sophisticated preference model that conditions on patient state \(s\), organizational context \(c\), and clinician capability \(\kappa\). The capability \(\kappa\) is further decomposed into execution capability \(\kappa_{\text{exec}}\) and alignment capability \(\kappa_{\text{align}}\), enabling a more detailed understanding of clinician behavior.
3. **Dual Learning Architecture**: A joint training approach that alternates between optimizing a reward model and a capability model. This architecture mitigates suppression bias, which occurs when correct but challenging recommendations are systematically ignored due to clinician capability limitations.

The training environment is designed to exploit the unique properties of override data in chronic disease management, emphasizing longitudinal outcome measurement and aligned financial incentives to ensure that the learned reward model is aligned with patient trajectories rather than merely economic considerations.

**Results**  
The authors demonstrate the effectiveness of their framework through empirical evaluations, although specific numerical results and comparisons to baseline models are not detailed in the abstract. The framework is positioned as a significant advancement over traditional methods, particularly in its ability to utilize clinician overrides to inform model updates in a way that is sensitive to the complexities of clinical decision-making.

**Limitations**  
The authors acknowledge several limitations, including the potential for bias in override data and the challenge of generalizing findings across diverse clinical settings. They also note that the framework's reliance on longitudinal data may not be feasible in all healthcare environments. Additionally, the complexity of the dual learning architecture may introduce challenges in training stability and convergence.

**Why it matters**  
This work has significant implications for the development of clinical AI systems, particularly in value-based care contexts. By framing clinician overrides as implicit preference signals, the proposed framework enhances the ability of AI systems to learn from expert decisions, potentially leading to more accurate and contextually relevant recommendations. This approach could improve patient outcomes by ensuring that AI systems are better aligned with the realities of clinical practice, ultimately fostering a more effective integration of AI in healthcare decision-making.

Authors: Prabhjot Singh, Abhishek Gupta, Chris Betz, Abe Flansburg, Brett Ives, Sudeep Lama, Jung Hoon Son  
Source: arXiv:2604.28010  
URL: https://arxiv.org/abs/2604.28010v1
