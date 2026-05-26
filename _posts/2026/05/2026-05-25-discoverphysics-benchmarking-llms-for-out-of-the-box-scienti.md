---
title: "DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Thinking"
date: 2026-05-25 17:50:07 +0000
category: research
subcategory: evaluation_benchmarks
company: "ServiceNow"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.26087v1"
arxiv_id: "2605.26087"
authors: ["Matt L. Wiemann", "Lindsay M. Smith", "Peter Melchior", "Siddharth Mishra-Sharma", "Andrew Gordon Wilson", "Pavel Izmailov"]
slug: discoverphysics-benchmarking-llms-for-out-of-the-box-scienti
summary_word_count: 466
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in evaluating the scientific reasoning capabilities of large language models (LLMs) in the context of physics. While frontier LLMs have demonstrated strong performance across various physics tasks, distinguishing genuine reasoning from mere recall of established scientific knowledge remains challenging. The authors introduce DiscoverPhysics, an interactive benchmark designed to assess LLMs' ability to discover and articulate the laws of motion in simulated worlds with non-standard physics. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
DiscoverPhysics comprises 22 unique simulated worlds, each governed by unconventional physical laws, such as screened and fractional-power gravity, multi-species interactions, and time-varying forces. The benchmark requires LLM agents to engage in a multi-step experimental process: proposing experiments, observing trajectory data from an N-body simulator, and ultimately providing a natural-language explanation along with a Python implementation of the inferred physical law. The evaluation metrics include trajectory mean squared error (MSE) on held-out particles and an LLM-judged explanation score based on a rubric assessing conceptual understanding. The benchmark emphasizes long-horizon reasoning and hypothesis refinement through iterative experimentation.

**Results**  
The evaluation of eleven frontier LLMs reveals that the most capable models only succeed in passing approximately 50% of the worlds. Notably, these models struggle particularly with tasks requiring the uncovering of latent structures within the data. Open-source models exhibit significantly lower performance compared to commercial counterparts, both in designing informative experiments and in deriving conclusions from the experimental data. The study also highlights a disconnect between predictive accuracy and explanation quality, indicating that high accuracy does not necessarily correlate with a robust conceptual understanding of the underlying physics.

**Limitations**  
The authors acknowledge several limitations, including the reliance on a specific set of simulated worlds that may not encompass the full diversity of physical phenomena. Additionally, the benchmark's focus on LLMs may overlook other AI paradigms that could potentially excel in scientific reasoning. The evaluation criteria, while comprehensive, may still be subjective, particularly the LLM-judged explanation scores. Furthermore, the paper does not explore the scalability of the benchmark or its applicability to other scientific domains beyond physics.

**Why it matters**  
DiscoverPhysics has significant implications for the development of LLMs in scientific contexts. By providing a structured framework for evaluating reasoning capabilities, it encourages the design of models that can engage in genuine scientific inquiry rather than rote memorization. The findings underscore the necessity for LLMs to refine hypotheses through experimental design, which could inform future research on improving model architectures and training methodologies. This benchmark could serve as a foundation for further exploration into the intersection of AI and scientific discovery, potentially leading to advancements in automated scientific reasoning and hypothesis generation.

Authors: Matt L. Wiemann, Lindsay M. Smith, Peter Melchior, Siddharth Mishra-Sharma, Andrew Gordon Wilson, Pavel Izmailov, Carolina Cuesta-Lázaro  
Source: arXiv:2605.26087  
URL: https://arxiv.org/abs/2605.26087v1
