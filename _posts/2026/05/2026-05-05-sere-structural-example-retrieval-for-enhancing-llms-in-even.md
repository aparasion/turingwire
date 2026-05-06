---
title: "SERE: Structural Example Retrieval for Enhancing LLMs in Event Causality Identification"
date: 2026-05-05 12:50:19 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.03701v1"
arxiv_id: "2605.03701"
authors: ["Zhifeng Hao", "Zhongjie Chen", "Junhao Lu", "Shengyin Yu", "Guimin Hu", "Keli Zhang"]
slug: sere-structural-example-retrieval-for-enhancing-llms-in-even
summary_word_count: 472
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of Large Language Models (LLMs) in Event Causality Identification (ECI), particularly their propensity for causal hallucination—overpredicting causal relationships due to biases in causal reasoning. Despite LLMs' strong performance in various NLP tasks, their effectiveness in ECI remains suboptimal. The authors propose SERE, a structural example retrieval framework, to enhance LLMs' performance in ECI. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
SERE introduces a novel retrieval mechanism that leverages three structural concepts to improve the selection of examples for guiding LLMs in causal reasoning:

1. **Conceptual Path Metric**: This metric quantifies the conceptual relationship between events using edit distance derived from ConceptNet, allowing for a nuanced understanding of event relationships.
2. **Syntactic Metric**: This metric employs tree edit distance to assess structural similarity between syntactic trees, facilitating the retrieval of examples that are structurally aligned with the target events.
3. **Causal Pattern Filtering**: This component filters retrieved examples based on predefined causal structures, utilizing LLMs to ensure that only relevant examples are considered.

The integration of these metrics allows SERE to select more pertinent examples, thereby enhancing the few-shot learning capabilities of LLMs in ECI tasks. The authors conducted extensive experiments across multiple ECI datasets, although specific details regarding training compute and hyperparameters are not disclosed.

**Results**  
SERE demonstrates significant improvements over baseline models in ECI tasks. The authors report that SERE achieves an accuracy increase of up to 15% compared to standard LLMs on benchmark datasets, including the ACE and SemEval datasets. Additionally, SERE reduces the rate of causal hallucination by approximately 20%, indicating a marked improvement in the reliability of causal predictions. These results suggest that the structural retrieval approach effectively mitigates biases inherent in LLMs.

**Limitations**  
The authors acknowledge several limitations, including the reliance on the quality of the underlying datasets and the potential for the structural metrics to miss nuanced causal relationships not captured by the defined metrics. Furthermore, the performance gains may vary across different domains, and the framework's scalability to larger datasets or more complex causal structures remains untested. The authors do not address the computational overhead introduced by the retrieval mechanism, which may impact real-time applications.

**Why it matters**  
The implications of this work are significant for advancing ECI methodologies, particularly in applications requiring robust causal reasoning, such as information extraction, knowledge graph construction, and automated reasoning systems. By enhancing LLMs' capabilities through structured example retrieval, SERE paves the way for more reliable and interpretable causal inference in NLP tasks. This framework could serve as a foundation for future research aimed at refining causal reasoning in AI systems, potentially influencing a wide range of applications in both academic and industrial settings.

Authors: Zhifeng Hao, Zhongjie Chen, Junhao Lu, Shengyin Yu, Guimin Hu, Keli Zhang, Ruichu Cai, Boyan Xu  
Source: arXiv:2605.03701  
URL: https://arxiv.org/abs/2605.03701v1
