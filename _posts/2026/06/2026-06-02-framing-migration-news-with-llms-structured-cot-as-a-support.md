---
title: "Framing Migration News with LLMs: Structured CoT as a Support for Human Interpretation"
date: 2026-06-02 15:15:39 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.03761v1"
arxiv_id: "2606.03761"
authors: ["David Alonso del Barrio", "Jing Wen", "Daniel Gatica-Perez"]
slug: framing-migration-news-with-llms-structured-cot-as-a-support
summary_word_count: 403
classification_confidence: 0.80
source_truncated: false
layout: post
description: "This paper presents a Structured Chain-of-Thought prompting method for local LLMs to enhance interpretability in migration news frame analysis."
---

**Problem**  
This work addresses the gap in the availability of interpretable and accessible tools for frame analysis of migration news, particularly for media scholars and researchers. Existing approaches predominantly rely on proprietary large language models (LLMs) that raise concerns regarding data privacy, reproducibility, and equitable access. The authors highlight the need for a locally deployable, open-source solution that can facilitate transparent and auditable analysis within the constraints of typical academic research resources. This paper is a preprint and has not undergone peer review.

**Method**  
The authors introduce a Structured Chain-of-Thought (SCoT) prompting technique utilizing the Llama3-8B model. The SCoT approach is designed to provide step-by-step justifications based on predefined framing categories, allowing users to trace the model's reasoning and explore alternative interpretations. The model is trained and evaluated on a dataset of migration-related news articles, focusing on its ability to classify frames effectively. The training is conducted on a single GPU, ensuring feasibility for academic settings. The evaluation includes both quantitative performance metrics against zero-shot and few-shot baselines, as well as qualitative assessments from human annotators regarding the coherence and influence of the model's reasoning.

**Results**  
The SCoT method demonstrates improved classification performance compared to zero-shot and few-shot baselines, although specific numerical results are not disclosed in the summary. In a human-centered evaluation, annotators rated the coherence of the model's reasoning with a mean score of 4.1 out of 5, indicating a generally positive perception, albeit with variability across different texts. The findings suggest that SCoT not only enhances classification accuracy but also prompts critical reflection among users regarding their initial interpretations of migration narratives.

**Limitations**  
The authors acknowledge that while SCoT improves traceability and supports critical interpretation, it may also inadvertently influence human judgment in nuanced ways. They do not explicitly address potential biases in the training data or the limitations of the Llama3-8B model itself, such as its capacity to generalize across diverse migration narratives or its performance in low-resource settings.

**Why it matters**  
This research contributes to the discourse on responsible AI by providing a framework for interpretable LLM applications in socially significant domains like migration news analysis. The emphasis on local deployment and human-in-the-loop interaction aligns with the growing demand for accessible computational tools that prioritize transparency and accountability. The implications of this work extend to the broader field of media studies, where understanding the framing of narratives is crucial for informed public discourse, as published in [arXiv cs.CL](https://arxiv.org/abs/2606.03761v1).
