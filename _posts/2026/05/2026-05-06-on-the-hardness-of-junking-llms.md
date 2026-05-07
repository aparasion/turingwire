---
title: "On the Hardness of Junking LLMs"
date: 2026-05-06 16:47:07 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.05116v1"
arxiv_id: "2605.05116"
authors: ["Marco Rando", "Samuel Vaiter"]
slug: on-the-hardness-of-junking-llms
summary_word_count: 421
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the understanding of vulnerabilities in large language models (LLMs), specifically focusing on the existence and discoverability of natural backdoors—token sequences that can elicit harmful outputs without explicit adversarial prompts. While prior research has concentrated on structured prompt-based jailbreak attacks, the authors highlight that the hardness of identifying these natural backdoors has not been systematically evaluated, leaving a critical area of LLM security unexplored.

**Method**  
The authors formalize the "junking problem" as the task of identifying token sequences that maximize the probability of generating harmful responses. They propose a greedy random-search algorithm to explore the space of potential token sequences. The method involves generating sequences and evaluating their effectiveness in triggering harmful outputs, contrasting this approach with traditional prompt-based methods. The study does not disclose specific training compute or dataset details, focusing instead on the algorithmic approach and its implications for LLM vulnerabilities.

**Results**  
The findings indicate that the junking problem is more challenging than conventional jailbreak attacks, underscoring the necessity of semantic structure in prompt design. However, the authors report that their random-search strategy achieves a high success rate in discovering these natural backdoors, suggesting that they are not only present but also relatively easy to recover. The perplexity analysis reveals that the identified token sequences reside in low-probability regions of the model's output distribution, reinforcing the notion that these sequences may have emerged during the training phase of the LLM.

**Limitations**  
The authors acknowledge that their study is a preliminary exploration and does not exhaustively characterize the landscape of natural backdoors. They do not address the potential for adversarial training or other mitigation strategies that could be employed to counteract these vulnerabilities. Additionally, the reliance on a greedy random-search method may not capture the full complexity of the token space, potentially overlooking more effective sequences. The generalizability of their findings across different LLM architectures and training regimes remains untested.

**Why it matters**  
This work has significant implications for the security and robustness of LLMs, particularly in applications where safety is paramount. By demonstrating that harmful behaviors can be elicited through natural backdoors, the study raises critical questions about the inherent risks associated with LLM deployment. The findings suggest that future research should focus on developing more robust defenses against both structured and unstructured attack vectors, as well as exploring the underlying mechanisms that give rise to these vulnerabilities. This could lead to improved model training methodologies and enhanced safety protocols in LLM applications.

Authors: Marco Rando, Samuel Vaiter  
Source: arXiv:2605.05116  
URL: https://arxiv.org/abs/2605.05116v1
