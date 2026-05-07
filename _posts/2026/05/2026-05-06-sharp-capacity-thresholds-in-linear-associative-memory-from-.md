---
title: "Sharp Capacity Thresholds in Linear Associative Memory: From Winner-Take-All to Listwise Retrieval"
date: 2026-05-06 17:53:20 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.05189v1"
arxiv_id: "2605.05189"
authors: ["Nicholas Barnfield", "Juno Kim", "Eshaan Nichani", "Jason D. Lee", "Yue M. Lu"]
slug: sharp-capacity-thresholds-in-linear-associative-memory-from-
summary_word_count: 446
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in understanding the capacity limits of linear associative memory systems, particularly in the context of different retrieval criteria. While previous works have explored the storage capabilities of linear memories, they often overlook how retrieval methods influence these capacities. The authors specifically investigate the transition from winner-take-all (WTA) retrieval to listwise retrieval, providing a theoretical framework for quantifying the maximum number of key-value associations that can be effectively stored and retrieved.

**Method**  
The authors introduce a theoretical model based on an isotropic Gaussian distribution for the stored key-target pairs. They demonstrate that for WTA retrieval, the memory capacity scales logarithmically as \(d^2 \asymp n \log n\), where \(d\) is the dimensionality of the memory and \(n\) is the number of stored associations. This is achieved through a correlation matrix memory construction that utilizes key-target outer products. For listwise retrieval, they propose the Tail-Average Margin (TAM) as a new convex upper-tail criterion, which ensures that the correct target remains among the top candidates. Under this criterion, the capacity scales quadratically as \(d^2 \asymp n\). The authors develop an exact asymptotic theory for the TAM empirical-risk minimizer, employing a two-parameter scalar variational principle to analyze the system's behavior under varying loads.

**Results**  
The paper presents several key findings:  
- For WTA retrieval, the authors establish a critical load threshold, indicating a phase transition between satisfiable and unsatisfiable states, with a sharp top-1 threshold conjectured at \(d^2 \sim 2n \log n\).  
- For listwise retrieval, the quadratic scaling of capacity is confirmed, with detailed predictions on the limiting distributions of true scores, competitor scores, and margins.  
- The empirical results align with theoretical predictions, demonstrating the effectiveness of the TAM criterion in maintaining retrieval accuracy as the load approaches critical thresholds.

**Limitations**  
The authors acknowledge that their model is based on an isotropic Gaussian assumption, which may not generalize to all real-world scenarios. Additionally, the focus on linear memory systems may limit the applicability of their findings to more complex architectures, such as deep neural networks. The paper does not address potential computational complexities associated with implementing the TAM criterion in practice.

**Why it matters**  
This work has significant implications for the design and understanding of associative memory systems in machine learning. By elucidating the capacity limits under different retrieval paradigms, it provides a foundational framework for optimizing memory architectures in applications such as information retrieval, recommendation systems, and neural network design. The introduction of the TAM criterion could inspire new approaches to enhance retrieval performance in scenarios where maintaining a list of candidates is crucial.

Authors: Nicholas Barnfield, Juno Kim, Eshaan Nichani, Jason D. Lee, Yue M. Lu  
Source: arXiv:2605.05189  
URL: https://arxiv.org/abs/2605.05189v1
