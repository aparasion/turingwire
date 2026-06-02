---
title: "Towards Multidisciplinary Summarization of Hospital Stays: Efficient Sentence-Level Clinical Provenance Categorization"
date: 2026-06-01 16:57:51 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.02487v1"
arxiv_id: "2606.02487"
authors: ["Baris Karacan", "Vaibhav Bhargava", "Barbara Di Eugenio", "Natalie Parde", "Mary Khetani", "Yu-Shan Tseng"]
slug: towards-multidisciplinary-summarization-of-hospital-stays-ef
summary_word_count: 405
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This study presents a clinical provenance categorization pipeline using fine-tuned LLMs to enhance multidisciplinary summarization in NICU settings."
---

**Problem**  
The paper addresses the challenge of effective summarization in high-complexity clinical environments, specifically the Neonatal Intensive Care Unit (NICU), where insights from various healthcare professionals must be synthesized from extensive free-text notes. The authors highlight a gap in the literature regarding structured summarization that requires accurate categorization of sentence-level provenance across multi-source clinical notes. This work is a pilot study and is presented as a preprint, indicating that it has not yet undergone peer review.

**Method**  
The authors propose a clinical provenance categorization pipeline that employs supervised fine-tuning (SFT) of large language models (LLMs). They adapted two variants of the Llama-3 model (8B and 70B parameters) to the MedSecId dataset, which consists of 2,002 MIMIC-III notes annotated with clinical provenance headers. The training process involved fine-tuning these models on the annotated dataset to achieve high accuracy in provenance categorization. The evaluation included a cross-domain generalization assessment using a gold-standard dataset of 227 sentence-level spans derived from multidisciplinary NICU summaries. The study also explored the effects of model capacity and quantization on performance.

**Results**  
Both Llama-3 models achieved in-domain Macro F1 scores exceeding 92% on the MedSecId dataset. In terms of cross-domain performance, the 70B model demonstrated a significant improvement, with a 7% increase in Macro F1 score after fine-tuning, while the 8B model showed only marginal changes. Notably, the quantized version of the fine-tuned 70B model outperformed its full-precision counterpart, indicating that quantization can effectively reduce computational requirements without sacrificing performance.

**Limitations**  
The authors acknowledge that their study is a pilot and thus may not generalize across all clinical settings. They also note that the reliance on a specific dataset (MIMIC-III) may limit the applicability of their findings to other clinical environments. Additionally, the study does not address potential biases in the training data or the implications of model interpretability in clinical contexts.

**Why it matters**  
This research has significant implications for improving structured summarization in clinical settings, particularly in multidisciplinary environments like the NICU. By demonstrating the effectiveness of fine-tuning large language models for clinical provenance categorization, the study paves the way for more coherent and contextually relevant summaries that can enhance communication among healthcare teams. The findings suggest that sufficient model capacity is essential for maintaining semantic flexibility during cross-domain clinical transfer, and that efficient quantized adaptation can facilitate structured provenance modeling for downstream summarization tasks. This work contributes to the ongoing discourse on leveraging LLMs in healthcare, as published in [arXiv](https://arxiv.org/abs/2606.02487v1).
