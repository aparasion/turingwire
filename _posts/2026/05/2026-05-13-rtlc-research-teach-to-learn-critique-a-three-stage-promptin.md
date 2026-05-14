---
title: "RTLC -- Research, Teach-to-Learn, Critique: A three-stage prompting paradigm inspired by the Feynman Learning Technique that lifts LLM-as-judge accuracy on JudgeBench with no fine-tuning"
date: 2026-05-13 15:48:16 +0000
category: research
subcategory: evaluation_benchmarks
company: "ServiceNow"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13695v1"
arxiv_id: "2605.13695"
authors: ["Andrea Morandi"]
slug: rtlc-research-teach-to-learn-critique-a-three-stage-promptin
summary_word_count: 426
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the inadequacy of existing LLM-as-judge systems in achieving reliable accuracy on the JudgeBench benchmark, where even well-tuned models perform marginally better than random chance on objective-correctness pairwise items. The authors identify a gap in the literature regarding effective prompting strategies that can enhance the performance of LLMs without requiring fine-tuning, retrieval, or external tools.

**Method**  
The core technical contribution is the RTLC (Research, Teach-to-Learn, Critique) prompting paradigm, which consists of three distinct stages. In Stage 1, the input is framed within a pedagogical scaffold inspired by the Feynman Learning Technique, which involves studying the material, teaching it, identifying gaps, and simplifying the content. Stage 2 generates N=10 independent candidate verdicts using a temperature setting of 0.4 to introduce variability. In Stage 3, the model critiques these candidates by cross-comparing them against the original question, ultimately producing a single, refined verdict at temperature 0. The authors conduct a clean three-step ablation study to quantify the contributions of each stage to the overall performance improvement.

**Results**  
On the JudgeBench-GPT benchmark, which consists of 350 hard pairwise items, the Claude 3.7 Sonnet model's accuracy improves from 64.6% with a single-shot vanilla prompt to 78.6% using the RTLC critique-of-10 approach, representing a significant absolute gain of 14.0 percentage points. This performance surpasses that of N=10 self-consistency majority voting (77.7%) and a zero-shot first candidate (74.0%). The ablation study reveals that the Teach-to-Learn scaffold contributes +9.4 percentage points, N=10 marginalization adds +3.7 percentage points, and explicit critique provides an additional +0.9 percentage points. The authors also discuss the cost-accuracy frontier, indicating that RTLC consistently outperforms self-consistency across various operational points.

**Limitations**  
The authors acknowledge that the RTLC method is contingent on the quality of the underlying LLM and may not generalize across all models or tasks. They do not address potential limitations related to the scalability of the approach or the computational cost associated with generating multiple candidate verdicts. Additionally, the reliance on a specific pedagogical framework may limit the applicability of RTLC to other domains or types of tasks.

**Why it matters**  
The implications of this work are significant for the development of more reliable LLMs in open-ended generation tasks. By demonstrating that a structured prompting approach can enhance LLM performance without fine-tuning, this research opens avenues for further exploration of pedagogical techniques in AI. The findings suggest that RTLC could be integrated with other interventions, such as post-hoc judge-score calibration, to achieve compounded improvements in model accuracy, thereby advancing the state of the art in LLM evaluation methodologies.

Authors: Andrea Morandi  
Source: arXiv:2605.13695  
URL: [https://arxiv.org/abs/2605.13695v1](https://arxiv.org/abs/2605.13695v1)
