---
title: "K-BrowseComp: A Web Browsing Agent Benchmark Grounded in Korean Contexts"
date: 2026-06-01 15:50:03 +0000
category: research
subcategory: evaluation_benchmarks
company: "OpenAI"
secondary_companies: ["DeepSeek"]
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.02404v1"
arxiv_id: "2606.02404"
authors: ["Nahyun Lee", "Dongkeun Yoon", "Guijin Son", "Geewook Kim", "Dayoon Ko", "Jeonghun Park"]
slug: k-browsecomp-a-web-browsing-agent-benchmark-grounded-in-kore
summary_word_count: 431
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces K-BrowseComp, a Korean-context web browsing agent benchmark, highlighting significant performance gaps in current LLMs."
---

**Problem**  
The paper addresses the lack of agentic benchmarks specifically tailored for Korean contexts in the evaluation of large language models (LLMs). While existing benchmarks focus on foundational capabilities, there is a notable absence of resources that assess compositional and agentic skills in web browsing tasks. This gap is critical as the performance of LLMs in real-world applications, particularly in non-English languages, remains underexplored. The authors present K-BrowseComp, a benchmark consisting of 400 web browsing problems, with a verified subset of 300 problems manually curated by native Korean speakers. This work is a preprint and has not undergone peer review.

**Method**  
K-BrowseComp is structured into two main subsets: K-BrowseComp-Verified and a synthetic diagnostic split. The K-BrowseComp-Verified subset comprises 300 manually constructed problems validated for linguistic and contextual accuracy. The authors evaluate several frontier LLMs, including GPT-5.5, DeepSeek-V4-Pro, and GLM-5.1, against this subset. The synthetic split consists of 100 problems generated using hard few-shot exemplars and targeted generation techniques to create challenging scenarios that exploit the disparity between problem-solving and problem-creation capabilities. The models are assessed based on their ability to navigate and respond to web browsing tasks, with performance metrics reported as accuracy percentages.

**Results**  
The evaluation reveals that frontier LLMs achieve only 30.00% to 45.67% accuracy on the K-BrowseComp-Verified subset, indicating a significant performance drop compared to the BrowseComp benchmark. In contrast, Korean LLMs developed through Korea's Proprietary AI Foundation Model program perform poorly, with accuracy ranging from 0.00% to 10.33%. On the adversarially filtered synthetic diagnostic split, the best-performing model reaches an accuracy of only 26.00%. These results underscore the challenges faced by current models in effectively handling web browsing tasks in a Korean context.

**Limitations**  
The authors acknowledge that the performance of LLMs on the K-BrowseComp benchmark is significantly lower than expected, highlighting the need for further research and development in this area. They also note that the synthetic split may not fully capture the complexity of real-world web browsing scenarios. Additionally, the benchmark's reliance on manually curated problems may introduce biases or limitations in coverage. The authors do not discuss potential scalability issues or the generalizability of their findings to other languages or contexts.

**Why it matters**  
K-BrowseComp serves as a crucial resource for evaluating LLMs in non-English contexts, particularly for Korean language applications. The benchmark's release aims to stimulate further research into agentic capabilities of LLMs and to encourage the development of more robust models that can handle diverse linguistic and contextual challenges. This work is significant for advancing the field of natural language processing and understanding the limitations of current models, as published in [arXiv](https://arxiv.org/abs/2606.02404v1).
