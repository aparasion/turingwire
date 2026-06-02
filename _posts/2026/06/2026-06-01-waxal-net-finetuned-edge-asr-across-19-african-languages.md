---
title: "WAXAL-NET: Finetuned Edge ASR Across 19 African Languages"
date: 2026-06-01 15:22:35 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.02375v1"
arxiv_id: "2606.02375"
authors: ["Victor Tolulope Olufemi", "Oreoluwa Babatunde", "Ramsey Njema", "Bolarinwa Gbotemi", "Wanchi Lucia Yen", "John Uzodinma"]
slug: waxal-net-finetuned-edge-asr-across-19-african-languages
summary_word_count: 410
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper presents WAXAL-NET, a fine-tuned ASR model for 19 African languages, demonstrating superior performance over multilingual baselines."
---

**Problem**  
This work addresses the gap in automatic speech recognition (ASR) for African languages, which are often underrepresented in existing multilingual models. The authors highlight the limitations of large-scale multilingual ASR systems when applied to spontaneous speech in diverse African languages, particularly in terms of word error rates (WER). This research is presented as a preprint, indicating that it has not yet undergone peer review.

**Method**  
The authors propose WAXAL-NET, a set of compact, domain-specialized ASR models fine-tuned on the WAXAL corpus, which encompasses 19 African languages. The models are significantly smaller than traditional multilingual models, with sizes ranging from 3 to 40 times smaller. The training process involves fine-tuning on a dataset specifically curated for conversational speech, leveraging connectionist temporal classification (CTC) and autoregressive architectures. The authors also provide a comprehensive error taxonomy based on a distributed native-speaker audit, which informs the model's design and evaluation. All model weights, fine-tuning scripts, and a cleaned subset of the WAXAL corpus are made publicly available to facilitate further research.

**Results**  
WAXAL-NET achieves a macro-averaged WER of 38.0%, a substantial improvement over the best zero-shot baseline, which records a WER of 64.9%. This results in a 26.9 percentage-point reduction in error rates, demonstrating that domain specialization is more effective than scaling model size for this specific task. Additionally, the fine-tuned models maintain usable performance on out-of-distribution (OOD) speech, while zero-shot models perform better when the test domain aligns with their pretraining distribution. The authors also note that for syllabary-script languages, the character error rate (CER) to WER ratios indicate higher character-level accuracy than the WER alone suggests.

**Limitations**  
The authors acknowledge that while their fine-tuned models outperform zero-shot baselines, the performance may still vary significantly across different language families due to inherent linguistic differences. They also note that the reliance on WER as a primary metric can be misleading, particularly for languages with syllabary scripts. Furthermore, the study does not explore the potential for further improvements through additional data augmentation or advanced model architectures.

**Why it matters**  
This research has significant implications for the development of ASR systems tailored to underrepresented languages, particularly in the African context. By demonstrating that specialized models can outperform larger, generalized models, the findings encourage a shift towards domain-specific approaches in ASR research. The release of the WAXAL corpus and associated resources will likely stimulate further advancements in African language processing, as highlighted in related works on multilingual ASR systems, such as those discussed in [arXiv cs.CL](https://arxiv.org/abs/2606.02375v1).
