---
title: "Is Grep All You Need? How Agent Harnesses Reshape Agentic Search"
date: 2026-05-14 17:58:41 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.15184v1"
arxiv_id: "2605.15184"
authors: ["Sahil Sen", "Akhil Kasturi", "Elias Lumer", "Anmol Gulati", "Vamse Kumar Subbiah"]
slug: is-grep-all-you-need-how-agent-harnesses-reshape-agentic-sea
summary_word_count: 447
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the literature regarding the interaction between retrieval strategies and agent architectures in retrieval-augmented generation (RAG) systems. While LLM agents have shown promise in executing complex workflows autonomously, there is a lack of systematic evaluation on how different retrieval methods (grep vs. vector retrieval) affect performance in agentic search tasks. The study specifically investigates how tool output presentation and the presence of irrelevant context impact the efficacy of these retrieval strategies.

**Method**  
The authors conducted two experiments using a custom agent harness named Chronos, alongside provider-native command-line interfaces (CLIs) such as Claude Code, Codex, and Gemini CLI. Experiment 1 involved a comparative analysis of grep and vector retrieval methods on a dataset of 116 questions sourced from LongMemEval. The evaluation focused on both inline tool results and file-based tool results, where the model reads outputs separately. Experiment 2 further explored the robustness of grep-only versus vector-only retrieval by introducing progressively more unrelated conversation history, thereby increasing the distractive context surrounding relevant passages. The experiments aimed to quantify the accuracy of each retrieval method under varying conditions.

**Results**  
The findings indicate that grep retrieval generally outperforms vector retrieval in terms of accuracy across both Chronos and the provider CLIs in Experiment 1. However, the overall performance is highly contingent on the specific harness and tool-calling paradigm employed, even when the underlying conversation data remains constant. In Experiment 2, as irrelevant context was introduced, the performance of both retrieval methods was affected, but grep maintained a relative advantage over vector retrieval. The paper does not provide specific numerical results or effect sizes, focusing instead on qualitative comparisons.

**Limitations**  
The authors acknowledge that their study is limited by the specific configurations of the agent harnesses and the choice of tools evaluated. They do not explore the scalability of their findings across different datasets or the potential impact of varying model architectures beyond those tested. Additionally, the reliance on a single dataset (LongMemEval) may limit the generalizability of the results. The paper does not address the computational costs associated with each retrieval method, which could be a critical factor in practical applications.

**Why it matters**  
This work has significant implications for the design and optimization of agentic search systems. By elucidating the performance dynamics between different retrieval strategies and their interaction with agent architectures, it provides a foundation for future research aimed at enhancing the efficiency and effectiveness of LLM agents in real-world applications. The insights gained could inform the development of more robust retrieval mechanisms that better handle irrelevant context, ultimately improving user experience in agentic workflows.

Authors: Sahil Sen, Akhil Kasturi, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah  
Source: arXiv:2605.15184  
URL: [https://arxiv.org/abs/2605.15184v1](https://arxiv.org/abs/2605.15184v1)
