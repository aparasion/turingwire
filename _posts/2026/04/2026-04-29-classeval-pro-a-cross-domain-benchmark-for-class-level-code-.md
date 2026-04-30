---
title: "ClassEval-Pro: A Cross-Domain Benchmark for Class-Level Code Generation"
date: 2026-04-29 17:38:37 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.26923v1"
arxiv_id: "2604.26923"
authors: ["Yeheng Chen", "Chaoxiang Xie", "Yuling Shi", "Wenhao Zeng", "Yongpan Wang", "Hongyu Zhang"]
slug: classeval-pro-a-cross-domain-benchmark-for-class-level-code-
summary_word_count: 501
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the capability of large language models (LLMs) for compositional code generation, specifically the task of generating complete, internally structured classes from specifications. While LLMs have demonstrated proficiency in function-level code synthesis and repository-level modifications, the intermediate task of class-level code generation remains underexplored. Existing benchmarks are either limited to isolated functions or rely on manually curated tasks, which are costly to scale and prone to data contamination. This work presents ClassEval-Pro, a novel benchmark designed to evaluate class-level code generation across diverse domains.

**Method**  
ClassEval-Pro comprises 300 class-level tasks across 11 domains, developed through an automated three-stage pipeline. The pipeline includes complexity enhancement, cross-domain class composition, and integration of real-world GitHub code contributed after January 2025. Each task is validated using an LLM Judge Ensemble and must achieve over 90% line coverage in test suites. The authors evaluate five state-of-the-art LLMs using five distinct generation strategies. The evaluation metrics focus on the Pass@1 rate, which measures the percentage of tasks for which the generated class meets the specification on the first attempt. The study also conducts error analysis on 500 manually annotated failures to identify common issues in generated code.

**Results**  
The best-performing model achieves a Pass@1 rate of 45.6%, indicating a substantial challenge in class-level code generation. There is a notable 17.7-point performance gap between the strongest and weakest models, underscoring the benchmark's discriminative power. The choice of generation strategy significantly influences model performance; structured approaches, such as bottom-up generation, enhance weaker models by up to 9.4 percentage points, while compositional generation strategies yield a low Pass@1 rate of only 1.3%. Error analysis reveals that logic errors account for 56.2% of failures, while dependency errors contribute 38.0%, highlighting cross-method coordination as a critical bottleneck in the generation process.

**Limitations**  
The authors acknowledge that the benchmark is limited to the specific domains and tasks included in the dataset, which may not encompass the full spectrum of class-level code generation challenges. Additionally, the reliance on LLMs for task validation may introduce biases based on the models' inherent limitations. The automated pipeline, while efficient, may not capture all nuances of class-level specifications, potentially affecting the quality of generated tasks. Furthermore, the dataset's reliance on GitHub code from a specific timeframe may limit its generalizability to other coding contexts.

**Why it matters**  
ClassEval-Pro provides a critical resource for advancing research in class-level code generation, offering a scalable and automated framework for evaluating LLMs in this domain. By identifying key error types and performance gaps, this benchmark lays the groundwork for future improvements in model architectures and training methodologies. The findings emphasize the need for enhanced coordination mechanisms in code generation, which could inform the design of more sophisticated LLMs capable of tackling complex programming tasks. This work has implications for both academic research and practical applications in software development, where automated code generation is increasingly sought after.

Authors: Yeheng Chen, Chaoxiang Xie, Yuling Shi, Wenhao Zeng, Yongpan Wang, Hongyu Zhang, Xiaodong Gu  
Source: arXiv:2604.26923  
URL: [https://arxiv.org/abs/2604.26923v1](https://arxiv.org/abs/2604.26923v1)
