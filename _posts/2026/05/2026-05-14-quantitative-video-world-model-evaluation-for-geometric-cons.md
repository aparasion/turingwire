---
title: "Quantitative Video World Model Evaluation for Geometric-Consistency"
date: 2026-05-14 17:59:04 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.15185v1"
arxiv_id: "2605.15185"
authors: ["Jiaxin Wu", "Yihao Pi", "Yinling Zhang", "Yuheng Li", "Xueyan Zou"]
slug: quantitative-video-world-model-evaluation-for-geometric-cons
summary_word_count: 449
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in evaluating generative video models as implicit world models, specifically focusing on the challenge of assessing the physical plausibility of 3D structures and motion in generated videos. Existing evaluation methods often rely on subjective human judgment or learned graders, which can lead to inconsistencies and a lack of diagnostic power for identifying geometric failures. The authors present a preprint work that introduces a quantitative framework, PDI-Bench (Perspective Distortion Index), aimed at providing a more objective and systematic evaluation of geometric coherence in generated video content.

**Method**  
The core technical contribution is the PDI-Bench framework, which quantitatively audits geometric consistency in generated videos. The methodology involves several key steps: 
1. **Object-Centric Observations**: The framework utilizes segmentation and point tracking techniques (e.g., SAM 2, MegaSaM, CoTracker3) to extract object-centric observations from the generated video clips.
2. **3D Reconstruction**: These observations are then lifted to 3D world-space coordinates using monocular reconstruction techniques.
3. **Geometric Residuals**: The authors compute projective-geometry residuals that capture three critical failure dimensions: scale-depth alignment, 3D motion consistency, and 3D structural rigidity. 
4. **Dataset Creation**: To facilitate systematic evaluation, the authors constructed the PDI-Dataset, which encompasses diverse scenarios designed to stress the geometric constraints relevant to video generation.

**Results**  
The evaluation of state-of-the-art video generators using PDI-Bench revealed consistent geometry-specific failure modes that were not detectable by traditional perceptual metrics. The authors provide quantitative results demonstrating that their framework can effectively identify and diagnose geometric inconsistencies across various generative models. Specific headline numbers and comparisons to named baselines are not disclosed in the abstract, but the results indicate a significant improvement in diagnostic capability over existing methods.

**Limitations**  
The authors acknowledge that their framework may not capture all aspects of video quality, particularly those related to perceptual fidelity, as it focuses specifically on geometric coherence. Additionally, the reliance on monocular reconstruction may introduce limitations in accuracy, especially in complex scenes with occlusions or ambiguous depth cues. The dataset, while diverse, may not encompass all possible scenarios encountered in real-world video generation, potentially limiting the generalizability of the findings.

**Why it matters**  
The introduction of PDI-Bench represents a significant advancement in the evaluation of generative video models, providing a robust tool for diagnosing geometric failures that can inform future research in physically grounded video generation. By offering a systematic approach to assess geometric consistency, this work lays the groundwork for improving the fidelity of implicit world models and enhances the understanding of the limitations of current generative techniques. The implications extend to various applications, including robotics, virtual reality, and any domain where accurate 3D motion and structure are critical.

Authors: Jiaxin Wu, Yihao Pi, Yinling Zhang, Yuheng Li, Xueyan Zou  
Source: arXiv:2605.15185  
URL: [https://arxiv.org/abs/2605.15185v1](https://arxiv.org/abs/2605.15185v1)
