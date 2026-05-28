---
title: "Thinking as Compression: Your Reasoning Model is Secretly a Context Compressor"
date: 2026-05-27 16:36:01 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.28713v1"
arxiv_id: "2605.28713"
authors: ["Guoxin Ma", "Yibing Liu", "Chengzhengxu Li", "Yu Liang", "Yan Wang", "Yueyang Zhang"]
slug: thinking-as-compression-your-reasoning-model-is-secretly-a-c
summary_word_count: 449
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding efficient context compression for long-context inputs in large language models (LLMs). Existing methods often depend on complex compression modules or specialized training, which can obscure the inherent capabilities of LLMs. The authors propose a novel approach that leverages the reasoning process of LLMs themselves as a means of context compression, thereby simplifying the compression paradigm and enhancing inference efficiency.

**Method**  
The core technical contribution is the introduction of the Thinking as Compression (TaC) paradigm, which posits that the reasoning model can inherently compress long contexts by organizing relevant information. TaC prompts the model to generate "thinking traces" that serve as a compressed context without the need for dedicated compression mechanisms. To address potential issues with budget control and shortcut behaviors in raw thinking outputs, the authors propose an extension called Thinking as Compression Constrained (TaC-C). This method employs a reward-driven optimization framework to refine the thinking outputs, ensuring they are both compact and controllable. The training process and specific architecture details are not disclosed, but the focus is on optimizing the reasoning outputs to achieve effective context compression.

**Results**  
The authors conducted experiments across four long-context question-answering (QA) benchmarks, demonstrating that TaC-C consistently outperforms existing compression baselines. At compression ratios of 4x and 8x, TaC-C achieved an average F1 score improvement of 17.4% and 23.4%, respectively, compared to the strongest competitor. Additionally, it improved the average Exact Match Score (EM) by 15.7% and 21.7% at the same compression ratios. These results indicate a significant enhancement in performance metrics, showcasing the effectiveness of the proposed methods over traditional compression techniques.

**Limitations**  
The authors acknowledge that while TaC and TaC-C show promising results, there may be limitations in terms of the generalizability of the approach across different tasks and domains. They do not explicitly address potential scalability issues or the computational overhead associated with the reward-driven optimization framework. Furthermore, the reliance on the intrinsic capabilities of LLMs may not be universally applicable to all architectures or training paradigms.

**Why it matters**  
This work has significant implications for the development of more efficient LLMs, particularly in applications requiring real-time processing of long-context inputs. By framing reasoning as a compression mechanism, it opens avenues for further research into optimizing LLM architectures and training methodologies. The findings suggest that leveraging the inherent reasoning capabilities of LLMs can lead to substantial improvements in performance while reducing the complexity of compression techniques. This could pave the way for more scalable and efficient AI systems in various domains, including natural language processing and beyond.

Authors: Guoxin Ma, Yibing Liu, Chengzhengxu Li, Yu Liang, Yan Wang, Yueyang Zhang, Kecheng Chen, Zhaohan Zhang et al.  
Source: arXiv:2605.28713  
URL: https://arxiv.org/abs/2605.28713v1
