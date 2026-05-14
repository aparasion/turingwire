---
title: "Force-Aware Neural Tangent Kernels for Scalable and Robust Active Learning of MLIPs"
date: 2026-05-13 17:08:37 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.13788v1"
arxiv_id: "2605.13788"
authors: ["Eszter Varga-Umbrich", "Zachary Weller-Davies", "Paul Duckworth", "Jules Tilly", "Olivier Peltre", "Shikha Surana"]
slug: force-aware-neural-tangent-kernels-for-scalable-and-robust-a
summary_word_count: 438
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of active learning in machine-learning interatomic potentials (MLIPs), specifically focusing on the challenges of scaling to large candidate pools, utilizing energy-force supervision, and ensuring robustness against biases in candidate pools relative to target distributions. Existing methods often struggle with computational efficiency and robustness, particularly when candidate pools do not represent the target distribution well.

**Method**  
The authors propose a novel acquisition framework that scales linearly by employing chunked feature-space posterior-variance shortlisting. This method circumvents the need to materialize candidate and training set kernels, allowing for the screening of approximately 200,000 structures within hours. The framework is versatile and can be applied to various acquisition strategies that utilize molecular similarity metrics. Additionally, the authors extend the Neural Tangent Kernel (NTK) to a force-aware context by incorporating mixed parameter-coordinate derivatives, resulting in a force NTK and a joint energy-force NTK. These new kernels serve as effective similarity metrics for vector-field predictions, enhancing the active learning process.

**Results**  
The proposed joint energy-force NTK demonstrates superior performance on the OC20 dataset, achieving the lowest mean absolute error (MAE) and root mean square error (RMSE) for both energy and force metrics across all evaluated splits. In comparative evaluations on the T1x, PMechDB, and RGD benchmarks, the force NTK methods maintain competitive performance against established baselines while exhibiting significantly greater efficiency than traditional committee-based approaches. In a controlled candidate-pool shift case study on T1x, the acquisition strategy leveraging pretrained MLIP embeddings and NTKs shows robustness, with lower variance compared to committee-based methods.

**Limitations**  
The authors acknowledge that their approach may still be sensitive to the choice of molecular similarity metrics and the quality of the pretrained MLIP embeddings. They do not address potential limitations related to the generalizability of their method across diverse chemical systems or the computational overhead associated with the initial training of the MLIP. Additionally, the scalability of the method in extremely large or complex molecular systems remains to be fully explored.

**Why it matters**  
This work has significant implications for the field of computational materials science and molecular modeling, as it provides a scalable and robust framework for active learning in MLIPs. By effectively integrating energy and force information into the acquisition process, the proposed methods can enhance the efficiency of training foundation models, potentially leading to more accurate predictions in molecular simulations. The ability to handle large candidate pools and maintain robustness against distribution shifts opens avenues for further research in active learning strategies and their applications in various domains, including drug discovery and materials design.

Authors: Eszter Varga-Umbrich, Zachary Weller-Davies, Paul Duckworth, Jules Tilly, Olivier Peltre, Shikha Surana  
Source: arXiv:2605.13788  
URL: [https://arxiv.org/abs/2605.13788v1](https://arxiv.org/abs/2605.13788v1)
