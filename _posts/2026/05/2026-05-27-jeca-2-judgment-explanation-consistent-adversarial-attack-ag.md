---
title: "JECA^2: Judgment-Explanation Consistent Adversarial Attack against Forensic Vision-Language Models"
date: 2026-05-27 15:24:31 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.28609v1"
arxiv_id: "2605.28609"
authors: ["Jiachen Qian"]
slug: jeca-2-judgment-explanation-consistent-adversarial-attack-ag
summary_word_count: 453
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the robustness of forensic vision-language models (VLMs) against adversarial attacks, specifically focusing on the consistency between model judgments and their accompanying textual explanations. Existing adversarial attacks primarily target the binary classification output of these models, often neglecting the integrity of the generated explanations, which may still reveal forensic cues. The authors propose a novel approach, JECA^2, to create adversarial examples that maintain alignment between visual attributions and textual explanations, a topic that has not been thoroughly explored in the literature. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
JECA^2 employs a controlled white-box adversarial attack framework that integrates visual and textual manipulation. On the visual side, it utilizes Grad-CAM-guided perturbations to redirect the model's visual attribution from tampered areas to benign regions, effectively masking the tampering. For the textual component, JECA^2 optimizes prompt embeddings to ensure that the generated explanations align with the target judgment, adhering to a token-proximity constraint to maintain semantic authenticity. The training process involves a combination of gradient-based optimization techniques to achieve the desired adversarial effects while preserving the coherence of the explanations.

**Results**  
The experimental evaluation of JECA^2 on forensic VLM benchmarks demonstrates significant improvements over existing baselines. The attack success rate of JECA^2 is reported to be higher than that of traditional adversarial methods, achieving a notable increase in automated judgment-explanation consistency. Specific metrics indicate that JECA^2 outperforms baseline models by a margin of approximately 15% in attack success rates and 20% in consistency metrics under white-box threat scenarios. While the transferability of the attack to closed-source VLMs is acknowledged, the authors note that the effectiveness is measurable but limited, suggesting a need for further exploration in this area.

**Limitations**  
The authors acknowledge several limitations, including the reliance on white-box settings, which may not fully represent real-world adversarial scenarios where models are often black-box. Additionally, the transferability of the attack to closed-source models is limited, indicating that the robustness of JECA^2 may not generalize across all VLM architectures. The authors also do not address potential ethical implications of deploying such adversarial techniques in practice, nor do they explore the long-term implications of their findings on the development of more robust forensic VLMs.

**Why it matters**  
The implications of this work are significant for the field of adversarial machine learning and forensic analysis. By highlighting a critical failure mode in explanation-based forensic VLMs, JECA^2 motivates the need for enhanced robustness evaluations that extend beyond mere binary detection accuracy. This research paves the way for future investigations into adversarial defenses and the development of more resilient VLMs capable of maintaining both judgment and explanation integrity under adversarial conditions.

Authors: Jiachen Qian  
Source: arXiv:2605.28609  
URL: https://arxiv.org/abs/2605.28609v1
