---
title: "MesonGS++: Post-training Compression of 3D Gaussian Splatting with Hyperparameter Searching"
date: 2026-04-29 15:30:06 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2604.26799v1"
arxiv_id: "2604.26799"
authors: ["Shuzhao Xie", "Junchen Ge", "Weixiang Zhang", "Jiahang Liu", "Chen Tang", "Yunpeng Bai"]
slug: mesongs-post-training-compression-of-3d-gaussian-splatting-w
summary_word_count: 424
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the practical deployment of 3D Gaussian Splatting (3DGS) due to its high storage requirements. While 3DGS provides high-quality novel view synthesis and real-time rendering, existing post-training compression techniques are limited by their reliance on numerous interdependent hyperparameters across various methods such as pruning, transformation, quantization, and entropy coding. This complexity complicates the control over the final compressed size and the effective exploitation of the rate-distortion trade-off. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce MesonGS++, a size-aware post-training codec specifically designed for 3D Gaussian compression. The architecture integrates several advanced techniques: joint importance-based pruning, octree geometry coding, attribute transformation, selective vector quantization for higher-degree spherical harmonics, and group-wise mixed-precision quantization combined with entropy coding. The configuration aspect of MesonGS++ optimizes the reserve ratio and bit-width allocation as key rate-distortion parameters, employing discrete sampling and 0-1 integer linear programming to achieve a target storage budget. Additionally, a linear size estimator and a CUDA parallel quantization operator are proposed to enhance the efficiency of the hyperparameter search process.

**Results**  
MesonGS++ demonstrates a remarkable compression ratio of over 34× while maintaining rendering fidelity, significantly outperforming existing state-of-the-art post-training methods. Notably, it achieves a PSNR that exceeds that of the original 3DGS at a 20× compression rate on the Stump scene, showcasing its effectiveness in meeting target size budgets without any retraining. The results indicate a substantial improvement in both compression efficiency and rendering quality compared to baseline methods.

**Limitations**  
The authors acknowledge that the proposed method may still be sensitive to the choice of hyperparameters, despite the optimization strategies employed. Additionally, the reliance on a specific target storage budget may limit its applicability in scenarios with varying constraints. The paper does not address potential performance degradation in more complex scenes or the scalability of the method to larger datasets beyond the tested benchmarks.

**Why it matters**  
The implications of MesonGS++ are significant for the field of 3D graphics and computer vision, particularly in applications requiring efficient storage and real-time rendering capabilities. By providing a robust framework for post-training compression, this work enables the deployment of high-fidelity 3D models in resource-constrained environments, paving the way for advancements in virtual reality, augmented reality, and other immersive technologies. The ability to surpass the original model's performance at reduced sizes opens new avenues for research in model optimization and compression techniques.

Authors: Shuzhao Xie, Junchen Ge, Weixiang Zhang, Jiahang Liu, Chen Tang, Yunpeng Bai, Shijia Ge, Jingyan Jiang et al.  
Source: arXiv:2604.26799  
URL: https://arxiv.org/abs/2604.26799v1
