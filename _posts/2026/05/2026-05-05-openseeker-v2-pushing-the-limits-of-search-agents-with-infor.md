---
title: "OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories"
date: 2026-05-05 17:55:25 +0000
category: research
subcategory: agents_robotics
company: "OpenAI"
secondary_companies: ["null"]
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.04036v1"
arxiv_id: "2605.04036"
authors: ["Yuwen Du", "Rui Ye", "Shuo Tang", "Keduan Huang", "Xinyu Zhu", "Yuzhu Cai"]
slug: openseeker-v2-pushing-the-limits-of-search-agents-with-infor
summary_word_count: 452
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the development of search agents for Large Language Models (LLMs), particularly focusing on the lack of accessible methodologies for training high-performance search agents without relying on resource-intensive pipelines typically employed by industrial entities. The authors present OpenSeeker-v2, a search agent developed by an academic team, which utilizes a straightforward supervised fine-tuning (SFT) approach, contrasting with the prevalent reliance on complex pre-training, continual pre-training (CPT), and reinforcement learning (RL) strategies. This work is a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this work is the introduction of three data synthesis modifications that enhance the training of search agents. These modifications include: 
1. **Scaling Knowledge Graph Size**: This allows for richer exploration of the search space.
2. **Expanding Tool Set Size**: This broadens the functional capabilities of the agent.
3. **Strict Low-Step Filtering**: This ensures that only high-quality trajectories are used for training.

The model, OpenSeeker-v2, is trained on a dataset comprising 10.6k data points, utilizing a 30B parameter architecture within the ReAct paradigm. The authors emphasize that their approach, which relies solely on SFT, is both simple and effective, enabling the development of a competitive search agent without the extensive computational resources typically required.

**Results**  
OpenSeeker-v2 achieves state-of-the-art performance across four benchmarks, outperforming the Tongyi DeepResearch model, which employs a more complex training pipeline. The performance metrics are as follows:
- **BrowseComp**: OpenSeeker-v2 scores 46.0% vs. Tongyi's 43.4%
- **BrowseComp-ZH**: OpenSeeker-v2 scores 58.1% vs. Tongyi's 46.7%
- **Humanity's Last Exam**: OpenSeeker-v2 scores 34.6% vs. Tongyi's 32.9%
- **xbench**: OpenSeeker-v2 scores 78.0% vs. Tongyi's 75.0%

These results indicate significant effect sizes, demonstrating the efficacy of the proposed method in enhancing search agent capabilities.

**Limitations**  
The authors acknowledge that their approach may not generalize across all types of search tasks, as the modifications are tailored to specific benchmarks. Additionally, the reliance on a relatively small dataset (10.6k data points) may limit the robustness of the model in more diverse or complex scenarios. The paper does not address potential overfitting issues that could arise from the low-step filtering process or the implications of scaling knowledge graphs beyond the tested parameters.

**Why it matters**  
The implications of this work are significant for the field of search agent development, particularly in making advanced search capabilities more accessible to researchers outside of industrial settings. By demonstrating that a simple SFT approach can yield competitive results, the authors encourage further exploration and innovation in search agent methodologies. The open-sourcing of the OpenSeeker-v2 model weights also promotes collaborative research and development, potentially accelerating advancements in LLM-based search technologies.

Authors: Yuwen Du, Rui Ye, Shuo Tang, Keduan Huang, Xinyu Zhu, Yuzhu Cai, Siheng Chen  
Source: arXiv:2605.04036  
URL: [https://arxiv.org/abs/2605.04036v1](https://arxiv.org/abs/2605.04036v1)
