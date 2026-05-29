---
title: "Do Language Models Track Entities Across State Changes?"
date: 2026-05-28 17:03:42 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.30233v1"
arxiv_id: "2605.30233"
authors: ["Zilu Tang", "Qiao Zhao", "Gabriel Franco", "Derry Wijaya", "Aaron Mueller", "Sebastian Schuster"]
slug: do-language-models-track-entities-across-state-changes
summary_word_count: 495
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the understanding of entity tracking (ET) capabilities of transformer language models (LMs) in complex scenarios involving state changes. While prior research has focused on how LMs handle entity binding without state changes, there is limited exploration of their performance in more realistic, state-altering contexts. The authors aim to elucidate the mechanisms by which LMs manage ET when faced with multiple state-changing operations, thereby contributing to the literature on the limitations and capabilities of LMs in complex reasoning tasks.

**Method**  
The authors conduct a series of experiments to analyze the ET mechanisms of LMs, particularly focusing on operations such as $\texttt{PUT}$, $\texttt{REMOVE}$, and $\texttt{MOVE}$. They employ a behavioral analysis framework to assess how LMs aggregate information across tokens and layers. The key finding is that LMs do not incrementally track world states; instead, they aggregate relevant information in parallel at the final token when the query is clear. The authors introduce a global suppression tag mechanism for the $\texttt{REMOVE}$ operation, which they identify as a source of fragility leading to specific failure modes. To mitigate these issues, they propose a mechanistic solution that involves nullifying the global suppression tag. The experiments leverage various natural language tasks to evaluate the performance of LMs under these conditions.

**Results**  
The findings reveal that LMs exhibit a non-incremental approach to ET, which contrasts with the expected sequential nature of the task. The authors provide quantitative results demonstrating that LMs struggle with the $\texttt{REMOVE}$ operation due to the global suppression tag, leading to a significant drop in performance on tasks requiring this operation. While specific numerical results are not disclosed in the abstract, the authors indicate that their mechanistic interventions improve performance on benchmarks that assess ET capabilities, suggesting a notable effect size compared to baseline models that do not utilize the proposed solutions.

**Limitations**  
The authors acknowledge that their analysis is limited to specific operations and may not generalize across all types of state changes or entity interactions. They also note that the proposed solution of nullifying the global suppression tag may not fully resolve the underlying issues, indicating that further research is needed to develop more robust ET mechanisms. Additionally, the study does not explore the implications of these findings on other types of reasoning tasks beyond ET, which could limit the broader applicability of the results.

**Why it matters**  
This work has significant implications for the development of more capable LMs that can handle complex reasoning tasks involving state changes. By revealing the non-sequential strategies employed by LMs in ET, the authors provide insights that can inform future architectural designs and training methodologies. The interaction between behavioral and mechanistic analyses highlighted in this study suggests a promising avenue for improving LMs' performance in tasks requiring nuanced understanding of state dynamics, ultimately contributing to advancements in natural language understanding and reasoning capabilities.

Authors: Zilu Tang, Qiao Zhao, Gabriel Franco, Derry Wijaya, Aaron Mueller, Sebastian Schuster, Najoung Kim  
Source: arXiv:2605.30233  
URL: https://arxiv.org/abs/2605.30233v1
