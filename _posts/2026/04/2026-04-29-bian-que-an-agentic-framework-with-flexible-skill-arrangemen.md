---
title: "Bian Que: An Agentic Framework with Flexible Skill Arrangement for Online System Operations"
date: 2026-04-29 15:35:01 +0000
category: research
subcategory: agents_robotics
company: "KuaiShou"
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26805v1"
arxiv_id: "2604.26805"
authors: ["Bochao Liu", "Zhipeng Qian", "Yang Zhao", "Xinyuan Jiang", "Zihan Liang", "Yufei Ma"]
slug: bian-que-an-agentic-framework-with-flexible-skill-arrangemen
summary_word_count: 432
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the operational challenges in maintaining large-scale online systems, specifically in the context of release monitoring, alert response, and root cause analysis. The authors identify a gap in the orchestration of LLM-based agents, where the primary bottleneck is not the reasoning capability of the models but rather the effective selection of relevant data and operational knowledge for each event. The work is presented as a preprint and has not undergone peer review.

**Method**  
The authors propose Bian Que, an agentic framework characterized by three main contributions:  
1. **Unified Operational Paradigm**: This framework abstracts O&M tasks into three canonical patterns: release interception, proactive inspection, and alert root cause analysis.  
2. **Flexible Skill Arrangement**: Each Skill within the framework specifies the data and knowledge to be retrieved based on the business-module context. Skills can be automatically generated and updated by LLMs or refined through natural language instructions from engineers.  
3. **Unified Self-Evolving Mechanism**: This mechanism utilizes a single correction signal to drive two parallel processes: case-memory-to-knowledge distillation and targeted Skill refinement, allowing the system to adapt and improve over time.

The framework was deployed on the e-commerce search engine of KuaiShou, a major short-video platform in China, demonstrating its practical applicability.

**Results**  
Bian Que achieved significant operational improvements:  
- Reduced alert volume by 75%.  
- Achieved 80% accuracy in root cause analysis.  
- Cut mean time to resolution by over 50%.  
- The framework also attained a 99.0% pass rate in offline evaluations, indicating high reliability and effectiveness compared to existing baselines.

**Limitations**  
The authors acknowledge that while Bian Que significantly improves operational efficiency, it may still face challenges in generalizing across different operational contexts or systems not aligned with the defined canonical patterns. Additionally, the reliance on LLMs for Skill generation and refinement may introduce variability based on the model's training data and architecture. The paper does not address potential issues related to the scalability of the framework or the computational overhead associated with real-time data processing and Skill updates.

**Why it matters**  
The implications of this work are substantial for the field of AI-driven operational management. By providing a structured framework for orchestrating LLM-based agents in online system operations, Bian Que can enhance the efficiency and accuracy of O&M tasks, potentially reducing the need for extensive human intervention. This framework could serve as a foundation for future research into automated operational systems, paving the way for more sophisticated AI applications in real-time monitoring and decision-making processes.

Authors: Bochao Liu, Zhipeng Qian, Yang Zhao, Xinyuan Jiang, Zihan Liang, Yufei Ma, Junpeng Zhuang, Ben Chen et al.  
Source: arXiv:2604.26805  
URL: https://arxiv.org/abs/2604.26805v1
