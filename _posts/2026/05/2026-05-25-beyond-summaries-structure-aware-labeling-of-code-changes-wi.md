---
title: "Beyond Summaries: Structure-Aware Labeling of Code Changes with Large Language Models"
date: 2026-05-25 17:56:46 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.26100v1"
arxiv_id: "2605.26100"
authors: ["Bar Weiss", "Antonio Abu-Nassar", "Adi Sosnovich", "Karen Yorav"]
slug: beyond-summaries-structure-aware-labeling-of-code-changes-wi
summary_word_count: 455
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in the literature regarding the structured labeling of code changes during code reviews, particularly in the context of increasing code patch sizes and the integration of AI code assistants. Existing approaches primarily focus on summarization and comment generation, neglecting the nuanced task of identifying specific types of changes (e.g., renames, moves, logic modifications) within code patches. The authors present a systematic study on utilizing large language models (LLMs) for taxonomy-based labeling of code changes, which remains underexplored. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a two-stage pipeline for labeling code changes in diff hunks. The first stage involves assigning initial labels to code changes, while the second stage refines these labels to capture structural relationships and semantic attributes, such as rename propagation and type changes. The approach leverages few-shot prompting techniques to generate language-agnostic and customizable labels, minimizing the engineering overhead typically associated with static analysis pipelines. The evaluation encompasses four different LLMs across various context configurations, using a benchmark dataset composed of both natural and synthetic code patches.

**Results**  
The proposed method achieves notable performance metrics, with the best configuration yielding up to 84% recall and 81% precision in labeling code changes. The authors report high accuracy in extracting relational and attribute metadata, indicating that their LLM-based approach can effectively complement traditional static analysis methods. The results demonstrate the potential for improved efficiency in code reviews through structured labeling, which facilitates prioritization, filtering, and automation of the review process.

**Limitations**  
The authors acknowledge several limitations, including the reliance on a manually curated benchmark, which may not fully represent the diversity of real-world code changes. Additionally, the performance of the LLMs may vary based on the specific context configurations used, and the few-shot prompting approach may not generalize well across all programming languages or codebases. The paper does not address the potential computational costs associated with deploying LLMs in production environments, nor does it explore the implications of model biases in labeling.

**Why it matters**  
This work has significant implications for enhancing code review workflows in software engineering. By enabling structured and automated labeling of code changes, the proposed method can improve the efficiency and effectiveness of code reviews, particularly in large-scale projects where manual review becomes increasingly burdensome. The ability to generate customizable and language-agnostic labels opens avenues for integrating LLMs into diverse development environments, potentially leading to more robust and scalable code review practices. Furthermore, this research lays the groundwork for future studies on the application of LLMs in software engineering tasks beyond code review, such as automated refactoring and code quality assessment.

Authors: Bar Weiss, Antonio Abu-Nassar, Adi Sosnovich, Karen Yorav  
Source: arXiv:2605.26100  
URL: [https://arxiv.org/abs/2605.26100v1](https://arxiv.org/abs/2605.26100v1)
