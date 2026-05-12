---
title: "Grounded Satirical Generation with RAG"
date: 2026-05-11 17:00:51 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.10853v1"
arxiv_id: "2605.10853"
authors: ["Oona Itkonen", "Yuxin Su", "Linyao Du", "Ona De Gibert"]
slug: grounded-satirical-generation-with-rag
summary_word_count: 446
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding the generation of satirical content using Large Language Models (LLMs), particularly focusing on the contextual nature of satire. Existing models struggle with humor generation due to its subjective interpretation, and there is a lack of frameworks that effectively evaluate satirical outputs. The authors propose a novel approach to grounded satire generation that leverages current news as a contextual basis for producing satirical definitions, specifically within the Finnish cultural context.

**Method**  
The authors introduce a Retrieval-Augmented Generation (RAG) pipeline that integrates real-time news retrieval to inform the generation of satirical dictionary definitions. The architecture combines a retriever that fetches relevant news articles and a generator that synthesizes these inputs into satirical content. The evaluation framework is task-specific, involving the annotation of 100 generated definitions by six human annotators across various experimental conditions, including cultural background and source-word type. The training compute details are not disclosed, but the methodology emphasizes the importance of contextual grounding in satire generation.

**Results**  
The generated definitions were assessed for political relevance and humor. The findings indicate that while the outputs are perceived as more politically relevant when using topic-based word selection and RAG, there is no significant improvement in humor generation. Specifically, the authors report that LLMs correlate well with human judgments on political relevance (exact correlation metrics not provided), but they perform poorly in humor assessment. The study highlights that the generated content is predominantly viewed as political rather than humorous, suggesting a misalignment between the intended satirical output and the actual reception.

**Limitations**  
The authors acknowledge several limitations, including the subjective nature of humor, which complicates the evaluation process. They note that the reliance on human annotators may introduce bias, and the cultural specificity of the Finnish context may limit the generalizability of the findings. Additionally, the lack of clear gains in humor generation raises questions about the effectiveness of the proposed RAG approach in achieving its primary goal. The study does not explore the potential for cross-cultural satire generation, which could further enhance the applicability of the model.

**Why it matters**  
This work has significant implications for the development of LLMs in generating contextually relevant and culturally grounded content. By establishing a new evaluation framework and releasing an annotated dataset, the authors provide valuable resources for future research in humor generation and contextual language understanding. The findings suggest that while political relevance can be enhanced through RAG, further exploration is needed to bridge the gap between political commentary and humor, which could inform the design of more sophisticated models capable of producing nuanced satirical content.

Authors: Oona Itkonen, Yuxin Su, Linyao Du, Ona De Gibert  
Source: arXiv:2605.10853  
URL: [https://arxiv.org/abs/2605.10853v1](https://arxiv.org/abs/2605.10853v1)
