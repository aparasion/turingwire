---
title: "Deep Reinforcement Learning for Flexible Job Shop Scheduling with Random Job Arrivals"
date: 2026-05-21 17:33:09 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22773v1"
arxiv_id: "2605.22773"
authors: ["Yu Tang", "Muhammad Zakwan", "Efe Balta", "John Lygeros", "Alisa Rupenyan"]
slug: deep-reinforcement-learning-for-flexible-job-shop-scheduling
summary_word_count: 433
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the Flexible Job Shop Scheduling Problem (FJSP), which involves optimally allocating jobs to machines under the constraints of unpredictable job arrivals and the combinatorial complexity that makes traditional mixed-integer linear programming (MILP) approaches intractable. The authors propose a novel solution using deep reinforcement learning (DRL) to tackle these challenges. Notably, this work is a preprint and has not yet undergone peer review.

**Method**  
The authors introduce an event-based DRL framework specifically designed for FJSP with random job arrivals. The core technical contribution is the application of the Proximal Policy Optimization (PPO) algorithm, which is well-suited for continuous action spaces. The DRL agent is trained using lightweight Multi-Layer Perceptrons (MLPs) to minimize the total completion time of jobs. The state representation is crafted to be directly accessible from the environment, allowing for real-time decision-making. The agent is constrained to select actions from a predefined set of established dispatching rules, which helps maintain interpretability and efficiency. The training process leverages simulations that reflect varying levels of job arrival rates and heterogeneity in job types.

**Results**  
The proposed DRL approach demonstrates superior performance compared to individual dispatching rules across multiple datasets characterized by different levels of heterogeneity and job arrival rates. Specifically, the DRL agent outperforms a baseline arrival-triggered MILP solution, particularly in heterogeneous scenarios. While exact numerical results are not provided in the abstract, the authors claim significant improvements in total completion time, indicating a robust effect size that suggests practical applicability in real-world scheduling tasks.

**Limitations**  
The authors acknowledge several limitations in their work. First, the reliance on predefined dispatching rules may restrict the exploration of potentially more effective strategies that could emerge from a fully unconstrained DRL approach. Additionally, the performance of the proposed method may vary with the complexity of the job arrival patterns, which could limit its generalizability. The paper does not address the computational overhead associated with training the DRL agent, which could be a concern in environments with high job arrival rates or complex job characteristics.

**Why it matters**  
This research has significant implications for the field of operations research and industrial engineering, particularly in environments where job scheduling is critical, such as manufacturing and logistics. By leveraging DRL for FJSP, the authors provide a framework that can adapt to dynamic job arrivals, potentially leading to more efficient scheduling solutions in practice. The findings encourage further exploration of DRL applications in combinatorial optimization problems, paving the way for future research that could enhance the scalability and robustness of scheduling algorithms.

Authors: Yu Tang, Muhammad Zakwan, Efe Balta, John Lygeros, Alisa Rupenyan  
Source: arXiv:2605.22773  
URL: https://arxiv.org/abs/2605.22773v1
