---
title: "\"I didn't Make the Micro Decisions\": Measuring, Inducing, and Exposing Goal-Level AI Contributions in Collaboration"
date: 2026-05-20 16:28:34 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21363v1"
arxiv_id: "2605.21363"
authors: ["Eunsu Kim", "Jessica R. Mindel", "Kyungjin Kim", "Sherry Tongshuang Wu"]
slug: i-didn-t-make-the-micro-decisions-measuring-inducing-and-exp
summary_word_count: 465
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the literature regarding the attribution of contributions in human-AI collaboration, particularly in the context of large language models (LLMs). Existing methodologies primarily focus on the final outputs of collaborative efforts, neglecting the intricate processes through which goals are formed and refined. This oversight hampers users' ability to accurately assess their reliance on AI systems and complicates evaluators' assessments of AI-assisted work. The authors propose a framework that emphasizes the importance of understanding goal-level contributions, which is critical for both users and researchers in the field.

**Method**  
The authors introduce CoTrace, a goal-level attribution framework designed to decompose explicit goals into verifiable requirements. CoTrace traces both direct contributions and indirect influences across dialogue turns in collaborative interactions. The framework was applied to a dataset comprising 638 real-world collaboration logs, allowing for a comprehensive analysis of goal-shaping contributions. The authors conducted controlled simulations to investigate how interaction design choices impact model behavior in goal shaping. Additionally, a user study was performed to evaluate how exposing participants to goal-level analyses affects their perception of AI contributions, utilizing a 5-point scale for quantification.

**Results**  
The findings reveal that LLMs account for only 11-26% of the overall goal-shaping contributions in collaborative settings. However, they significantly enhance the introduction of lower-level concrete requirements, indicating a nuanced role in the goal formation process. The study also highlights various indirect contributions made by the models, which are often overlooked in traditional evaluations. In the user study, participants' perceptions of AI contributions shifted by nearly 2 points on a 5-point scale when exposed to goal-level analyses, indicating a systematic miscalibration in users' understanding of their collaborative work with AI.

**Limitations**  
The authors acknowledge several limitations, including the potential biases inherent in the dataset of collaboration logs, which may not be representative of all collaborative contexts. The framework's reliance on dialogue turns may also overlook non-verbal cues that could influence goal shaping. Furthermore, the user study's sample size and demographic diversity are not disclosed, which could affect the generalizability of the findings. The authors do not address the scalability of CoTrace in more complex or multi-agent scenarios, which could limit its applicability in broader contexts.

**Why it matters**  
This work has significant implications for the design and evaluation of AI systems in collaborative environments. By providing a framework for understanding goal-level contributions, it enables users to better calibrate their reliance on AI, fostering more effective human-AI partnerships. The insights gained from this research can inform the development of more transparent AI systems that enhance user understanding and trust. Additionally, the findings encourage further exploration into the indirect contributions of AI, which could lead to improved interaction designs and more effective collaborative tools.

Authors: Eunsu Kim, Jessica R. Mindel, Kyungjin Kim, Sherry Tongshuang Wu  
Source: arXiv:2605.21363  
URL: https://arxiv.org/abs/2605.21363v1
