---
title: "QAP-Router: Tackling Qubit Routing as Dynamic Quadratic Assignment with Reinforcement Learning"
date: 2026-05-12 16:34:01 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.12365v1"
arxiv_id: "2605.12365"
authors: ["Kien X. Nguyen", "Ankit Kulshrestha", "Ilya Safro", "Xiaoyuan Liu"]
slug: qap-router-tackling-qubit-routing-as-dynamic-quadratic-assig
summary_word_count: 471
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the qubit routing problem in quantum compilation, which is known to be NP-hard. The dynamic nature of qubit routing complicates the decision-making process, as local routing choices can have cascading effects over time. Existing heuristic methods typically rely on local rules with limited foresight, while recent learning-based approaches often fail to leverage the specific structural properties of the routing problem. This work presents QAP-Router, a novel approach that frames qubit routing as a dynamic Quadratic Assignment Problem (QAP), thereby filling a gap in the literature regarding efficient, structure-aware solutions for this complex problem. The paper is a preprint and has not yet undergone peer review.

**Method**  
QAP-Router formulates the qubit routing problem by modeling logical interactions (quantum gates) as flow matrices and the hardware topology as a distance matrix. This formulation allows the method to capture the interaction-distance coupling in a unified objective, which serves as the reward signal in a reinforcement learning (RL) framework. The architecture employs a solution-aware Transformer backbone, which encodes the relationship between the flow and distance matrices into its attention mechanism. This design choice enhances the model's ability to make informed routing decisions. Additionally, a lookahead mechanism is integrated into the QAP framework, enabling the model to consider future implications of current routing decisions, thus mitigating the limitations of myopic decision-making. The training process and computational resources utilized are not explicitly disclosed in the paper.

**Results**  
QAP-Router was evaluated on 1,831 real-world quantum circuits sourced from the MQTBench, AgentQ, and QUEKO datasets. The results demonstrate significant improvements in routing efficiency, with reductions in the CNOT gate count of routed circuits by 15.7%, 30.4%, and 12.1% compared to existing industry compilers, respectively. These results indicate a substantial enhancement in performance over baseline methods, showcasing the effectiveness of the proposed QAP formulation and the reinforcement learning approach.

**Limitations**  
The authors acknowledge that the performance of QAP-Router may be sensitive to the specific characteristics of the datasets used for training and evaluation. They also note that the method's reliance on a Transformer architecture may introduce computational overhead, which could limit scalability for larger quantum circuits. Additionally, the paper does not address the potential impact of varying hardware topologies on the routing performance, nor does it explore the generalizability of the approach across different quantum computing platforms.

**Why it matters**  
The introduction of QAP-Router has significant implications for the field of quantum computing, particularly in optimizing qubit routing, which is critical for efficient quantum circuit execution. By framing the problem as a dynamic QAP and leveraging advanced reinforcement learning techniques, this work paves the way for more sophisticated and efficient quantum compilation strategies. The findings could inspire further research into structure-aware learning methods for other NP-hard problems in quantum computing and beyond.

Authors: Kien X. Nguyen, Ankit Kulshrestha, Ilya Safro, Xiaoyuan Liu  
Source: arXiv:2605.12365  
URL: [https://arxiv.org/abs/2605.12365v1](https://arxiv.org/abs/2605.12365v1)
