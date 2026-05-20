---
title: "optimize_anything: A Universal API for Optimizing any Text Parameter"
date: 2026-05-19 10:18:12 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.19633v1"
arxiv_id: "2605.19633"
authors: ["Lakshya A Agrawal", "Donghyun Lee", "Shangyin Tan", "Wenjie Ma", "Karim Elmaaroufi", "Rohit Sandadi"]
slug: optimize-anything-a-universal-api-for-optimizing-any-text-pa
summary_word_count: 448
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the capability of existing optimization systems, which are often domain-specific and lack generalizability across diverse tasks. The authors propose a universal optimization framework that leverages large language models (LLMs) to optimize text artifacts evaluated by scoring functions. This work aims to unify various optimization tasks under a single architecture, challenging the notion that specialized tools are necessary for different optimization problems.

**Method**  
The core technical contribution is the development of the "optimize_anything" framework, which employs LLMs to perform both single-task and multi-task optimization. The architecture is designed to support cross-problem transfer and generalization to unseen inputs. The authors utilize a scoring function to evaluate the quality of generated text artifacts, allowing the system to iteratively improve solutions. Key innovations include the use of actionable side information, which enhances convergence speed and final performance, and a multi-task search strategy that outperforms independent optimizations. The framework is open-sourced as part of the GEPA project, with support for multiple backends.

**Results**  
The framework demonstrates significant performance improvements across six diverse tasks. Notably, it achieves a 32.5% to 89.5% accuracy increase on Gemini Flash's ARC-AGI benchmark, nearly tripling the previous state-of-the-art. Additionally, it identifies scheduling algorithms that reduce cloud costs by 40% and generates CUDA kernels that match or exceed the performance of PyTorch in 87% of cases. The optimization results also surpass AlphaEvolve's reported performance on circle packing problems (n=26). Ablation studies indicate that incorporating actionable side information leads to faster convergence and higher final scores, while multi-task optimization benefits from cross-task transfer, with performance improvements scaling with the number of related tasks.

**Limitations**  
The authors acknowledge that the framework's performance may vary depending on the complexity of the optimization problem and the quality of the scoring function used. They do not address potential limitations related to the scalability of the LLMs for extremely large or complex datasets, nor do they discuss the computational overhead associated with multi-task optimization. Additionally, the reliance on text-based representations may not be suitable for all optimization scenarios, particularly those requiring numerical or graphical data.

**Why it matters**  
This work has significant implications for the field of optimization in machine learning, as it presents a novel approach that consolidates various optimization tasks into a single framework. By demonstrating that LLMs can effectively handle diverse optimization problems, the authors pave the way for future research on general-purpose optimization systems. This could lead to more efficient algorithms that reduce the need for domain-specific solutions, ultimately enhancing the accessibility and applicability of optimization techniques across different fields.

Authors: Lakshya A Agrawal, Donghyun Lee, Shangyin Tan, Wenjie Ma, Karim Elmaaroufi, Rohit Sandadi, Sanjit A. Seshia, Koushik Sen et al.  
Source: arXiv:2605.19633  
URL: [https://arxiv.org/abs/2605.19633v1](https://arxiv.org/abs/2605.19633v1)
