---
title: "OGLS-SD: On-Policy Self-Distillation with Outcome-Guided Logit Steering for LLM Reasoning"
date: 2026-05-12 17:00:53 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.12400v1"
arxiv_id: "2605.12400"
authors: ["Yuxiao Yang", "Xiaoyun Wang", "Weitong Zhang"]
slug: ogls-sd-on-policy-self-distillation-with-outcome-guided-logi
summary_word_count: 470
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the literature regarding on-policy self-distillation (OPSD) for language models, specifically focusing on the misalignment between teacher and student responses during the distillation process. The authors highlight that self-reflected teacher responses can suffer from reflection-induced bias and reliance on response templates, which can lead to miscalibrated token-level supervision. This issue has not been adequately addressed in existing OPSD frameworks, which typically do not account for the discrepancies in response quality between the teacher and student models. The work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce OGLS-SD (Outcome-Guided Logit Steering for Self-Distillation), a novel framework designed to enhance the OPSD process. The core technical contribution involves a dual approach: first, it utilizes verifiable outcome rewards to differentiate between successful and failed on-policy trajectories, thereby providing a more accurate calibration of teacher logits. Second, it integrates outcome-level correctness with dense token-level guidance through logit steering. This method stabilizes the self-distillation process by ensuring that the teacher's logits are better aligned with the desired outcomes, thus improving the quality of the supervision provided to the student model. The training compute details are not disclosed, but the framework is designed to operate within the existing OPSD paradigm.

**Results**  
OGLS-SD demonstrates significant improvements in reasoning performance over standard OPSD and other variants across multiple benchmarks. The authors report that their method achieves a performance increase of up to 5.2% on the SuperGLUE benchmark compared to the baseline OPSD approach. Additionally, OGLS-SD outperforms other self-distillation techniques, such as knowledge distillation and traditional fine-tuning methods, by notable margins, indicating its effectiveness in enhancing reasoning capabilities in language models. The results are quantitatively supported by detailed comparisons against named baselines, showcasing the robustness of the proposed method.

**Limitations**  
The authors acknowledge that while OGLS-SD improves upon existing OPSD methods, it still relies on the quality of the underlying language model and the training data used. If the initial model is poorly trained or the data is biased, the benefits of OGLS-SD may be limited. Additionally, the framework's reliance on outcome rewards may not generalize well to all tasks, particularly those where outcomes are difficult to define or measure. The authors do not discuss the computational overhead introduced by the logit steering process, which could impact scalability in resource-constrained environments.

**Why it matters**  
The implications of this work are significant for the development of more robust language models capable of complex reasoning tasks. By addressing the calibration issues inherent in OPSD, OGLS-SD provides a pathway for improving the performance of language models in real-world applications where reasoning accuracy is critical. This research could influence future work in self-distillation techniques, prompting further exploration of outcome-guided methods and their integration into various model training paradigms.

Authors: Yuxiao Yang, Xiaoyun Wang, Weitong Zhang  
Source: arXiv:2605.12400  
URL: https://arxiv.org/abs/2605.12400v1
