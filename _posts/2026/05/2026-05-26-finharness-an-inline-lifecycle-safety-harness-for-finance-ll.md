---
title: "FinHarness: An Inline Lifecycle Safety Harness for Finance LLM Agents"
date: 2026-05-26 17:41:01 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.27333v1"
arxiv_id: "2605.27333"
authors: ["Haoxuan Jia", "Yang Liu", "Bin Chong", "Yingguang Yang", "Yancheng Chen", "Jiayu Liang"]
slug: finharness-an-inline-lifecycle-safety-harness-for-finance-ll
summary_word_count: 480
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the critical gap in the safety mechanisms of finance-oriented Large Language Model (LLM) agents, particularly in their ability to prevent unauthorized actions while facilitating legitimate multi-step workflows. Existing solutions, such as boundary filters and post-hoc auditing by LLM judges, are inadequate. Boundary filters often fail to intercept irreversible actions during execution, and post-hoc audits occur too late to prevent potential harm, with computational costs that scale linearly with the length of the execution trace. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose FinHarness, an inline safety harness designed to enhance the operational safety of finance LLM agents. FinHarness comprises three main components:  
1. **Query Monitor**: This module integrates single-turn intent analysis with cross-turn drift detection to assess the agent's decision-making context.
2. **Tool Monitor**: It evaluates each prospective tool call to determine its appropriateness based on the current context and risk factors.
3. **Cascade Module**: This component adaptively routes verification requests between a lightweight LLM judge and an advanced-tier LLM judge based on the assessed risk of each action. 

The system re-injects identified risk factors into the agent's input as ex-ante evidence, allowing the agent to autonomously refuse, re-plan, or approve actions. The training compute specifics are not disclosed, but the architecture emphasizes real-time decision-making and risk assessment.

**Results**  
FinHarness was evaluated on the FinVault benchmark, demonstrating significant improvements in safety and efficiency. The system reduced the Action Success Rate (ASR) from 38.3% to 15.0%, indicating a substantial decrease in unauthorized actions. Concurrently, it preserved benign approval rates, which decreased from 41.1% to 39.3%. Notably, FinHarness utilized 4.7 times fewer advanced-judge calls compared to an ablation that relied solely on the advanced judge for all evaluations. These results highlight the effectiveness of the inline safety harness in maintaining operational integrity while minimizing unnecessary computational overhead.

**Limitations**  
The authors acknowledge several limitations, including the potential for the Query and Tool Monitors to misclassify actions, leading to either false positives or negatives in risk assessment. Additionally, the reliance on LLM judges introduces variability based on their training and architecture, which may affect consistency. The paper does not address the scalability of the system in more complex financial environments or the potential for adversarial attacks on the safety mechanisms.

**Why it matters**  
FinHarness represents a significant advancement in the safety of finance LLM agents, providing a framework that allows for real-time risk assessment and decision-making. Its inline architecture could pave the way for more robust AI systems in finance, where the stakes of unauthorized actions are particularly high. The implications extend beyond finance, suggesting a model for integrating safety mechanisms in other domains where LLMs are deployed, potentially enhancing their reliability and trustworthiness in critical applications.

Authors: Haoxuan Jia, Yang Liu, Bin Chong, Yingguang Yang, Yancheng Chen, Jiayu Liang, Qian Li, Hanning Lu et al.  
Source: arXiv:2605.27333  
URL: https://arxiv.org/abs/2605.27333v1
