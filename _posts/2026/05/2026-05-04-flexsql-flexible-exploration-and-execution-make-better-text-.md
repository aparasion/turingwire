---
title: "FlexSQL: Flexible Exploration and Execution Make Better Text-to-SQL Agents"
date: 2026-05-04 16:51:31 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.02815v1"
arxiv_id: "2605.02815"
authors: ["Quang Hieu Pham", "Yang He", "Ping Nie", "Canwen Xu", "Davood Rafiei", "Yuepeng Wang"]
slug: flexsql-flexible-exploration-and-execution-make-better-text-
summary_word_count: 431
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing text-to-SQL systems that operate on a fixed pipeline, where schema elements are retrieved upfront and the database is revisited only for post-hoc repairs. This approach restricts the system's ability to recover from early mistakes, particularly in complex query scenarios involving large analytical databases. The authors propose FlexSQL, a flexible text-to-SQL agent that allows for dynamic interaction with the database throughout the reasoning process. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
FlexSQL's core technical contribution lies in its architecture that facilitates flexible database interaction. The agent can explore schema structures, inspect data values, and execute verification queries at any point during the reasoning process. It generates diverse execution plans to accommodate multiple interpretations of a query and implements these plans in either SQL or Python, depending on the task requirements. The system employs a two-tiered repair mechanism that allows it to backtrack from code-level errors to plan-level revisions, enhancing its robustness. The model is trained using the Spider2-Snow dataset and leverages the gpt-oss-120b model for its execution.

**Results**  
FlexSQL achieves a score of 65.4% on the Spider2-Snow benchmark, outperforming notable open-source baselines, including gpt-o3 and DeepSeek-R1, which utilize larger models. Additionally, when integrated into a general-purpose coding agent (as skills in Claude Code), FlexSQL demonstrates over a 10% relative improvement on the same benchmark. The authors provide evidence that both flexible exploration and flexible execution are critical to the system's performance, indicating that flexibility is a fundamental design principle that enhances effectiveness.

**Limitations**  
The authors acknowledge that while FlexSQL improves upon existing systems, it may still struggle with highly ambiguous queries or those requiring extensive contextual understanding beyond schema exploration. They do not address potential scalability issues when applied to significantly larger databases or the computational overhead introduced by the flexible exploration mechanism. Furthermore, the reliance on the gpt-oss-120b model may limit generalizability to other architectures or smaller models.

**Why it matters**  
The implications of this work are significant for the development of more robust text-to-SQL systems capable of handling complex queries in dynamic environments. By introducing flexibility in both exploration and execution, FlexSQL sets a precedent for future research to prioritize adaptable architectures that can better navigate the intricacies of large databases. This approach could lead to advancements in natural language processing applications that require real-time data interaction and error recovery, ultimately enhancing the usability and accuracy of automated SQL generation tools.

Authors: Quang Hieu Pham, Yang He, Ping Nie, Canwen Xu, Davood Rafiei, Yuepeng Wang, Xi Ye, Jocelyn Qiaochu Chen  
Source: arXiv:2605.02815  
URL: https://arxiv.org/abs/2605.02815v1
