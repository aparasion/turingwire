---
title: "Translating Under Pressure: Domain-Aware LLMs for Crisis Communication"
date: 2026-04-29 12:27:56 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26597v1"
arxiv_id: "2604.26597"
authors: ["Antonio Castaldo", "Maria Carmen Staiano", "Johanna Monti", "Sheila Castilho", "Francesca Chiusaroli"]
slug: translating-under-pressure-domain-aware-llms-for-crisis-comm
summary_word_count: 421
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the critical gap in effective multilingual communication during crises, where timely and reliable information dissemination is paramount. The authors highlight the challenge posed by the scarcity of curated parallel datasets specifically tailored for crisis communication, which limits the development of robust translation systems in emergency contexts. 

**Method**  
The authors propose a domain-adaptive pipeline that enhances a limited reference corpus by retrieving and filtering relevant data from general corpora. This approach involves several key steps: first, they expand the dataset through data retrieval techniques, ensuring that the additional data is pertinent to crisis scenarios. Next, they fine-tune a small language model specifically for crisis-domain translation. The model is then optimized using preference optimization techniques to bias the outputs towards CEFR A2-level English, which is characterized by simplified language suitable for non-native speakers. The training compute details are not disclosed, but the methodology emphasizes the importance of domain adaptation and readability in the translation outputs.

**Results**  
The proposed method demonstrates significant improvements in both automatic and human evaluations compared to baseline models. The authors report that their domain-adaptive approach yields a notable increase in readability scores while maintaining strong adequacy in translation. Specific metrics or numerical improvements over named baselines are not provided in the summary, but the qualitative assessments indicate that the model effectively serves as a practical lingua franca for emergency communication, particularly when comprehensive multilingual coverage is not achievable.

**Limitations**  
The authors acknowledge several limitations, including the reliance on a small reference corpus, which may not capture the full diversity of crisis communication scenarios. Additionally, the effectiveness of the model may vary across different languages and contexts, as the training data is primarily derived from general corpora. The potential for bias in the retrieved data and the simplification process could also lead to loss of nuanced information in translations. Notably, the authors do not discuss the computational efficiency or scalability of their approach, which could be critical in real-time crisis situations.

**Why it matters**  
This work has significant implications for the field of crisis communication, particularly in enhancing the accessibility of information during emergencies. By demonstrating that simplified English, combined with domain adaptation, can effectively serve as a communication bridge, the authors provide a framework that can be leveraged in future research and practical applications. This approach could inform the development of more robust multilingual systems that prioritize clarity and comprehension, ultimately improving the efficacy of communication in high-stakes environments.

Authors: Antonio Castaldo, Maria Carmen Staiano, Johanna Monti, Sheila Castilho, Francesca Chiusaroli  
Source: arXiv:2604.26597  
URL: https://arxiv.org/abs/2604.26597v1
