---
title: "Leave a Window Out: Modifying the Jackknife for Predictive Inference in Time Series"
date: 2026-05-28 17:41:12 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.30292v1"
arxiv_id: "2605.30292"
authors: ["Hanyang Jiang", "Rina Foygel Barber", "Ashwin Pananjady", "Yao Xie"]
slug: leave-a-window-out-modifying-the-jackknife-for-predictive-in
summary_word_count: 450
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing conformal prediction methods in the context of time series data, where the assumptions of exchangeability and memoryless predictors are often violated. Traditional methods, such as the vanilla leave-one-out jackknife, can lead to significant coverage loss in time series models due to temporal dependence. The authors aim to provide a solution that maintains valid predictive inference without relying on data splitting, which can compromise accuracy.

**Method**  
The core technical contribution is the introduction of the Leave-a-Window-Out (LWO) method, a modification of the jackknife approach specifically designed for time series data. The LWO method operates by excluding a window of consecutive observations rather than a single observation, which allows it to better account for temporal dependencies. The authors establish theoretical guarantees for valid coverage under mild stability conditions of the model-fitting procedure. They introduce new coefficients to quantify the degree of departure from cyclic exchangeability, which is critical for assessing the performance of the LWO method. The experiments utilize various time series datasets to validate the effectiveness of the proposed method against traditional jackknife and split conformal prediction approaches.

**Results**  
The LWO method demonstrates superior performance in terms of coverage and interval width compared to the vanilla jackknife and split conformal prediction. Specifically, the LWO method achieves valid coverage rates above 95% in scenarios where the vanilla jackknife fails, which can drop below 80%. Additionally, the LWO method produces narrower prediction intervals, enhancing the precision of the forecasts. The empirical results indicate that the LWO method consistently outperforms the baselines across multiple time series datasets, showcasing its robustness in practical applications.

**Limitations**  
The authors acknowledge that the LWO method relies on the assumption of mild stability in the model-fitting process, which may not hold in all real-world scenarios. They also note that while the method improves coverage and interval width, it may still be sensitive to the choice of window size, which requires careful tuning. Furthermore, the theoretical guarantees are contingent on the specific structure of the time series data, and the method may not generalize well to highly non-stationary or chaotic time series.

**Why it matters**  
The introduction of the LWO method has significant implications for predictive inference in time series analysis, particularly in fields where accurate forecasting is critical, such as finance, meteorology, and healthcare. By providing a robust alternative to traditional jackknife methods, the LWO approach enhances the reliability of predictive intervals, enabling practitioners to make more informed decisions based on their models. This work opens avenues for further research into adaptive methods for time series prediction that can accommodate various forms of temporal dependence and non-exchangeability.

Authors: Hanyang Jiang, Rina Foygel Barber, Ashwin Pananjady, Yao Xie  
Source: arXiv:2605.30292  
URL: https://arxiv.org/abs/2605.30292v1
