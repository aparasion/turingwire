---
title: "Adapting Large Language Models to a Low-Resource Agglutinative Language: A Comparative Study of LoRA and QLoRA for Bashkir"
date: 2026-05-06 14:14:35 +0000
category: research
subcategory: efficiency_inference
company: "DeepSeek"
secondary_companies: ["Hugging Face", "Mistral"]
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.04948v1"
arxiv_id: "2605.04948"
authors: ["Mullosharaf K. Arabov", "Svetlana S. Khaybullina"]
slug: adapting-large-language-models-to-a-low-resource-agglutinati
summary_word_count: 434
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in adapting large language models (LLMs) to low-resource agglutinative languages, specifically Bashkir, which is part of the Turkic family. The authors conduct a comparative study of parameter-efficient fine-tuning (PEFT) methods, namely LoRA and QLoRA, to evaluate their effectiveness in this context. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors employ various architectures, including DistilGPT2, GPT-2 (base and medium), Phi-2, Qwen2.5-7B, DeepSeek-7B, and Mistral-7B, to fine-tune on a Bashkir text corpus comprising 71,000 documents (46.9 million tokens). The study utilizes three random seeds for each configuration to enhance the reliability of the results. The core technical contributions include the application of LoRA and QLoRA for PEFT, with QLoRA particularly noted for its efficiency in reducing the number of trainable parameters while maintaining performance. The lowest perplexity achieved was 3.34 with full fine-tuning on GPT-2 medium, while QLoRA on Mistral-7B and Phi-2 yielded perplexities of 3.79 and 3.81, respectively, with over 40 times fewer trainable parameters compared to full fine-tuning.

**Results**  
The results indicate that while QLoRA can achieve competitive performance with significantly fewer parameters, the effectiveness of PEFT methods is highly dependent on the choice of the base model and its tokenizer. For instance, DeepSeek-7B with a rank of 8 exhibited a perplexity of 129.55, indicating substantial quality degradation. Qualitatively, the models with the best perplexity did not necessarily produce the most coherent outputs; for example, QLoRA-tuned models generated coherent Bashkir text, whereas the fully fine-tuned model with the lowest perplexity often switched to English in its outputs. These findings suggest a nuanced relationship between perplexity and output quality.

**Limitations**  
The authors acknowledge that the performance of PEFT methods can vary significantly based on the underlying model architecture and tokenizer, which may limit generalizability. They also note the potential for quality degradation in certain configurations, particularly with DeepSeek-7B. Additionally, the study is constrained by the low-resource nature of the Bashkir language, which may affect the robustness of the findings. The authors plan to release open data, code, and trained adapters to facilitate reproducibility upon acceptance.

**Why it matters**  
This research has significant implications for the adaptation of LLMs to low-resource languages, providing insights into the trade-offs between computational efficiency and output quality. The findings suggest that QLoRA on 7B-scale models can serve as a viable approach for similar languages, potentially enabling broader access to advanced NLP capabilities in underrepresented linguistic contexts. This work lays the groundwork for future research in PEFT methods and their application to other low-resource languages.

Authors: Mullosharaf K. Arabov, Svetlana S. Khaybullina  
Source: arXiv:2605.04948  
URL: [https://arxiv.org/abs/2605.04948v1](https://arxiv.org/abs/2605.04948v1)
