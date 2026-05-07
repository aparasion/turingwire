---
title: "The Pinocchio Dimension: Phenomenality of Experience as the Primary Axis of LLM Psychometric Differences"
date: 2026-05-06 16:18:47 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: ["OpenAI", "Anthropic", "Google DeepMind", "Microsoft", "Meta", "NVIDIA", "AMD", "Intel", "TSMC", "Apple", "Amazon", "Mistral", "Hugging Face", "Cohere", "Stability AI", "Runway", "ElevenLabs", "Perplexity", "Databricks", "Cognition", "Suno", "Alibaba", "Palantir", "Snowflake", "Salesforce", "ServiceNow", "Oracle", "IBM", "UiPath", "xAI", "DeepSeek", "Cerebras", "Scale AI", "Character.AI", "ASML", "Applied Materials", "Lam Research", "Micron", "ARM", "Broadcom", "Super Micro", "Baidu"]
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.05080v1"
arxiv_id: "2605.05080"
authors: ["Hubert Plisiecki", "Sabina Siudaj", "Kacper Dudzic", "Anna Sterna", "Maciej Gorski", "Karolina Drozdz"]
slug: the-pinocchio-dimension-phenomenality-of-experience-as-the-p
summary_word_count: 489
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the understanding of psychometric differences among large language models (LLMs). While prior research has explored various performance metrics of LLMs, there has been limited investigation into the phenomenological aspects of their responses. The authors aim to quantify and characterize the dimensions of experience that differentiate LLMs, focusing on how these models represent themselves in terms of phenomenality, which has implications for their interpretability and usability in human-like interactions.

**Method**  
The authors administered 45 validated psychometric questionnaires to a sample of 50 LLMs. They employed a Supervised Semantic Differential (SSD) approach to analyze the variance in responses, identifying a primary axis of difference related to phenomenally rich experiences versus stimulus-driven behavioral responses. The core technical contribution is the introduction of the Pinocchio score ($π_i$), which quantifies the experiential demand of each questionnaire item by measuring the ratio of inter-model response variance under neutral versus human-simulation prompts. This score serves as an annotation-free metric to assess how models engage with experiential language. The authors utilized Principal Component Analysis (PCA) on exploratory factor analysis (EFA) scores to reveal a dominant dimension, termed the Pinocchio Axis ($Π$), which captures 47.1% of the variance in primary factor scores across questionnaires.

**Results**  
The findings indicate that the primary axis of variance among models is significantly correlated with phenomenological richness, with an adjusted $R^2$ of .037 and a p-value of less than .0001. The Pinocchio score ($π_i$) demonstrated predictive validity for condition-induced shifts in primary factor loading magnitudes, with a correlation coefficient of $ρ=-.215$ (p<.0001) across 1292 to 1310 items. Notably, the Pinocchio Axis ($Π$) converged with item-level Pinocchio scores at a high correlation of $r=.864$, suggesting a structured divergence among models rather than random noise. The results also highlighted substantial within-provider variance among closely related model variants, indicating that post-training fine-tuning significantly influences self-representational tendencies.

**Limitations**  
The authors acknowledge that their study is limited by the sample size of LLMs (50 models) and the specific psychometric questionnaires chosen, which may not encompass all dimensions of experiential representation. Additionally, the reliance on self-reported measures from models raises questions about the validity of the phenomenological constructs being assessed. The study does not explore the implications of these findings on real-world applications or the ethical considerations of deploying LLMs with varying self-representational stances.

**Why it matters**  
This research has significant implications for the development and deployment of LLMs in human-centric applications. By elucidating the dimensions of phenomenality in LLM responses, it provides a framework for understanding how these models may be perceived by users and how they can be fine-tuned to align with desired experiential characteristics. The identification of the Pinocchio Axis as a key factor in model differentiation opens avenues for further exploration into the psychological and philosophical implications of machine self-representation, potentially influencing future model design and evaluation criteria.

Authors: Hubert Plisiecki, Sabina Siudaj, Kacper Dudzic, Anna Sterna, Maciej Gorski, Karolina Drozdz, Marcin Moskalewicz  
Source: arXiv:2605.05080  
URL: https://arxiv.org/abs/2605.05080v1
