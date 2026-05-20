---
title: "Mind Your Moras: Orthography-Aware Error Analysis of Neural Japanese Morphological Generation"
date: 2026-05-19 16:04:33 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.20043v1"
arxiv_id: "2605.20043"
authors: ["Wen Zhang"]
slug: mind-your-moras-orthography-aware-error-analysis-of-neural-j
summary_word_count: 411
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how orthographic representations, specifically hiragana in Japanese, influence the performance of neural models in morphological generation tasks. While existing literature has focused on aggregate accuracy, it often overlooks the systematic errors that arise from the interaction between orthography and morphology. The authors aim to provide a detailed error analysis of past-tense morphological inflection, highlighting the need for orthography-aware evaluation in morphologically rich languages.

**Method**  
The authors evaluate two character-level sequence-to-sequence architectures on the task of Japanese past-tense formation, utilizing datasets formatted according to the SIGMORPHON 2020 and 2023 shared task conventions. They introduce a concise error taxonomy that identifies seven primary failure modes, with a particular focus on gemination-related errors. The models are trained on datasets that reflect the complexities of Japanese morphology, and the analysis includes both quantitative metrics and qualitative assessments of error types. The architectures are subjected to rigorous testing across various random seeds to ensure the robustness of the findings.

**Results**  
The models achieve high aggregate accuracy; however, they exhibit systematic errors that are linguistically interpretable. Notably, gemination-related errors account for 75-80% of the total errors, particularly affecting verbs with stems ending in the vowel 'e', which require gemination before the past-tense suffix. The error patterns are consistent across different architectures and random seeds, indicating a strong interaction between orthographic representation and morphological structure. This suggests that while the models perform well overall, they struggle with specific linguistic phenomena that are critical for accurate morphological generation.

**Limitations**  
The authors acknowledge that their analysis is limited to past-tense morphological inflection and may not generalize to other morphological forms or languages. Additionally, the focus on character-level architectures may overlook the potential benefits of more complex models, such as those incorporating contextual embeddings or attention mechanisms. The study also does not explore the impact of varying training data sizes or the effects of different hyperparameter settings on model performance.

**Why it matters**  
This work has significant implications for the development of neural models in morphologically complex languages. By highlighting the importance of orthography-aware evaluation, the authors provide a framework for understanding how linguistic properties influence model generalization. This could inform future research on morphological generation and error analysis, leading to improved model architectures and training methodologies that better account for the intricacies of language. The findings also suggest that addressing specific error types, such as gemination, could enhance the performance of models in similar tasks.

Authors: Wen Zhang  
Source: arXiv:2605.20043  
URL: https://arxiv.org/abs/2605.20043v1
