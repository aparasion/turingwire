---
title: "Post-Hoc Understanding of Metaphor Processing in Decoder-Only Language Models via Conditional Scale Entropy"
date: 2026-05-20 16:45:59 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21391v1"
arxiv_id: "2605.21391"
authors: ["Lawhori Chakrabarti", "Jennifer Johnson-Leung", "Bert Baumgaertner", "Aleksandar Vakanski", "Min Xian", "Boyu Zhang"]
slug: post-hoc-understanding-of-metaphor-processing-in-decoder-onl
summary_word_count: 458
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in mechanistic interpretability of transformer models, specifically regarding how these models process metaphorical language. While existing literature has explored various aspects of language understanding, the specific mechanisms by which decoder-only architectures reinterpret metaphorical tokens—where contextual meanings diverge from literal interpretations—remain inadequately understood. The authors aim to elucidate the structural patterns of updates in transformer layers when processing metaphors, contributing to a deeper understanding of language model behavior.

**Method**  
The authors introduce Conditional Scale Entropy (CSE), a novel metric derived from wavelet analysis, to quantify the breadth of transformer computations across different frequency scales at each layer position. Two theorems are presented, demonstrating that CSE is invariant to the magnitude of updates, allowing for a focus on the structural patterns of updates rather than their intensity. The study employs a range of decoder-only architectures, including models from the GPT-2 family, LLaMA-2 7B, and GPT-oss 20B, with parameter counts ranging from 124M to 20B. The training compute specifics are not disclosed, but the analysis involves examining the spectral breadth of metaphorical versus literal tokens across contiguous layer positions.

**Results**  
The findings reveal that metaphorical tokens exhibit significantly higher spectral breadth compared to literal tokens across all tested models. This effect is consistent across the early-to-mid relative depth range and survives cluster-based permutation correction, indicating robustness. The authors also conduct an independent analysis of 200 naturalistic metaphor-usage pairs (VUA), which corroborates their findings. Specificity controls demonstrate that the observed effects are not attributable to semantic complexity or matched propositional content. The results suggest a consistent signature of multi-scale coordination in metaphor processing, with CSE serving as a reliable tool for analyzing cross-depth structures in transformer architectures.

**Limitations**  
The authors acknowledge that their analysis is limited to decoder-only architectures and may not generalize to encoder-decoder models or other architectures. Additionally, while the study controls for semantic complexity, it does not explore the potential influence of other linguistic features, such as syntactic structure or pragmatic context, on metaphor processing. The reliance on specific model families may also limit the generalizability of the findings across the broader landscape of language models.

**Why it matters**  
This work has significant implications for the field of natural language processing and mechanistic interpretability. By establishing CSE as a principled method for analyzing transformer behavior, the study opens avenues for further research into the cognitive and structural underpinnings of metaphor processing in language models. Understanding these mechanisms can enhance model design, improve interpretability, and inform the development of more sophisticated language understanding systems. The insights gained may also contribute to advancements in applications requiring nuanced language comprehension, such as sentiment analysis, creative writing, and human-computer interaction.

Authors: Lawhori Chakrabarti, Jennifer Johnson-Leung, Bert Baumgaertner, Aleksandar Vakanski, Min Xian, Boyu Zhang  
Source: arXiv:2605.21391  
URL: [https://arxiv.org/abs/2605.21391v1](https://arxiv.org/abs/2605.21391v1)
