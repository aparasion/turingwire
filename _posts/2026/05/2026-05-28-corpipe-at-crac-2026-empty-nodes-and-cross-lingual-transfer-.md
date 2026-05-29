---
title: "CorPipe at CRAC 2026: Empty Nodes and Cross-Lingual Transfer in Multilingual Coreference Resolution"
date: 2026-05-28 16:01:03 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.30133v1"
arxiv_id: "2605.30133"
authors: ["Milan Straka"]
slug: corpipe-at-crac-2026-empty-nodes-and-cross-lingual-transfer-
summary_word_count: 470
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of multilingual coreference resolution (MCR), particularly in the context of the CRAC 2026 Shared Task. The task emphasizes the comparison between generative large language models (LLMs) and specialized systems, while also introducing five new datasets and two additional languages. The authors identify a gap in existing methodologies regarding the prediction of empty nodes alongside coreference links and mentions, which has not been adequately explored in prior work. This paper is a preprint and has not yet undergone peer review.

**Method**  
CorPipe 26 builds upon its predecessor, CorPipe 25, by integrating a novel architecture that predicts empty nodes in conjunction with mentions and coreference links within a unified model. The authors employ a transformer-based architecture, leveraging advancements in LLMs while optimizing for multilingual contexts. The training process involves a diverse set of datasets, including the newly introduced ones, and utilizes a combination of supervised and unsupervised learning techniques. The model's performance is evaluated through a series of ablation studies that assess the impact of varying model sizes, different methodologies for empty node prediction, and cross-lingual zero-shot evaluation strategies. The authors disclose that the training compute involved is substantial, although specific compute resources are not detailed.

**Results**  
CorPipe 26 achieves a notable performance improvement, surpassing all other submissions in the LLM track by 2.8 percentage points and in the unconstrained track by 9.5 percentage points. The results are benchmarked against various established systems, demonstrating significant effect sizes that indicate the robustness of the proposed method. The paper provides detailed performance metrics across the new datasets, showcasing the model's efficacy in handling multilingual coreference tasks, particularly in the newly introduced languages.

**Limitations**  
The authors acknowledge several limitations, including the potential overfitting to the training datasets and the challenges associated with generalizing the model to less-resourced languages. They also note that while the model performs well in the evaluated scenarios, its performance in real-world applications may vary due to the complexities of natural language. Additionally, the reliance on large-scale training data may limit accessibility for researchers with fewer resources. An obvious limitation not explicitly mentioned is the lack of a comprehensive error analysis, which could provide insights into specific failure modes of the model.

**Why it matters**  
The implications of this work are significant for the field of multilingual NLP, particularly in enhancing the capabilities of coreference resolution systems. By successfully integrating empty node prediction into a unified model, this research paves the way for more sophisticated approaches to MCR that can handle the intricacies of multiple languages. The findings may influence future research directions, encouraging further exploration of cross-lingual transfer techniques and the development of more inclusive datasets. The availability of the source code and trained models fosters collaboration and innovation within the community, potentially accelerating advancements in multilingual understanding.

Authors: Milan Straka  
Source: arXiv:2605.30133  
URL: https://arxiv.org/abs/2605.30133v1
