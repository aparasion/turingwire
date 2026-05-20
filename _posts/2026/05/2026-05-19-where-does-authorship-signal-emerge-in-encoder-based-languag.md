---
title: "Where Does Authorship Signal Emerge in Encoder-Based Language Models?"
date: 2026-05-19 14:37:51 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.19908v1"
arxiv_id: "2605.19908"
authors: ["Francis Kulumba", "Guillaume Vimont", "Laurent Romary", "Florian Cafiero"]
slug: where-does-authorship-signal-emerge-in-encoder-based-languag
summary_word_count: 467
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the understanding of how scoring mechanisms in authorship attribution models impact performance. While existing literature has established the importance of fine-tuning pretrained encoders with consistent data and loss functions, it has not sufficiently explored how variations in scoring methods can lead to substantial differences in model efficacy. The authors aim to elucidate the mechanisms behind these discrepancies, particularly focusing on the emergence of authorship signals within encoder-based language models.

**Method**  
The authors employ a combination of mechanistic interpretability tools and causal intervention techniques to analyze the impact of different scoring mechanisms on authorship attribution performance. They investigate various scoring methods, including mean pooling and late interaction, to determine how these approaches influence the consolidation of authorship signals across the layers of encoder models. The study reveals that mean pooling compels the model to consolidate authorship signals in the early to mid layers, while late interaction allows for this consolidation to occur in later layers. The authors derive insights from the gradient structures associated with each scoring method and analyze the training dynamics to illustrate how these differences manifest in distinct learning trajectories.

**Results**  
The findings indicate that models fine-tuned with different scoring mechanisms can exhibit performance variations of up to four-fold, despite being trained on the same encoder, data, and loss function. The authors benchmark their models against standard authorship attribution tasks, demonstrating that the choice of scoring mechanism significantly influences the model's ability to capture stylistic features such as word length, punctuation density, and function-word frequency. The results underscore that the scoring mechanism is a critical determinant of where in the model architecture the authorship signal is consolidated, which in turn affects overall performance.

**Limitations**  
The authors acknowledge that their study is limited to the specific scoring mechanisms analyzed and may not generalize to all possible scoring methods in authorship attribution. Additionally, the focus on encoder-based models means that the findings may not apply to other architectures, such as decoder-based or hybrid models. The authors also note that while they provide insights into the learning dynamics, the exact mechanisms by which different scoring methods influence model performance remain an area for further exploration.

**Why it matters**  
This work has significant implications for the design and evaluation of authorship attribution models. By highlighting the critical role of scoring mechanisms in the consolidation of authorship signals, the study encourages researchers to reconsider their model architectures and scoring strategies. The insights gained from this research can inform future work in authorship attribution, potentially leading to more robust and interpretable models. Furthermore, the findings may extend to other areas of natural language processing where encoder-based architectures are employed, prompting a reevaluation of how scoring and aggregation methods are utilized.

Authors: Francis Kulumba, Guillaume Vimont, Laurent Romary, Florian Cafiero  
Source: arXiv:2605.19908  
URL: https://arxiv.org/abs/2605.19908v1
