---
title: "MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research"
date: 2026-05-25 17:59:49 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.26114v1"
arxiv_id: "2605.26114"
authors: ["Dingbang Wu", "Rui Hao", "Haiyang Wang", "Shuzhe Wu", "Han Xiao", "Zhenghong Li"]
slug: mobilegym-a-verifiable-and-highly-parallel-simulation-platfo
summary_word_count: 458
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper presents MobileGym, a preprint simulation platform designed to address the limitations in existing mobile GUI agent research environments. Traditional platforms often lack verifiable outcome signals and scalability for online reinforcement learning (RL) due to proprietary backend constraints. MobileGym aims to fill this gap by providing a lightweight, browser-hosted environment that allows for deterministic evaluation and high parallelism, which are critical for developing robust mobile agents.

**Method**  
MobileGym employs a structured JSON state representation to capture the full environment state, enabling deterministic state-based judging. The architecture supports hundreds of parallel instances on a single server, with each instance consuming approximately 400 MB of memory and achieving a cold start time of about 3 seconds. The platform features a layered state model and a declarative task-definition framework that facilitate scalable task creation and state programmability. A unified judging mechanism provides both deterministic evaluation outcomes and dense RL rewards. The accompanying MobileGym-Bench includes 416 parameterized task templates across 28 applications, with 256 designated for testing and 160 for training. This setup allows for structured evaluation through a standardized AnswerSheet protocol, mitigating issues related to free-text matching.

**Results**  
In a Sim-to-Real case study, the authors demonstrate that the GRPO algorithm, when applied to the Qwen3-VL-4B-Instruct model, achieves a performance improvement of +12.8 percentage points on the 256-task test set compared to baseline methods. Furthermore, when evaluated on a subset of 59 tasks executed on real devices, the model retains 95.1% of the training gains achieved in the simulation environment. These results indicate that MobileGym effectively bridges the gap between simulated and real-world performance for mobile GUI agents.

**Limitations**  
The authors acknowledge several limitations, including the potential for overfitting to the specific task templates provided in MobileGym-Bench and the reliance on structured JSON, which may not capture all nuances of real-world interactions. Additionally, the cold start time, while relatively short, could still pose challenges for applications requiring immediate responsiveness. The paper does not address the scalability of the platform beyond the tested limits or the implications of using a browser-hosted environment for performance-critical applications.

**Why it matters**  
MobileGym represents a significant advancement in the development of mobile GUI agents by providing a verifiable and scalable simulation platform. Its ability to deliver deterministic evaluation and facilitate parallel rollouts opens new avenues for research in reinforcement learning and agent-based systems. The structured approach to task definition and evaluation can enhance reproducibility and comparability in mobile agent research, potentially leading to more robust and generalizable models. This work lays the groundwork for future explorations in mobile AI applications, particularly in environments where interaction fidelity and real-time performance are paramount.

Authors: Dingbang Wu, Rui Hao, Haiyang Wang, Shuzhe Wu, Han Xiao, Zhenghong Li, Bojiang Zhou, Zheng Ju et al.  
Source: arXiv cs.AI  
URL: [https://arxiv.org/abs/2605.26114v1](https://arxiv.org/abs/2605.26114v1)
