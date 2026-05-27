---
title: "Semantic Gradients Interactions in SSD: A Case Study in Racial Identity and Hate Speech"
date: 2026-05-26 17:33:02 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: ["Supervised Semantic Differential", "UC Berkeley Measuring Hate Speech corpus"]
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.27322v1"
arxiv_id: "2605.27322"
authors: ["Felix Ostrowicki", "Hubert Plisiecki"]
slug: semantic-gradients-interactions-in-ssd-a-case-study-in-racia
summary_word_count: 423
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the literature regarding the interpretability of semantic meaning variations in supervised learning contexts, particularly in the realm of hate speech detection. The authors propose a novel framework, interaction SSD, as an extension of the Supervised Semantic Differential (SSD) to model how semantic judgments are influenced by moderators such as racial identity. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the interaction SSD framework, which extends the traditional SSD by incorporating interaction effects. The method estimates three types of gradients: a main semantic gradient, an interaction gradient, and conditional gradients. These gradients are derived from the underlying data and are interpretable using standard SSD tools. The authors apply this framework to the UC Berkeley Measuring Hate Speech corpus, focusing on how annotator racial identity influences hate-speech judgments. The training process involves a supervised learning setup where the model learns to predict hate-speech ratings based on semantic cues, with the interaction SSD allowing for the quantification of moderation effects.

**Results**  
The interaction SSD framework reveals a significant moderation effect of annotator racial identity on hate-speech judgments. Specifically, the shared semantic gradient contrasts dehumanizing hostility with counter-speech, while the interaction gradient uncovers nuanced differences in how various semantic cues predict hate-speech ratings across different racial identities. The authors report effect sizes that indicate substantial differences in hate-speech ratings based on the racial identity of the annotators, although specific numerical results and comparisons to baseline models are not detailed in the abstract.

**Limitations**  
The authors acknowledge that their approach may be limited by the representativeness of the UC Berkeley Measuring Hate Speech corpus, which may not capture the full spectrum of hate speech across diverse contexts. Additionally, the interaction SSD framework's reliance on the quality of the semantic cues and the annotators' biases could introduce variability in the results. The paper does not address potential scalability issues when applying this method to larger datasets or other domains beyond hate speech.

**Why it matters**  
The introduction of interaction SSD has significant implications for the field of natural language processing, particularly in the areas of bias detection and interpretability in machine learning models. By making moderated meaning-outcome relationships statistically testable and interpretable, this framework can enhance the understanding of how different demographic factors influence semantic judgments. This work paves the way for future research to explore similar interactions in other sensitive domains, potentially leading to more equitable and transparent AI systems.

Authors: Felix Ostrowicki, Hubert Plisiecki  
Source: arXiv:2605.27322  
URL: https://arxiv.org/abs/2605.27322v1
