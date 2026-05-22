---
title: "Antigravity 2.0 Tops the OpenSCAD Architectural 3D LLM Benchmark"
date: 2026-05-22 10:38:26 +0000
category: research
subcategory: evaluation_benchmarks
company: "ModelRift"
secondary_companies: []
impact: notable
source_publisher: "Hacker News (AI filtered)"
source_url: "https://modelrift.com/blog/openscad-llm-benchmark/"
arxiv_id: ""
authors: []
slug: antigravity-2-0-tops-the-openscad-architectural-3d-llm-bench
summary_word_count: 434
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in evaluating AI coding tools specifically for architectural 3D modeling using OpenSCAD, a text-based CAD tool. Existing benchmarks primarily focus on basic syntax or simple geometric shapes, failing to assess the models' capabilities in generating complex architectural structures. The authors aim to establish a more relevant benchmark by using the Pantheon as a case study, which requires a nuanced understanding of spatial geometry and architectural intent.

**Method**  
The authors developed a benchmark that prompts various AI coding tools to generate OpenSCAD code for the Pantheon, utilizing reference images for guidance. The benchmark evaluates the models based on their ability to produce parametric CAD code that accurately represents the architectural features of the Pantheon, including its radial symmetry, dome, and portico. The tools are assessed on their output quality and rendering speed using the OpenSCAD CLI to visualize the generated models. The evaluation includes six different AI models, with a focus on their ability to handle complex geometric transformations and Boolean operations inherent in architectural design.

**Results**  
The benchmark results indicate varying performance across the tested models:
- **Cursor 3.5 / Composer 2.5**: Fastest execution time but scored 1.4/5 for quality, capturing basic features but lacking in architectural detail.
- **Codex 5.5**: Achieved a quality score of 4/5, demonstrating strong detail density, though the final STL export did not match the PNG preview, affecting its overall score.
- **Claude Code 2.1 / Opus 4.7**: Scored 2/5, slower performance with moderate structural accuracy.
The results highlight that while some models excel in speed, they may compromise on quality, indicating a trade-off between execution time and output fidelity.

**Limitations**  
The authors acknowledge that the benchmark is limited to OpenSCAD and may not generalize to other CAD tools or modeling paradigms, particularly those that require organic or sculptural forms. Additionally, the reliance on reference images may introduce variability in interpretation among different models. The benchmark does not account for the models' performance in real-time interactive scenarios, which could be critical for practical applications.

**Why it matters**  
This work is significant as it establishes a more relevant evaluation framework for AI coding tools in architectural design, moving beyond simplistic geometric tasks to more complex, real-world applications. By focusing on OpenSCAD and the Pantheon, the authors provide insights into the capabilities and limitations of current LLMs in generating architectural code, which can inform future developments in AI-assisted design tools. This benchmark could serve as a foundation for further research into improving LLMs' understanding of spatial geometry and architectural intent, ultimately enhancing their utility in CAD applications.

Authors: unknown  
Source: arXiv: [insert ID]  
URL: https://modelrift.com/blog/openscad-llm-benchmark/
