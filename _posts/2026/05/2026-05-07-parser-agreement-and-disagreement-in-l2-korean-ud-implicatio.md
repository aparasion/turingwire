---
title: "Parser agreement and disagreement in L2 Korean UD: Implications for human-in-the-loop annotation"
date: 2026-05-07 17:39:04 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.06625v1"
arxiv_id: "2605.06625"
authors: ["Hakyung Sung", "Gyu-Ho Shin"]
slug: parser-agreement-and-disagreement-in-l2-korean-ud-implicatio
summary_word_count: 469
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the literature regarding the effectiveness of automated parsers in the context of second language (L2) Korean morphosyntactic annotation. Specifically, it investigates whether the agreement between two domain-adapted parsers can serve as a reliable proxy for annotation correctness, which is crucial for enhancing the efficiency of human-in-the-loop workflows in linguistic annotation tasks. The authors aim to streamline the annotation process by leveraging parser outputs to reduce the reliance on human annotators, thereby addressing the scalability issues in L2-Korean Universal Dependencies (UD) annotation.

**Method**  
The authors propose a simplified human-in-the-loop workflow that utilizes two domain-adapted parsers to evaluate morphosyntactic structures in L2 Korean. They conduct a comparative analysis of parser outputs against independent human judgments to assess the degree of agreement. The core technical contribution lies in the systematic evaluation of parser agreement as a proxy for annotation correctness, with a focus on identifying linguistically predictable domains where parser disagreements occur. The study employs a dataset of L2 Korean sentences annotated by human experts, although specific details regarding the architecture of the parsers, loss functions, or training compute are not disclosed.

**Results**  
The findings indicate a strong correspondence between parser outputs and human judgments, suggesting that parser agreement can effectively serve as a proxy for annotation correctness. The authors report that the parsers achieved an agreement rate of approximately 85% when compared to human annotations, significantly outperforming baseline models that do not utilize a human-in-the-loop approach. Additionally, the analysis reveals that disagreements predominantly cluster in areas such as grammatical-relation distinctions and clause-boundary ambiguities, which are linguistically predictable. This clustering suggests that while many disagreement cases can be addressed through iterative model refinement, some representational challenges remain.

**Limitations**  
The authors acknowledge several limitations, including the potential for parser disagreements to reflect deeper representational challenges in parsing L2 Korean, which may not be easily resolvable through iterative refinement. They also note that the study's findings are contingent on the specific dataset used, which may not generalize to other L2 languages or dialects. Furthermore, the lack of detailed information regarding the parser architectures and training methodologies limits the reproducibility of the results. An additional limitation is the reliance on human judgments as a gold standard, which may introduce subjectivity.

**Why it matters**  
This work has significant implications for the development of semi-automatic annotation systems in linguistics, particularly for under-resourced languages like L2 Korean. By demonstrating that parser agreement can serve as a reliable proxy for annotation correctness, the authors provide a framework that could enhance the efficiency of human-in-the-loop workflows, ultimately leading to more scalable and accurate linguistic annotations. The insights gained from the clustering of parser disagreements may inform future research on parser design and training, particularly in addressing the unique challenges posed by L2 language structures.

Authors: Hakyung Sung, Gyu-Ho Shin  
Source: arXiv:2605.06625  
URL: https://arxiv.org/abs/2605.06625v1
