---
title: "Foundation Models to Unlock Real-World Evidence from Nationwide Medical Claims"
date: 2026-05-04 15:38:31 +0000
category: research
subcategory: foundation_models
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02740v1"
arxiv_id: "2605.02740"
authors: ["Fan Ma", "Yuntian Liu", "Xiang Lan", "Weipeng Zhou", "Jun Ni", "Mauro Giuffr\u00e8"]
slug: foundation-models-to-unlock-real-world-evidence-from-nationw
summary_word_count: 439
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the underutilization of administrative claims data as a foundation for healthcare models. While real-world evidence (RWE) from large-scale datasets is critical for regulatory and clinical decision-making, the potential of these datasets, particularly in the context of generative models, has not been fully explored. The authors aim to bridge this gap by leveraging a generative transformer model, ReClaim, trained on extensive medical claims data.

**Method**  
ReClaim is a generative transformer architecture trained from scratch on 43.8 billion medical events derived from the MarketScan claims database, encompassing over 200 million enrollees from 2008 to 2022. The model was scaled to three sizes: 140 million, 700 million, and 1.7 billion parameters. The training process involved modeling longitudinal trajectories of diagnoses, procedures, medications, and healthcare expenditures. The authors employed a variety of tasks, including over 1,000 disease-onset prediction tasks, to evaluate the model's performance. Notably, post-training fine-tuning was applied, resulting in a significant performance boost of 13.8 percentage points over pre-training alone.

**Results**  
ReClaim achieved a mean Area Under the Curve (AUC) of 75.6% across disease-onset prediction tasks, significantly outperforming the disease-specific LightGBM model (66.3%) and the transformer-based Delphi model (69.4%). The performance improvements were particularly pronounced for rare diseases. The model's efficacy was validated through both retrospective and prospective evaluations, as well as external validation on two independent datasets. In terms of healthcare expenditure forecasting, ReClaim increased the explained variance from 0.28 to 0.37 compared to LightGBM. Additionally, in a target trial emulation, it reduced systematic bias by an average of 72% relative to the Delphi model.

**Limitations**  
The authors acknowledge that the model's performance may be influenced by the quality and completeness of the underlying claims data. They also note that while the model shows promise in various applications, its generalizability to other healthcare systems or datasets remains to be fully established. Furthermore, the computational resources required for training such large models may limit accessibility for some researchers and institutions.

**Why it matters**  
This work has significant implications for the integration of machine learning in healthcare analytics. By demonstrating that administrative claims can serve as a robust substrate for foundation models, the authors pave the way for enhanced disease surveillance, more accurate expenditure forecasting, and improved RWE generation. The findings suggest that generative models can effectively capture complex longitudinal patterns in healthcare data, which could lead to better-informed clinical and policy decisions. This research could inspire further exploration of large-scale healthcare datasets and the development of more sophisticated models to address pressing healthcare challenges.

Authors: Fan Ma, Yuntian Liu, Xiang Lan, Weipeng Zhou, Jun Ni, Mauro Giuffrè, Lingfei Qian, Xueqing Peng et al.  
Source: arXiv:2605.02740  
URL: https://arxiv.org/abs/2605.02740v1
