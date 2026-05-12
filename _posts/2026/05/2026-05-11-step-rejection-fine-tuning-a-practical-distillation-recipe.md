---
title: "Step Rejection Fine-Tuning: A Practical Distillation Recipe"
date: 2026-05-11 14:55:20 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.10674v1"
arxiv_id: "2605.10674"
authors: ["Igor Slinko", "Ilia Zavidnyi", "Egor Bogomolov", "Yaroslav Zharov"]
slug: step-rejection-fine-tuning-a-practical-distillation-recipe
summary_word_count: 444
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the training methodologies for large language model (LLM) agents, specifically in the context of software engineering tasks evaluated through SWE-bench. The authors identify that traditional Rejection Fine-Tuning (RFT) discards unsuccessful trajectories entirely, which can lead to the loss of potentially useful information from unresolved trajectories. This is particularly problematic for complex tasks where many trajectories may be partially correct but not fully successful. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose Step Rejection Fine-Tuning (SRFT), which introduces a novel mechanism for utilizing unresolved trajectories during training. SRFT employs a critic LLM that evaluates the correctness of each step within a trajectory. Instead of discarding erroneous steps, SRFT masks the loss associated with these steps while retaining them in the context window. This allows the model to learn from the trajectory without reinforcing incorrect behaviors. The architecture details are not explicitly disclosed, but the method relies on a critic LLM that presumably operates in conjunction with the primary LLM being fine-tuned. The training compute requirements are not specified, but the approach suggests a more complex training regime due to the additional evaluation step.

**Results**  
The evaluation of SRFT is conducted on the SWE-bench Verified benchmark. The authors report that RFT achieves a resolution rate improvement of 2.4% by excluding unresolved trajectories, while SRFT surpasses this by achieving a 3.7% improvement, resulting in a total resolution rate of 32.2%. This indicates that SRFT not only retains more information during training but also enhances the model's ability to resolve tasks effectively compared to the baseline RFT approach.

**Limitations**  
The authors acknowledge that while SRFT improves upon RFT, it still relies on the critic LLM's ability to accurately assess trajectory correctness, which may introduce its own biases or errors. Additionally, the method's performance may vary depending on the complexity of the tasks and the quality of the critic LLM. The paper does not discuss the computational overhead introduced by the critic evaluation, which could impact scalability. Furthermore, the generalizability of SRFT to other domains beyond SWE-bench is not explored.

**Why it matters**  
The implications of this work are significant for the training of LLMs in complex task environments. By effectively leveraging unresolved trajectories, SRFT provides a pathway to improve model performance without discarding potentially informative data. This approach could lead to more robust LLMs capable of handling intricate tasks with higher resolution rates. The methodology may inspire further research into hybrid training techniques that balance error correction with knowledge retention, potentially influencing future developments in LLM training paradigms.

Authors: Igor Slinko, Ilia Zavidnyi, Egor Bogomolov, Yaroslav Zharov  
Source: arXiv:2605.10674  
URL: [https://arxiv.org/abs/2605.10674v1](https://arxiv.org/abs/2605.10674v1)
