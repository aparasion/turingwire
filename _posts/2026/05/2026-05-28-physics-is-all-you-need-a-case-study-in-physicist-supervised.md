---
title: "Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software"
date: 2026-05-28 17:59:59 +0000
category: research
subcategory: agents_robotics
company: "Anthropic"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.30353v1"
arxiv_id: "2605.30353"
authors: ["Nhat-Minh Nguyen"]
slug: physics-is-all-you-need-a-case-study-in-physicist-supervised
summary_word_count: 460
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the role of AI agents in scientific software development, particularly in the context of physicist-supervised AI. The study investigates the limitations of current AI coding agents (specifically Claude Code, Sonnet, and Opus models) when tasked with building a differentiable one-loop perturbation theory module (CLAX-PT) in JAX. It highlights the inadequacies of these agents in resolving complex scientific problems autonomously and the necessity for effective supervision to ensure the reliability of their outputs.

**Method**  
The core technical contribution involves a detailed case study over 12 workdays and 57 sessions, where a physicist supervised the AI agent. The authors documented 15 supervision events, classifying them by intervention level. The AI agent autonomously resolved 10 issues through iterative testing against oracle tests, while the physicist's domain knowledge was required for 2 additional issues. The study emphasizes the importance of supervision practices, including testing at diverse parameter points, maintaining shared changelogs, and enforcing rules against unphysical numerical adjustments. The authors argue that the agent's inability to propose architectural alternatives or distinguish between predictive adequacy and explanatory correctness limits its effectiveness.

**Results**  
The AI agent demonstrated a mixed performance: it successfully resolved 10 out of 15 issues autonomously, but struggled with three critical problems that evaded oracle detection. Notably, the agent spent 33 sessions adjusting coefficients within an unsuitable code architecture, failing to re-evaluate its design choices until prompted by an injected physics concept. Additionally, a calibrated correction passed all oracle tests but yielded incorrect predictions in other cosmological contexts. The study underscores that supervision design, rather than the AI model's inherent capabilities, was pivotal in determining the trustworthiness of the outputs.

**Limitations**  
The authors acknowledge that the study is limited by its single-case design (N=1), which may not generalize across different contexts or AI models. They also note that the AI agent's inability to propose architectural changes or recognize unphysical outputs represents a significant limitation. Furthermore, the reliance on oracle tests may not capture all potential issues, suggesting that more robust evaluation frameworks are needed. The study does not explore the scalability of the proposed supervision practices across larger teams or more complex projects.

**Why it matters**  
This research has significant implications for the development of AI agents in scientific domains. It highlights the critical role of human supervision in ensuring the reliability of AI-generated outputs, particularly in complex fields like physics. The findings suggest that future AI systems must be designed to propose alternative architectures and differentiate between predictive and explanatory correctness to enhance their utility in scientific research. This work lays the groundwork for further exploration into the integration of AI in scientific workflows and the necessary conditions for effective collaboration between human experts and AI agents.

Authors: Nhat-Minh Nguyen  
Source: arXiv:2605.30353  
URL: https://arxiv.org/abs/2605.30353v1
