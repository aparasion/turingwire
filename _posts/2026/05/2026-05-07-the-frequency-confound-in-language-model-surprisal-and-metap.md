---
title: "The Frequency Confound in Language-Model Surprisal and Metaphor Novelty"
date: 2026-05-07 16:20:37 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.06506v1"
arxiv_id: "2605.06506"
authors: ["Omar Momen", "Sina Zarrie\u00df"]
slug: the-frequency-confound-in-language-model-surprisal-and-metap
summary_word_count: 480
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the relationship between language-model (LM) surprisal and metaphor novelty, particularly highlighting the confounding effect of lexical frequency. Previous studies have suggested a correlation between LM surprisal and metaphor novelty judgments, but the authors argue that this relationship may be misleading due to the influence of word frequency. The paper aims to clarify how these two factors interact and to challenge the prevailing assumption that LM surprisal is a reliable proxy for metaphor novelty.

**Method**  
The authors conducted an empirical analysis using surprisal estimates derived from eight different sizes of the Pythia language model, evaluated across 154 training checkpoints. They employed two distinct measures of word frequency to assess its impact on metaphor novelty ratings. The analysis involved comparing the predictive power of surprisal and word frequency on metaphor novelty, utilizing regression techniques to quantify their relationships. The study systematically tracked how the surprisal-novelty association evolved over the training stages of the language models, particularly focusing on the early and later stages of training.

**Results**  
The findings reveal that word frequency is a more robust predictor of metaphor novelty than LM surprisal across all model sizes and training checkpoints. Specifically, the authors report that the correlation between surprisal and metaphor novelty peaks during the early training stages of the models, after which it declines. In contrast, the correlation between surprisal and lexical frequency increases over the same period. These results suggest that the previously reported optimal settings for LM surprisal may be misleading, as they do not adequately account for the confounding influence of lexical frequency on metaphor processing. The authors provide quantitative metrics demonstrating that the effect size of word frequency on metaphor novelty ratings is significantly larger than that of surprisal.

**Limitations**  
The authors acknowledge that their analysis is limited to the Pythia model family and may not generalize to other language models or architectures. Additionally, the study focuses on metaphor novelty without exploring other linguistic phenomena that may also be influenced by the frequency-surprisal interaction. The reliance on specific frequency measures may also introduce biases, as different corpora or contexts could yield varying results. Furthermore, the paper does not address the implications of these findings for practical applications in NLP tasks beyond metaphor analysis.

**Why it matters**  
This work has significant implications for the interpretation of LM outputs in relation to linguistic phenomena. By elucidating the confounding role of lexical frequency in the surprisal-novelty relationship, the study encourages researchers to reconsider the use of LM surprisal as a standalone metric for assessing contextual predictability and processing difficulty. It highlights the necessity for more nuanced approaches in evaluating language models, particularly in tasks involving metaphor and other figurative language forms. This research could inform future studies on language understanding and the development of more effective NLP systems that account for frequency effects.

Authors: Omar Momen, Sina Zarrieß  
Source: arXiv:2605.06506  
URL: [https://arxiv.org/abs/2605.06506v1](https://arxiv.org/abs/2605.06506v1)
