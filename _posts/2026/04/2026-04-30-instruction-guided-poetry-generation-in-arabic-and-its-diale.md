---
title: "Instruction-Guided Poetry Generation in Arabic and Its Dialects"
date: 2026-04-30 11:58:13 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.27766v1"
arxiv_id: "2604.27766"
authors: ["Abdelrahman Sadallah", "Kareem Elozeiri", "Mervat Abassy", "Rania Elbadry", "Mohamed Anwar", "Abed Alhakim Freihat"]
slug: instruction-guided-poetry-generation-in-arabic-and-its-diale
summary_word_count: 480
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the capability of Large Language Models (LLMs) regarding the generation of poetry in Arabic and its dialects. While prior research has predominantly focused on analytical tasks related to Arabic poetry, such as interpretation and metadata prediction, there has been limited exploration into the creative generation of poetry. This work aims to fill that void by providing a framework for controllable poetry generation that aligns with user-defined criteria.

**Method**  
The authors introduce a large-scale, instruction-based dataset specifically curated for poetry generation in Modern Standard Arabic (MSA) and various Arabic dialects. The dataset includes tasks such as writing, revising, and continuing poems, guided by specific instructions related to style, rhyme, and thematic elements. The authors fine-tune existing LLMs on this dataset, employing a supervised learning approach to enhance the models' ability to generate poetry that meets user specifications. The training process involves leveraging a diverse set of prompts and examples to ensure the models can adapt to different poetic styles and dialects. The dataset and code are publicly available, facilitating reproducibility and further research.

**Results**  
The fine-tuned models demonstrate significant improvements in poetry generation capabilities compared to baseline models that were not specifically trained on the instruction-based dataset. The authors report that their models achieve a notable increase in performance on both automated metrics (e.g., BLEU, ROUGE) and human evaluations conducted with native Arabic speakers. While specific numerical results are not disclosed in the abstract, the qualitative feedback indicates that the generated poetry aligns well with user expectations, showcasing the effectiveness of the instruction-based approach.

**Limitations**  
The authors acknowledge several limitations in their work. Firstly, the dataset may not encompass the full diversity of Arabic dialects, potentially limiting the model's applicability across all Arabic-speaking regions. Additionally, the reliance on human evaluators introduces subjectivity, which may affect the consistency of the evaluation results. The authors also note that while the models perform well on the tasks defined in the dataset, they may struggle with more abstract or nuanced poetic forms that require deeper cultural or contextual understanding. Furthermore, the work does not address the computational costs associated with fine-tuning large models, which may be prohibitive for some researchers.

**Why it matters**  
This research has significant implications for the field of natural language processing, particularly in the context of culturally rich languages like Arabic. By enabling controllable poetry generation, the work opens avenues for creative applications in education, cultural preservation, and artistic expression. It also sets a precedent for future research on instruction-based datasets in other languages and domains, potentially leading to advancements in generative models that can cater to specific user needs. The availability of the dataset and code encourages further exploration and innovation in the intersection of AI and creative writing.

Authors: Abdelrahman Sadallah, Kareem Elozeiri, Mervat Abassy, Rania Elbadry, Mohamed Anwar, Abed Alhakim Freihat, Preslav Nakov, Fajri Koto  
Source: arXiv cs.CL  
URL: https://arxiv.org/abs/2604.27766v1
