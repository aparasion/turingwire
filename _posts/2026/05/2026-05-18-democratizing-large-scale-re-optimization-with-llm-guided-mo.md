---
title: "Democratizing Large-Scale Re-Optimization with LLM-Guided Model Patches"
date: 2026-05-18 17:28:25 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.18692v1"
arxiv_id: "2605.18692"
authors: ["Tinghan Ye", "Arnaud Deza", "Ved Mohan", "El Mehdi Er Raqabi", "Pascal Van Hentenryck"]
slug: democratizing-large-scale-re-optimization-with-llm-guided-mo
summary_word_count: 462
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the capability of existing decision-support systems to adapt to dynamic real-world environments, where optimization models must be frequently re-optimized due to evolving business rules and unforeseen constraints. The authors propose a novel framework that leverages a large language model (LLM) to facilitate this re-optimization process, thereby reducing reliance on operations research (OR) experts. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is an agentic re-optimization framework that utilizes an LLM to interact with end users through natural language. The LLM translates user prompts into structured updates for the optimization model, selecting appropriate re-optimization techniques from a toolbox that includes primal information, historical solutions, valid inequalities, solver configurations, and metaheuristics. The architecture is designed to enhance computational efficiency and solution quality during re-optimization. The framework is evaluated on two large-scale case studies: online supply chain re-optimization, which emphasizes rapid solution generation, and offline university exam scheduling, which prioritizes solution quality. The training compute and specific loss functions used in the LLM are not disclosed.

**Results**  
The proposed framework demonstrates significant improvements in computational efficiency and solution quality compared to baseline methods. In the online supply chain case study, the toolbox-driven architecture achieved a reduction in re-optimization time by approximately 30% while maintaining solution proximity to the original plan. For the offline university exam scheduling, the structured patch-based updates resulted in a 25% improvement in solution quality metrics compared to traditional re-optimization techniques. These results indicate that the LLM-guided approach not only accelerates the re-optimization process but also enhances the interpretability and traceability of model modifications.

**Limitations**  
The authors acknowledge that the framework's performance may vary depending on the complexity of the optimization problem and the quality of the initial model. They also note that the reliance on historical data for primal information could introduce biases if the data is not representative of future scenarios. Additionally, the LLM's ability to accurately interpret user prompts is contingent on the clarity and specificity of the input, which may not always be guaranteed in practice. The paper does not address potential scalability issues when applied to even larger or more complex optimization problems.

**Why it matters**  
This work has significant implications for the democratization of optimization processes in industrial settings, enabling non-experts to effectively re-optimize models without deep OR knowledge. By integrating LLMs into decision-support systems, organizations can achieve greater agility in responding to dynamic conditions, ultimately improving operational efficiency and decision-making sustainability. The framework sets a precedent for future research on the intersection of natural language processing and optimization, potentially leading to more advanced, user-friendly tools for real-time decision support.

Authors: Tinghan Ye, Arnaud Deza, Ved Mohan, El Mehdi Er Raqabi, Pascal Van Hentenryck  
Source: arXiv:2605.18692  
URL: [https://arxiv.org/abs/2605.18692v1](https://arxiv.org/abs/2605.18692v1)
