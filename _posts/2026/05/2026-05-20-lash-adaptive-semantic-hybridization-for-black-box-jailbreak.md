---
title: "LASH: Adaptive Semantic Hybridization for Black-Box Jailbreaking of Large Language Models"
date: 2026-05-20 16:27:00 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21362v1"
arxiv_id: "2605.21362"
authors: ["Abdullah Al Nomaan Nafi", "Fnu Suya", "Swarup Bhunia", "Prabuddha Chakraborty"]
slug: lash-adaptive-semantic-hybridization-for-black-box-jailbreak
summary_word_count: 433
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the persistent vulnerability of large language models (LLMs) to jailbreak attacks, which exploit the gap between their intended safety behaviors and their responses to adversarial prompts. Existing automated jailbreak methods are limited by their commitment to specific attack families, such as refinement loops or mutation spaces, and no single method consistently outperforms others across different models and harm categories. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose LASH (LLM Adaptive Semantic Hybridization), a black-box framework that leverages outputs from multiple base attack strategies as reusable seed prompts. LASH employs a two-stage process: first, it searches over subsets of seed prompts and optimizes softmax-normalized mixture weights. A composition module synthesizes a single candidate prompt from these seeds. The optimization of weights is performed using a derivative-free genetic algorithm that relies on black-box feedback from the target model. The fitness function combines keyword-based refusal detection with LLM-judge scoring to evaluate the effectiveness of the generated prompts. The framework is evaluated on JailbreakBench, which consists of 100 harmful prompts categorized into 10 distinct types.

**Results**  
LASH achieves an average attack success rate of 84.5% under keyword-based evaluation and 74.5% under the two-stage evaluation, which includes a filtering step for refusals followed by scoring by an LLM judge. These results are benchmarked against five state-of-the-art baselines, demonstrating superior performance with only 30 mean target queries. Additionally, LASH maintains competitive performance against three different defense mechanisms and generates internal representations that are more aligned with successful attack outcomes.

**Limitations**  
The authors acknowledge that LASH's performance may vary depending on the specific characteristics of the target model and the nature of the harmful prompts. They do not address potential ethical implications of deploying such a framework or the risks associated with its misuse. Furthermore, the reliance on black-box feedback may limit the interpretability of the optimization process, and the effectiveness of the method in real-world scenarios remains untested.

**Why it matters**  
The development of LASH signifies a notable advancement in the field of adversarial robustness for LLMs, particularly in the context of black-box red-teaming. By enabling adaptive composition of diverse jailbreak strategies, this work opens avenues for more effective testing of model safety and robustness. The implications extend to improving the design of LLMs with enhanced safety features and informing future research on adversarial attacks and defenses. The findings suggest that hybridization of attack strategies could be a fruitful area for further exploration in the ongoing battle against adversarial prompting.

Authors: Abdullah Al Nomaan Nafi, Fnu Suya, Swarup Bhunia, Prabuddha Chakraborty  
Source: arXiv:2605.21362  
URL: https://arxiv.org/abs/2605.21362v1
