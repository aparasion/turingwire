---
title: "From Model Scaling to System Scaling: Scaling the Harness in Agentic AI"
date: 2026-05-25 17:59:36 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.26112v1"
arxiv_id: "2605.26112"
authors: ["Shangding Gu"]
slug: from-model-scaling-to-system-scaling-scaling-the-harness-in-
summary_word_count: 468
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a critical gap in the literature regarding the scaling of agentic AI systems, emphasizing the need for a shift from model-centric evaluations to a focus on system scaling. The authors argue that while large language models (LLMs) have advanced capabilities in tool use, memory retention, and long-horizon task execution, the evaluation frameworks remain inadequate. They highlight that current assessments often overlook the intricate interactions among various components of an agent's architecture, such as memory, retrieval, and governance, which are essential for translating model capabilities into effective agent behavior.

**Method**  
The paper introduces the concept of "scaling the harness," which involves treating the structured execution layer around foundation models as a primary design object. The authors identify three core bottlenecks in this context: context governance, trustworthy memory, and dynamic skill routing. They propose a modular architecture that integrates these components with orchestration and governance mechanisms to enhance agent performance. To illustrate their framework, the authors develop CheetahClaws, a Python-native reference harness that serves as a testbed for evaluating agentic AI systems. They compare CheetahClaws against existing systems like Claude Code and OpenClaw, focusing on how these architectures can be optimized for better performance in real-world applications.

**Results**  
The authors present qualitative comparisons of CheetahClaws with Claude Code and OpenClaw, emphasizing improvements in trajectory quality, memory hygiene, context efficiency, communication fidelity, verification cost, and safe evolution over time. While specific quantitative metrics are not disclosed in the abstract, the paper suggests that CheetahClaws outperforms the baselines in these dimensions, indicating a significant advancement in harness-level evaluations. The proposed benchmarks aim to provide a more comprehensive assessment of agentic AI systems beyond mere task success, thereby setting a new standard for future research.

**Limitations**  
The authors acknowledge that their framework is still in the early stages of development and that the proposed benchmarks require further validation and refinement. They do not address potential scalability issues of the harness itself when applied to larger models or more complex tasks. Additionally, the reliance on a Python-native implementation may limit accessibility for researchers using other programming environments. The paper does not discuss the computational overhead introduced by the additional layers of governance and orchestration, which could impact real-time performance.

**Why it matters**  
This work has significant implications for the future of agentic AI, as it shifts the focus from merely enhancing model capabilities to optimizing the entire system architecture. By advocating for a comprehensive evaluation framework that includes harness-level metrics, the authors lay the groundwork for more robust and reliable agentic systems. This approach could lead to safer and more effective AI applications in various domains, including autonomous systems, robotics, and interactive agents. The proposed research agenda encourages further exploration of system design, which is crucial for advancing the field beyond current limitations.

Authors: Shangding Gu  
Source: arXiv:2605.26112  
URL: [https://arxiv.org/abs/2605.26112v1](https://arxiv.org/abs/2605.26112v1)
