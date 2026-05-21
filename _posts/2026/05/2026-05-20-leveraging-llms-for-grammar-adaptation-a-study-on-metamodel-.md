---
title: "Leveraging LLMs for Grammar Adaptation: A Study on Metamodel-Grammar Co-Evolution"
date: 2026-05-20 17:51:51 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21465v1"
arxiv_id: "2605.21465"
authors: ["Weixing Zhang", "Bowen Jiang", "Rahul Sharma", "Regina Hebig", "Daniel Str\u00fcber"]
slug: leveraging-llms-for-grammar-adaptation-a-study-on-metamodel-
summary_word_count: 448
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in automating grammar adaptation in model-driven engineering, specifically in the context of metamodel evolution. Traditional rule-based methods provide only partial automation and struggle with complex grammar scenarios, necessitating significant manual intervention. The authors propose a Large Language Model (LLM)-based approach to automate grammar adaptations, leveraging learned adaptations from previous grammar versions. This work is presented as a preprint and has not undergone peer review.

**Method**  
The proposed method utilizes three LLMs: Claude Sonnet 4.5, ChatGPT 5.1, and Gemini 3, to automate grammar adaptations for domain-specific languages (DSLs). The authors developed prompting strategies using four DSLs as a training set and validated the approach on two additional DSLs. The evaluation metrics included grammar rule-level adaptation consistency, output similarity, and metamodel conformance. The training process involved longitudinal case studies, particularly focusing on QVTo, to assess the LLMs' ability to reuse learned adaptations across multiple evolution steps without manual intervention. The architecture leverages the inherent capabilities of LLMs to understand and generate grammar rules, although specific training compute details are not disclosed.

**Results**  
The results indicate that all three LLMs achieved 100% adaptation consistency and output similarity on the test set, significantly outperforming the rule-based approach, which achieved only 84.21% on DOT and 62.50% on Xcore. In the longitudinal study of QVTo, the LLM-based method successfully reused adaptations across all three evolution steps without requiring manual grammar edits, while the rule-based method necessitated manual adjustments in two out of three transitions. However, for large-scale grammars, such as EAST-ADL with 297 rules, the adaptation consistency of LLMs fell below 90%, highlighting a performance drop in more complex scenarios.

**Limitations**  
The authors acknowledge that while the LLM-based approach excels in smaller and less complex grammar scenarios, it struggles with large-scale grammars, indicating a limitation in scalability. They do not address potential issues related to the interpretability of LLM-generated adaptations or the computational costs associated with using LLMs for grammar adaptation tasks. Additionally, the reliance on specific LLMs may limit generalizability across different DSLs or grammar types.

**Why it matters**  
This study demonstrates the potential of LLMs to significantly enhance automation in grammar adaptation processes, reducing the manual workload associated with metamodel evolution. The findings suggest that LLMs can effectively handle complex grammar scenarios, which could lead to more efficient development workflows in model-driven engineering. However, the limitations identified in large-scale grammar adaptation indicate that further research is needed to improve the robustness and scalability of LLM-based approaches. This work opens avenues for future exploration into hybrid models that combine LLM capabilities with rule-based methods to achieve better performance across varying grammar complexities.

Authors: Weixing Zhang, Bowen Jiang, Rahul Sharma, Regina Hebig, Daniel Strüber  
Source: arXiv:2605.21465  
URL: [https://arxiv.org/abs/2605.21465v1](https://arxiv.org/abs/2605.21465v1)
