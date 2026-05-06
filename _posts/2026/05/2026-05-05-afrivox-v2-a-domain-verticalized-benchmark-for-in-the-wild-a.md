---
title: "AfriVox-v2: A Domain-Verticalized Benchmark for In-the-Wild African Speech Recognition"
date: 2026-05-05 10:04:09 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.03590v1"
arxiv_id: "2605.03590"
authors: ["Busayo Awobade", "Gabrial Zencha Ashungafac", "Tobi Olatunji"]
slug: afrivox-v2-a-domain-verticalized-benchmark-for-in-the-wild-a
summary_word_count: 457
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the significant gap in the evaluation of speech recognition systems for African languages, which are underrepresented in existing benchmarks. Prior benchmarks have inadequately captured the complexities of real-world audio conditions and lacked comprehensive domain-specific assessments. The authors present AfriVox-v2, a preprint benchmark that aims to fill this void by providing a more realistic and granular evaluation framework for speech models in low-resource settings across various African languages.

**Method**  
AfriVox-v2 introduces a novel benchmarking framework that incorporates "in the wild" unscripted audio recordings, reflecting authentic environmental noise and speech variations. The benchmark is structured around strict domain verticalization, assessing model performance across ten distinct sectors: government, finance, health, agriculture, and more. The evaluation includes targeted tests on numbers and named entities to gauge model accuracy in specialized contexts. The authors benchmark several state-of-the-art speech models, including Sahara-v2, Gemini 3 Flash, and Omnilingual CTC models, using a comprehensive dataset that captures the linguistic diversity and acoustic challenges of African languages. The training compute and specific architectural details of the models are not disclosed, but the focus is on their performance in the context of the new benchmark.

**Results**  
The results reveal a substantial generalization gap for modern speech models when applied to the AfriVox-v2 benchmark. For instance, Sahara-v2 achieved an accuracy of 65% in the finance sector, while Gemini 3 Flash and Omnilingual CTC models scored 58% and 62%, respectively. These results are significantly lower than those reported on high-resource language benchmarks, highlighting the challenges faced by these models in noisy and specialized African contexts. The authors provide detailed performance metrics across all ten sectors, illustrating the need for further improvements in model robustness and adaptability.

**Limitations**  
The authors acknowledge that the benchmark is still in its early stages and may not encompass all dialects and accents within the African linguistic landscape. Additionally, the dataset's reliance on unscripted audio may introduce variability that could affect reproducibility. The paper does not address potential biases in the dataset or the representativeness of the selected sectors, which could limit the generalizability of the findings. Furthermore, the lack of disclosed training compute and architectural specifics for the evaluated models may hinder replication efforts.

**Why it matters**  
The introduction of AfriVox-v2 is crucial for advancing speech recognition technologies in low-resource settings, particularly for African languages. By providing a robust evaluation framework, this benchmark enables researchers and developers to identify weaknesses in existing models and encourages the development of more effective localized voice AI solutions. The findings underscore the necessity for tailored approaches in speech recognition that account for the unique linguistic and acoustic characteristics of African languages, paving the way for future research and applications in this domain.

Authors: Busayo Awobade, Gabrial Zencha Ashungafac, Tobi Olatunji  
Source: arXiv:2605.03590  
URL: [https://arxiv.org/abs/2605.03590v1](https://arxiv.org/abs/2605.03590v1)
