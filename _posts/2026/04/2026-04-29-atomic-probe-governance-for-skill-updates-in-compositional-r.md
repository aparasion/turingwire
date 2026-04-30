---
title: "Atomic-Probe Governance for Skill Updates in Compositional Robot Policies"
date: 2026-04-29 13:56:11 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26689v1"
arxiv_id: "2604.26689"
authors: ["Xue Qin", "Simin Luan", "John See", "Cong Yang", "Zhijun Li"]
slug: atomic-probe-governance-for-skill-updates-in-compositional-r
summary_word_count: 453
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the literature regarding the dynamic updating of skill libraries in robotic systems. Existing compositional methods, such as BLADE, SymSkill, and Generative Skill Chaining, treat skill libraries as static during test time, failing to analyze how the replacement of a skill affects composition outcomes. The authors propose a novel approach to evaluate the impact of skill updates on performance, which is particularly relevant for real-world robotic applications where skills must be continuously refined.

**Method**  
The authors introduce a paired-sampling cross-version swap protocol applied to manipulation tasks in the robosuite environment. They investigate the dominant-skill effect, where one skill can significantly outperform others, impacting overall task success rates. The study employs an atomic-quality probe and a Hybrid Selector that combines low-cost per-skill probes with selective composition revalidation. The atomic-quality probe is designed to assess the effectiveness of skills without incurring the full computational cost of revalidation. The Hybrid Selector optimizes the trade-off between cost and accuracy, characterized through a Pareto frontier analysis across 144 skill-update decisions. The evaluation is conducted on dual-arm peg-in-hole and simpler pick tasks, with performance metrics reported as atomic success rates.

**Results**  
In the dual-arm peg-in-hole task, the dominant skill achieved an atomic success rate of 86.7%, while all other skills were at or below 26.7%. The presence of the dominant skill in a composition could shift the success rate by up to 50 percentage points (pp). In simpler tasks where all atomic policies reached 100% success, the effect of skill dominance was undefined. The atomic-only probe achieved a success rate of 64.6% compared to 87.5% for full revalidation, representing a 23pp gap at zero per-decision cost. The Hybrid Selector with m=10 reduced this gap to approximately 12pp while maintaining 46% of the full revalidation cost. Across 144 events, the atomic-only probe was within 3pp of full revalidation under a mixed-oracle condition.

**Limitations**  
The authors acknowledge that their approach may not generalize across all robotic tasks, particularly those with more complex skill interactions. They also note that off-policy behavioral distance metrics failed to identify the dominant skill, indicating potential limitations in existing evaluation methods. Additionally, the reliance on a specific set of tasks may restrict the applicability of their findings to broader robotic applications.

**Why it matters**  
This work introduces the atomic-quality probe as a principled, deployment-ready tool for skill-update governance in compositional robot policies. By enabling more efficient skill evaluation and selection, it has the potential to enhance the adaptability and performance of robotic systems in dynamic environments. The findings could inform future research on skill composition and governance, leading to more robust and flexible robotic applications.

Authors: Xue Qin, Simin Luan, John See, Cong Yang, Zhijun Li  
Source: arXiv:2604.26689  
URL: [https://arxiv.org/abs/2604.26689v1](https://arxiv.org/abs/2604.26689v1)
