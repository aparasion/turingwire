---
title: "Neural at ArchEHR-QA 2026: One Method Fits All: Unified Prompt Optimization for Clinical QA over EHRs"
date: 2026-05-11 17:27:30 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.10877v1"
arxiv_id: "2605.10877"
authors: ["Abrar Majeedi", "Viswanatha Reddy Gajjala", "Sai Prasanna Teja Reddy Bogireddy", "Siddhant Rai"]
slug: neural-at-archehr-qa-2026-one-method-fits-all-unified-prompt
summary_word_count: 413
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of automated question answering (QA) over electronic health records (EHRs), which requires precise evidence retrieval, accurate answer generation, and explicit grounding of answers in clinical notes. The authors present their work as a preprint, indicating that it has not yet undergone peer review. The existing literature lacks a unified approach that effectively integrates the various subtasks involved in clinical QA, such as question interpretation, evidence identification, answer generation, and evidence alignment.

**Method**  
The authors introduce Neural1.5, a modular framework that decouples the QA process into four independent stages corresponding to the subtasks. The method employs DSPy’s MIPROv2 optimizer to automatically discover high-performing prompts, optimizing both instructions and few-shot demonstrations for each stage. To enhance reliability, the approach incorporates self-consistency voting across multiple stochastic inference runs, which mitigates spurious errors. Additionally, stage-specific verification mechanisms, including self-reflection and chain-of-verification, are utilized to refine output quality. The architecture is designed to be cost-effective, avoiding the need for extensive model fine-tuning while still achieving high performance.

**Results**  
Neural1.5 achieved a mean rank of 4.00 across all participating teams in the ArchEHR-QA 2026 shared task, ranking 4th, 1st, 4th, and 7th in Subtasks 1 through 4, respectively. These results indicate a strong performance, particularly in Subtask 2, where the method secured the top position. The authors highlight that their systematic approach to prompt optimization, combined with self-consistency mechanisms, provides a viable alternative to traditional model fine-tuning, demonstrating significant improvements in reliability and output quality.

**Limitations**  
The authors acknowledge that their method may not generalize well to other domains outside of clinical QA, as it is specifically tailored for EHRs. They also note potential limitations in the scalability of the approach, particularly regarding the computational resources required for the self-consistency voting mechanism. Furthermore, the reliance on prompt optimization may introduce biases based on the quality of the initial prompts and few-shot examples provided.

**Why it matters**  
This work has significant implications for the field of clinical NLP, particularly in enhancing the reliability and accuracy of automated QA systems over EHRs. By demonstrating that a modular, prompt-optimized approach can outperform traditional fine-tuning methods, the authors pave the way for future research to explore similar strategies in other complex NLP tasks. The findings suggest that systematic prompt optimization could be a key technique for improving performance in various applications, potentially leading to more effective clinical decision support systems.

Authors: Abrar Majeedi, Viswanatha Reddy Gajjala, Sai Prasanna Teja Reddy Bogireddy, Siddhant Rai  
Source: arXiv:2605.10877  
URL: [https://arxiv.org/abs/2605.10877v1](https://arxiv.org/abs/2605.10877v1)
