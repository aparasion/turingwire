---
title: "What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema"
date: 2026-05-20 17:02:36 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.21404v1"
arxiv_id: "2605.21404"
authors: ["Mahdi Naser Moghadasi", "Faezeh Ghaderi"]
slug: what-twelve-llm-agent-benchmark-papers-disclose-about-themse
summary_word_count: 449
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of transparency and standardization in the reporting of evaluation methodologies in large language model (LLM) agent benchmarks. The authors note that discrepancies in reported results across different papers using the same benchmarks and models often arise from variations in evaluation settings, which are not clearly documented. This preprint highlights the need for a systematic approach to audit and disclose evaluation practices in LLM research, as existing literature does not provide sufficient clarity on these aspects.

**Method**  
The authors developed a pilot audit schema consisting of five dimensions: benchmark identity, harness specification, inference settings, cost reporting, and failure breakdown. They applied this schema to twelve benchmark papers—eight focused on LLM agents and four on classical static benchmarks. The audit was conducted by a single auditor who scored each paper based on the completeness of its disclosures rather than the correctness of its results. The scoring codebook included boundary cases encountered during the audit, and the authors provide the schema as a JSON file, the codebook in Markdown format, and the raw scoring data in CSV format. The methodology emphasizes the need for a structured approach to evaluate the transparency of benchmark reporting.

**Results**  
The mean audit score for the eight agent-benchmark papers was 0.38 out of 1.0, indicating a significant lack of disclosure. In contrast, the four classical static benchmark papers scored a mean of 0.66. Notably, none of the eight agent benchmark papers disclosed inference costs, and there was a complete absence of fully specified content-addressed container images for the evaluation environment. These results highlight critical gaps in reporting practices that hinder reproducibility and comparability in LLM research.

**Limitations**  
The authors acknowledge that the audit was conducted by a single auditor in one pass, which may introduce bias and limit the reliability of the scores. They suggest that a multi-rater audit could provide a more robust assessment of disclosure practices. Additionally, the study is limited to twelve papers, which may not represent the broader landscape of LLM research. The authors do not address potential variations in the interpretation of the audit schema across different evaluators, which could affect the consistency of scoring.

**Why it matters**  
This work underscores the importance of transparency in LLM research, particularly as the field matures and the deployment of these models becomes more widespread. By providing a structured audit framework, the authors aim to encourage researchers to adopt more rigorous reporting standards, thereby enhancing the reproducibility and trustworthiness of benchmark results. The implications extend to downstream applications, where understanding the evaluation context is crucial for assessing model performance and making informed decisions about model deployment in real-world scenarios.

Authors: Mahdi Naser Moghadasi, Faezeh Ghaderi  
Source: arXiv:2605.21404  
URL: [https://arxiv.org/abs/2605.21404v1](https://arxiv.org/abs/2605.21404v1)
