---
title: "BenchCAD: A Comprehensive, Industry-Standard Benchmark for Programmatic CAD"
date: 2026-05-11 17:13:36 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.10865v1"
arxiv_id: "2605.10865"
authors: ["Haozhe Zhang", "Kaichen Liu", "Miaomiao Chen", "Lei Li", "Shaojie Yang", "Cheng Peng"]
slug: benchcad-a-comprehensive-industry-standard-benchmark-for-pro
summary_word_count: 451
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of a comprehensive benchmark for evaluating the capabilities of multimodal large language models (MLLMs) in the context of industrial Computer-Aided Design (CAD) code generation. Existing literature has not sufficiently assessed whether MLLMs can jointly handle the complexities of generating executable parametric programs from visual or textual inputs in realistic industrial settings. The authors present BenchCAD, a unified benchmark designed to fill this gap.

**Method**  
BenchCAD comprises 17,900 execution-verified CadQuery programs spanning 106 industrial part families, including components like bevel gears and compression springs. The benchmark evaluates models through four primary tasks: visual question answering, code question answering, image-to-code generation, and instruction-guided code editing. This multifaceted approach allows for a detailed analysis of model performance across three dimensions: perception (understanding visual inputs), parametric abstraction (inferring engineering parameters), and executable program synthesis (generating valid CAD code). The authors also explore fine-tuning and reinforcement learning techniques to enhance model performance, although specific training compute details are not disclosed.

**Results**  
BenchCAD's evaluation of over 10 state-of-the-art models reveals significant shortcomings in their ability to generate accurate parametric CAD programs. While models can often recover the coarse outer geometry of parts, they frequently fail to capture fine 3D structures and misinterpret critical industrial design parameters. For instance, essential CAD operations like sweeps, lofts, and twist-extrudes are often replaced with simpler sketch-and-extrude patterns, indicating a lack of understanding of the design intent. Fine-tuning and reinforcement learning approaches yield improvements in in-distribution performance, but generalization to unseen part families remains limited, highlighting the models' current inadequacies.

**Limitations**  
The authors acknowledge that while BenchCAD provides a robust framework for evaluating CAD code generation, the benchmark itself may not encompass all possible industrial scenarios. Additionally, the reliance on execution-verified programs may limit the diversity of tasks that can be evaluated. The paper does not address the computational resources required for training the models on this benchmark, which could be a barrier for some researchers. Furthermore, the generalization capabilities of the models to novel part families are notably constrained, which the authors flag as a critical area for future research.

**Why it matters**  
BenchCAD serves as a pivotal resource for advancing the field of CAD automation by providing a standardized method for assessing the industrial readiness of MLLMs. The insights gained from this benchmark can inform the development of more sophisticated models that better understand the nuances of CAD design and manufacturing processes. By highlighting the current limitations of existing models, this work encourages further research into improving the fidelity of CAD code generation, ultimately contributing to more efficient and effective design workflows in industrial applications.

Authors: Haozhe Zhang, Kaichen Liu, Miaomiao Chen, Lei Li, Shaojie Yang, Cheng Peng, Hanjie Chen  
Source: arXiv:2605.10865  
URL: [https://arxiv.org/abs/2605.10865v1](https://arxiv.org/abs/2605.10865v1)
