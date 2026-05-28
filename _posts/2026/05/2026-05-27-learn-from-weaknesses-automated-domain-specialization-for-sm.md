---
title: "Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents"
date: 2026-05-27 17:37:00 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.28775v1"
arxiv_id: "2605.28775"
authors: ["Suji Kim", "Kangsan Kim", "Sung Ju Hwang"]
slug: learn-from-weaknesses-automated-domain-specialization-for-sm
summary_word_count: 438
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of effectively specializing small computer-use agents (CUAs) for diverse software domains without the need for large expert models, which are costly to deploy. The authors note that while existing methods for synthesizing large-scale training data for target domains yield only marginal improvements, there is a lack of frameworks that leverage the strengths of a reference agent to enhance the performance of smaller agents. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel framework called LearnWeak, which automates the specialization of small CUAs by utilizing a stronger reference agent to identify weaknesses in the target domain. The framework operates without requiring manual annotations, instead synthesizing targeted tasks based on the identified weaknesses. A key technical contribution is the introduction of an error-aware specialization objective that differentiates between planning and execution errors, allowing for more precise updates to the agent's behavior. The training process involves generating a student-aware dataset that focuses on the specific shortcomings of the small agent, thereby enhancing its learning efficiency. The architecture details, loss functions, and specific training compute requirements are not disclosed in the abstract.

**Results**  
LearnWeak demonstrates significant performance improvements on the OSWorld benchmark, achieving average gains of 11.6 percentage points over the EvoCUA-8B baseline and 11.1 percentage points over the OpenCUA-7B baseline across eight distinct domains. These results indicate a substantial enhancement in the specialization of small CUAs compared to existing methods, particularly in terms of targeted task performance. The authors also validate their approach against existing autonomous trajectory generation and training baselines, showing that their student-aware dataset generation and training methods outperform these alternatives.

**Limitations**  
The authors acknowledge that their approach may still be limited by the quality and capabilities of the reference agent used for identifying weaknesses. Additionally, the framework's reliance on the reference agent may not generalize well across all domains, particularly those that are highly specialized or require unique contextual understanding. The paper does not discuss potential scalability issues or the computational overhead associated with generating targeted tasks, which could impact practical deployment.

**Why it matters**  
This work has significant implications for the development of more efficient and effective small CUAs, particularly in environments where deploying large models is impractical. By emphasizing the importance of student awareness in both data synthesis and training, LearnWeak paves the way for more principled approaches to agent specialization. This could lead to advancements in various applications, including automated software assistance, where smaller agents can be tailored to specific user needs without extensive resource investment.

Authors: Suji Kim, Kangsan Kim, Sung Ju Hwang  
Source: arXiv:2605.28775  
URL: https://arxiv.org/abs/2605.28775v1
