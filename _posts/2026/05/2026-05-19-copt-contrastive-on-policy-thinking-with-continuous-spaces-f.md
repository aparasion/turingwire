---
title: "CopT: Contrastive On-Policy Thinking with Continuous Spaces for General and Agentic Reasoning"
date: 2026-05-19 16:28:53 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.20075v1"
arxiv_id: "2605.20075"
authors: ["Dachuan Shi", "Hanlin Zhu", "Xiangchi Yuan", "Wanjia Zhao", "Kejing Xia", "Wen Xiao"]
slug: copt-contrastive-on-policy-thinking-with-continuous-spaces-f
summary_word_count: 434
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of the conventional Chain-of-Thought (CoT) paradigm in large language models (LLMs), which typically requires reasoning to precede answering. This sequential approach can lead to inefficiencies, such as delayed access to plausible answers and increased token costs, particularly when the model can generate a valid answer without extensive reasoning. The authors propose a novel framework, CopT, to mitigate these issues. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
CopT introduces a restructured reasoning pipeline that prioritizes generating a draft answer before engaging in on-policy thinking. The core technical contribution lies in its use of continuous embeddings as inference-time contrastive verifiers. Specifically, CopT contrasts the model's support for generated tokens under both discrete-token and continuous-embedding inputs. This results in a sequence-level reverse Kullback-Leibler (KL) estimator that assesses answer reliability. The authors demonstrate that, under certain assumptions, this estimator reflects the mutual information between the unresolved latent state and the emitted answer token, effectively capturing answer-relevant uncertainty. When the draft answer is deemed unreliable, CopT employs further on-policy thinking, utilizing a second KL estimator to dynamically manage draft-answer visibility, thereby preserving useful partial information while minimizing the risk of misleading content.

**Results**  
CopT demonstrates significant improvements across various tasks, including mathematics, coding, and agentic reasoning. The model achieves peak accuracy enhancements of up to 23% compared to baseline models while simultaneously reducing token usage by up to 57% without requiring additional training. The benchmarks for comparison are not explicitly named in the abstract, but the results indicate a substantial performance gain in efficiency and accuracy.

**Limitations**  
The authors acknowledge that their approach relies on specific assumptions regarding the relationship between latent states and answer tokens, which may not hold universally. Additionally, the paper does not address potential scalability issues or the impact of varying task complexities on the effectiveness of the CopT framework. The reliance on continuous embeddings may also introduce challenges in implementation and generalization across diverse LLM architectures.

**Why it matters**  
The implications of CopT are significant for the development of more efficient reasoning mechanisms in LLMs. By reversing the traditional order of reasoning and answering, this framework not only enhances the speed and efficiency of generating plausible answers but also reduces computational costs associated with token usage. This work could pave the way for future research into hybrid reasoning models that leverage both draft answers and on-policy thinking, potentially leading to more robust and adaptable AI systems capable of complex reasoning tasks.

Authors: Dachuan Shi, Hanlin Zhu, Xiangchi Yuan, Wanjia Zhao, Kejing Xia, Wen Xiao, Wenke Lee  
Source: arXiv:2605.20075v1  
URL: https://arxiv.org/abs/2605.20075v1
