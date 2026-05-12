---
title: "Clin-JEPA: A Multi-Phase Co-Training Framework for Joint-Embedding Predictive Pretraining on EHR Patient Trajectories"
date: 2026-05-11 16:54:23 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.10840v1"
arxiv_id: "2605.10840"
authors: ["Yixuan Yang", "Mehak Arora", "Ryan Zhang", "Baraa Abed", "Junseob Kim", "Tilendra Choudhary"]
slug: clin-jepa-a-multi-phase-co-training-framework-for-joint-embe
summary_word_count: 481
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of effectively applying joint-embedding predictive (JEPA) pretraining to electronic health record (EHR) patient trajectories. Existing JEPA frameworks either discard the predictor post-pretraining or train it on a frozen encoder, which limits the encoder's ability to adapt to the predictive tasks. The authors propose Clin-JEPA, a multi-phase co-training framework that aims to stabilize the co-training of the encoder and predictor, thereby enabling a single backbone model to forecast patient trajectories and perform diverse downstream risk-prediction tasks without the need for per-task fine-tuning. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
Clin-JEPA employs a five-phase pretraining curriculum designed to mitigate common issues in co-training, such as representation collapse and online/target drift. The phases include: 
1. **Predictor Warmup**: Initial training of the predictor to establish a baseline.
2. **Joint Refinement**: Simultaneous training of the encoder and predictor to align their learning objectives.
3. **EMA Target Alignment**: Utilizing exponential moving averages to stabilize the target for the predictor.
4. **Hard Sync**: Enforcing tighter synchronization between the encoder and predictor.
5. **Predictor Finalization**: Final adjustments to the predictor to ensure optimal performance.

The architecture is based on a Qwen3-8B encoder and a 92M-parameter latent trajectory predictor. The training process leverages MIMIC-IV ICU data, focusing on the stability of the latent space during autoregressive rollout.

**Results**  
Clin-JEPA demonstrates significant improvements over baseline models in three independent evaluations on MIMIC-IV ICU data:
1. The latent $\ell_1$ rollout drift converges at -15.7% over 48-hour horizons, while baseline models diverge, showing increases ranging from +3% to +4951%.
2. The encoder achieves a clinically discriminative latent geometry, with deteriorating patient cohorts displacing 4.83× further in latent space compared to stable patients, while baseline encoders show displacements of ≤2.62×.
3. In multi-task downstream evaluations, Clin-JEPA achieves a mean AUROC of 0.851 on the ICareFM EEP benchmark and 0.883 on eight binary risk tasks, outperforming strong tabular and sequence baselines by +0.038 and +0.041, respectively.

**Limitations**  
The authors acknowledge potential limitations, including the reliance on the MIMIC-IV dataset, which may not generalize to other EHR datasets. Additionally, the complexity of the multi-phase training process may pose challenges in practical deployment. The paper does not address the computational cost associated with the extensive training phases or the scalability of the model to larger datasets.

**Why it matters**  
Clin-JEPA's framework has significant implications for the field of predictive modeling in healthcare. By enabling a single model to perform multiple tasks without fine-tuning, it streamlines the deployment of predictive analytics in clinical settings. The stability of the co-training process also suggests that similar approaches could be applied to other domains where joint learning from multiple tasks is beneficial, potentially leading to more robust and interpretable models in healthcare and beyond.

Authors: Yixuan Yang, Mehak Arora, Ryan Zhang, Baraa Abed, Junseob Kim, Tilendra Choudhary, Md Hassanuzzaman, Kevin Zhu et al.  
Source: arXiv:2605.10840  
URL: https://arxiv.org/abs/2605.10840v1
