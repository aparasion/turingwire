---
title: "Loong: A Human-Like Long Document Translation Agent with Observe-and-Act Adaptive Context Selection"
date: 2026-05-28 17:32:25 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.30274v1"
arxiv_id: "2605.30274"
authors: ["Yutong Wang", "Xuebo Liu", "Derek F. Wong", "Zhilin Li", "Rongqing Jiang", "Min Zhang"]
slug: loong-a-human-like-long-document-translation-agent-with-obse
summary_word_count: 446
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing large language models in document-level translation, particularly the constraints imposed by fixed context windows that hinder global coherence and the presence of redundant contextual information that negatively impacts translation quality. The authors propose a novel approach to long document translation, which is not only a significant gap in the literature but also a preprint work, indicating that it has not yet undergone peer review.

**Method**  
The core technical contribution of this work is the development of the Loong translation agent, which incorporates a 3E memory module (Essence-Exemplar-Entity) designed to store and manage historical context effectively. This module retains summaries, sentence pairs, and entity records, allowing for a more nuanced understanding of the document's content. Loong employs a reinforcement learning framework to optimize its context selection policy, utilizing preference data derived from its own sampled observe-and-act reasoning trajectories. This adaptive context selection enables Loong to perform deep reasoning, identifying the most relevant context for translation rather than passively attending to all historical data. The training compute details are not disclosed, but the architecture's reliance on reinforcement learning suggests a potentially high computational demand.

**Results**  
Empirical evaluations demonstrate that Loong significantly outperforms established baselines in English ↔ Chinese, German, and French translation tasks. The reported average gains are up to 13.0 BLEU points across three evaluation metrics, indicating substantial improvements in translation quality. The benchmarks used for evaluation are not specified in the abstract, but the results suggest that Loong exhibits strong generalization capabilities across different domains and maintains robustness against contextual noise, which is critical for ultra-long document translation.

**Limitations**  
The authors acknowledge that while Loong shows promising results, there are inherent limitations, such as the potential for overfitting to the training data due to the reinforcement learning approach. Additionally, the paper does not address the scalability of the 3E memory module in extremely large datasets or the computational efficiency of the observe-and-act reasoning process. Furthermore, the lack of peer review raises questions about the reproducibility and validation of the results presented.

**Why it matters**  
The implications of this work are significant for downstream applications in machine translation, particularly in scenarios requiring high-quality translations of long documents, such as legal texts, academic papers, and technical manuals. By improving context selection and coherence in translations, Loong could enhance the usability of machine translation systems in professional settings. This research also opens avenues for further exploration into adaptive context management and reinforcement learning applications in natural language processing, potentially influencing future architectures and methodologies in the field.

Authors: Yutong Wang, Xuebo Liu, Derek F. Wong, Zhilin Li, Rongqing Jiang, Min Zhang, Shimin Tao, Daimeng Wei et al.  
Source: arXiv:2605.30274  
URL: https://arxiv.org/abs/2605.30274v1
