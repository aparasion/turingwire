---
title: "Proposal and study of statistical features for string similarity computation and classification"
date: 2026-05-14 17:27:04 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.15110v1"
arxiv_id: "2605.15110"
authors: ["E. O. Rodrigues", "D. Casanova", "M. Teixeira", "V. Pegorini", "F. Favarim", "E. Clua"]
slug: proposal-and-study-of-statistical-features-for-string-simila
summary_word_count: 421
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in string similarity computation and classification, particularly focusing on the limitations of existing statistical measures such as longest common subsequence, mutual information, and edit distances. The authors propose adaptations of features from visual computing—specifically, co-occurrence matrix (COM) and run-length matrix (RLM)—to enhance string similarity assessments across diverse languages and contexts, which are often sensitive to linguistic structures.

**Method**  
The core technical contribution involves the introduction of COM and RLM features for string similarity computation. The COM captures the frequency of co-occurring characters in a string, while the RLM focuses on the lengths of consecutive character runs. These features are designed to be language-agnostic and purely statistical, making them applicable to various types of strings, including words, phrases, and code. The authors conducted synthetic experiments to evaluate the performance of these features against traditional statistical measures. The training compute specifics are not disclosed, but the experiments include a comparative analysis of the proposed features against established methods, with a focus on statistical significance (P-value < 0.001) in performance metrics.

**Results**  
In the synthetic experiments, the COM and RLM features demonstrated superior performance, outperforming traditional statistical measures in 3 out of 4 cases. The authors report that the RLM features achieved the best results on a real text plagiarism dataset, indicating a significant improvement over the second-best group based on distance metrics. The exact performance metrics (e.g., accuracy, F1 score) are not detailed in the summary, but the statistical significance of the results suggests a robust advantage of the proposed features.

**Limitations**  
The authors acknowledge that their study is limited to the evaluation of COM and RLM features against a specific set of traditional measures and datasets. They do not address potential scalability issues or the computational efficiency of their methods in large-scale applications. Additionally, the generalizability of the results across different domains or types of strings beyond those tested remains unexamined.

**Why it matters**  
The implications of this work are significant for downstream applications in natural language processing, information retrieval, and plagiarism detection. By providing a set of features that are not sensitive to linguistic variations, the proposed methods could enhance the robustness and applicability of string similarity computations across diverse languages and contexts. This could lead to improved performance in various tasks, such as text classification, semantic similarity assessments, and automated code analysis, thereby broadening the scope of statistical methods in string processing.

Authors: E. O. Rodrigues, D. Casanova, M. Teixeira, V. Pegorini, F. Favarim, E. Clua, A. Conci, Panos Liatsis  
Source: arXiv:2605.15110  
URL: [https://arxiv.org/abs/2605.15110v1](https://arxiv.org/abs/2605.15110v1)
