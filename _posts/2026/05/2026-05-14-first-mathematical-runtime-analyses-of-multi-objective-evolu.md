---
title: "First Mathematical Runtime Analyses of Multi-Objective Evolutionary Algorithms for Multi-Valued Decision Variables"
date: 2026-05-14 13:42:52 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.14836v1"
arxiv_id: "2605.14836"
authors: ["Mingfeng Li", "Zheng Cheng", "Weijie Zheng", "Benjamin Doerr"]
slug: first-mathematical-runtime-analyses-of-multi-objective-evolu
summary_word_count: 458
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the theoretical understanding of multi-objective evolutionary algorithms (MOEAs) applied to multi-valued decision variables, where the decision space consists of more than two values (i.e., \( r > 2 \)). While binary decision spaces have been extensively analyzed, the lack of mathematical runtime analyses for MOEAs dealing with multi-valued decision variables has left a void in the literature. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors focus on the classic SEMO (Single-Objective Evolutionary Multi-Objective) algorithm, specifically employing a unit-strength local mutation strategy. They analyze the expected number of function evaluations required for the SEMO algorithm to cover the Pareto front of an \( r \)-valued version of the classic \oneminmax benchmark. The authors derive an upper bound of \( O(n^2 r^2 \log n) \) and a near-tight lower bound of \( \Omega(n^2 r (r + \log n)) \) for the expected runtime. Furthermore, they propose a variant of the SEMO algorithm that only accepts strictly better solutions, which allows them to tighten the bounds, achieving an upper bound of \( O(n^2 r (r + \log n)) \) that matches the lower bound.

**Results**  
The analysis reveals that the SEMO algorithm exhibits a runtime complexity of \( O(n^2 r^2 \log n) \) for the standard case and \( O(n^2 r (r + \log n)) \) for the variant that accepts only strictly better solutions. These results indicate that the classic MOEAs do not face significant additional challenges when adapting to multi-valued decision variables compared to binary cases. The authors provide a comprehensive comparison against existing benchmarks, demonstrating that the derived bounds are effective in characterizing the performance of the SEMO algorithm in this context.

**Limitations**  
The authors acknowledge that their results are specific to the SEMO algorithm and may not generalize to other MOEAs with more complex population dynamics. They also note that while they have established bounds for the expected number of function evaluations, further research is needed to develop tighter bounds for algorithms that incorporate more sophisticated mechanisms. Additionally, the analysis does not consider the impact of varying population sizes or the effects of different mutation strategies on runtime.

**Why it matters**  
This work is significant as it lays the groundwork for future theoretical explorations of MOEAs in multi-valued decision spaces, which are increasingly relevant in practical applications. By providing mathematical runtime analyses, the authors contribute to a deeper understanding of the efficiency and effectiveness of MOEAs in handling complex optimization problems. The findings may inform the design of more advanced evolutionary algorithms and encourage further research into the theoretical aspects of multi-objective optimization.

Authors: Mingfeng Li, Zheng Cheng, Weijie Zheng, Benjamin Doerr  
Source: arXiv cs.NE  
URL: [https://arxiv.org/abs/2605.14836v1](https://arxiv.org/abs/2605.14836v1)  
arXiv ID: 2605.14836
