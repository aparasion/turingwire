---
title: "Towards LLM-Assisted Architecture Recovery for Real-World ROS~2 Systems: An Agent-Based Multi-Level Approach to Hierarchical Structural Architecture Reconstruction"
date: 2026-05-19 16:14:33 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.20055v1"
arxiv_id: "2605.20055"
authors: ["Dominique Briechle", "Raj Chanchad", "Tobias Geger", "Ruidi He", "Dhruv Jajadiya", "Dhruv Kapadiya"]
slug: towards-llm-assisted-architecture-recovery-for-real-world-ro
summary_word_count: 442
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in recovering hierarchical software architecture models for ROS~2-based robotic systems, where structural (de-)composition and integration semantics are often implicitly encoded across distributed artifacts. Existing methods primarily focus on node-level entities and communication wiring, lacking support for multi-level architectural recovery. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose an enhanced architecture recovery pipeline that builds upon their previous blueprint-guided LLM-assisted approach. The core contributions include:  
1. **Refined Prompting**: This technique improves the consistency and controllability of architecture synthesis by optimizing the input prompts given to the language model.  
2. **Staged Recovery Strategy**: This involves a multi-level approach that utilizes intermediate architectural representations, incorporating both the atomic ROS node list and launch file dependencies. This strategy enables a structurally constrained reconstruction process across various abstraction levels, facilitating a more comprehensive recovery of the system architecture.

The evaluation is conducted on a real-world automated product disassembly system, which features cooperative robotic arms and heterogeneous ROS~2 artifacts. The training compute specifics are not disclosed, but the enhancements are designed to handle increased integration complexity and richer functionality compared to prior work.

**Results**  
The proposed method demonstrates significant improvements over previous architecture recovery techniques. Key results include:  
- Enhanced structural consistency in the recovered architecture, as evidenced by qualitative assessments.  
- Improved scalability, allowing for the recovery of more complex systems without a proportional increase in error rates.  
- Increased robustness in architecture recovery, particularly in handling dynamic integration semantics.  
While specific numerical metrics are not provided, the qualitative improvements suggest a substantial effect size compared to baseline methods focused on simpler node-level recovery.

**Limitations**  
The authors acknowledge several limitations, including challenges related to dynamic integration semantics in large-scale ROS~2 systems, which may still hinder complete recovery in certain scenarios. Additionally, the reliance on LLMs may introduce variability based on the model's training data and inherent biases. The paper does not address potential scalability issues related to the computational resources required for processing larger systems or the generalizability of the approach to other software architectures outside of ROS~2.

**Why it matters**  
This work has significant implications for the field of software architecture recovery, particularly in robotic systems where complexity is increasing. By providing a more robust framework for hierarchical architecture reconstruction, it enables better communication, analysis, and evolution of complex software-intensive systems. The enhancements in consistency and scalability can facilitate more effective maintenance and evolution of ROS~2 systems, potentially influencing future research in automated software engineering and architecture recovery methodologies.

Authors: Dominique Briechle, Raj Chanchad, Tobias Geger, Ruidi He, Dhruv Jajadiya, Dhruv Kapadiya, Andreas Rausch, Meng Zhang  
Source: arXiv:2605.20055  
URL: https://arxiv.org/abs/2605.20055v1
