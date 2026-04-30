---
title: "When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models"
date: 2026-04-29 13:15:44 +0000
category: research
subcategory: reasoning
company: "DeepSeek"
secondary_companies: ["OpenAI"]
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26649v1"
arxiv_id: "2604.26649"
authors: ["Dongxin Guo", "Jikun Wu", "Siu Ming Yiu"]
slug: when-to-retrieve-during-reasoning-adaptive-retrieval-for-lar
summary_word_count: 444
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the integration of retrieval-augmented generation (RAG) with large reasoning models, specifically highlighting the misalignment between the two. Current RAG systems typically optimize for context provision prior to reasoning, which does not align with the needs of reasoning models that require evidence injection during multi-step inference. The authors propose a solution to this issue through their framework, ReaLM-Retrieve. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
ReaLM-Retrieve introduces three core innovations to enhance the integration of retrieval within reasoning processes:  
1. **Step-Level Uncertainty Detector**: This component identifies knowledge gaps at the granularity of individual reasoning steps, rather than at the token or sentence level, allowing for more precise retrieval interventions.
2. **Retrieval Intervention Policy**: This policy is designed to learn the optimal moments for injecting external evidence into the reasoning process, thereby maximizing the utility of retrieved information.
3. **Efficiency-Optimized Integration Mechanism**: This mechanism reduces the overhead associated with each retrieval by a factor of 3.2 compared to naive integration methods, streamlining the overall process.

The authors conducted experiments on three benchmarks: MuSiQue, HotpotQA, and 2WikiMultiHopQA, employing a training regime that emphasizes the adaptive retrieval of evidence during reasoning.

**Results**  
ReaLM-Retrieve demonstrates a substantial performance improvement over standard RAG systems, achieving an average absolute increase of 10.1% in answer F1 scores across the benchmarks (with specific improvements ranging from 9.0% to 11.8%). Notably, on the MuSiQue benchmark, which necessitates complex 2-4 hop reasoning, the framework attained a 71.2% F1 score while averaging only 1.8 retrieval calls per question. Additionally, the method reduced retrieval calls by 47% compared to fixed-interval approaches like IRCoT. The retrieval quality was also enhanced, achieving 81.3% Recall@5, with improved precision and Mean Reciprocal Rank (MRR) compared to fixed-interval baselines, establishing new state-of-the-art efficiency-accuracy trade-offs for reasoning-intensive retrieval tasks.

**Limitations**  
The authors acknowledge that their approach may still be limited by the quality of the underlying reasoning model and the retrieval corpus. They do not address potential scalability issues when applied to larger datasets or more complex reasoning tasks. Furthermore, the reliance on a learned intervention policy may introduce variability based on training data and conditions, which could affect generalizability.

**Why it matters**  
The implications of this work are significant for the development of more effective retrieval-augmented reasoning systems. By aligning retrieval processes with the dynamic needs of reasoning models, ReaLM-Retrieve paves the way for improved performance in tasks requiring complex reasoning and evidence synthesis. This framework could influence future research in adaptive retrieval strategies and enhance the capabilities of AI systems in knowledge-intensive applications.

Authors: Dongxin Guo, Jikun Wu, Siu Ming Yiu  
Source: arXiv:2604.26649  
URL: [https://arxiv.org/abs/2604.26649v1](https://arxiv.org/abs/2604.26649v1)
