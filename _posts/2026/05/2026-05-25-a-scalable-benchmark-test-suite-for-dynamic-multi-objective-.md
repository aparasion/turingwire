---
title: "A Scalable Benchmark Test Suite for Dynamic Multi-Objective Optimization with a Changing Number of Objectives"
date: 2026-05-25 12:33:20 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.25785v1"
arxiv_id: "2605.25785"
authors: ["Ke Shang", "Zhiyun Xiao", "Yuxuan Liu", "Jianguo Li", "Shaojiang Wang", "Wei Sun"]
slug: a-scalable-benchmark-test-suite-for-dynamic-multi-objective-
summary_word_count: 431
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the literature on dynamic multi-objective optimization (DMOO) by highlighting the limitations of existing benchmark test suites. Current benchmarks often conflate changes in the number of objectives with changes in the objective functions themselves, making it challenging to evaluate an algorithm's performance specifically in handling dynamic objective counts. The authors argue that this conflation undermines the validity of theoretical properties claimed in prior studies. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel benchmark test suite designed to isolate the dynamics of changing objective counts while keeping the objective functions constant. The suite is constructed by defining a maximum-objective problem and dynamically selecting subsets of these objectives over time. To mitigate degeneracy issues commonly found in classical DTLZ and WFG problems, the authors introduce Minus-DTLZ and Minus-WFG formulations, ensuring that all objectives are mutually conflicting. The benchmark suite is scalable, allowing for a variety of configurations to test different algorithms under controlled conditions. The paper does not disclose specific training compute requirements, focusing instead on the structural design of the benchmark.

**Results**  
The proposed benchmark suite was evaluated using a range of representative algorithms from the literature, demonstrating its effectiveness and flexibility. While specific numerical results are not detailed in the abstract, the authors claim that their suite allows for a more accurate assessment of algorithm performance in the context of dynamic objective changes. The results indicate that existing algorithms can be benchmarked more reliably, leading to better insights into their capabilities in handling dynamic multi-objective scenarios.

**Limitations**  
The authors acknowledge that their benchmark suite, while addressing the issue of conflated objective dynamics, may still be limited by the inherent complexity of real-world applications where objective functions can change in non-linear ways. Additionally, the paper does not explore the computational overhead that may arise from implementing the proposed benchmark in practice. The scalability of the benchmark is also contingent on the selection of algorithms, which may not cover all possible approaches in DMOO.

**Why it matters**  
This work has significant implications for the field of multi-objective optimization, particularly in real-world applications where the criteria for evaluation are not static. By providing a benchmark that isolates the dynamics of objective counts, researchers can better evaluate and compare the performance of various optimization algorithms. This clarity can lead to improved algorithm design and more robust solutions in dynamic environments, ultimately advancing the state of the art in DMOO.

Authors: Ke Shang, Zhiyun Xiao, Yuxuan Liu, Jianguo Li, Shaojiang Wang, Wei Sun  
Source: arXiv:2605.25785  
URL: [https://arxiv.org/abs/2605.25785v1](https://arxiv.org/abs/2605.25785v1)
