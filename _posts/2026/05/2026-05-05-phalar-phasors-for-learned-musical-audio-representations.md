---
title: "PHALAR: Phasors for Learned Musical Audio Representations"
date: 2026-05-05 16:19:58 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.03929v1"
arxiv_id: "2605.03929"
authors: ["Davide Marincione", "Michele Mancusi", "Giorgio Strano", "Luca Cerovaz", "Donato Crisostomi", "Roberto Ribuoli"]
slug: phalar-phasors-for-learned-musical-audio-representations
summary_word_count: 471
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing models in stem retrieval, specifically their inability to effectively utilize temporal information. The authors highlight that current approaches often overlook the significance of phase and pitch information in audio representations, which hampers performance in matching missing audio stems to submixes. This work is presented as a preprint, indicating that it has not yet undergone peer review.

**Method**  
The core technical contribution of this work is the PHALAR framework, which employs a contrastive learning approach to enhance stem retrieval accuracy. PHALAR integrates a Learned Spectral Pooling layer and a complex-valued head, which together enforce pitch-equivariant and phase-equivariant biases in the model. This architecture allows for a more nuanced representation of musical audio, capturing essential temporal and spectral features. The authors report that PHALAR achieves a relative accuracy increase of approximately 70% over the state-of-the-art while utilizing less than 50% of the parameters and achieving a 7× speedup in training time. The training compute specifics are not disclosed, but the efficiency gains suggest a significant reduction in resource requirements compared to previous models.

**Results**  
PHALAR establishes new state-of-the-art performance on multiple benchmarks, including MoisesDB, Slakh, and ChocoChorales. The model demonstrates a substantial improvement in retrieval accuracy, achieving a relative increase of up to 70% compared to existing methods. Additionally, PHALAR correlates significantly higher with human coherence judgments than semantic baselines, indicating its effectiveness in capturing the nuances of musical structure. The authors also report successful zero-shot beat tracking and linear chord probing, further validating the model's ability to generalize beyond the primary retrieval task.

**Limitations**  
The authors acknowledge that while PHALAR shows significant improvements, it may still be limited by the quality and diversity of the training data used for contrastive learning. They do not discuss potential issues related to the generalizability of the model across different genres or styles of music, nor do they address the computational overhead that may arise from the complex-valued operations in the architecture. Additionally, the reliance on human coherence judgments for evaluation may introduce subjectivity into the assessment of model performance.

**Why it matters**  
The implications of this work are substantial for the field of music information retrieval and audio processing. By effectively leveraging phase and pitch information, PHALAR sets a new benchmark for stem retrieval tasks, which could enhance applications in music production, remixing, and automated audio editing. The framework's ability to generalize to other musical tasks, as evidenced by its performance in zero-shot scenarios, suggests that it could serve as a foundational model for future research in learned audio representations. This work opens avenues for further exploration of complex-valued neural networks in audio applications, potentially leading to more sophisticated models that can better understand and manipulate musical content.

Authors: Davide Marincione, Michele Mancusi, Giorgio Strano, Luca Cerovaz, Donato Crisostomi, Roberto Ribuoli, Emanuele Rodolà  
Source: arXiv:2605.03929  
URL: https://arxiv.org/abs/2605.03929v1
