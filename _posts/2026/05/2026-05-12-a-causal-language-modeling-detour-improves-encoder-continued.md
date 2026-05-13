---
title: "A Causal Language Modeling Detour Improves Encoder Continued Pretraining"
date: 2026-05-12 17:34:00 +0000
category: research
subcategory: training_methods
company: "null"
secondary_companies: ["OpenAI", "Google", "Microsoft"]
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.12438v1"
arxiv_id: "2605.12438"
authors: ["Rian Touchent", "Eric de la Clergerie"]
slug: a-causal-language-modeling-detour-improves-encoder-continued
summary_word_count: 444
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding the adaptation of encoder models to new domains, specifically in the context of biomedical text. The standard practice of continuing training with Masked Language Modeling (MLM) may not fully leverage the potential of encoder architectures. The authors propose a novel approach that incorporates a temporary switch to Causal Language Modeling (CLM) during continued pretraining, aiming to enhance downstream task performance.

**Method**  
The core technical contribution is the introduction of a CLM detour in the continued pretraining of encoder models, specifically ModernBERT, on biomedical datasets. The authors implement a training regimen where the model first undergoes CLM for a specified duration, followed by a decay phase of MLM. The experiments are conducted on both French and English biomedical tasks, with the model sizes categorized as Base and Large. The training compute is not explicitly disclosed, but the authors ensure that the data and compute resources are identical across the MLM and CLM phases. The study also investigates the impact of freezing different transformer layers during the CLM phase, revealing that freezing low layers negates the performance gains, while freezing mid layers retains them.

**Results**  
The CLM detour demonstrates significant improvements over standard MLM baselines. On French biomedical tasks, the CLM approach yields performance enhancements ranging from +1.2 to +2.8 percentage points (pp), while for English tasks, the improvements range from +0.3 to +0.8 pp. These results are quantified against named baselines, indicating that the CLM detour effectively enhances the model's ability to generalize across various biomedical tasks. The authors also release two new models, ModernCamemBERT-bio and ModernBERT-bio, which achieve state-of-the-art performance in their respective categories.

**Limitations**  
The authors acknowledge that the study is limited to biomedical texts and may not generalize to other domains without further validation. Additionally, the impact of the CLM detour on different model architectures beyond ModernBERT is not explored. The authors do not discuss potential overfitting issues that may arise from the additional training phase or the computational cost implications of the proposed method.

**Why it matters**  
This work has significant implications for the field of transfer learning in NLP, particularly in specialized domains like biomedicine. By demonstrating that a CLM detour can enhance the representational capacity of encoder models, the findings encourage further exploration of hybrid training strategies that combine different modeling paradigms. The persistence of representational changes through the MLM decay phase suggests that such techniques could be beneficial in other contexts, potentially leading to more robust and adaptable language models. The release of state-of-the-art biomedical encoders also provides valuable resources for researchers and practitioners in the field.

Authors: Rian Touchent, Eric de la Clergerie  
Source: arXiv:2605.12438  
URL: https://arxiv.org/abs/2605.12438v1
