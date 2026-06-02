---
title: "SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction"
date: 2026-06-01 17:45:39 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.02540v1"
arxiv_id: "2606.02540"
authors: ["Yuting Ning", "Zhehao Zhang", "Yash Kumar Lal", "Boyu Gou", "Junyi Li", "Weitong Ruan"]
slug: skillharm-lifecycle-aware-skill-based-attacks-via-automated-
summary_word_count: 403
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces SkillHarm, a benchmark for evaluating skill-based attacks in agents, highlighting vulnerabilities and proposing an automated attack construction pipeline."
---

**Problem**  
This work addresses the gap in understanding skill-based attacks on agents, particularly the lifecycle of skill usage and the associated risks. Previous studies have primarily focused on single-task execution and provided ad-hoc risk assessments without a systematic framework. The authors present SkillHarm, a comprehensive benchmark that evaluates skill-based attacks across the entire skill-use lifecycle, which is crucial for developing robust defenses against such vulnerabilities. This paper is a preprint and has not undergone peer review.

**Method**  
The authors propose two attack scenarios: Fixed-Payload Poisoning (FPP) and Self-Mutating Poisoning (SMP). FPP involves a poisoned skill package that directly compromises any task session invoking it, while SMP allows an initially benign skill to mutate over time, deferring harm until subsequent uses. The authors define 12 risk types based on the targeted components of the agent workflow, including data pipelines, system environments, and agent autonomy. To facilitate large-scale attack instantiation, they developed AutoSkillHarm, an automated construction pipeline utilizing coding agents driven by natural-language harnesses. The benchmark comprises 879 attack samples across 71 distinct skills, enabling a thorough evaluation of agent vulnerabilities.

**Results**  
The experiments reveal significant vulnerabilities in current agents, with attack success rates reaching 86.3% for FPP and 69.3% for SMP. Notably, the analysis indicates that many apparent failures of attacks are due to agents not engaging with the poisoned files rather than effective resistance. This highlights a critical flaw in the current understanding of agent defenses, as existing mitigation strategies do not reliably address these threats.

**Limitations**  
The authors acknowledge that their framework primarily focuses on the skill-use lifecycle and may not encompass all potential attack vectors. Additionally, the reliance on automated construction may introduce biases based on the natural-language harnesses used. The study does not explore the long-term implications of these attacks on agent performance or the potential for adaptive defenses. Furthermore, the benchmark's effectiveness in real-world scenarios remains to be validated.

**Why it matters**  
The introduction of SkillHarm and its systematic taxonomy of skill-based attack risks is a significant advancement in the field of agent security. By highlighting the vulnerabilities inherent in skill execution, this work lays the groundwork for future research aimed at developing more resilient agents. The findings underscore the necessity for improved defensive mechanisms against skill-based attacks, which could have far-reaching implications for the deployment of autonomous systems in sensitive environments. This research is crucial for informing the design of robust agent architectures and is available on [arXiv](https://arxiv.org/abs/2606.02540v1).
