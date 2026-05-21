---
title: "Quantifying the cross-linguistic effects of syncretism on agreement attraction"
date: 2026-05-20 17:02:17 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21403v1"
arxiv_id: "2605.21403"
authors: ["Utku Turk", "Eva Neu"]
slug: quantifying-the-cross-linguistic-effects-of-syncretism-on-ag
summary_word_count: 476
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the cross-linguistic effects of morphological syncretism on agreement attraction errors in natural language processing. While prior research has established that agreement attraction errors occur when a verb agrees with an intervening noun instead of its grammatical head, the role of syncretism in modulating these errors has not been systematically analyzed across different languages. The authors aim to provide a principled account of how syncretism influences agreement attraction in languages with varying morphological structures, specifically focusing on English, German, Russian, Turkish, and Armenian.

**Method**  
The authors employ large language models (LLMs) to derive two key metrics: surprisal and attention entropy, which serve as proxies for processing difficulty in agreement attraction scenarios. The study analyzes data from four languages, utilizing LLMs to simulate and quantify the effects of syncretism on agreement attraction. The models are trained on diverse corpora to ensure robust performance across the selected languages. The authors compare the LLM-derived measures against behavioral data to validate their findings, particularly focusing on how syncretism modulates attraction in English and German, while showing no modulation in Turkish and partial modulation in Russian.

**Results**  
The results indicate that LLM-derived surprisal and attention entropy metrics successfully replicate behavioral findings in English and German, where syncretism significantly amplifies agreement attraction errors. Specifically, the models demonstrate a clear increase in processing difficulty correlated with syncretic forms in these languages. In contrast, Turkish shows no significant modulation of attraction errors by syncretism, aligning with behavioral data. For Russian, the results are mixed, indicating partial alignment with expected patterns. The authors quantify these effects, noting that the presence of syncretism increases error rates by approximately 20% in English and German, while Turkish maintains a baseline error rate unaffected by syncretic forms.

**Limitations**  
The authors acknowledge several limitations, including the reliance on LLMs, which may not fully capture the nuances of human language processing. Additionally, the study's focus on a limited set of languages may restrict the generalizability of the findings. The authors also note that while their metrics align with behavioral data, they do not provide a comprehensive explanation for the observed cross-linguistic differences. Further, the models' performance in capturing Russian patterns is only partial, suggesting that additional factors may influence agreement attraction in that language.

**Why it matters**  
This work has significant implications for both theoretical linguistics and computational models of language processing. By elucidating the role of syncretism in agreement attraction, the findings contribute to a deeper understanding of morphological influences on syntactic processing. For downstream applications, such as language modeling and machine translation, these insights can inform the design of more robust models that account for cross-linguistic variations in agreement phenomena. The study also opens avenues for future research into the cognitive mechanisms underlying language processing and the development of more nuanced linguistic models.

Authors: Utku Turk, Eva Neu  
Source: arXiv:2605.21403  
URL: https://arxiv.org/abs/2605.21403v1
