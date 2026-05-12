---
title: "CADBench: A Multimodal Benchmark for AI-Assisted CAD Program Generation"
date: 2026-05-11 17:25:47 +0000
category: research
subcategory: evaluation_benchmarks
company: "Hugging Face"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.10873v1"
arxiv_id: "2605.10873"
authors: ["Anna C. Doris", "Jacob Thomas Sony", "Ghadi Nehme", "Era Syla", "Amin Heyrani Nobari", "Faez Ahmed"]
slug: cadbench-a-multimodal-benchmark-for-ai-assisted-cad-program-
summary_word_count: 459
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of a comprehensive evaluation framework for AI-assisted CAD program generation, which has hindered progress in the field. Existing benchmarks are fragmented across various datasets, modalities, and metrics, making it difficult to assess advancements in the recovery of editable CAD programs from diverse inputs such as images and 3D observations. The authors present CADBench, a unified benchmark designed to fill this gap and facilitate systematic evaluation of multimodal CAD generation systems. This work is a preprint and has not yet undergone peer review.

**Method**  
CADBench comprises 18,000 evaluation samples organized into six benchmark families derived from existing datasets, including DeepCAD, Fusion 360, ABC, MCB, and Objaverse. It incorporates five input modalities: clean meshes, noisy meshes, single-view renders, photorealistic renders, and multi-view renders. The benchmark evaluates systems using six metrics that assess geometric fidelity, executability, and program compactness. The STEP-based families are stratified by B-rep face count, and diversity sampling is employed to enable controlled analysis across varying complexity and object types. The authors benchmark eleven CAD-specialized and general-purpose vision-language models, generating over 1.4 million CAD programs to evaluate performance under idealized conditions.

**Results**  
The results indicate that specialized mesh-to-CAD models significantly outperform general-purpose code-generating vision-language models (VLMs) in terms of CAD program reconstruction. The performance gap is particularly pronounced under idealized input conditions, where specialized models demonstrate superior reconstruction capabilities. However, the study identifies three recurring failure modes: (1) reconstruction quality diminishes with increased geometric complexity, (2) CAD-specialized models exhibit brittleness when faced with modality shifts, and (3) model rankings can vary significantly across different evaluation metrics. These findings highlight the nuanced performance characteristics of the evaluated systems and underscore the need for a robust benchmarking framework.

**Limitations**  
The authors acknowledge that CADBench may not fully capture the complexities of real-world CAD program generation, as it primarily focuses on idealized inputs. Additionally, the reliance on specific datasets may introduce biases that affect generalizability. The study also does not explore the implications of model interpretability or the potential for transfer learning across modalities, which could be critical for advancing the field. Furthermore, the benchmark's effectiveness in evaluating systems under non-ideal conditions remains to be validated.

**Why it matters**  
The introduction of CADBench represents a significant advancement in the evaluation of AI-assisted CAD program generation, providing a standardized framework for assessing multimodal systems. By revealing the strengths and weaknesses of various models, CADBench serves as a diagnostic tool that can guide future research and development efforts. The insights gained from this benchmark can inform the design of more robust and versatile CAD generation systems, ultimately enhancing the capabilities of AI in the domain of computer-aided design.

Authors: Anna C. Doris, Jacob Thomas Sony, Ghadi Nehme, Era Syla, Amin Heyrani Nobari, Faez Ahmed  
Source: arXiv:2605.10873  
URL: [https://arxiv.org/abs/2605.10873v1](https://arxiv.org/abs/2605.10873v1)
