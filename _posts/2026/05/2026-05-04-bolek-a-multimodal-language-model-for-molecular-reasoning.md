---
title: "Bolek: A Multimodal Language Model for Molecular Reasoning"
date: 2026-05-04 15:46:39 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02745v1"
arxiv_id: "2605.02745"
authors: ["Frederic Grabowski", "Jacek Szczerbi\u0144ski", "Maciej Ja\u015bkowski", "Kalina Jasi\u0144ska-Kobus", "Pawe\u0142 D\u0105browski-Tuma\u0144ski", "Tomasz Jetka"]
slug: bolek-a-multimodal-language-model-for-molecular-reasoning
summary_word_count: 470
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the interpretability and auditability of molecular property models used in drug discovery. Traditional models provide scores without rationale, while existing language models (LMs) generate explanations that are often not well-grounded in molecular data. The authors present Bolek, a multimodal language model designed to enhance the interpretability of molecular reasoning by integrating molecular structure information directly into the reasoning process. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
Bolek is a compact multimodal language model that incorporates Morgan fingerprint embeddings into an instruction-tuned text decoder. The architecture leverages a fine-tuning process on molecular alignment tasks, which include molecule description, RDKit descriptor prediction, and substructure detection. The model is further trained on 15 binary classification tasks from the TDC (Toxicology Data Challenge) using synthetic chains-of-thought that are anchored in specific molecular features. The training compute details are not disclosed, but the model is noted to be less than half the size of the TxGemma-9B-Chat baseline, indicating a focus on efficiency without sacrificing performance.

**Results**  
Bolek demonstrates significant performance improvements over its Qwen3-4B-Instruct base model across all endpoints in yes/no mode and on 13 out of 15 tasks in chain-of-thought mode, achieving a mean ROC/PR AUC increase from 0.55 to 0.76. When compared to TxGemma-9B-Chat, Bolek outperforms it on 13 of 15 binary classification tasks, despite being less than half its size. The model's explanations are notably more grounded, citing numerical descriptors 10-100 times more frequently per chain-of-thought, with strong agreement with RDKit for key descriptors such as TPSA, MolLogP, and MolWt (Spearman rho = 0.87-0.91). Additionally, Bolek shows generalization capabilities, matching TxGemma on five unseen TDC classification endpoints and producing non-trivial rank correlations on three held-out regression endpoints, despite not being trained on regression tasks.

**Limitations**  
The authors acknowledge that while Bolek shows improved interpretability and performance, it is still limited by the scope of the training data and tasks. The model's performance on unseen data, while promising, may not generalize to all molecular contexts. Additionally, the reliance on synthetic chains-of-thought may not fully capture the complexity of real-world molecular reasoning scenarios. The paper does not discuss potential biases in the training data or the implications of model size on performance.

**Why it matters**  
The development of Bolek has significant implications for the field of molecular modeling and drug discovery. By providing a model that integrates molecular structure with natural language reasoning, Bolek enhances the auditability of predictions, which is crucial for high-stakes decision-making in drug development. The findings suggest that targeted modality injection and reasoning supervision can lead to more compact and interpretable models, paving the way for future research in multimodal AI applications in chemistry and beyond.

Authors: Frederic Grabowski, Jacek Szczerbiński, Maciej Jaśkowski, Kalina Jasińska-Kobus, Paweł Dąbrowski-Tumański, Tomasz Jetka, Bartosz Topolski  
Source: arXiv:2605.02745  
URL: https://arxiv.org/abs/2605.02745v1
