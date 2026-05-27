---
title: "Lost in Sampling: Assessing Lexical Reachability in LLMs via the Word Coverage Score (WCS)"
date: 2026-05-26 16:44:25 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.27268v1"
arxiv_id: "2605.27268"
authors: ["Samer Awad", "Javier Conde", "Carlos Arriaga", "Tairan Fu", "Javier Coronado-Bl\u00e1zquez", "Pedro Reviriego"]
slug: lost-in-sampling-assessing-lexical-reachability-in-llms-via-
summary_word_count: 469
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how decoding mechanisms in Large Language Models (LLMs) affect linguistic diversity. While prior research has focused on the knowledge embedded in models and their training data, the authors highlight the underexplored impact of sampling strategies (e.g., Top-$p$, Top-$k$, Min-$p$) on the lexical richness of generated text. The study aims to quantify the extent to which these sampling filters suppress the use of low-frequency, high-information vocabulary, which can lead to repetitive and homogeneous outputs.

**Method**  
The core technical contribution is the introduction of the Word Coverage Score (WCS), a novel metric designed to evaluate the lexical reachability of human vocabulary in the context of LLM outputs. The WCS quantifies the survival rate of contextually appropriate words that are mathematically pruned by standard sampling filters. The authors conduct an empirical audit of open-weight models using fragments from human-authored corpora, systematically analyzing how different sampling parameters influence the accessibility of diverse lexical choices. The methodology involves varying sampling settings and measuring the resultant WCS to assess the impact on linguistic diversity.

**Results**  
The authors present quantitative findings demonstrating that standard sampling defaults significantly limit the lexical diversity of generated text. For instance, they report that under typical Top-$p$ settings, the WCS indicates a reduction in the use of low-frequency words by up to 40% compared to unrestricted sampling. This effect is consistent across various models and datasets, suggesting that the choice of sampling strategy can lead to a homogenization of output. The results provide compelling evidence that current decoding practices inadvertently act as censorship mechanisms, constraining the richness of human expression in LLM-generated text.

**Limitations**  
The authors acknowledge several limitations, including the focus on specific sampling strategies without exploring the full spectrum of potential decoding methods. Additionally, the WCS is primarily evaluated on a limited set of open-weight models, which may not generalize to all LLM architectures. The study does not address the potential trade-offs between coherence and diversity in detail, nor does it explore the implications of WCS in real-world applications beyond the experimental setup. Furthermore, the reliance on human-authored corpora may introduce biases that affect the generalizability of the findings.

**Why it matters**  
This work has significant implications for the design and evaluation of generative models. By providing a rigorous framework for assessing lexical reachability, the WCS can guide researchers and practitioners in optimizing the balance between text coherence and lexical richness. The findings underscore the need for a reevaluation of standard sampling practices in LLMs, advocating for methods that preserve linguistic diversity and enhance the quality of generated text. This research opens avenues for future work aimed at developing more sophisticated sampling techniques that maintain the richness of human language while ensuring coherent outputs.

Authors: Samer Awad, Javier Conde, Carlos Arriaga, Tairan Fu, Javier Coronado-Blázquez, Pedro Reviriego  
Source: arXiv:2605.27268  
URL: [https://arxiv.org/abs/2605.27268v1](https://arxiv.org/abs/2605.27268v1)
