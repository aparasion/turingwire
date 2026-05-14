---
title: "RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data"
date: 2026-05-13 16:54:36 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.13775v1"
arxiv_id: "2605.13775"
authors: ["Harold Haodong Chen", "Sirui Chen", "Yingjie Xu", "Wenhang Ge", "Ying-Cong Chen"]
slug: roboevolve-co-evolving-planner-simulator-for-robotic-manipul
summary_word_count: 433
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the critical gap in robotic manipulation scalability due to the limited availability of task-aligned physical interaction data. Existing approaches, such as vision-language models (VLMs) and video generation models (VGMs), struggle with semantic-spatial misalignment and physical hallucinations, which hinder their effectiveness in generating reliable training data for robotic tasks. The authors propose RoboEvolve as a solution to synthesize high-quality interaction data through a co-evolutionary framework that integrates planning and simulation.

**Method**  
RoboEvolve introduces a dual-phase mechanism that operates on unlabeled seed images. The framework consists of two main components: a VLM planner and a VGM simulator, which engage in a mutually reinforcing loop. During the "daytime" phase, the system explores the environment to discover physically grounded behaviors using a semantic-controlled multi-granular reward structure. In the "nighttime" phase, it consolidates learning by analyzing "near-miss" failures to enhance policy optimization. The training process is guided by an autonomous progressive curriculum that allows the system to scale from simple atomic actions to more complex tasks. The architecture's data efficiency is highlighted by its ability to achieve significant performance improvements with only 500 unlabeled seed images, representing a 50x reduction compared to fully supervised methods.

**Results**  
RoboEvolve demonstrates substantial improvements over baseline methods. Specifically, it elevates the performance of base planners by 30 absolute points and increases simulator success rates by an average of 48%. These results were achieved on various benchmarks, showcasing the framework's effectiveness in both planning and simulation tasks. The authors emphasize that RoboEvolve's data efficiency allows it to outperform fully supervised baselines, achieving comparable results with significantly fewer training samples.

**Limitations**  
The authors acknowledge several limitations, including the reliance on unlabeled seed images, which may not cover the full spectrum of task scenarios. Additionally, while the framework shows robust continual learning capabilities, the potential for catastrophic forgetting in more complex environments remains a concern. The paper does not address the computational overhead associated with the dual-phase mechanism, which may impact scalability in real-world applications.

**Why it matters**  
RoboEvolve's innovative approach to co-evolving planning and simulation has significant implications for the field of robotic manipulation. By effectively synthesizing interaction data with minimal labeled input, it paves the way for more scalable and efficient training methodologies. This work could inspire further research into hybrid models that leverage the strengths of VLMs and VGMs while addressing their inherent limitations. The framework's ability to facilitate continual learning without catastrophic forgetting also opens avenues for developing more adaptive robotic systems capable of learning from ongoing interactions in dynamic environments.

Authors: Harold Haodong Chen, Sirui Chen, Yingjie Xu, Wenhang Ge, Ying-Cong Chen  
Source: arXiv:2605.13775  
URL: [https://arxiv.org/abs/2605.13775v1](https://arxiv.org/abs/2605.13775v1)
