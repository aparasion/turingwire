---
title: "One prompt is not enough: Instruction Sensitivity Undermines Embedding Model Evaluation"
date: 2026-05-21 14:27:46 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.22544v1"
arxiv_id: "2605.22544"
authors: ["Yevhen Kostiuk", "Kenneth Enevoldsen"]
slug: one-prompt-is-not-enough-instruction-sensitivity-undermines-
summary_word_count: 481
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the evaluation methodology of instruction embedding models, which are prevalent in state-of-the-art natural language processing (NLP) systems. The authors highlight that current evaluation practices typically rely on a single prompt per task, neglecting the inherent sensitivity of these models to the phrasing of instructions. This oversight can lead to misleading performance metrics, as the evaluation does not account for the variability introduced by different prompt formulations. The study aims to empirically demonstrate the extent of this sensitivity and its implications for model ranking and performance assessment.

**Method**  
The authors conduct an empirical analysis involving six instruction embedding models across eleven datasets, utilizing a total of fifteen task-specific prompts per dataset, culminating in 990 evaluations. The core technical contribution lies in the systematic exploration of prompt sensitivity, where the authors assess how variations in prompt phrasing affect model performance. They employ a robust evaluation framework that not only measures the performance of each model using a single prompt but also aggregates results across multiple prompts to capture the distribution of scores. This approach allows for a more nuanced understanding of model capabilities and the robustness of their evaluations.

**Results**  
The findings reveal that the performance scores reported for instruction embedding models can be significantly skewed by the choice of prompt. The authors demonstrate that the default prompt can either understate or overstate a model's true performance, leading to unreliable leaderboard rankings. For instance, by strategically selecting prompts, any model in the study could be elevated to the top position on the leaderboard, indicating a lack of robustness in current evaluation practices. The study quantitatively illustrates that the variance in scores across different prompts is substantial, suggesting that single-point evaluations are inadequate for capturing the true performance landscape of these models.

**Limitations**  
The authors acknowledge that their study is limited to the specific models and datasets chosen, which may not encompass the full diversity of instruction embedding models in the field. Additionally, while the study highlights the importance of prompt robustness, it does not propose a standardized methodology for incorporating this robustness into existing benchmarks. An obvious limitation not explicitly mentioned is the potential for overfitting to specific prompts during model training, which could further complicate the evaluation landscape.

**Why it matters**  
This work has significant implications for the future of model evaluation in NLP, particularly for instruction-tuned embedding models. By highlighting the critical role of prompt sensitivity, the authors advocate for a paradigm shift in evaluation practices, urging the community to adopt multi-prompt evaluations or to report sensitivity metrics alongside point estimates. This could lead to more reliable assessments of model performance, fostering the development of more robust and generalizable NLP systems. The findings encourage researchers and practitioners to reconsider how they evaluate and compare models, ultimately contributing to more trustworthy benchmarks in the field.

Authors: Yevhen Kostiuk, Kenneth Enevoldsen  
Source: arXiv:2605.22544  
URL: https://arxiv.org/abs/2605.22544v1
