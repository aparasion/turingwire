---
title: "A multilingual hallucination benchmark: MultiWikiQHalluA"
date: 2026-05-04 11:57:56 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.02504v1"
arxiv_id: "2605.02504"
authors: ["Freja Thoresen", "Dan Saattrup Smart"]
slug: a-multilingual-hallucination-benchmark-multiwikiqhallua
summary_word_count: 398
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the evaluation of hallucination phenomena in multilingual settings, particularly focusing on lower-resource languages. Most existing research on hallucinations in AI models has predominantly centered on English, leaving a significant void in understanding how these findings translate to other languages. The authors present a preprint work that introduces a benchmark for assessing faithfulness hallucinations across 306 languages, thereby expanding the scope of hallucination evaluation beyond English-centric studies.

**Method**  
The authors leverage the multilingual MultiWikiQA dataset to create synthetic hallucination datasets using the LettuceDetect framework. This approach enables the generation of token-level hallucination classifiers specifically for 30 European languages. The classifiers are trained to identify instances of hallucinations—defined as model-generated content that is fluent and plausible but diverges from the input or is internally inconsistent. The evaluation involves several models, including Qwen3-0.6B, Qwen3-14B, Gemma-3-12B-IT, cogito-v1-preview-qwen-32B, and cogito-v1-preview-llama-70B. The authors systematically assess the hallucination rates across selected languages: English, Danish, German, and Icelandic.

**Results**  
The findings reveal that Qwen3-0.6B exhibits the highest hallucination rates, with up to 60% of its answers containing at least one hallucination, particularly peaking in Icelandic. In contrast, larger models such as cogito-v1-preview-qwen-32B and cogito-v1-preview-llama-70B demonstrate significantly lower hallucination rates across most languages evaluated. The results indicate a consistent trend where lower-resource languages, especially Icelandic, experience higher hallucination rates compared to their higher-resource counterparts. This suggests that model performance is not uniform across languages, highlighting the need for tailored evaluations.

**Limitations**  
The authors acknowledge that their study is limited to a selection of European languages and may not fully represent the diversity of multilingual contexts. Additionally, the reliance on synthetic datasets may introduce biases that do not reflect real-world scenarios. The paper does not address the potential impact of varying model architectures or training data quality on hallucination rates, which could be critical for understanding the underlying causes of hallucinations in different languages.

**Why it matters**  
This work has significant implications for the development of multilingual AI systems, particularly in ensuring the reliability and faithfulness of generated content across diverse languages. By highlighting the discrepancies in hallucination rates between high- and low-resource languages, the study underscores the necessity for more comprehensive evaluation frameworks that account for linguistic diversity. This research could inform future model training and evaluation strategies, ultimately leading to more robust and trustworthy AI applications in multilingual contexts.

Authors: Freja Thoresen, Dan Saattrup Smart  
Source: arXiv:2605.02504  
URL: [https://arxiv.org/abs/2605.02504v1](https://arxiv.org/abs/2605.02504v1)
