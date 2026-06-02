---
title: "Not What, But How: A Communicative Audit of LLM Response Framing"
date: 2026-06-01 17:01:31 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.02493v1"
arxiv_id: "2606.02493"
authors: ["Siddhesh Milind Pawar", "Sarah Masud", "Haneul Yoo", "Alice Oh", "Isabelle Augenstein"]
slug: not-what-but-how-a-communicative-audit-of-llm-response-frami
summary_word_count: 418
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper introduces FRANZ, a framework for auditing LLM response framing, highlighting the importance of communicative characteristics in subjective queries."
---

**Problem**  
Existing evaluations of large language models (LLMs) primarily focus on factual correctness, neglecting the significance of response framing in subjective, information-seeking contexts. This gap is particularly relevant as users are increasingly sensitive to how information is communicated, not just its accuracy. The authors address this oversight by proposing a new framework for assessing LLM responses, emphasizing the need for a more nuanced evaluation of communication styles in LLM outputs. This work is presented as a preprint and has not undergone peer review.

**Method**  
The authors introduce FRANZ, an automated framework designed for the communicative audit of LLM responses across four dimensions: cultural positioning, use of generalizing language, anthropomorphic cues, and adherence to conversational maxims. To facilitate this evaluation, they contribute SQUARE, a novel corpus comprising 376,000 subjective questions sourced from 57 subreddits, categorized into 19 question types and mapped to 7 countries. The framework was applied to analyze responses from three open-weight LLMs, allowing for a comparative assessment of how different models frame their answers.

**Results**  
The application of FRANZ revealed statistically significant differences in the frequency of response characteristics among the evaluated LLMs. For instance, the analysis indicated that insider positioning and anthropomorphism are positively correlated, with the strength of this relationship varying by country. The authors provide specific metrics demonstrating that certain models exhibit a higher tendency to employ anthropomorphic language, which may influence user perception and trust. The results underscore the importance of response framing, suggesting that LLMs can significantly differ in their communicative styles, which may affect user engagement and satisfaction.

**Limitations**  
The authors acknowledge several limitations, including the potential biases inherent in the SQUARE corpus, which is derived from social media platforms and may not represent a comprehensive range of subjective queries. Additionally, the framework's reliance on automated scoring may overlook nuanced human interpretations of communication styles. The study also does not explore the implications of these findings on user behavior or the effectiveness of LLMs in practical applications, which could be a valuable area for future research.

**Why it matters**  
This work highlights the critical role of response framing in LLM interactions, suggesting that evaluations should extend beyond factual correctness to include communicative effectiveness. The introduction of FRANZ and the SQUARE corpus provides a valuable tool for researchers and practitioners aiming to enhance LLM performance in subjective contexts. By revealing the intricacies of how LLMs communicate, this research paves the way for more user-centered AI systems that can better align with human expectations and cultural sensitivities, as published in [arXiv cs.CL](https://arxiv.org/abs/2606.02493v1).
