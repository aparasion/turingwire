---
title: "(POSTER) From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications"
date: 2026-05-04 17:21:37 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02844v1"
arxiv_id: "2605.02844"
authors: ["Komal Thareja", "Anirban Mandal", "Ewa Deelman"]
slug: poster-from-sensors-to-insight-rapid-edge-to-core-applicatio
summary_word_count: 452
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of transforming raw sensor data into actionable insights across the edge-to-cloud continuum, a task that typically requires diverse expertise in data management and computational workflows. The authors highlight the gap in existing methodologies that complicate the rapid development of sensor-driven applications, particularly for users with limited experience in workflow design. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a pattern-based, AI-assisted methodology for the rapid development of sensor-driven applications, leveraging Pegasus workflows executed on the FABRIC testbed. The core technical contribution is a 5-step development loop that transitions from a code-first to an intent-first design approach. This methodology utilizes an existing Orcasound hydrophone workflow as a reusable template, which is adapted for various applications, including air quality monitoring, earthquake detection, and soil moisture assessment. The workflows are designed to extend to edge resources, such as BlueField-3 Data Processing Units (DPUs) and Raspberry Pis, through configuration and placement rather than requiring a complete redesign. The authors emphasize the use of AI to facilitate pattern reuse, which significantly accelerates the workflow development process.

**Results**  
The evaluation indicates that the AI-assisted pattern reuse methodology compresses the multi-stage workflow development time to approximately 1-1.5 days per workflow. This is a substantial improvement compared to traditional methods, which can be significantly more time-consuming. The authors do not provide specific baseline comparisons or quantitative metrics against existing methodologies, but they assert that the approach maintains the rigor and portability of workflow-based execution, which is critical for deployment in diverse environments.

**Limitations**  
The authors acknowledge that their approach may not fully address the complexities involved in highly specialized sensor applications that require intricate domain knowledge. Additionally, the reliance on existing templates may limit flexibility in novel use cases. The paper does not discuss potential scalability issues when deploying workflows across a larger number of sensors or more complex data streams. Furthermore, the evaluation is conducted from the perspective of novice users, which may not reflect the experiences of more advanced users who could leverage additional optimizations.

**Why it matters**  
This work has significant implications for the development of sensor-driven applications, particularly in fields such as environmental monitoring, disaster response, and smart city initiatives. By streamlining the workflow development process, the proposed methodology lowers the barrier to entry for non-experts, enabling broader participation in sensor data utilization. The ability to rapidly adapt workflows for various applications can accelerate innovation and deployment in real-world scenarios, fostering advancements in data-driven decision-making. This research could serve as a foundation for future work aimed at enhancing the accessibility and efficiency of sensor data processing across diverse domains.

Authors: Komal Thareja, Anirban Mandal, Ewa Deelman  
Source: arXiv:2605.02844  
URL: https://arxiv.org/abs/2605.02844v1
