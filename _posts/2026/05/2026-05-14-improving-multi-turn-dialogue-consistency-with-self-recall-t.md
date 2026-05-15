---
title: "Improving Multi-turn Dialogue Consistency with Self-Recall Thinking"
date: 2026-05-14 17:20:14 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.15102v1"
arxiv_id: "2605.15102"
authors: ["Renning Pang", "Tian Lan", "Leyuan Liu", "Xiaoming Huang", "Piao Tong", "Xiaosong Zhang"]
slug: improving-multi-turn-dialogue-consistency-with-self-recall-t
summary_word_count: 419
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of large language model (LLM) based multi-turn dialogue systems in tracking dependencies across non-adjacent turns, which leads to issues with consistency and scalability. As dialogues lengthen, relevant information becomes obscured by irrelevant context, and existing solutions either rely on high-latency external memory or lose critical details through iterative summarization. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce Self-Recall Thinking (SRT), a framework that enhances long-range contextual dependency management and improves the extraction of informative signals in multi-turn dialogues. SRT operates through three main components:  
1. **Dependency Construction**: This step involves generating self-recall chains that identify and convert relevant historical turns into a structured format for recall.  
2. **Capability Initialization**: The model is trained to utilize recall tokens, enabling it to construct reasoning chains that leverage the identified dependencies.  
3. **Reasoning Improvement**: The framework employs verifiable rewards to refine the accuracy of the recall and reasoning processes, optimizing the model's ability to generate correct responses. The architecture is designed to facilitate an endogenous reasoning process, integrating interpretable recall steps without the need for external modules.

**Results**  
The experimental evaluation demonstrates that SRT achieves a 4.7% improvement in F1 score and a 14.7% reduction in end-to-end latency compared to prior methods. These results were obtained across multiple datasets, indicating that SRT effectively balances reasoning latency and accuracy. The framework outperforms state-of-the-art baselines, showcasing its potential for enhancing multi-turn dialogue systems.

**Limitations**  
The authors acknowledge that while SRT improves dialogue consistency and efficiency, it may still struggle with extremely long dialogues where context may become too sparse. Additionally, the reliance on self-recall chains may introduce biases based on the selected historical turns, potentially affecting the diversity of responses. The paper does not address the scalability of SRT in real-time applications or its performance in highly dynamic conversational contexts.

**Why it matters**  
The implications of this work are significant for the development of more robust multi-turn dialogue systems. By improving the ability to track contextual dependencies and efficiently recall relevant information, SRT paves the way for more coherent and contextually aware conversational agents. This advancement could enhance user experience in applications ranging from customer support to interactive storytelling, where maintaining dialogue consistency is crucial. Furthermore, the framework's focus on endogenous reasoning may inspire future research into self-contained reasoning mechanisms in LLMs, potentially leading to more interpretable and efficient AI systems.

Authors: Renning Pang, Tian Lan, Leyuan Liu, Xiaoming Huang, Piao Tong, Xiaosong Zhang  
Source: arXiv:2605.15102  
URL: [https://arxiv.org/abs/2605.15102v1](https://arxiv.org/abs/2605.15102v1)
