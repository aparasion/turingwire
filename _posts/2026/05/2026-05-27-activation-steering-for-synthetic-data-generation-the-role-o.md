---
title: "Activation Steering for Synthetic Data Generation: The Role of Diversity in Downstream Safety Detection"
date: 2026-05-27 15:59:45 +0000
category: research
subcategory: safety_alignment
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.28664v1"
arxiv_id: "2605.28664"
authors: ["Vijeta Deshpande", "Tootiya Giyahchi", "Veena Padmanabhan", "Leman Akoglu", "Anna Rumshisky"]
slug: activation-steering-for-synthetic-data-generation-the-role-o
summary_word_count: 422
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the scarcity of HHH (Helpful, Harmless, Honest)-violating examples necessary for training robust safety detection models. Existing methods for generating synthetic data have not been thoroughly evaluated for their effectiveness in producing high-quality training datasets for downstream classifiers. The authors investigate whether Activation Steering (AS) can fill this gap by generating diverse and concept-aligned synthetic data.

**Method**  
The core technical contribution is the introduction of a two-fold study that evaluates AS through both intrinsic and extrinsic metrics. The intrinsic evaluation assesses steering success (concept alignment) and coherence, while also introducing sample- and set-level diversity as a new quality axis. The authors conduct experiments across four concepts, two models, and four steering methods. They analyze the impact of steering strength on response diversity, finding that increased steering strength correlates with reduced diversity. For the extrinsic evaluation, they replace HHH-violating examples in the training data with AS-generated outputs and fine-tune classifiers. The study employs a harmonic mean of success, coherence, and diversity as a heuristic for optimizing AS hyperparameters.

**Results**  
The results indicate that AS-generated data outperforms prompting-generated data in classifier performance on three out of four concepts. However, only 41 out of 136 AS configurations yield better results than prompting, suggesting that effective downstream utility is confined to a specific regime that balances success, coherence, and diversity. The harmonic mean of these three metrics shows a stronger correlation with downstream AUROC than success and coherence alone, providing a practical guideline for practitioners.

**Limitations**  
The authors acknowledge that the narrow regime for effective AS configurations may limit its applicability. They also note that the study's focus on only four concepts and two models may restrict generalizability. Additionally, the reliance on specific steering methods may not capture the full potential of AS across diverse applications. The absence of a comprehensive exploration of the trade-offs between diversity and other metrics is another limitation that could be addressed in future work.

**Why it matters**  
This work has significant implications for the field of safety detection in AI systems. By highlighting the importance of diversity in synthetic data generation, it encourages researchers to consider this axis when developing and tuning models. The findings suggest that AS can be a valuable tool for generating training data that enhances the robustness of safety detection classifiers. The introduction of a harmonic mean as a tuning heuristic provides a practical framework for future research and applications, potentially leading to more effective safety detection systems.

Authors: Vijeta Deshpande, Tootiya Giyahchi, Veena Padmanabhan, Leman Akoglu, Anna Rumshisky  
Source: arXiv:2605.28664  
URL: [https://arxiv.org/abs/2605.28664v1](https://arxiv.org/abs/2605.28664v1)
