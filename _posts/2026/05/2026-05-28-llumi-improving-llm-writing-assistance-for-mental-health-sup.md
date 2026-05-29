---
title: "LLUMI: Improving LLM Writing Assistance for Mental Health Support with Online Community Feedback"
date: 2026-05-28 17:30:57 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.30273v1"
arxiv_id: "2605.30273"
authors: ["Jiwon Kim", "Maya Ajit", "Sherry Gong", "Soorya Ram Shimgekar", "Dong Whi Yoo", "Eshwar Chandrasekharan"]
slug: llumi-improving-llm-writing-assistance-for-mental-health-sup
summary_word_count: 476
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the capability of large language models (LLMs) to provide effective mental health support while ensuring privacy and data governance. Existing LLMs often require extensive compute resources, expert input, and labeled datasets to enhance their performance in generating empathetic and safe responses. Additionally, the deployment of proprietary cloud-based models raises significant privacy concerns, particularly in sensitive mental health contexts. The authors propose LLUMI, a system designed to operate in-house, mitigating these issues while improving the quality of LLM-generated responses.

**Method**  
LLUMI comprises two main components: a Generation Model (GM) and an Improvement Model (IM). The GM generates initial responses to mental health queries, while the IM refines these responses based on community feedback. The authors utilize feedback from Reddit mental health communities, specifically leveraging upvote and downvote patterns to create chosen-rejected response pairs. These pairs are employed for Supervised Fine Tuning (SFT) and Direct Preference Optimization (DPO). The alignment of LLUMI is further enhanced through human evaluations across five dimensions: readability, empathy, connection, actionability, and safety. The authors do not disclose specific training compute details but emphasize the use of smaller open-source models instead of proprietary ones.

**Results**  
LLUMI demonstrates competitive performance compared to proprietary models, achieving comparable results in linguistic analyses and human evaluations. The authors report that LLUMI's responses are rated similarly in terms of empathy and safety when benchmarked against established models. While specific numerical results are not provided in the abstract, the implication is that LLUMI effectively meets or exceeds the performance of proprietary models in the evaluated dimensions, suggesting a significant effect size in favor of community-informed training methods.

**Limitations**  
The authors acknowledge that LLUMI's reliance on community feedback may introduce biases inherent in the Reddit data, which may not be representative of broader populations. Additionally, the system's performance is contingent on the quality and diversity of the feedback received. The authors do not address potential limitations related to the generalizability of their findings across different mental health contexts or the scalability of the in-house deployment model. Furthermore, the absence of a comprehensive evaluation against a wider array of benchmarks limits the assessment of LLUMI's robustness.

**Why it matters**  
The implications of this work are significant for the development of privacy-preserving mental health support systems. By demonstrating that open-source models can be effectively trained using community-derived feedback, LLUMI paves the way for more accessible and ethical AI applications in sensitive domains. This approach not only enhances the quality of LLM-generated responses but also addresses critical privacy concerns, making it a viable alternative to proprietary solutions. Future research can build on LLUMI's framework to explore further enhancements in model training and evaluation methodologies, potentially leading to broader applications in mental health and other sensitive areas.

Authors: Jiwon Kim, Maya Ajit, Sherry Gong, Soorya Ram Shimgekar, Dong Whi Yoo, Eshwar Chandrasekharan, Koustuv Saha  
Source: arXiv:2605.30273  
URL: [https://arxiv.org/abs/2605.30273v1](https://arxiv.org/abs/2605.30273v1)
