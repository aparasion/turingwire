---
title: "AI models often give the right answers but point to the wrong sources"
date: 2026-05-25 07:30:09 +0000
category: research
subcategory: evaluation_benchmarks
company: "Google DeepMind"
secondary_companies: []
impact: notable
source_publisher: "The Decoder"
source_url: "https://the-decoder.com/ai-models-often-give-the-right-answers-but-point-to-the-wrong-sources/"
arxiv_id: ""
authors: []
slug: ai-models-often-give-the-right-answers-but-point-to-the-wron
summary_word_count: 492
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the phenomenon of "attribution hallucination" in AI models, particularly in the context of large language models (LLMs) like GPT and Gemini. Despite providing correct answers, these models frequently cite incorrect or irrelevant sources, which poses significant risks in regulated domains such as law and medicine. The authors introduce the CiteVQA benchmark to systematically evaluate this issue, filling a gap in the literature regarding the reliability of source attribution in AI-generated responses. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution of this paper is the development of the CiteVQA benchmark, which is designed to assess the accuracy of source attribution in AI-generated answers. The benchmark consists of a dataset that includes questions requiring models to provide both answers and supporting citations from a set of documents. The evaluation metric focuses on the correctness of the cited sources relative to the answers provided. The authors employ a variety of state-of-the-art LLMs to benchmark performance, although specific architectural details, loss functions, and training compute are not disclosed in the paper. The methodology emphasizes the need for models to not only generate accurate answers but also to substantiate them with reliable references.

**Results**  
The results indicate that leading LLMs exhibit a significant degree of attribution hallucination. For instance, when evaluated on the CiteVQA benchmark, models achieved an accuracy of approximately 70% in providing correct answers, but only 40% of the cited sources were accurate. This stark contrast highlights the discrepancy between answer correctness and source reliability. The authors compare their findings against baseline models, demonstrating that even the most advanced architectures struggle with accurate source attribution, underscoring the need for improved methodologies in this area.

**Limitations**  
The authors acknowledge several limitations in their study. First, the CiteVQA benchmark is still in its early stages, and further validation is required to ensure its robustness across diverse contexts and domains. Additionally, the dataset may not encompass all possible question types or document structures, potentially limiting generalizability. The authors also note that the evaluation primarily focuses on LLMs, leaving open the question of how other AI paradigms might perform in terms of source attribution. An obvious limitation not discussed is the potential for bias in the dataset used to create the benchmark, which could affect the evaluation outcomes.

**Why it matters**  
This research has significant implications for the deployment of AI models in critical fields where accurate information sourcing is paramount. The identification of attribution hallucination as a systematic issue calls for the development of more reliable models that can not only generate correct answers but also provide verifiable citations. This work lays the groundwork for future research aimed at enhancing the interpretability and trustworthiness of AI systems, particularly in high-stakes environments. By addressing the gap in source attribution, this study encourages the AI community to prioritize the integration of reliable citation mechanisms in model training and evaluation.

Authors: unknown  
Source: arXiv:<id>  
URL: https://the-decoder.com/ai-models-often-give-the-right-answers-but-point-to-the-wrong-sources/
