---
title: "TextReg: Mitigating Prompt Distributional Overfitting via Regularized Text-Space Optimization"
date: 2026-05-20 15:47:26 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21318v1"
arxiv_id: "2605.21318"
authors: ["Lucheng Fu", "Ye Yu", "Yiyang Wang", "Yiqiao Jin", "Haibo Jin", "B. Aditya Prakash"]
slug: textreg-mitigating-prompt-distributional-overfitting-via-reg
summary_word_count: 434
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the issue of prompt distributional overfitting in large language models (LLMs), a phenomenon where prompts optimized through iterative feedback from LLMs become overly tailored to the training data, leading to poor generalization on out-of-distribution (OOD) tasks. The authors argue that existing prompt optimization methods lack representational control, resulting in prompts that are not only longer but also incorporate narrow, sample-specific rules. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce TextReg, a regularization framework designed to mitigate prompt distributional overfitting by optimizing the representation of prompts in the text space. TextReg employs a soft-penalty objective that integrates three key components:  
1. **Dual-Evidence Gradient Purification**: This technique refines the gradients used for prompt updates by filtering out noise and irrelevant information.
2. **Semantic Edit Regularization**: This component ensures that the semantic integrity of the prompts is maintained during optimization, preventing excessive alterations that could lead to overfitting.
3. **Regularization-Guided Prompt Update**: This mechanism guides the prompt updates in a way that balances capacity cost and scope narrowness, addressing the dual-factor measure of representational inefficiency.

The authors do not disclose specific details regarding the training compute used for their experiments, but they evaluate TextReg across multiple reasoning benchmarks to assess its effectiveness.

**Results**  
TextReg demonstrates significant improvements in OOD generalization compared to established baselines. Specifically, it achieves accuracy gains of up to +11.8% over TextGrad and +16.5% over REVOLVE on various reasoning tasks. These results indicate that TextReg effectively reduces the risk of prompt distributional overfitting, enhancing the robustness of LLMs when faced with novel inputs.

**Limitations**  
The authors acknowledge that while TextReg improves OOD performance, it may still be sensitive to the initial prompt selection and the specific benchmarks used for evaluation. They do not address potential computational overhead introduced by the regularization techniques, which could impact scalability in real-world applications. Additionally, the generalizability of the proposed methods across different LLM architectures remains untested.

**Why it matters**  
The implications of this work are significant for the field of prompt engineering and LLM deployment. By providing a framework that enhances OOD generalization, TextReg could lead to more robust applications of LLMs in diverse domains, particularly where the distribution of input data may vary significantly from the training set. This research opens avenues for further exploration into regularization techniques in discrete optimization tasks and encourages the development of more resilient LLMs that can adapt to a wider range of scenarios without succumbing to overfitting.

Authors: Lucheng Fu, Ye Yu, Yiyang Wang, Yiqiao Jin, Haibo Jin, B. Aditya Prakash, Haohan Wang  
Source: arXiv:2605.21318  
URL: https://arxiv.org/abs/2605.21318v1
