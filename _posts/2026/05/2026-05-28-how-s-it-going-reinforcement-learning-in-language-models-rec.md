---
title: "How's it going? Reinforcement learning in language models recruits a functional welfare axis"
date: 2026-05-28 17:03:18 +0000
category: research
subcategory: alignment_safety
company: "null"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.30232v1"
arxiv_id: "2605.30232"
authors: ["Andy Q Han", "David J. Chalmers", "Pavel Izmailov"]
slug: how-s-it-going-reinforcement-learning-in-language-models-rec
summary_word_count: 456
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how reinforcement learning (RL) influences the internal representations of language models, particularly in relation to a functional welfare axis. Prior literature has not sufficiently explored the mechanisms by which RL modifies model behavior and representation, especially in terms of welfare-related concepts. The authors aim to elucidate how RL can recruit pre-existing representations of functional welfare, which may have implications for model interpretability and alignment.

**Method**  
The authors employ a novel maze environment designed to be semantically neutral, allowing for the isolation of RL effects on language model representations. They train several language models using RL and extract concept vectors corresponding to rewarded and punished trajectories. The analysis includes evaluating these vectors in contexts unrelated to the maze, ensuring robustness across various factors such as tile-to-reward mapping, model scale, instruction tuning, RL algorithms, and fine-tuning methods (LoRA vs. full fine-tuning). The study demonstrates that the punishment vector correlates with negative welfare, promoting tokens associated with failure and negative emotions, while the reward vector exhibits an antiparallel relationship, representing positive welfare. The findings indicate that these vectors are effective even in models prior to maze training, suggesting that the functional welfare axis is pre-existing and merely recruited by RL.

**Results**  
The study reports that the punishment vector significantly influences model behavior, leading to increased occurrences of failure tokens and negative self-reports, while the reward vector enhances goal achievement and positive self-reports. The effects are robust across various configurations, with the authors noting that the vectors maintain their properties even when RL is replaced with supervised fine-tuning. The authors do not provide specific quantitative metrics or effect sizes in the abstract, but they emphasize the robustness of the findings across different experimental setups.

**Limitations**  
The authors acknowledge that their claims do not extend to any assertions about the models' experiences of welfare, which remains an abstract representation rather than a conscious experience. Additionally, the study's reliance on a specific maze environment may limit the generalizability of the findings to other contexts. The lack of quantitative performance metrics in the abstract also presents a limitation for evaluating the practical implications of the results.

**Why it matters**  
This work has significant implications for the fields of model interpretability and alignment. By demonstrating that minimal reward signals can effectively recruit pre-existing welfare-like representations, the study suggests new avenues for enhancing model behavior through targeted training strategies. Understanding the functional welfare axis could lead to improved alignment techniques, ensuring that language models behave in ways that are more consistent with human values and goals. This research opens up further inquiries into the dynamics of post-training behavior and the interpretability of model decisions.

Authors: Andy Q Han, David J. Chalmers, Pavel Izmailov  
Source: arXiv:2605.30232  
URL: [https://arxiv.org/abs/2605.30232v1](https://arxiv.org/abs/2605.30232v1)
