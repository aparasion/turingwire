---
title: "Theory-Grounded Evaluation Exposes the Authorship Gap in LLM Personalization"
date: 2026-04-29 09:17:01 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.26460v1"
arxiv_id: "2604.26460"
authors: ["Yash Ganpat Sawant"]
slug: theory-grounded-evaluation-exposes-the-authorship-gap-in-llm
summary_word_count: 455
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the evaluation of stylistic personalization in large language models (LLMs), specifically the lack of grounding in authorship science. Existing benchmarks fail to provide meaningful assessments of how well LLMs can adapt to an individual's writing style, which is critical for applications requiring personalized content generation. The authors argue that traditional evaluation methods do not capture the nuances of authorship, leading to misleading conclusions about the effectiveness of personalization techniques.

**Method**  
The authors propose a theory-grounded evaluation framework that leverages three distinct measurement traditions:  
1. **LUAR**: A trained authorship verification model that serves as a calibrated baseline for evaluating personalization methods.
2. **LLM-as-judge**: An LLM that performs decoupled trait matching to assess stylistic alignment with individual authors.
3. **Classical function-word stylometrics**: A traditional approach that analyzes the frequency of function words to infer stylistic characteristics.

The study evaluates four inference-time personalization methods across a dataset of 50 authors and 1,000 generated text samples. The LUAR model establishes a human ceiling score of 0.756 and a cross-author floor score of 0.626, providing a robust framework for comparison. The authors highlight that all evaluated methods score below this floor, ranging from 0.484 to 0.508, indicating a significant authorship gap.

**Results**  
The results reveal that the three metrics employed (LUAR, LLM-as-judge, and stylometrics) exhibit near-zero pairwise correlations, with absolute correlation coefficients (r) less than 0.07. This lack of correlation underscores the importance of theoretical grounding in metric selection, as the LLM judge suggests a clear winner among methods, while LUAR indicates no meaningful differentiation. The findings demonstrate that without a solid theoretical foundation, evaluation metrics can lead to divergent conclusions about the effectiveness of personalization techniques.

**Limitations**  
The authors acknowledge that their study is limited by the specific set of authors and generated samples used, which may not generalize to broader contexts. Additionally, the reliance on a single authorship verification model (LUAR) may introduce biases inherent to that model. They also do not explore the potential impact of varying the number of authors or the diversity of writing styles on the evaluation outcomes, which could further illuminate the authorship gap.

**Why it matters**  
This work has significant implications for the field of LLM personalization, as it highlights the necessity of grounding evaluation metrics in established theories of authorship. By exposing the limitations of ad hoc benchmarks, the study encourages researchers to adopt more rigorous evaluation frameworks that can accurately assess the capabilities of LLMs in stylistic adaptation. This could lead to improved personalization techniques and a better understanding of how LLMs can be tailored to individual users, ultimately enhancing user experience in applications such as content creation, automated writing assistants, and personalized communication tools.

Authors: Yash Ganpat Sawant  
Source: arXiv:2604.26460  
URL: https://arxiv.org/abs/2604.26460v1
