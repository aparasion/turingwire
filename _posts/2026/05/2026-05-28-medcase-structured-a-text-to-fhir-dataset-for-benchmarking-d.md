---
title: "MedCase-Structured: A Text-to-FHIR Dataset for Benchmarking Diagnostic Reasoning in Clinically Realistic EHR Settings"
date: 2026-05-28 17:42:43 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.30295v1"
arxiv_id: "2605.30295"
authors: ["Valentina Bui Muti", "Eug\u00e9nie Dulout", "Ziquan Fu"]
slug: medcase-structured-a-text-to-fhir-dataset-for-benchmarking-d
summary_word_count: 435
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in evaluating large language models (LLMs) for clinical reasoning within the context of electronic health records (EHRs). Existing benchmarks often utilize static datasets or unstructured inputs, which do not accurately reflect the structured, interoperable formats (HL7 FHIR R4) prevalent in clinical settings. The authors present a preprint work that aims to create a more realistic evaluation framework for clinical decision support systems by generating structured datasets from unstructured clinical narratives.

**Method**  
The authors propose a novel pipeline for generating HL7 FHIR R4 bundles from unstructured text, which involves a two-stage process: LLM generation followed by terminology-grounded validation and repair. This approach aims to minimize hallucinations of codes and ensure both structural and semantic consistency in the generated FHIR data. The dataset, named MedCase-Structured, is constructed from clinician-authored diagnostic cases, achieving a valid FHIR generation rate of 82.5%. The authors do not disclose specific details regarding the architecture of the LLMs used, the loss functions, or the compute resources required for training, focusing instead on the dataset generation process.

**Results**  
The evaluation of LLMs on the MedCase-Structured dataset reveals a significant drop in diagnostic accuracy when using structured FHIR inputs compared to plain text inputs. The authors report that LLMs exhibit consistently lower performance metrics on structured data, underscoring the necessity for deployment-aligned benchmarking. While specific numerical results are not provided in the abstract, the implication is that the performance gap is substantial enough to warrant attention in future research.

**Limitations**  
The authors acknowledge that the generated dataset is synthetic and may not fully capture the complexities of real-world clinical data. Additionally, they note that the reliance on LLMs for generating structured data could introduce biases or inaccuracies that may not be present in actual clinical scenarios. An obvious limitation not explicitly mentioned is the potential lack of generalizability of the findings across different clinical contexts or EHR systems, as the dataset is based on a specific set of clinician-authored cases.

**Why it matters**  
This work has significant implications for the development and evaluation of AI systems in healthcare. By providing a structured dataset that aligns with real-world clinical practices, it enables more accurate assessments of LLMs in diagnostic reasoning tasks. The findings highlight the critical need for benchmarking methodologies that reflect the operational realities of clinical environments, which could influence future research directions in clinical AI and the design of decision support tools. The paper sets a precedent for the integration of structured data formats in the evaluation of AI systems, potentially leading to improved clinical outcomes.

Authors: Valentina Bui Muti, Eugénie Dulout, Ziquan Fu  
Source: arXiv:2605.30295  
URL: https://arxiv.org/abs/2605.30295v1
