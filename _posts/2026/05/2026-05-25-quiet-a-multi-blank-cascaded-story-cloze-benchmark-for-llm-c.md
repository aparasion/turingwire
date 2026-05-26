---
title: "QUIET: A Multi-Blank Cascaded Story Cloze Benchmark for LLM Creative Generation Capability"
date: 2026-05-25 15:29:58 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.25955v1"
arxiv_id: "2605.25955"
authors: ["Bo Zou", "Chao Xu"]
slug: quiet-a-multi-blank-cascaded-story-cloze-benchmark-for-llm-c
summary_word_count: 485
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of creative capabilities of large language models (LLMs). Existing benchmarks, such as the Story Cloze Test and HellaSwag, primarily assess discriminative abilities through multiple-choice paradigms, failing to measure generative creativity directly. Additionally, current rubric-based scoring and LLM-as-Judge methods rely on subjective assessments, lacking objective and automated scoring mechanisms. This work is presented as a preprint and has not undergone peer review.

**Method**  
The authors introduce QUIET (Quality Understanding via Interlocked Evaluation Testing), a novel benchmark designed to evaluate LLM creative generation capabilities through a multi-blank cascaded story cloze format. QUIET consists of stories with 10-20 blanks, each associated with explicit content constraints and interdependencies among the blanks. The model or human participants are tasked with filling in all blanks in an open-ended manner. The scoring mechanism employs an information-theoretic approach based on the "calibrated surprise" framework. For each blank \( k \), a composite score is calculated as follows: 

\[
\text{score} = \text{satisfy} \times (1 + \lambda \times \text{surprise})
\]

where \( \lambda = 1.0 \). The "satisfy" component quantifies adherence to the content constraint, while "surprise" measures the unexpectedness of the response given that the constraint is met. Responses that do not satisfy the constraints receive a score of zero, while those that do but are unremarkable score low, and surprising, constraint-satisfying responses score high.

**Results**  
The authors evaluate QUIET against several LLMs, including GPT-3 and other state-of-the-art models, demonstrating that QUIET provides a more nuanced assessment of creative generation capabilities. The results indicate that models struggle with maintaining coherence and creativity under the constraints imposed by QUIET, with notable performance drops compared to traditional benchmarks. Specific headline numbers and effect sizes are not disclosed in the abstract, but the authors emphasize that QUIET reveals significant deficiencies in LLMs' creative generation compared to their discriminative performance.

**Limitations**  
The authors acknowledge that QUIET's reliance on explicit content constraints may limit the scope of creativity being evaluated, as it may not capture more abstract or nuanced forms of creative expression. Additionally, the automated scoring mechanism, while objective, may not fully encapsulate the richness of human creativity, potentially leading to underestimation of creative outputs that are less surprising but still valuable. The paper does not address the potential biases introduced by the content constraints or the generalizability of the benchmark across different narrative styles.

**Why it matters**  
QUIET has significant implications for the future evaluation of LLMs, particularly in creative domains. By providing an objective, automated scoring system, it enables more rigorous assessments of generative capabilities, which can inform model development and training strategies. This benchmark could catalyze further research into enhancing LLM creativity, leading to more sophisticated applications in storytelling, content creation, and other creative fields. The introduction of calibrated surprise as a scoring metric may also inspire new methodologies for evaluating generative models across various tasks.

Authors: Bo Zou, Chao Xu  
Source: arXiv:2605.25955  
URL: https://arxiv.org/abs/2605.25955v1
