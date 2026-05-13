---
title: "Pretraining Exposure Explains Popularity Judgments in Large Language Models"
date: 2026-05-12 16:45:38 +0000
category: research
subcategory: other
company: "null"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.12382v1"
arxiv_id: "2605.12382"
authors: ["Jamshid Mozafari", "Bhawna Piryani", "Adam Jatowt"]
slug: pretraining-exposure-explains-popularity-judgments-in-large-
summary_word_count: 454
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the origins of popularity bias in large language models (LLMs). While previous literature has suggested that LLMs exhibit preferences for well-known entities due to popularity bias, the authors argue that it remains unclear whether these preferences stem from actual real-world popularity or are merely a reflection of statistical exposure during pretraining. The inaccessibility of most training corpora has hindered direct analysis, making this work significant in providing empirical evidence grounded in observable pretraining data.

**Method**  
The authors utilize the open OLMo models and their complete pretraining corpus, Dolma, which consists of 7.4 trillion tokens. They compute entity-level exposure statistics for 2,000 entities across five categories: Person, Location, Organization, Art, and Product. The analysis involves comparing pretraining exposure metrics against Wikipedia pageviews and two LLM popularity signals: direct scalar estimation and pairwise comparison. The methodology emphasizes the correlation between pretraining exposure and real-world popularity, particularly focusing on how these metrics influence LLM judgments of popularity.

**Results**  
The findings reveal a strong correlation between pretraining exposure and Wikipedia popularity, suggesting that exposure serves as a valid proxy for real-world salience during the training phase. Notably, LLM popularity judgments, especially when assessed through pairwise comparisons, align more closely with exposure metrics than with Wikipedia pageviews. This trend is particularly pronounced in larger models and remains consistent even in the long tail of entity popularity, where Wikipedia metrics may be less reliable. The authors provide quantitative evidence that supports the assertion that popularity biases in LLMs are predominantly shaped by pretraining exposure rather than external popularity indicators.

**Limitations**  
The authors acknowledge that their analysis is limited to the OLMo models and the Dolma corpus, which may not generalize to other LLM architectures or datasets. Additionally, while the study focuses on a diverse set of entities, the selection of only 2,000 entities may not capture the full spectrum of popularity dynamics across all domains. The reliance on Wikipedia as a benchmark for popularity could also introduce biases, as it may not represent all facets of public interest. Furthermore, the study does not explore the implications of these findings on the ethical considerations surrounding LLM deployment.

**Why it matters**  
This work has significant implications for understanding the mechanisms behind LLM behavior and the biases that arise from pretraining data. By establishing that popularity judgments in LLMs are primarily influenced by exposure rather than external popularity signals, the findings encourage researchers to reconsider how training data is curated and the potential biases that may emerge from it. This insight could inform future model training practices and the development of techniques to mitigate popularity bias, ultimately leading to more equitable and representative LLMs.

Authors: Jamshid Mozafari, Bhawna Piryani, Adam Jatowt  
Source: arXiv:2605.12382  
URL: [https://arxiv.org/abs/2605.12382v1](https://arxiv.org/abs/2605.12382v1)
