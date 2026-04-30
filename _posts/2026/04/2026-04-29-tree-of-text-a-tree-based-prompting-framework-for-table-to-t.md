---
title: "Tree-of-Text: A Tree-based Prompting Framework for Table-to-Text Generation in the Sports Domain"
date: 2026-04-29 10:05:18 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.26501v1"
arxiv_id: "2604.26501"
authors: ["Shang-Hsuan Chiang", "Tsan-Tsung Yang", "An-Zi Yen", "Wen-Chih Peng"]
slug: tree-of-text-a-tree-based-prompting-framework-for-table-to-t
summary_word_count: 431
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing table-to-text generation methods in the sports domain, particularly the reliance on large annotated datasets in traditional model-based approaches and the hallucination issues faced by prompt-based methods using large language models (LLMs). The authors propose a novel framework, Tree-of-Text, to enhance the generation of sports game reports from structured tables. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the Tree-of-Text framework, which employs a tree-structured prompting mechanism to facilitate a three-stage generation process:  
1. **Content Planning**: This stage involves selecting relevant operations and arguments from the input tables, effectively determining the key information to be reported.  
2. **Operation Execution**: Here, the framework decomposes large tables into smaller, manageable sub-tables, allowing for more focused processing of the data.  
3. **Content Generation**: In this final stage, the outputs from the previous steps are merged and rewritten into a coherent narrative report. The authors do not disclose specific architectural details of the LLMs used or the exact training compute, but the framework is designed to optimize the use of LLMs for table comprehension and narrative generation.

**Results**  
The Tree-of-Text framework demonstrates significant performance improvements over existing methods. On the ShuttleSet+ benchmark, it outperforms prior approaches, achieving superior results in ROUGE (RG) and Content Overlap (CO) metrics on the RotoWire-FG dataset. Additionally, it excels in Content Similarity (CS) and CO metrics on the MLB dataset. Notably, Tree-of-Text operates with approximately 40% of the time and cost compared to the Chain-of-Table method, indicating a substantial efficiency gain while maintaining or improving output quality.

**Limitations**  
The authors acknowledge that the framework's performance may be contingent on the quality and structure of the input tables, which could limit its applicability to less structured or noisy data. They also do not address potential scalability issues when applied to larger datasets or more complex sports scenarios. Furthermore, the reliance on LLMs may still introduce some degree of hallucination, particularly if the underlying model has not been fine-tuned for the specific sports domain.

**Why it matters**  
The Tree-of-Text framework represents a significant advancement in the field of table-to-text generation, particularly for sports reporting. By effectively combining structured prompting with LLM capabilities, it opens new avenues for generating high-quality narratives from structured data with reduced resource requirements. This work has implications for automating sports journalism, enhancing data-driven storytelling, and potentially influencing the design of future prompt-based systems in other domains where structured data needs to be translated into coherent text.

Authors: Shang-Hsuan Chiang, Tsan-Tsung Yang, An-Zi Yen, Wen-Chih Peng  
Source: arXiv:2604.26501  
URL: [https://arxiv.org/abs/2604.26501v1](https://arxiv.org/abs/2604.26501v1)
