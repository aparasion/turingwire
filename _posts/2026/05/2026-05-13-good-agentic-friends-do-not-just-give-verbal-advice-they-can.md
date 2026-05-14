---
title: "Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights"
date: 2026-05-13 17:58:32 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13839v1"
arxiv_id: "2605.13839"
authors: ["Wenrui Bao", "Huan Wang", "Jian Wang", "Zhangyang Wang", "Kai Wang", "Yuzhang Shang"]
slug: good-agentic-friends-do-not-just-give-verbal-advice-they-can
summary_word_count: 454
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiencies in multi-agent large language model (LLM) systems that communicate through natural language messages. The traditional method of serializing intermediate computations into tokens for communication leads to increased token generation costs, prefill overhead, and memory usage in the key-value (KV) cache. The authors propose a novel communication interface that circumvents these limitations by allowing agents to update the receiver's weights directly, rather than relying solely on tokenized messages. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of TFlow (Thought Flow), a weight-space communication framework designed for a fixed receiver architecture. In this framework, sender agents, which are role-prompted and frozen during inference, process the input and generate internal activations. These activations are then mapped to low-rank LoRA (Low-Rank Adaptation) perturbations by a learned parameter generator. The generated perturbations are transient and specifically target the receiver's modules, allowing for instance-level adaptation during the receiver's generation phase without altering the model permanently or expanding the text context. This method significantly reduces the number of tokens processed and the computational overhead associated with traditional message passing.

**Results**  
TFlow demonstrates substantial improvements over a standalone receiver model, achieving up to an 8.5 accuracy point increase across five benchmarks. Notably, it reduces the number of processed tokens by up to 32.69%. When compared to a text-based three-agent baseline, TFlow achieves a remarkable reduction in total processed tokens by up to 83.27% and decreases wall-clock inference time by up to 4.6 times, while maintaining competitive accuracy on four out of five benchmarks. These results indicate that the use of transient low-rank weight perturbations can effectively serve as a communication medium, enhancing the efficiency of multi-agent LLM collaboration.

**Limitations**  
The authors acknowledge that TFlow is designed for a known and fixed receiver architecture, which may limit its applicability to more dynamic or heterogeneous systems. Additionally, the reliance on low-rank perturbations may introduce constraints on the expressiveness of the communication, potentially affecting performance in more complex scenarios. The paper does not address the scalability of the approach to larger models or the implications of using this method in real-world applications.

**Why it matters**  
The implications of this work are significant for the development of more efficient multi-agent systems in natural language processing. By enabling direct weight updates as a form of communication, TFlow reduces the computational burden associated with traditional token-based messaging, paving the way for faster and more resource-efficient LLM interactions. This approach could inspire further research into alternative communication paradigms in multi-agent systems, potentially leading to advancements in collaborative AI applications across various domains.

Authors: Wenrui Bao, Huan Wang, Jian Wang, Zhangyang Wang, Kai Wang, Yuzhang Shang  
Source: arXiv:2605.13839  
URL: [https://arxiv.org/abs/2605.13839v1](https://arxiv.org/abs/2605.13839v1)
