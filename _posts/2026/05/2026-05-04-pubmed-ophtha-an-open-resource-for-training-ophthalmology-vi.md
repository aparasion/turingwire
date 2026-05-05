---
title: "PubMed-Ophtha: An open resource for training ophthalmology vision-language models on scientific literature"
date: 2026-05-04 15:19:42 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.02720v1"
arxiv_id: "2605.02720"
authors: ["Verena Jasmin Hallitschke", "Carsten Eickhoff", "Philipp Berens"]
slug: pubmed-ophtha-an-open-resource-for-training-ophthalmology-vi
summary_word_count: 466
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the significant gap in high-quality, large-scale image-text datasets specifically tailored for training vision-language models in the field of ophthalmology. Existing datasets are limited in scope and quality, hindering the development of robust models that can effectively interpret and generate insights from ophthalmological literature. The authors introduce PubMed-Ophtha, a comprehensive dataset designed to facilitate advancements in this domain.

**Method**  
The core technical contribution is the creation of the PubMed-Ophtha dataset, which comprises 102,023 ophthalmological image-caption pairs sourced from 15,842 open-access articles in PubMed Central. The dataset is notable for its hierarchical structure, where figures are extracted directly from article PDFs at full resolution. The extraction process decomposes figures into constituent panels, each annotated with imaging modalities (e.g., color fundus photography, optical coherence tomography) and mark statuses indicating the presence of annotation marks. The authors employ a two-step large language model (LLM) approach to split figure captions into panel-level subcaptions, achieving a mean average sentence BLEU score of 0.913 on human-annotated data. Additionally, the performance of panel and image detection models is quantified, achieving a mean Average Precision (mAP) at IoU 0.50 of 0.909 and 0.892, respectively. The figure extraction process demonstrates a median Intersection over Union (IoU) of 0.997. The authors also provide the human-annotated ground-truth data, all trained models, and the complete dataset generation pipeline to ensure reproducibility.

**Results**  
The dataset's extraction and annotation methods yield high-quality results, with the panel detection model achieving an mAP of 0.909 and the image detection model achieving an mAP of 0.892. The figure extraction process shows a median IoU of 0.997, indicating exceptional accuracy in identifying and segmenting figures from the source articles. These results are benchmarked against existing methodologies, demonstrating superior performance in both image and caption extraction tasks.

**Limitations**  
The authors acknowledge that while the dataset is extensive, it is limited to open-access articles from PubMed Central, which may not encompass the entirety of ophthalmological literature. Additionally, the reliance on LLMs for caption splitting may introduce biases based on the training data of the models used. The authors do not discuss potential limitations related to the generalizability of the models trained on this dataset to real-world clinical scenarios or the potential for overfitting due to dataset size.

**Why it matters**  
The introduction of PubMed-Ophtha has significant implications for the development of vision-language models in ophthalmology. By providing a high-quality, structured dataset, this work enables researchers to train models that can better understand and generate insights from complex ophthalmological data. This advancement could lead to improved diagnostic tools, enhanced research capabilities, and ultimately better patient outcomes in the field of ophthalmology. The release of the dataset and associated resources promotes reproducibility and encourages further research in multimodal learning applications within medical domains.

Authors: Verena Jasmin Hallitschke, Carsten Eickhoff, Philipp Berens  
Source: arXiv:2605.02720  
URL: [https://arxiv.org/abs/2605.02720v1](https://arxiv.org/abs/2605.02720v1)
