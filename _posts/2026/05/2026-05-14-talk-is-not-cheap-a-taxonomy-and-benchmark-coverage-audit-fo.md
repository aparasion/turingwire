---
title: "Talk is (Not) Cheap: A Taxonomy and Benchmark Coverage Audit for LLM Attacks"
date: 2026-05-14 17:30:36 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.15118v1"
arxiv_id: "2605.15118"
authors: ["Karthik Raghu Iyer", "Yazdan Jamshidi", "Nicholas Bray", "Alexey A. Shvets"]
slug: talk-is-not-cheap-a-taxonomy-and-benchmark-coverage-audit-fo
summary_word_count: 450
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inadequacy of existing benchmarks for evaluating the security of large language models (LLMs) against inference-time attacks. The authors identify a significant gap in the collective coverage of the threat surface by current benchmarks, which is critical for understanding the vulnerabilities of LLMs. The work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors propose a comprehensive framework for auditing LLM attack benchmarks, structured as a 4×6 matrix that categorizes attacks based on the STRIDE threat model (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege). This matrix is derived from a detailed 507-leaf taxonomy of inference-time attacks, which includes 401 data-populated leaves and 106 threat-model-derived leaves, compiled from 932 security studies published between 2023 and 2026. The framework allows for benchmark-external validation, focusing on collective coverage rather than individual benchmark performance. The authors apply this framework to six public benchmarks, including HarmBench, InjecAgent, and AgentDojo, revealing that these frameworks cover at most 25% of the matrix, with significant gaps in evaluating entire STRIDE categories such as Service Disruption and Model Internals.

**Results**  
The analysis shows that the three primary frameworks occupy non-overlapping cells within the matrix, indicating a lack of comprehensive coverage. Notably, attacks in the uncovered categories have demonstrated high efficacy, achieving up to 46× token amplification and 96% success rates, yet remain untested by existing benchmarks. The study also identifies a corpus of 2,521 unique attack groups, highlighting pervasive naming fragmentation, with some attacks having up to 29 different surface forms. The concentration of attacks in the Safety & Alignment Bypass category is particularly pronounced, revealing structural properties that are not visible when examining smaller scales.

**Limitations**  
The authors acknowledge that their framework is limited by the current state of benchmarks and the evolving nature of LLM attacks. They do not address potential biases in the selection of studies or the completeness of the taxonomy. Additionally, the framework's effectiveness in guiding future benchmark development remains to be validated in practice. The reliance on existing literature may also overlook emerging attack vectors that have not yet been documented.

**Why it matters**  
This work has significant implications for the field of AI security, as it provides a structured approach to identifying and addressing gaps in benchmark coverage for LLMs. By releasing the taxonomy, attack records, and coverage mappings as extensible artifacts, the authors enable the community to systematically track the evolution of benchmark evaluations. This framework can guide future research and development of more robust benchmarks, ultimately enhancing the security posture of LLMs against a broader range of inference-time attacks.

Authors: Karthik Raghu Iyer, Yazdan Jamshidi, Nicholas Bray, Alexey A. Shvets  
Source: arXiv:2605.15118  
URL: https://arxiv.org/abs/2605.15118v1
