---
title: "ENPMR-Bench: Benchmarking Proactive Memory Retrieval for Emotional Support Agents"
date: 2026-05-26 16:22:35 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.27240v1"
arxiv_id: "2605.27240"
authors: ["Xing Fu", "Yulin Hu", "Mengtong Ji", "Haozhen Li", "Yixin Sun", "Weixiang Zhao"]
slug: enpmr-bench-benchmarking-proactive-memory-retrieval-for-emot
summary_word_count: 497
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the literature regarding the use of memory-augmented language agents in emotional support applications. While existing research primarily focuses on factual retrieval, it neglects the critical aspect of understanding and responding to users' latent emotional needs. The authors introduce ENPMR-Bench, a benchmark specifically designed to evaluate Emotional Need-aware Proactive Memory Retrieval (ENPMR), which is essential for enabling agents to proactively infer and address users' emotional requirements. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this paper is the development of the ENPMR-Bench benchmark, which consists of over 1,800 memory-augmented dialogues. The benchmark is structured around Maslow's hierarchy of needs, establishing clear mappings between various emotional needs and corresponding supportive memory types. The authors evaluate existing retrieval paradigms, including embedding-based methods and large language model (LLM) approaches, to assess their effectiveness in proactive memory retrieval. The evaluation metrics include empathy scores, which quantify the alignment between inferred emotional needs and the retrieved memories. The authors also explore the impact of chain-of-thought prompting on retrieval performance, aiming to enhance the alignment of emotional needs with memory retrieval.

**Results**  
The experimental results reveal that current retrieval paradigms significantly underperform in terms of empathy scores when compared to the golden memory conditions established in the benchmark. Specifically, the authors report that existing methods lag substantially behind the ideal performance, indicating a critical deficiency in their ability to support empathetic interactions. While chain-of-thought prompting does yield some improvement in aligning inferred emotional needs with retrieved memories, a notable performance gap persists, underscoring the limitations of current approaches in effectively addressing users' emotional needs.

**Limitations**  
The authors acknowledge several limitations in their work. Firstly, the benchmark is based on a specific framework (Maslow's hierarchy of needs), which may not encompass the full spectrum of emotional needs in diverse contexts. Additionally, the reliance on existing retrieval paradigms may limit the generalizability of the findings. The authors also note that while chain-of-thought prompting shows promise, it does not fully bridge the performance gap, indicating that further advancements are necessary. An obvious limitation not explicitly mentioned is the potential bias in the dataset, which may affect the generalizability of the results across different user demographics and emotional contexts.

**Why it matters**  
The implications of this work are significant for the development of personalized emotional support agents. By establishing a benchmark for ENPMR, the authors provide a foundation for future research aimed at enhancing the emotional intelligence of language agents. The findings highlight the urgent need for improved memory retrieval mechanisms that are sensitive to users' emotional states, paving the way for more empathetic and effective interactions in affective computing applications. This research could catalyze advancements in the design of emotionally aware AI systems, ultimately leading to better user experiences in mental health and emotional support contexts.

Authors: Xing Fu, Yulin Hu, Mengtong Ji, Haozhen Li, Yixin Sun, Weixiang Zhao, Yanyan Zhao, Bing Qin  
Source: arXiv:2605.27240  
URL: [https://arxiv.org/abs/2605.27240v1](https://arxiv.org/abs/2605.27240v1)
