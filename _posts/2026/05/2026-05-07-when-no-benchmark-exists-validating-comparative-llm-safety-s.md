---
title: "When No Benchmark Exists: Validating Comparative LLM Safety Scoring Without Ground-Truth Labels"
date: 2026-05-07 17:56:41 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06652v1"
arxiv_id: "2605.06652"
authors: ["Sushant Gautam", "Finn Schwall", "Annika Willoch Olstad", "Fernando Vallecillos Ruiz", "Birk Torpmann-Hagen", "Sunniva Maria Stordal Bj\u00f8rklund"]
slug: when-no-benchmark-exists-validating-comparative-llm-safety-s
summary_word_count: 488
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of evaluating the safety of language models (LMs) in scenarios where no labeled benchmark exists, particularly in specific languages, sectors, or regulatory contexts. The authors formalize this issue as "benchmarkless comparative safety scoring," which is crucial for deployments that require safety assessments without established ground-truth labels. This work is presented as a preprint and has not undergone peer review.

**Method**  
The authors propose a framework for validating safety scores through a scenario-based audit process, which relies on an "instrumental-validity chain." This chain includes three key components: (1) responsiveness to a controlled safe-versus-abliterated contrast, (2) dominance of target-driven variance over auditor and judge artifacts, and (3) stability across multiple reruns. The framework is instantiated in a tool called SimpleAudit, which operates locally and is validated using a Norwegian safety pack. The authors report that the separation between safe and abliterated targets yields area under the receiver operating characteristic (AUROC) values ranging from 0.89 to 1.00. They also quantify the variance attributable to target identity, with an effect size of $η^2 \approx 0.52$, indicating that target identity is the primary source of variance in the scoring process. The methodology emphasizes the importance of reporting various metrics, including scores, matched deltas, critical rates, and the specific auditor and judge used, rather than condensing results into a single ranking.

**Results**  
The validation of SimpleAudit on the Norwegian safety pack demonstrates strong performance, with AUROC values between 0.89 and 1.00 for distinguishing safe from abliterated targets. The analysis shows that target identity accounts for approximately 52% of the variance in scores, indicating a robust differentiation capability. In a practical application involving a Norwegian public-sector procurement case comparing two models, Borealis and Gemma 3, the results reveal that the perceived safety of the models is contingent on the scenario category and the risk measure employed. This highlights the necessity of context in safety evaluations.

**Limitations**  
The authors acknowledge that the validity of the scoring is contingent upon the fixed parameters of the scenario pack, rubric, auditor, judge, sampling configuration, and rerun budget. They do not address potential biases introduced by the selection of scenarios or the subjective nature of the auditing process. Additionally, the framework's reliance on a specific context may limit its generalizability to other languages or sectors without further adaptation.

**Why it matters**  
This work has significant implications for the deployment of LMs in safety-critical applications, particularly in environments lacking established benchmarks. By providing a structured approach to comparative safety scoring, it enables practitioners to make informed decisions about model selection based on safety metrics. The emphasis on reporting a comprehensive set of evaluation metrics rather than a single score encourages transparency and accountability in model assessments, which is essential for regulatory compliance and public trust in AI systems.

Authors: Sushant Gautam, Finn Schwall, Annika Willoch Olstad, Fernando Vallecillos Ruiz, Birk Torpmann-Hagen, Sunniva Maria Stordal Bjørklund, Leon Moonen, Klas Pettersen et al.  
Source: arXiv:2605.06652  
URL: https://arxiv.org/abs/2605.06652v1
