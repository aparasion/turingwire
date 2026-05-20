---
title: "TideGS: Scalable Training of Over One Billion 3D Gaussian Splatting Primitives via Out-of-Core Optimization"
date: 2026-05-19 17:40:59 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.20150v1"
arxiv_id: "2605.20150"
authors: ["Chonghao Zhong", "Linfeng Shi", "Hua Chen", "Tiecheng Sun", "Hao Zhao", "Binhang Yuan"]
slug: tidegs-scalable-training-of-over-one-billion-3d-gaussian-spl
summary_word_count: 493
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of training 3D Gaussian Splatting (3DGS) models at a scale exceeding one billion primitives, a task that is fundamentally constrained by GPU memory limitations. Prior systems have been restricted to tens of millions of Gaussians due to the large attribute vectors associated with each primitive, which quickly exhaust available GPU memory. The authors propose a solution to this problem through an out-of-core optimization framework, TideGS, which allows for scalable training on commodity hardware. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
TideGS introduces an out-of-core training framework that leverages a hierarchical SSD-CPU-GPU architecture to manage the large parameter space efficiently. The core technical contributions include:

1. **Block-Virtualized Geometry**: This technique organizes Gaussian primitives in a manner that aligns with SSD storage, optimizing spatial locality and reducing I/O overhead.
2. **Hierarchical Asynchronous Pipeline**: This approach overlaps I/O operations with computation, allowing for more efficient use of resources and minimizing idle time during training.
3. **Trajectory-Adaptive Differential Streaming**: This method selectively transfers only the incremental deltas of the working set between iterations, significantly reducing the amount of data that needs to be moved and processed.

The authors detail the implementation of these techniques, emphasizing their synergistic effects in enabling the training of over one billion Gaussians on a single 24 GB GPU.

**Results**  
TideGS demonstrates significant improvements in both scalability and reconstruction quality compared to existing baselines. Specifically, it achieves the capability to train with over one billion Gaussians, surpassing previous out-of-core methods that were limited to approximately 100 million Gaussians and standard in-memory training approaches that capped at around 11 million Gaussians. The reconstruction quality of the models trained with TideGS is reported to be the best among evaluated single-GPU baselines on large-scale scenes, although specific quantitative metrics (e.g., PSNR, SSIM) are not disclosed in the abstract.

**Limitations**  
The authors acknowledge that while TideGS significantly enhances the scalability of 3DGS training, it is still constrained by the performance of the underlying SSD and CPU components, which may introduce bottlenecks in I/O operations. Additionally, the reliance on a single GPU may limit the applicability of the framework in scenarios requiring distributed training across multiple GPUs. The paper does not address potential issues related to the generalization of the model trained on specific datasets or the impact of varying scene complexities on training efficiency.

**Why it matters**  
The development of TideGS has important implications for the field of 3D graphics and computer vision, particularly in applications requiring high-fidelity scene reconstruction and rendering. By enabling the training of models with a billion Gaussian primitives, this work paves the way for more detailed and complex 3D representations, which can enhance virtual reality, augmented reality, and other immersive technologies. Furthermore, the techniques introduced could inspire future research into memory-efficient training methods for other large-scale machine learning models.

Authors: Chonghao Zhong, Linfeng Shi, Hua Chen, Tiecheng Sun, Hao Zhao, Binhang Yuan, Chaojian Li  
Source: arXiv:2605.20150  
URL: https://arxiv.org/abs/2605.20150v1
