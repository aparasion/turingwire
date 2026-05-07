---
title: "Wasserstein-Aligned Localisation for VLM-Based Distributional OOD Detection in Medical Imaging"
date: 2026-05-06 17:32:34 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.05161v1"
arxiv_id: "2605.05161"
authors: ["Bernhard Kainz", "Johanna P Mueller", "Matthew Baugh", "Cosmin Bercea"]
slug: wasserstein-aligned-localisation-for-vlm-based-distributiona
summary_word_count: 422
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of zero-shot anomaly localization in medical imaging using vision-language models (VLMs), particularly the challenge posed by the lack of healthy anatomical context for rare pathology detection. Existing methods struggle to effectively identify anomalies due to insufficient comparative reasoning against normal anatomical distributions. The authors propose a novel framework that leverages optimal transport theory to enhance the localization process.

**Method**  
The proposed framework, WALDO (Wasserstein-Aligned Localisation for VLM-Based Distributional OOD Detection), reformulates zero-shot localization as a comparative inference problem. Key components of WALDO include:

1. **Entropy-weighted Sliced Wasserstein Distances**: This technique is employed for selecting anatomically-aware reference distributions from DINOv2 patch distributions, allowing for a more informed comparison against normal anatomy.
   
2. **Goldilocks Zone Sampling**: This method exploits the non-monotonic relationship between reference similarity and localization accuracy, identifying an optimal range of reference similarity that minimizes bias and variance in the localization task.

3. **Self-consistency Aggregation**: Implemented through weighted non-maximum suppression, this step aggregates the results to enhance the robustness of the localization output.

The authors provide a theoretical analysis of the Goldilocks effect through distributional divergence, demonstrating that references with moderate similarity yield optimal performance in comparative visual reasoning.

**Results**  
WALDO was evaluated on the NOVA brain MRI benchmark, achieving a mean Average Precision (mAP) of $43.5_{\pm1.6}\%$ at a threshold of 30 (95% CI: [40.4, 46.7]), which represents a 19% relative improvement over existing zero-shot baselines. Cross-model evaluations further confirmed the robustness of WALDO, with GPT-4o and Qwen3-VL-32B achieving mAP scores of $32.0_{\pm6.5}\%$ and $32.0_{\pm6.6}\%$, respectively. Statistical significance was confirmed through paired McNemar tests, yielding $p<0.01$.

**Limitations**  
The authors acknowledge that WALDO is a training-free framework, which may limit its adaptability to specific datasets or pathological contexts that require fine-tuning. Additionally, the reliance on DINOv2 for reference selection may introduce biases based on the training data of the VLM. The theoretical analysis, while insightful, may not fully capture the complexities of real-world anatomical variations. Furthermore, the performance metrics are confined to the NOVA benchmark, necessitating further validation across diverse medical imaging datasets.

**Why it matters**  
WALDO's approach to anomaly localization through comparative reasoning and optimal transport theory represents a significant advancement in the field of medical imaging. By effectively utilizing reference distributions, it enhances the detection of rare pathologies, which is critical for clinical applications. The implications of this work extend to improving diagnostic accuracy and efficiency in medical imaging workflows, potentially influencing future research on VLMs and their applications in healthcare.

Authors: Bernhard Kainz, Johanna P Mueller, Matthew Baugh, Cosmin Bercea  
Source: arXiv:2605.05161  
URL: [https://arxiv.org/abs/2605.05161v1](https://arxiv.org/abs/2605.05161v1)
