---
title: "ATLAS: Article Tracking, Linking, and Analysis of Swedish Encyclopedias"
date: 2026-05-04 11:08:59 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.02466v1"
arxiv_id: "2605.02466"
authors: ["Albin Andersson", "Salam Jonasson", "Fredrik Wastring", "Pierre Nugues"]
slug: atlas-article-tracking-linking-and-analysis-of-swedish-encyc
summary_word_count: 458
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the digitization of historical encyclopedias, specifically focusing on the Swedish encyclopedia *Nordisk familjebok*. Traditional digitization methods often rely solely on optical character recognition (OCR), neglecting the underlying structural information that is crucial for knowledge tracking and evolution analysis across multiple editions. The authors aim to develop a comprehensive pipeline that not only digitizes but also structures and links the content of these encyclopedias, thereby enhancing access to historically significant knowledge.

**Method**  
The authors propose a multi-step pipeline for processing the encyclopedia entries. The pipeline includes the following components: 

1. **Headword Extraction**: Identifying and extracting headwords from the text.
2. **Entry Categorization**: Classifying the extracted entries into predefined categories.
3. **Cross-Edition Matching**: Establishing correspondences between entries across different editions of the encyclopedia.
4. **Wikidata Linking**: Associating entries with relevant Wikidata items to enrich the contextual information.

The authors report an F1 score of 97.8% for headword extraction and 93.4% for headword classification. For cross-edition matching, they achieved a precision of 93%, while the Wikidata linking yielded 85% precision and 16.5% recall. The implementation details regarding the architecture, loss functions, and training compute are not disclosed, but the results indicate a robust automated approach to structuring historical knowledge.

**Results**  
The pipeline demonstrated high efficacy in extracting and classifying headwords, with F1 scores of 97.8% and 93.4%, respectively. The cross-edition matching precision was reported at 93%, indicating a strong capability to identify corresponding entries across different editions. However, the Wikidata linking performance was less robust, with an 85% precision but only 16.5% recall, suggesting that while many entries can be accurately linked, a significant number remain unlinked. These results were evaluated on the four major editions of *Nordisk familjebok*, showcasing the pipeline's effectiveness on a historically significant dataset.

**Limitations**  
The authors acknowledge that the recall for Wikidata linking is notably low, which may limit the comprehensiveness of the knowledge representation. Additionally, the study is constrained by the specific dataset of *Nordisk familjebok*, which may not generalize to other encyclopedias or historical texts. The lack of detailed information on the computational resources and specific algorithms used in the pipeline also presents a limitation for reproducibility and further research.

**Why it matters**  
This work has significant implications for the digitization and preservation of historical knowledge. By providing a structured approach to the content of encyclopedias, it facilitates better access to historical data and enhances the understanding of knowledge evolution over time. The automated pipeline can serve as a model for similar projects involving other historical texts, potentially leading to a broader application in the field of digital humanities. The availability of datasets and programs online further encourages collaboration and innovation in this area.

Authors: Albin Andersson, Salam Jonasson, Fredrik Wastring, Pierre Nugues  
Source: arXiv:2605.02466  
URL: [https://arxiv.org/abs/2605.02466v1](https://arxiv.org/abs/2605.02466v1)
