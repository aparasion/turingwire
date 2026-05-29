---
title: "GRUFF: LLM Pronoun Fidelity, Reasoning, and Biases in German"
date: 2026-05-28 16:47:46 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.30214v1"
arxiv_id: "2605.30214"
authors: ["Fabian Mewes", "Anne Lauscher", "Vagrant Gautam"]
slug: gruff-llm-pronoun-fidelity-reasoning-and-biases-in-german
summary_word_count: 411
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in understanding pronoun fidelity and reasoning biases in German language models, a topic that has been predominantly explored in English. The authors highlight the lack of large-scale datasets for evaluating pronoun usage and biases in German, particularly in the context of its complex grammatical gender system. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors introduce the GRUFF dataset, a comprehensive resource designed to evaluate pronoun fidelity in German. The dataset encompasses four distinct gender agreement systems for nouns and includes four sets of pronouns. The evaluation focuses on the ability of large language models (LLMs) to maintain grammatical agreement with masculine and feminine entities, as well as neopronouns (xier and en). The study employs various LLM architectures, including encoder-only models, to assess their robustness against distractors in discourse. The training compute specifics are not disclosed, but the dataset is made publicly available to facilitate further research.

**Results**  
The findings reveal that LLMs exhibit strong grammatical agreement for masculine and feminine pronouns when explicit context is absent. However, performance diminishes significantly for neopronouns. The models generally struggle with distractors, although encoder-only models demonstrate greater robustness in German compared to their English counterparts. Notably, the correlation of occupational stereotypes across grammatical cases is found to be weak, with exceptions observed in models with closely related architectures. The results indicate that the models' performance varies significantly based on the gender agreement system employed.

**Limitations**  
The authors acknowledge several limitations, including the potential biases inherent in the dataset and the models' reliance on training data that may not fully represent the diversity of German language use. They also note that the evaluation primarily focuses on grammatical agreement and does not encompass the broader implications of gender biases in language. An additional limitation is the lack of exploration into the performance of other model architectures beyond those tested.

**Why it matters**  
This research has significant implications for the development of gender-inclusive language models and the understanding of referential reasoning in languages with complex gender systems. By providing a robust dataset and insights into model performance, the work encourages further exploration of biases in language processing and the importance of grammatical gender in shaping model outputs. The findings may inform future research on multilingual models and their ability to handle gender-related linguistic phenomena, ultimately contributing to more equitable AI systems.

Authors: Fabian Mewes, Anne Lauscher, Vagrant Gautam  
Source: arXiv:2605.30214  
URL: [https://arxiv.org/abs/2605.30214v1](https://arxiv.org/abs/2605.30214v1)
