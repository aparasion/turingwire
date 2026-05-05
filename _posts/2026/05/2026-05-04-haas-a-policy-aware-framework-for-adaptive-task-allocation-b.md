---
title: "HAAS: A Policy-Aware Framework for Adaptive Task Allocation Between Humans and Artificial Intelligence Systems"
date: 2026-05-04 17:09:21 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02832v1"
arxiv_id: "2605.02832"
authors: ["Vicente Pelechanoa", "Antoni Mestre", "Manoli Albert", "Miriam Gil"]
slug: haas-a-policy-aware-framework-for-adaptive-task-allocation-b
summary_word_count: 445
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the literature regarding adaptive task allocation between humans and AI systems, particularly in organizational contexts such as software engineering and manufacturing. Existing approaches typically treat task allocation as a binary decision, failing to capture the nuanced interplay of human and AI roles based on contextual factors like fatigue and task stakes. The authors propose a preprint framework, Human-AI Adaptive Symbiosis (HAAS), to explore this complex decision-making landscape.

**Method**  
HAAS comprises two main components: a rule-based expert system and a contextual-bandit learner. The expert system enforces governance constraints prior to any learning, ensuring that task allocation adheres to predefined operational guidelines. The contextual-bandit learner dynamically selects among various collaboration modes based on feedback from task outcomes. The framework incorporates five auditable cognitive dimensions to represent task-agent fit and a five-mode autonomy spectrum ranging from human-only to fully autonomous systems. The authors provide a reproducible benchmark that spans both software engineering and manufacturing domains, allowing for empirical evaluation of the framework's effectiveness.

**Results**  
The authors present three key empirical findings. First, they demonstrate that governance is a tunable design variable rather than a binary switch; tighter governance constraints can shift task assignments from fully autonomous AI to supervised human-AI collaborations, with specific domain-related costs and benefits. Second, in manufacturing contexts, stronger governance can enhance operational performance while simultaneously reducing worker fatigue, indicating a workload-buffering effect that challenges the conventional view of governance as merely an overhead. Third, the study reveals that no single governance setting is universally optimal; moderate governance becomes increasingly effective as the contextual-bandit learner gains experience within the governed action space. These findings suggest that HAAS can serve as a valuable pre-deployment tool for organizations to evaluate and refine human-AI allocation policies.

**Limitations**  
The authors acknowledge that their framework is still in the preprint stage and has not undergone peer review, which may limit its immediate applicability. Additionally, the empirical findings are context-specific, primarily focusing on software engineering and manufacturing, which may not generalize to other domains. The reliance on a contextual-bandit approach may also introduce variability based on the quality and quantity of feedback data available during training.

**Why it matters**  
The implications of HAAS extend to various fields where human-AI collaboration is critical. By providing a structured framework for adaptive task allocation, HAAS enables organizations to optimize the distribution of work between humans and AI, enhancing efficiency and oversight while mitigating fatigue. This work lays the groundwork for future research into governance mechanisms in human-AI systems, potentially influencing the design of more effective collaborative environments across diverse applications.

Authors: Vicente Pelechanoa, Antoni Mestre, Manoli Albert, Miriam Gil  
Source: arXiv cs.AI  
URL: https://arxiv.org/abs/2605.02832v1  
arXiv ID: 2605.02832
