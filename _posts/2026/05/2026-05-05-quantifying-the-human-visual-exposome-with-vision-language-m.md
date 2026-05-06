---
title: "Quantifying the human visual exposome with vision language models"
date: 2026-05-05 15:25:00 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.03863v1"
arxiv_id: "2605.03863"
authors: ["Christian Rominger", "Andreas R. Schwerdtfeger", "Malay Gaherwar Singh", "Dimitri Khudyakow", "Elizabeth A. M. Michels", "Fabian Wolf"]
slug: quantifying-the-human-visual-exposome-with-vision-language-m
summary_word_count: 414
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the inadequacy of existing methods for quantifying the human visual exposome, which is crucial for understanding its impact on mental health. Current approaches primarily rely on coarse geospatial proxies or biased self-reports, which fail to capture the nuanced first-person visual context of daily life. The authors aim to fill this gap by leveraging vision language models (VLMs) to provide a more objective and detailed quantification of visual experiences.

**Method**  
The authors employed a two-pronged approach: first, they utilized ecological momentary assessment (EMA) alongside VLMs to analyze 2,674 participant-generated photographs. The VLMs were tasked with estimating the semantic richness of these images, particularly focusing on features like greenness. The second component involved developing a semi-autonomous pipeline using a large language model (LLM) to mine over seven million scientific publications, extracting nearly 1,000 environmental features empirically linked to mental health. The training compute specifics were not disclosed, but the methodology emphasizes high-throughput analysis of visual data in relation to mental health metrics.

**Results**  
The VLM-derived estimates of greenness demonstrated a robust predictive relationship with momentary affect and chronic stress, achieving effect sizes that were statistically significant. Specifically, up to 33% of the context ratings extracted from real-world imagery correlated significantly with measures of affect and stress. These results were benchmarked against established metrics in the field, indicating a substantial improvement in quantifying the visual exposome compared to traditional methods.

**Limitations**  
The authors acknowledge several limitations, including the reliance on participant-generated photographs, which may introduce bias based on individual perspectives. Additionally, the study's cross-sectional design limits causal inferences between visual exposure and mental health outcomes. The authors also note that while the VLMs provide a scalable approach, the generalizability of the findings across diverse populations and settings remains to be validated. Furthermore, the computational resources required for processing large datasets with VLMs may pose accessibility challenges for broader applications.

**Why it matters**  
This work has significant implications for the field of mental health research and environmental psychology. By establishing a scalable and objective framework for visual exposomics, it opens avenues for future studies to explore the intricate relationships between visual environments and mental health outcomes. The integration of VLMs into this domain could lead to more personalized mental health interventions and inform urban planning and public health policies aimed at enhancing mental well-being through environmental design.

Authors: Christian Rominger, Andreas R. Schwerdtfeger, Malay Gaherwar Singh, Dimitri Khudyakow, Elizabeth A. M. Michels, Fabian Wolf, Jakob Nikolas Kather, Magdalena Katharina Wekenborg  
Source: arXiv:2605.03863  
URL: [https://arxiv.org/abs/2605.03863v1](https://arxiv.org/abs/2605.03863v1)
