---
title: "Do Proactive Agents Really Need an LLM to Decide When to Wake and What to Anchor?"
date: 2026-05-28 16:10:32 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.30152v1"
arxiv_id: "2605.30152"
authors: ["Xiaoze Liu", "Ruowang Zhang", "Amir H. Abdi", "Michel Galley", "Zhikai Chen", "Siheng Xiong"]
slug: do-proactive-agents-really-need-an-llm-to-decide-when-to-wak
summary_word_count: 459
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the inefficiency of current proactive agents that rely on large language models (LLMs) to interpret user activity, which is represented as structured event streams (actor, verb, object, timestamp tuples). The authors identify a gap in the literature regarding the need for LLMs to process this structured data, arguing that converting it to text for LLM consumption introduces unnecessary latency and computational overhead. The paper proposes an alternative approach that leverages the inherent structure of the data without the need for LLMs at every event.

**Method**  
The authors introduce a temporal-graph-learning (TGL) model that encodes the structured event stream directly, bypassing the need for text conversion. The TGL model outputs a per-event trigger probability and a per-entity routing score in a single forward pass. This architecture allows for a more efficient decision-making process, as the LLM is only invoked when the trigger fires, significantly reducing the number of calls to the LLM. The model operates at a speed of 11.13 ms per event on a GPU server and 13.99 ms on a consumer laptop, with a memory footprint of approximately 220 MiB in BF16 format, making it suitable for on-device deployment alongside the activity stream.

**Results**  
The TGL model demonstrates substantial improvements in performance across 14 backbone architectures, achieving a mean F1 score increase of +16.7, with some configurations reaching up to +46.0. In trigger-architecture comparisons, the TGL model consistently yields the highest area under the curve (AUC) for trigger detection and maintains a stable deployed threshold. The efficiency gains are notable, with the TGL model running approximately 4–7 times faster on a GPU server and 12–83 times faster on a consumer laptop compared to LLM-as-trigger configurations.

**Limitations**  
The authors acknowledge that their approach may not generalize to all types of user interactions, particularly those that are less structured or require nuanced language understanding. Additionally, the reliance on a specific architecture may limit flexibility in deployment across diverse systems. The paper does not address potential challenges in scaling the TGL model for larger datasets or more complex event streams, nor does it explore the implications of model interpretability in decision-making processes.

**Why it matters**  
This work has significant implications for the design of proactive agents, particularly in contexts where real-time responsiveness and computational efficiency are critical. By demonstrating that structured event streams can be processed effectively without the overhead of LLMs, the authors pave the way for more efficient AI systems that can operate in privacy-sensitive environments. This approach could lead to advancements in various applications, including personal assistants, smart home devices, and other interactive systems that rely on understanding user behavior in real-time.

Authors: Xiaoze Liu, Ruowang Zhang, Amir H. Abdi, Michel Galley, Zhikai Chen, Siheng Xiong, Xiaoqian Wang, Jing Gao  
Source: arXiv:2605.30152  
URL: [https://arxiv.org/abs/2605.30152v1](https://arxiv.org/abs/2605.30152v1)
