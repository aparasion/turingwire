---
title: "SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer"
date: 2026-05-14 17:58:03 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.15178v1"
arxiv_id: "2605.15178"
authors: ["Haoyi Zhu", "Haozhe Liu", "Yuyang Zhao", "Tian Ye", "Junsong Chen", "Jincheng Yu"]
slug: sana-wm-efficient-minute-scale-world-modeling-with-hybrid-li
summary_word_count: 436
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper presents SANA-WM, a preprint work addressing the gap in efficient minute-scale world modeling for video generation. Existing models, such as LingBot-World and HY-WorldPlay, achieve high visual fidelity but lack efficiency in training and inference. SANA-WM aims to synthesize high-fidelity, 720p videos with precise camera control while significantly improving computational efficiency.

**Method**  
SANA-WM is a 2.6B-parameter architecture that integrates four key innovations:  
1. **Hybrid Linear Attention**: This mechanism combines frame-wise Gated DeltaNet (GDN) with traditional softmax attention, enabling memory-efficient long-context modeling, which is crucial for handling minute-scale video sequences.  
2. **Dual-Branch Camera Control**: This design ensures adherence to precise 6-DoF camera trajectories, enhancing the realism of generated videos.  
3. **Two-Stage Generation Pipeline**: The model employs a long-video refiner that processes stage-1 outputs, improving the quality and consistency of the generated sequences.  
4. **Robust Annotation Pipeline**: This pipeline extracts accurate metric-scale 6-DoF camera poses from public videos, providing high-quality, spatiotemporally consistent action labels for training.  

SANA-WM is trained on approximately 213K public video clips with metric-scale pose supervision, completing training in 15 days using 64 NVIDIA H100 GPUs. The model can generate a 60-second video clip on a single GPU, and its distilled variant can denoise a 60-second 720p clip in 34 seconds on an RTX 5090 with NVFP4 quantization.

**Results**  
SANA-WM demonstrates superior action-following accuracy compared to prior open-source baselines on its one-minute world-model benchmark. Notably, it achieves comparable visual quality to large-scale industrial models while operating at a throughput that is 36 times higher, indicating a significant improvement in efficiency. The paper does not provide specific numerical results or effect sizes against named baselines, which would be beneficial for a more detailed comparison.

**Limitations**  
The authors acknowledge that while SANA-WM improves efficiency and visual quality, it is still reliant on the quality of the public video clips used for training. The model's performance may degrade with lower-quality input data. Additionally, the paper does not address potential limitations in generalization to diverse environments or scenarios not represented in the training data. The reliance on specific hardware configurations (e.g., H100 GPUs) may also limit accessibility for broader applications.

**Why it matters**  
The development of SANA-WM has significant implications for scalable world modeling in AI-driven video synthesis. By achieving high visual fidelity and efficiency, it opens avenues for real-time applications in virtual reality, gaming, and simulation. The architectural innovations presented could inspire further research into hybrid attention mechanisms and efficient training paradigms, potentially influencing future models in the domain of generative video modeling.

Authors: Haoyi Zhu, Haozhe Liu, Yuyang Zhao, Tian Ye, Junsong Chen, Jincheng Yu, Tong He, Song Han et al.  
Source: arXiv:2605.15178  
URL: https://arxiv.org/abs/2605.15178v1
