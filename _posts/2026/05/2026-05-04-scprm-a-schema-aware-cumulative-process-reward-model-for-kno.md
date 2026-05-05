---
title: "SCPRM: A Schema-aware Cumulative Process Reward Model for Knowledge Graph Question Answering"
date: 2026-05-04 16:56:01 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02819v1"
arxiv_id: "2605.02819"
authors: ["Jiujiu Chen", "Yazheng Liu", "Sihong Xie", "Hui Xiong"]
slug: scprm-a-schema-aware-cumulative-process-reward-model-for-kno
summary_word_count: 443
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing process reward models in knowledge graph (KG) reasoning, particularly the risk compensation effect, where incorrect reasoning steps can be compensated by subsequent correct ones, leading to misleadingly high rewards. This issue is critical in risk-sensitive domains such as medical and legal reasoning, where flawed paths can have significant consequences. The authors propose a novel approach, the Schema-aware Cumulative Process Reward Model (SCPRM), to enhance the evaluation of reasoning paths by incorporating schema information and cumulative rewards. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core contribution of this paper is the SCPRM, which evaluates reasoning paths by conditioning on the reasoning prefix and integrating schema distance metrics. The model computes cumulative rewards based on the distance between the current reasoning step and the target entity derived from the query schema. This approach aims to provide more accurate guidance for path exploration in KG reasoning tasks. The authors further integrate SCPRM into a Monte Carlo Tree Search (MCTS) framework, resulting in SCPRM-MCTS, which facilitates multi-hop reasoning for question answering (QA) tasks. The training methodology and computational resources utilized for training SCPRM-MCTS are not explicitly disclosed in the paper.

**Results**  
The performance of SCPRM-MCTS is evaluated on multiple benchmarks, including medical and legal KGQA and the Complex Web Questions (CWQ) dataset. The model demonstrates an average improvement of 1.18% in Hits@k over strong baseline models, indicating enhanced accuracy in reasoning evaluation. While the paper does not provide detailed statistical significance metrics, the reported effect size suggests a meaningful advancement in the model's ability to handle risk-sensitive reasoning tasks.

**Limitations**  
The authors acknowledge that the SCPRM may still be susceptible to certain limitations inherent in the MCTS framework, such as the exploration-exploitation trade-off and potential computational inefficiencies during tree search. Additionally, the paper does not address the scalability of the model to larger knowledge graphs or the impact of varying schema complexities on performance. The lack of extensive ablation studies to isolate the contributions of different components of SCPRM is another notable omission.

**Why it matters**  
The development of SCPRM has significant implications for downstream applications in risk-sensitive domains, where accurate reasoning is paramount. By providing a more nuanced evaluation of reasoning paths, this model could enhance the reliability of KG-based question answering systems, particularly in fields like healthcare and law. The integration of schema-aware mechanisms into reward modeling may inspire further research into hybrid approaches that combine symbolic reasoning with neural architectures, potentially leading to more robust AI systems capable of complex decision-making in critical scenarios.

Authors: Jiujiu Chen, Yazheng Liu, Sihong Xie, Hui Xiong  
Source: arXiv:2605.02819  
URL: https://arxiv.org/abs/2605.02819v1
