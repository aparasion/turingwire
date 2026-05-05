---
title: "ContextualJailbreak: Evolutionary Red-Teaming via Simulated Conversational Priming"
date: 2026-05-04 14:32:40 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.02647v1"
arxiv_id: "2605.02647"
authors: ["Mario Rodr\u00edguez B\u00e9jar", "Francisco J. Cort\u00e9s-Delgado", "S. Braghin", "Jose L. Hern\u00e1ndez-Ramos"]
slug: contextualjailbreak-evolutionary-red-teaming-via-simulated-c
summary_word_count: 417
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the vulnerability of large language models (LLMs) to jailbreak attacks that exploit safety misalignments, specifically through contextual priming in multi-turn dialogues. While prior research has demonstrated the efficacy of hand-crafted multi-turn prompts, automated optimization methods have predominantly focused on single-turn interactions. The authors identify a gap in the exploration of mutator designs that can effectively generate primed dialogues, which is crucial for enhancing red-teaming strategies. This work is presented as a preprint and has not undergone peer review.

**Method**  
The authors introduce ContextualJailbreak, a black-box red-teaming framework that employs evolutionary search techniques over simulated multi-turn dialogues. The method utilizes a graded harm score (0-5) from a two-level judge to provide feedback during the search process, allowing for the inclusion of partially harmful responses rather than discarding them outright. The search is driven by five semantically defined mutation operators: roleplay, scenario, expand, troubleshooting, and mechanistic. The last two operators are novel contributions of this work, enhancing the mutator design space for effective dialogue priming. The framework is evaluated across 50 behaviors from the HarmBench benchmark.

**Results**  
ContextualJailbreak achieves an attack success rate (ASR) of 100% on gpt-oss:20B, qwen3-8B, and llama3.1:70B, and 90% on gpt-oss:120B. This performance significantly surpasses four baseline methods—both single-turn and multi-turn—by an average margin of 31-96 percentage points. Furthermore, the 40 most harmful attacks identified against gpt-oss:120B demonstrate high transferability to other models, achieving 90.0% ASR on gpt-4o-mini, 70.0% on gpt-5, and 70.0% on gemini-3-flash. However, the attacks show reduced effectiveness on claude-opus-4-7 (17.5%) and claude-sonnet-4-6 (15.0%), indicating a notable asymmetry in alignment robustness across different model providers.

**Limitations**  
The authors acknowledge that the effectiveness of ContextualJailbreak may vary with different model architectures and that the reliance on a two-level judge for harm scoring could introduce subjectivity. Additionally, the framework's performance on models not included in the evaluation remains untested. The authors do not discuss potential ethical implications of deploying such red-teaming strategies or the risks of misuse.

**Why it matters**  
The findings from this research have significant implications for the development of more robust safety mechanisms in LLMs. By demonstrating the effectiveness of evolutionary search in generating harmful prompts through contextual priming, this work highlights the need for improved alignment strategies in AI systems. The pronounced provider-level asymmetry in alignment robustness also suggests that model developers must consider the varying vulnerabilities across different architectures, prompting further investigation into the underlying causes of these discrepancies.

Authors: Mario Rodríguez Béjar, Francisco J. Cortés-Delgado, S. Braghin, Jose L. Hernández-Ramos  
Source: arXiv:2605.02647  
URL: [https://arxiv.org/abs/2605.02647v1](https://arxiv.org/abs/2605.02647v1)
