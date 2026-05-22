---
title: "Tokenisation via Convex Relaxations"
date: 2026-05-21 17:59:56 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.22821v1"
arxiv_id: "2605.22821"
authors: ["Jan Tempus", "Philip Whittington", "Craig W. Schmidt", "Dennis Komm", "Tiago Pimentel"]
slug: tokenisation-via-convex-relaxations
summary_word_count: 494
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing tokenization algorithms in natural language processing (NLP), specifically the greedy nature of Byte Pair Encoding (BPE) and Unigram models. These algorithms make locally optimal decisions without considering the global structure of the vocabulary, leading to suboptimal tokenization. The authors propose a novel approach to tokenization that formulates the problem as a linear program, which is a gap in the literature as it leverages convex optimization techniques for this purpose. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the introduction of ConvexTok, a tokenization algorithm that utilizes convex relaxation to construct tokenizers. The authors frame the tokenization problem as a linear programming task, allowing for a global optimization of the vocabulary. ConvexTok is designed to minimize the bits-per-byte (BpB) metric, which is crucial for language model efficiency. The authors provide a method to certify the optimality of the tokenization by offering a lower bound on the objective function, demonstrating that ConvexTok can achieve solutions within 1% of the optimal for common vocabulary sizes. The training compute requirements are not explicitly disclosed, but the use of convex optimization suggests a potentially efficient computational framework.

**Results**  
ConvexTok demonstrates significant improvements over baseline tokenization methods, particularly in intrinsic tokenization metrics and BpB for language models. The authors report consistent enhancements in BpB metrics compared to BPE and Unigram, although specific numerical improvements are not detailed in the abstract. For downstream tasks, the performance gains are less consistent, indicating that while ConvexTok improves tokenization quality, the impact on task performance may vary depending on the specific application. The paper suggests that ConvexTok can be a more effective choice for tokenization in various NLP tasks, although the exact effect sizes and benchmark comparisons are not provided in the abstract.

**Limitations**  
The authors acknowledge that while ConvexTok shows promise, the improvements in downstream task performance are not uniformly significant, suggesting that the benefits of the new tokenization method may not translate to all applications. Additionally, the paper does not discuss the computational complexity of the linear programming approach in detail, which could be a concern for large-scale applications. The lack of peer review also raises questions about the robustness of the findings and the potential for undisclosed limitations.

**Why it matters**  
This work has important implications for the design of tokenization algorithms in NLP, particularly in enhancing the efficiency of language models. By framing tokenization as a linear programming problem, the authors open new avenues for research into optimal vocabulary construction, which could lead to more effective and efficient NLP systems. The ability to certify the proximity to optimal solutions also provides a valuable tool for practitioners seeking to evaluate and improve their tokenization strategies. Overall, ConvexTok represents a significant advancement in the field, potentially influencing future research and applications in tokenization and language modeling.

Authors: Jan Tempus, Philip Whittington, Craig W. Schmidt, Dennis Komm, Tiago Pimentel  
Source: arXiv:2605.22821  
URL: https://arxiv.org/abs/2605.22821v1
