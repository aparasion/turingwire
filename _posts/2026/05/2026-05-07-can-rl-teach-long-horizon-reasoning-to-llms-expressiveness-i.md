---
title: "Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key"
date: 2026-05-07 17:48:42 +0000
category: research
subcategory: reasoning
company: "Scale AI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06638v1"
arxiv_id: "2605.06638"
authors: ["Tianle Wang", "Zhaoyang Wang", "Guangchen Lan", "Xinpeng Wei", "Sipeng Zhang", "Guanwen Qiu"]
slug: can-rl-teach-long-horizon-reasoning-to-llms-expressiveness-i
summary_word_count: 461
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how reinforcement learning (RL) can enhance long-horizon reasoning capabilities in large language models (LLMs). Prior work has not systematically explored the relationship between task difficulty and training efficiency due to the absence of controlled environments that allow for independent manipulation of reasoning depth and logical expressiveness.

**Method**  
The authors introduce ScaleLogic, a synthetic logical reasoning framework designed to facilitate the study of RL in LLMs. ScaleLogic allows for independent control over two critical dimensions: the depth of proof planning (horizon) and the expressiveness of the underlying logic. The framework encompasses a spectrum of logical systems, from basic implication-only logic to more complex first-order logic that includes conjunction, disjunction, negation, and universal quantification. The authors empirically demonstrate that the training compute \( T \) required for RL scales with reasoning depth \( D \) according to a power law \( T \propto D^{\gamma} \), with \( R^{2} > 0.99 \). The scaling exponent \( \gamma \) is shown to increase with logical expressiveness, ranging from \( 1.04 \) for simpler logics to \( 2.60 \) for more expressive logics. The study also highlights that curriculum-based training significantly enhances scaling efficiency.

**Results**  
The authors report that more expressive training settings lead to substantial performance improvements on downstream mathematics and general reasoning benchmarks, with gains of up to \( +10.66 \) points compared to less expressive settings. The results indicate that the nature of the training data (expressiveness) is a critical factor influencing the efficiency of transfer learning, rather than merely the volume of training. The power-law relationship between training compute and reasoning depth is consistent across various RL methods, reinforcing the robustness of their findings.

**Limitations**  
The authors acknowledge that their framework is synthetic and may not fully capture the complexities of real-world reasoning tasks. Additionally, while the power-law relationship is established, the implications of this scaling behavior in practical applications remain to be explored. The study does not address potential overfitting issues that may arise from training on highly expressive logics, nor does it consider the impact of different RL algorithms beyond those tested.

**Why it matters**  
This work has significant implications for the design of training regimes for LLMs, particularly in tasks requiring complex reasoning. By demonstrating that both the depth of reasoning and the expressiveness of the logic are critical to training efficiency, the findings suggest that future research should focus on developing more expressive training datasets and curricula. This could lead to more capable LLMs that can tackle a broader range of reasoning tasks, ultimately advancing the field of AI in areas such as automated theorem proving, natural language understanding, and decision-making.

Authors: Tianle Wang, Zhaoyang Wang, Guangchen Lan, Xinpeng Wei, Sipeng Zhang, Guanwen Qiu, Abulhair Saparov  
Source: arXiv:2605.06638  
URL: https://arxiv.org/abs/2605.06638v1
