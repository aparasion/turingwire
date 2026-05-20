---
title: "Text-to-SPARQL Generation with Reinforcement Learning: A GRPO-based Approach on DBLP"
date: 2026-05-19 16:20:57 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.20066v1"
arxiv_id: "2605.20066"
authors: ["Jann Pfeifer", "Debayan Banerjee", "Ricardo Usbeck"]
slug: text-to-sparql-generation-with-reinforcement-learning-a-grpo
summary_word_count: 425
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of zero-shot Text-to-SPARQL generation for knowledge graph question answering, specifically in the scholarly domain. Existing methods typically depend on large models or require extensive supervision through gold query annotations, which limits their applicability. The authors propose a reinforcement learning (RL) approach that leverages outcome-based rewards to train a smaller instruction-tuned language model, thereby filling a gap in the literature regarding efficient, low-resource methods for generating executable queries from natural language.

**Method**  
The core technical contribution is the application of Group-Relative Policy Optimization (GRPO) to the Qwen3-1.7B model, specifically tuned for the DBLP-QuAD dataset. The training process utilizes prompts that integrate natural language questions with symbolic hints about entities and relations. The model is trained using execution feedback, structural constraints, and answer-level rewards. An additional variant incorporates gold-query-based shaping to enhance performance. The training regime emphasizes outcome-based reinforcement learning, which allows the model to learn from the execution results of generated queries rather than relying solely on token-level supervision.

**Results**  
The GRPO-enhanced model demonstrates significant improvements over the unmodified zero-shot baseline, achieving a marked increase in answer-level accuracy and execution accuracy. While the supervised DoRA-finetuned baseline yields higher overall accuracy, the GRPO approach exhibits competitive generalization capabilities, particularly on held-out templates. The authors report that execution-based rewards contribute substantially to performance gains, with limited additional benefits from gold-query shaping. Specific metrics and effect sizes are not disclosed in the abstract, but the comparative performance indicates a robust advancement in zero-shot generation capabilities.

**Limitations**  
The authors acknowledge that while GRPO improves performance, it does not reach the accuracy levels of fully supervised methods. They also note that the additional shaping from gold queries provides only marginal benefits, suggesting that the reliance on execution feedback is a double-edged sword. An obvious limitation not explicitly mentioned is the potential for overfitting to the DBLP-QuAD dataset, which may affect generalization to other domains or datasets. Furthermore, the study does not explore the scalability of the approach to larger models or more complex query structures.

**Why it matters**  
This work has significant implications for the development of efficient, low-resource methods for knowledge graph question answering. By demonstrating that reinforcement learning can effectively train models for zero-shot Text-to-SPARQL generation, the authors open avenues for further research into RL-based training strategies in NLP tasks where labeled data is scarce. The findings suggest that outcome-based rewards can be a viable alternative to traditional supervised learning, potentially leading to more accessible AI systems in scholarly and other domains.

Authors: Jann Pfeifer, Debayan Banerjee, Ricardo Usbeck  
Source: arXiv:2605.20066  
URL: [https://arxiv.org/abs/2605.20066v1](https://arxiv.org/abs/2605.20066v1)
