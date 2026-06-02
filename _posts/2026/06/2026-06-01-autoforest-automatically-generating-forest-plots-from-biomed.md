---
title: "AutoForest: Automatically Generating Forest Plots from Biomedical Studies with End-to-End Evidence Extraction and Synthesis"
date: 2026-06-01 15:49:33 +0000
category: research
subcategory: other
company: "Meta"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2606.02403v1"
arxiv_id: "2606.02403"
authors: ["Massimiliano Pronesti", "Angelo Miculescu", "Mohsin Kapdi", "Paul Flanagan", "Ois\u00edn Redmond", "Joao Bettencourt-Silva"]
slug: autoforest-automatically-generating-forest-plots-from-biomed
summary_word_count: 434
classification_confidence: 0.70
source_truncated: false
layout: post
description: "AutoForest is an end-to-end system that automates the generation of forest plots from biomedical studies, streamlining evidence synthesis."
---

**Problem**  
The paper addresses the inefficiencies in generating forest plots for systematic reviews in biomedical research, a process that is traditionally labor-intensive and fragmented. Researchers face challenges in interpreting complex clinical texts, manually extracting outcome data, harmonizing study designs, and performing meta-analytic computations. While recent advancements have shown that large language models can extract data from unstructured text, there is currently no comprehensive system that automates the entire pipeline from raw documents to publication-ready forest plots. This work presents AutoForest, which fills this gap by providing an automated solution for evidence synthesis.

**Method**  
AutoForest employs a novel architecture that integrates natural language processing (NLP) techniques with statistical synthesis methods. The system takes as input one or more biomedical study papers and automatically identifies key ICO (Intervention, Comparator, Outcome) elements. It utilizes large language models for data extraction and applies statistical methods to synthesize the extracted outcome data into forest plots. The authors detail the user interface and the underlying algorithms, although specific training compute resources and model parameters are not disclosed. The end-to-end nature of AutoForest allows for seamless transitions from text extraction to plot generation, significantly reducing the need for domain expertise.

**Results**  
In a user study involving clinicians, AutoForest demonstrated a significant reduction in the time required to generate forest plots compared to traditional methods. The system was able to produce publication-ready plots with a high degree of accuracy, although specific quantitative metrics (e.g., time savings, accuracy rates) are not provided in the abstract. The authors compare AutoForest's performance against baseline methods, highlighting its effectiveness in accelerating evidence synthesis and lowering barriers for conducting meta-analyses.

**Limitations**  
The authors acknowledge that while AutoForest automates many aspects of forest plot generation, it may still struggle with highly complex or ambiguous texts that require nuanced interpretation. Additionally, the system's reliance on the quality of the input documents means that poorly written or structured studies could lead to suboptimal outputs. The paper does not address potential biases in the data extraction process or the generalizability of the system across different biomedical domains.

**Why it matters**  
AutoForest represents a significant advancement in the automation of systematic reviews, potentially transforming how biomedical evidence is synthesized and presented. By lowering the barriers to conducting meta-analyses, it could facilitate more rapid and widespread adoption of evidence-based practices in clinical settings. This work is particularly relevant for researchers and practitioners in the field of biomedical informatics and systematic review methodology, as it streamlines a critical aspect of evidence synthesis. The implications of this research extend to improving the efficiency of clinical decision-making processes, as highlighted in the findings available on [arXiv](https://arxiv.org/abs/2606.02403v1).
