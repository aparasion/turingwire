---
title: "Reducing cross-sample prediction churn in scientific machine learning"
date: 2026-05-13 17:50:57 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.13826v1"
arxiv_id: "2605.13826"
authors: ["Gordan Prastalo", "Kevin Maik Jablonka"]
slug: reducing-cross-sample-prediction-churn-in-scientific-machine
summary_word_count: 471
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in scientific machine learning (SciML) literature regarding the stability of predictions across different training data samples. While predictive performance is often reported, the authors highlight the lack of attention to "cross-sample prediction churn," which refers to the variability in predictions when classifiers are trained on independent bootstraps of the same dataset. The study reveals that, despite similar aggregate accuracy (within 1.3–4.2 percentage points), classifiers can disagree on class labels for 8.0–21.8% of test molecules, indicating a critical need for methods that enhance prediction consistency.

**Method**  
The authors propose two data-side methods to mitigate cross-sample prediction churn. The first method is $K$-bootstrap bagging, which involves training multiple classifiers on $K$ independent bootstraps of the training set. This approach reduces churn by 40–54% across all evaluated datasets without sacrificing accuracy, requiring $K \times$ empirical risk minimization (ERM) compute. The second method, termed "twin-bootstrap," involves training two networks simultaneously on independent bootstraps while enforcing a symmetric Kullback-Leibler (sym-KL) consistency loss between their predictions. This method, at a matched compute cost of $2 \times$ ERM, further reduces churn by a median of 45% compared to bagging with $K=2$. The authors argue that these methods should be reported alongside predictive performance metrics in SciML benchmarks to provide a more comprehensive evaluation of model reliability.

**Results**  
The study evaluates the proposed methods across nine chemistry benchmarks. The $K$-bootstrap bagging method consistently reduces churn by 40–54% without any loss in accuracy. The twin-bootstrap method achieves a median reduction of 45% in churn compared to the baseline of $K$-bootstrap bagging with $K=2$. These results indicate that while traditional parameter-side techniques (e.g., deep ensembles, Monte Carlo dropout) do not effectively address prediction churn, the proposed data-side methods significantly enhance prediction stability.

**Limitations**  
The authors acknowledge that their methods may not generalize to all types of datasets or domains outside of chemistry, as the study is limited to specific benchmarks. Additionally, the computational cost associated with the twin-bootstrap method, while matched to $2 \times$ ERM, may still be prohibitive in resource-constrained environments. The paper does not explore the impact of varying $K$ in bagging beyond the tested values, nor does it address potential overfitting issues that could arise from the twin-bootstrap approach.

**Why it matters**  
This work has significant implications for the field of scientific machine learning, as it emphasizes the importance of reporting prediction stability alongside traditional performance metrics. By introducing methods that effectively reduce cross-sample prediction churn, the authors provide a framework for enhancing the reliability of machine learning models in scientific applications. This could lead to more robust models that are better suited for real-world applications, where data variability is common. The findings encourage researchers to adopt a more holistic approach to model evaluation, potentially influencing future benchmark standards in SciML.

Authors: Gordan Prastalo, Kevin Maik Jablonka  
Source: arXiv:2605.13826  
URL: https://arxiv.org/abs/2605.13826v1
