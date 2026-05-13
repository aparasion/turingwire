---
title: "Covering Human Action Space for Computer Use: Data Synthesis and Benchmark"
date: 2026-05-12 17:59:58 +0000
category: research
subcategory: evaluation_benchmarks
company: "null"
secondary_companies: ["OpenAI", "Anthropic"]
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.12501v1"
arxiv_id: "2605.12501"
authors: ["Miaosen Zhang", "Xiaohan Zhao", "Zhihong Tan", "Zhou Huoshen", "Yijia Fan", "Yifan Yang"]
slug: covering-human-action-space-for-computer-use-data-synthesis-
summary_word_count: 471
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inadequacy of existing computer-use agents (CUAs) in handling complex, low-frequency interactions within graphical user interfaces (GUIs). Despite advancements in models like GPT-5.4 and Claude, their performance remains suboptimal for intricate tasks, which are critical for user trust. The authors identify a long-tail distribution in task failures, where a small subset of complex interactions leads to a significant proportion of errors. This issue is exacerbated by the lack of sufficient training data for these complex interactions. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a new benchmark, CUActSpot, designed to evaluate model performance on a diverse set of complex interactions across five modalities: GUI, text, table, canvas, and natural image. Unlike previous benchmarks that primarily focus on click-centric tasks, CUActSpot encompasses a wider range of actions, including clicking, dragging, and drawing. To generate the necessary training data, the authors develop a renderer-based data synthesis pipeline. This pipeline automatically creates scenes for each modality, captures screenshots and element coordinates, and utilizes a large language model (LLM) to generate corresponding instructions and action traces. The model trained on this synthesized dataset is named Phi-Ground-Any-4B, which is specifically designed to outperform existing open-source models with fewer than 32 billion parameters.

**Results**  
Phi-Ground-Any-4B demonstrates superior performance compared to several baseline models on the CUActSpot benchmark. While specific numerical results are not disclosed in the abstract, the authors assert that their model outperforms open-source alternatives, indicating a significant improvement in handling complex interactions. The benchmark's comprehensive nature allows for a more nuanced evaluation of model capabilities, particularly in low-frequency scenarios that have been historically challenging for CUAs.

**Limitations**  
The authors acknowledge that the synthesized data may not fully capture the variability and unpredictability of real-world user interactions, potentially limiting the generalizability of the trained models. Additionally, the reliance on an LLM for generating instructions and action traces may introduce biases or inaccuracies inherent to the language model itself. The paper does not address the computational resources required for training Phi-Ground-Any-4B, which could be a barrier for some researchers. Furthermore, the benchmark's focus on specific modalities may overlook other relevant interaction types that could be critical in broader applications.

**Why it matters**  
This work has significant implications for the development of more reliable CUAs, particularly in applications requiring complex user interactions. By providing a robust benchmark and a novel data synthesis approach, the authors pave the way for future research aimed at enhancing the capabilities of AI systems in real-world scenarios. The release of the benchmark, data, code, and models will facilitate further exploration and improvement in the field, potentially leading to more trustworthy and effective automation tools for users.

Authors: Miaosen Zhang, Xiaohan Zhao, Zhihong Tan, Zhou Huoshen, Yijia Fan, Yifan Yang, Kai Qiu, Bei Liu et al.  
Source: arXiv:2605.12501  
URL: https://arxiv.org/abs/2605.12501v1
