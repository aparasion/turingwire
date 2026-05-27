---
title: "FineVLA: Fine-Grained Instruction Alignment for Steerable Vision-Language-Action Policies"
date: 2026-05-26 17:01:10 +0000
category: research
subcategory: agents_robotics
company: "ARM"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.27284v1"
arxiv_id: "2605.27284"
authors: ["Xintong Hu", "Xuhong Huang", "Jinyu Zhang", "Yutong Yao", "Yuchong Sun", "Qiuyue Wang"]
slug: finevla-fine-grained-instruction-alignment-for-steerable-vis
summary_word_count: 421
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in existing Vision-Language-Action (VLA) models, which typically rely on coarse goal-level language for robot task execution. The lack of fine-grained instruction details—such as the specific arm to use, approach direction, and contact region—limits the effectiveness of steerable policy learning and robotic video understanding. The authors present FineVLA, an open framework designed to provide action-aligned fine-grained VLA supervision. This work is a preprint and has not yet undergone peer review.

**Method**  
FineVLA comprises several key components:  
1. **Data Construction Tool**: It integrates 972,247 trajectories from 85,000 tasks across 10 open-source robot datasets, resulting in FineVLA-Data, which includes 47,159 human-verified fine-grained trajectories.  
2. **Benchmark**: A held-out benchmark is introduced, featuring 500 videos, 10,816 atomic facts, and 1,030 Visual Question Answering (VQA) questions.  
3. **VLM Annotator**: A robotics-specialized Vision-Language Model (VLM) annotator is developed for scalable fine-grained annotation.  
4. **Steerable VLA Policy**: The policy is trained using controlled mixtures of fine-grained and raw goal-level instructions, allowing for a nuanced approach to task execution.

**Results**  
The experiments yield significant findings:  
- Fine-grained supervision enhances performance without sacrificing goal-level success, with improvements ranging from +1.4 to +8.1 percentage points in success rates across various settings when comparing Fine-Grained (FG) only to Raw (goal-level) only.  
- The combination of fine-grained and raw instructions shows complementary effects, peaking at a ratio of FG:Raw = 1:2 to 1:1. The optimal mixed setting achieves success rates of 86.8% in RoboTwin simulation and 62.7% in real-world dual-arm manipulation, compared to 49.9% for Raw-only.  
- Fine-grained supervision significantly enhances steerable control, with the largest real-world gains observed in pose (+23), color (+18), and approach direction (+18)—areas where goal-level instructions provide no guidance.

**Limitations**  
The authors acknowledge that while fine-grained supervision improves task execution, the framework's reliance on human-verified data may limit scalability. Additionally, the performance gains are context-dependent, and the optimal FG:Raw ratio may vary across different tasks. The paper does not address potential biases in the human-verified dataset or the generalizability of the findings to other robotic platforms.

**Why it matters**  
The implications of this work are substantial for the field of robotics and AI. By demonstrating that fine-grained instructions can significantly enhance the performance of VLA models, this research paves the way for more sophisticated human-robot interaction paradigms. It suggests that future work should focus on integrating fine-grained language alongside goal-level instructions to improve task execution and adaptability in dynamic environments.

Authors: Xintong Hu, Xuhong Huang, Jinyu Zhang, Yutong Yao, Yuchong Sun, Qiuyue Wang, Mingsheng Li, Sicheng Xie et al.  
Source: arXiv:2605.27284  
URL: [https://arxiv.org/abs/2605.27284v1](https://arxiv.org/abs/2605.27284v1)
