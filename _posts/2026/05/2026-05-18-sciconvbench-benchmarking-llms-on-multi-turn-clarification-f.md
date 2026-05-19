---
title: "SCICONVBENCH: Benchmarking LLMs on Multi-Turn Clarification for Task Formulation in Computational Science"
date: 2026-05-18 16:34:45 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.18630v1"
arxiv_id: "2605.18630"
authors: ["Nithin Somasekharan", "Youssef Hassan", "Shiyao Lin", "Gihan Panapitiya", "Patrick Emami", "Anurag Acharya"]
slug: sciconvbench-benchmarking-llms-on-multi-turn-clarification-f
summary_word_count: 462
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of Large Language Models (LLMs) as scientific AI assistants, specifically focusing on the multi-turn clarification process necessary for task formulation in computational science. Existing benchmarks primarily assess LLM capabilities under the assumption that user requests are well-posed, neglecting the reality that scientific inquiries often begin as ill-structured problems requiring iterative dialogue for clarification. The authors introduce SCICONVBENCH, a novel benchmark designed to systematically evaluate LLM performance in this context. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
SCICONVBENCH targets two key capabilities: disambiguation (eliciting missing information) and inconsistency resolution (detecting and correcting contradictory requests). The benchmark encompasses four domains of computational science: fluid mechanics, solid mechanics, materials science, and partial differential equations (PDEs). It employs a structured task ontology paired with a rubric-based evaluation framework, allowing for the measurement of LLM performance across three dimensions: clarification behavior, conversational grounding, and final-specification fidelity. The authors utilize a dataset that includes multi-turn dialogues, although specific details regarding the size of the dataset, training compute, or model architectures used for evaluation are not disclosed.

**Results**  
The evaluation reveals that current frontier LLMs exhibit relatively strong performance in inconsistency resolution, achieving a resolution rate of 52.7% in fluid mechanics disambiguation cases. However, this indicates a substantial limitation, as over 47% of disambiguation cases remain unresolved. The authors also note that LLMs often make silent assumptions and perform implicit repairs that lack grounding in the conversational context, which could lead to inaccuracies in task formulation. These findings highlight the need for improved conversational reasoning capabilities in LLMs to function effectively as scientific assistants.

**Limitations**  
The authors acknowledge that while SCICONVBENCH provides a structured approach to evaluating multi-turn clarification, it may not encompass all possible scientific domains or the full complexity of real-world scientific inquiries. Additionally, the reliance on a rubric-based evaluation may introduce subjectivity in assessing clarification behavior and conversational grounding. The lack of detailed information regarding the dataset size and model architectures limits reproducibility and generalizability of the results. Furthermore, the benchmark does not address the potential impact of user variability in dialogue quality on LLM performance.

**Why it matters**  
SCICONVBENCH establishes a foundational framework for assessing the upstream conversational reasoning required for reliable computational science assistance. By highlighting the limitations of current LLMs in handling ill-posed scientific inquiries, this work paves the way for future research aimed at enhancing LLM capabilities in multi-turn dialogue scenarios. The implications extend to the development of more robust AI systems that can effectively assist researchers in formulating and refining scientific tasks, ultimately improving the efficiency and accuracy of computational science workflows.

Authors: Nithin Somasekharan, Youssef Hassan, Shiyao Lin, Gihan Panapitiya, Patrick Emami, Anurag Acharya, Sameera Horawalavithana, Shaowu Pan  
Source: arXiv:2605.18630  
URL: https://arxiv.org/abs/2605.18630v1
