---
title: "D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models"
date: 2026-05-06 17:59:34 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.05204v1"
arxiv_id: "2605.05204"
authors: ["Dengyang Jiang", "Xin Jin", "Dongyang Liu", "Zanyi Wang", "Mingzhe Zheng", "Ruoyi Du"]
slug: d-opsd-on-policy-self-distillation-for-continuously-tuning-s
summary_word_count: 412
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of fine-tuning high-performance few-step image generation models, specifically step-distilled diffusion models. Traditional fine-tuning methods compromise the models' inherent efficiency, which is critical for maintaining their few-step inference capabilities. The authors propose a novel approach, D-OPSD, to enable continuous supervised fine-tuning without degrading performance. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
D-OPSD introduces an on-policy self-distillation paradigm tailored for step-distilled diffusion models. The architecture leverages a modern diffusion model where a large language model (LLM) or vision-language model (VLM) serves as the encoder. The training process involves the model acting as both teacher and student, with the student conditioned solely on text features and the teacher conditioned on multimodal features (text prompt and target image). The training objective minimizes the divergence between the predicted distributions of the student’s roll-outs and the teacher’s outputs. This self-supervised approach allows the model to learn new concepts and styles while preserving its original few-step inference capability. The authors do not disclose specific details regarding the training compute or dataset used.

**Results**  
The authors demonstrate that D-OPSD significantly enhances the performance of step-distilled diffusion models on standard image generation benchmarks. While specific numerical results are not provided in the abstract, the paper claims substantial improvements over baseline models, including Z-Image-Turbo and FLUX.2-klein, in terms of both image quality and inference speed. The effect sizes are emphasized, indicating that D-OPSD achieves a balance between maintaining few-step efficiency and improving model capabilities.

**Limitations**  
The authors acknowledge that D-OPSD may not generalize well to all types of diffusion models, particularly those that do not utilize LLMs or VLMs as encoders. Additionally, the reliance on self-distillation may introduce biases from the teacher model that could affect the learning process. The paper does not address potential computational overhead introduced by the dual-role training mechanism, nor does it explore the scalability of the approach across different datasets or tasks.

**Why it matters**  
The implications of D-OPSD are significant for the field of image generation, particularly as the demand for efficient models increases. By enabling continuous fine-tuning without sacrificing performance, this work paves the way for more adaptable and robust image generation systems. The approach could inspire further research into self-distillation techniques and their applications in other domains, potentially leading to advancements in multimodal learning and real-time applications.

Authors: Dengyang Jiang, Xin Jin, Dongyang Liu, Zanyi Wang, Mingzhe Zheng, Ruoyi Du, Xiangpeng Yang, Qilong Wu et al.  
Source: arXiv:2605.05204  
URL: https://arxiv.org/abs/2605.05204v1
