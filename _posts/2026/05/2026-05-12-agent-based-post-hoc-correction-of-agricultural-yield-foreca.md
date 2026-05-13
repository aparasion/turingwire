---
title: "Agent-Based Post-Hoc Correction of Agricultural Yield Forecasts"
date: 2026-05-12 16:41:54 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.12375v1"
arxiv_id: "2605.12375"
authors: ["Matthew Beddows", "Aiden Durrant", "Georgios Leontidis"]
slug: agent-based-post-hoc-correction-of-agricultural-yield-foreca
summary_word_count: 441
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in agricultural yield forecasting, particularly in commercial soft fruit production, where traditional models are limited by the lack of comprehensive data sources such as sensor networks, satellite imagery, and high-resolution meteorological inputs. Existing state-of-the-art approaches often assume access to these data types, which are not typically available in commercial farm records. The authors propose a novel framework that leverages a structured LLM agent to perform post-hoc corrections on yield predictions, thereby enhancing the accuracy of forecasts derived from limited data.

**Method**  
The core technical contribution is a structured LLM agent framework designed for post-hoc correction of yield forecasts. This framework integrates agricultural domain knowledge through tools for phase detection, bias learning, and range validation. The authors utilized XGBoost as the baseline model for yield predictions and applied the LLM agent for refinement. The agent was implemented using Llama 3.1 with 8 billion parameters, which demonstrated the most effective corrections across various configurations. The evaluation was conducted on a proprietary strawberry yield dataset and a public USDA corn harvest dataset, with performance metrics including Mean Absolute Error (MAE) and Mean Absolute Scaled Error (MASE).

**Results**  
The results indicate significant improvements in yield forecasting accuracy through the proposed framework. Specifically, the agent refinement of XGBoost achieved a 20% reduction in MAE and a 56% reduction in MASE for the strawberry dataset. For the Moirai2 baseline, the improvements were 24% in MAE and 22% in MASE, while the Random Forest baseline saw reductions of 28% in MAE and 66% in MASE. These results highlight the effectiveness of the structured LLM agent in enhancing model predictions, particularly in scenarios with limited data.

**Limitations**  
The authors acknowledge several limitations, including the reliance on specific datasets that may not generalize across all agricultural contexts. The performance of the LLM agent was sensitive to the choice of the underlying model, as evidenced by the inconsistent gains observed with LLaVA 13B. Additionally, the framework's effectiveness in other crop types or agricultural settings remains untested, which could limit its applicability. The authors also do not address potential computational costs associated with training and deploying the LLM agent in real-world scenarios.

**Why it matters**  
This work has significant implications for agricultural forecasting, particularly in contexts where data is sparse or incomplete. By demonstrating that post-hoc corrections can substantially enhance yield predictions, the proposed framework opens avenues for more accurate agricultural decision-making and resource allocation. The integration of domain knowledge into machine learning models could lead to improved practices in crop management and yield optimization, ultimately contributing to food security and sustainability in agricultural systems.

Authors: Matthew Beddows, Aiden Durrant, Georgios Leontidis  
Source: arXiv:2605.12375  
URL: [https://arxiv.org/abs/2605.12375v1](https://arxiv.org/abs/2605.12375v1)
