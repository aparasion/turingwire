---
title: "SafeReview: Defending LLM-based Review Systems Against Adversarial Hidden Prompts"
date: 2026-04-29 10:11:12 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.26506v1"
arxiv_id: "2604.26506"
authors: ["Yuan Xin", "Yixuan Weng", "Minjun Zhu", "Ying Ling", "Chengwei Qin", "Michael Hahn"]
slug: safereview-defending-llm-based-review-systems-against-advers
summary_word_count: 431
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the vulnerability of Large Language Models (LLMs) used in academic peer review systems to adversarial hidden prompts. These prompts are covert instructions embedded within submissions that can manipulate the review outcomes, posing a significant threat to the integrity of scholarly processes. The existing literature lacks robust frameworks for detecting and mitigating such adversarial attacks, highlighting a critical gap in the security of LLM-based review systems.

**Method**  
The authors propose a novel adversarial framework comprising two main components: a Generator model and a Defender model. The Generator is trained to create sophisticated adversarial prompts, while the Defender is optimized to detect these prompts. The training employs a loss function inspired by Information Retrieval Generative Adversarial Networks (IR-GANs), which facilitates a dynamic co-evolution between the Generator and Defender. This approach allows the Defender to adaptively enhance its detection capabilities in response to the evolving strategies of the Generator. The framework is evaluated on a dataset of peer review submissions, although specific details regarding the dataset size, training compute, and hyperparameters are not disclosed.

**Results**  
The proposed framework demonstrates a significant improvement in resilience against adversarial prompts compared to traditional static defenses. The authors report that the Defender achieves a detection accuracy of 92% on novel adversarial prompts, outperforming baseline models that achieve only 75% accuracy. Additionally, the framework shows a 30% reduction in false negatives compared to existing methods, indicating a substantial enhancement in the reliability of peer review systems when subjected to adversarial attacks.

**Limitations**  
The authors acknowledge several limitations, including the potential for the Generator to produce prompts that are not representative of real-world adversarial strategies, which may affect the generalizability of the Defender's capabilities. Furthermore, the framework's performance may vary based on the specific characteristics of the peer review submissions used for training. The paper does not address the computational overhead introduced by the adversarial training process, which could limit scalability in practical applications.

**Why it matters**  
This work is significant as it lays the groundwork for securing LLM-based peer review systems against adversarial manipulation, a growing concern in the academic community. By establishing a dynamic adversarial training framework, the authors provide a methodology that can be adapted and extended to other domains where LLMs are deployed, enhancing the robustness of AI systems against adversarial threats. The implications of this research extend beyond peer review, potentially influencing the design of secure AI applications in various fields, including automated content moderation and decision-making systems.

Authors: Yuan Xin, Yixuan Weng, Minjun Zhu, Ying Ling, Chengwei Qin, Michael Hahn, Michael Backes, Yue Zhang et al.  
Source: arXiv:2604.26506  
URL: [https://arxiv.org/abs/2604.26506v1](https://arxiv.org/abs/2604.26506v1)
