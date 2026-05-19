---
title: "EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL"
date: 2026-05-18 17:37:40 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.18703v1"
arxiv_id: "2605.18703"
authors: ["Minrui Xu", "Zilin Wang", "Mengyi DENG", "Zhiwei Li", "Zhicheng Yang", "Xiao Zhu"]
slug: envfactory-scaling-tool-use-agents-via-executable-environmen
summary_word_count: 467
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations in equipping large language models (LLMs) with tool-use capabilities through Agentic Reinforcement Learning (Agentic RL). The authors identify two primary challenges: the lack of scalable and robust execution environments and the scarcity of realistic training data that effectively captures implicit human reasoning. Existing methodologies often rely on expensive real-world APIs, unreliable LLM simulators, or synthetic environments that are either single-turn or dependent on pre-collected documents. Additionally, the synthetic trajectories generated are frequently over-specified, resembling rigid instruction sequences rather than natural human intents, which diminishes their utility for RL training. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose EnvFactory, an automated framework designed to synthesize executable environments and generate realistic training trajectories. EnvFactory autonomously explores and verifies stateful environments from authentic resources, employing topology-aware sampling and calibrated refinement to create natural multi-turn trajectories. This process results in grounded queries that encapsulate implicit intents. The framework utilizes only 85 verified environments across seven distinct domains to generate a total of 2,575 supervised fine-tuning (SFT) and reinforcement learning (RL) trajectories. The architecture leverages a combination of environment construction and trajectory synthesis, which is fully automated, thereby enhancing scalability and robustness in the training process.

**Results**  
EnvFactory demonstrates significant improvements in training efficiency and downstream performance compared to prior methodologies that typically utilize five times more environments. The Qwen3-series models trained with EnvFactory show performance enhancements of up to +15% on the BFCLv3 benchmark, +8.6% on MCP-Atlas, and +6% on conversational benchmarks, including $τ^2$-Bench and VitaBench. These results indicate that EnvFactory not only reduces the number of environments required for effective training but also enhances the overall performance of the models.

**Limitations**  
The authors acknowledge that while EnvFactory automates environment construction and trajectory synthesis, the reliance on a limited number of verified environments (85) may restrict the diversity of training scenarios. Additionally, the framework's performance is contingent on the quality of the authentic resources used for environment verification. The paper does not address potential issues related to the generalizability of the trained models across unseen environments or the robustness of the synthesized trajectories in real-world applications.

**Why it matters**  
The introduction of EnvFactory has significant implications for the field of Agentic RL and the broader landscape of tool-use capabilities in LLMs. By providing a scalable and robust framework for environment synthesis and trajectory generation, this work paves the way for more effective training methodologies that can leverage fewer resources while achieving superior performance. The advancements made in this paper could facilitate further research into more complex agentic behaviors and enhance the applicability of LLMs in real-world scenarios where tool use is essential.

Authors: Minrui Xu, Zilin Wang, Mengyi DENG, Zhiwei Li, Zhicheng Yang, Xiao Zhu, Yinhong Liu, Boyu Zhu et al.  
Source: arXiv:2605.18703  
URL: [https://arxiv.org/abs/2605.18703v1](https://arxiv.org/abs/2605.18703v1)
