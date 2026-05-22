---
title: "Tokenization with Split Trees"
date: 2026-05-21 16:46:23 +0000
category: research
subcategory: efficiency_inference
company: "UiPath"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.22705v1"
arxiv_id: "2605.22705"
authors: ["Craig W. Schmidt", "Michael Krumdick", "Adam Wiemerslage", "Seth Ebner", "Varshini Reddy", "Yuval Pinter"]
slug: tokenization-with-split-trees
summary_word_count: 457
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing subword tokenization methods, specifically focusing on the inefficiencies in token count and vocabulary selection. Current methods like Byte Pair Encoding (BPE), WordPiece, and Unigram Language Model (UnigramLM) do not optimize for compression effectively, leading to suboptimal tokenization and increased inference token counts. The authors propose a novel approach, Tokenization with Split Trees (ToaST), which is presented as a preprint and has not yet undergone peer review.

**Method**  
ToaST introduces a recursive inference procedure that constructs a full binary tree for each pretoken, utilizing precomputed byte n-gram counts. This method operates independently of any predefined vocabulary. The inference process involves recursively traversing the split tree to emit the first in-vocabulary node encountered along each path. The vocabulary selection is framed as an Integer Programming (IP) problem aimed at minimizing the total token count across all split trees. The authors note that the Linear Programming (LP) relaxation of this problem is near-integral in practice, allowing for the derivation of near-optimal vocabularies. The training time for ToaST scales quadratically with the number of split trees, which is a critical consideration for implementation.

**Results**  
ToaST demonstrates a significant reduction in token counts, achieving over an 11% decrease compared to BPE, WordPiece, and UnigramLM at vocabulary sizes of 40,960 and above. This reduction translates to fewer inference tokens for models utilizing ToaST, effectively extending the context length. In experiments involving the training of 1.5 billion parameter language models, ToaST achieved the highest CORE score, outperforming the baselines by 2.6% to 7.6%, with statistical significance for two out of three comparisons. Additionally, ToaST excelled in 13 out of 22 individual tasks, indicating its robustness across various benchmarks.

**Limitations**  
The authors acknowledge that the quadratic scaling of training time with respect to the number of split trees may pose challenges for very large datasets or models. They do not discuss potential limitations related to the generalizability of ToaST across languages with different morphological structures or the computational overhead associated with the initial precomputation of byte n-gram counts. Furthermore, the reliance on a specific vocabulary size may limit flexibility in certain applications.

**Why it matters**  
The implications of ToaST are significant for downstream applications in natural language processing (NLP), particularly in enhancing the efficiency of language models. By reducing token counts and improving Renyi efficiency, ToaST can lead to more effective use of context in language generation tasks, potentially improving performance in applications such as machine translation, text summarization, and conversational agents. The method's ability to derive near-optimal vocabularies also opens avenues for further research into adaptive tokenization strategies that can dynamically adjust to varying input characteristics.

Authors: Craig W. Schmidt, Michael Krumdick, Adam Wiemerslage, Seth Ebner, Varshini Reddy, Yuval Pinter, Chris Tanner  
Source: arXiv:2605.22705  
URL: [https://arxiv.org/abs/2605.22705v1](https://arxiv.org/abs/2605.22705v1)
