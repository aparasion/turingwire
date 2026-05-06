---
title: "A Benchmark for Interactive World Models with a Unified Action Generation Framework"
date: 2026-05-05 16:30:03 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.03941v1"
arxiv_id: "2605.03941"
authors: ["Jianjie Fang", "Yingshan Lei", "Qin Wan", "Ziyou Wang", "Yuchao Huang", "Yongyan Xu"]
slug: a-benchmark-for-interactive-world-models-with-a-unified-acti
summary_word_count: 440
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the lack of large-scale datasets and unified benchmarks for evaluating the physical interaction capabilities of interactive world models, which are essential for advancing Artificial General Intelligence (AGI). The authors note that existing research has not sufficiently explored the interaction-related abilities of these models, such as distance perception and memory. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce iWorld-Bench, a comprehensive benchmark designed for training and testing world models on interaction tasks. The dataset comprises 330,000 video clips, from which 2,100 high-quality samples are selected to ensure diversity in perspectives, weather conditions, and scenes. To facilitate a unified evaluation framework, the authors propose an Action Generation Framework that encompasses six distinct task types, generating an additional 4,900 test samples. These tasks are designed to assess model performance across various dimensions, including visual generation, trajectory following, and memory retention. The evaluation involves 14 representative world models, allowing for a comparative analysis of their interaction capabilities.

**Results**  
The evaluation of the 14 world models on the iWorld-Bench benchmark reveals significant performance disparities. The authors provide detailed metrics, although specific headline numbers are not disclosed in the abstract. The results highlight key limitations in existing models, particularly in their ability to handle complex interaction scenarios. The iWorld-Bench leaderboard is made publicly available, enabling ongoing comparisons and fostering community engagement in this research area.

**Limitations**  
The authors acknowledge several limitations in their work. First, the benchmark may not cover all possible interaction modalities, potentially restricting the generalizability of the findings. Additionally, the reliance on video clips may introduce biases related to the quality and variability of the data. The authors also note that the benchmark is still in its early stages, and further iterations may be necessary to refine the tasks and evaluation metrics. An obvious limitation not explicitly mentioned is the potential computational overhead associated with training and evaluating multiple world models on the extensive dataset.

**Why it matters**  
The introduction of iWorld-Bench has significant implications for the field of interactive world models and AGI research. By providing a standardized framework for evaluating interaction capabilities, this benchmark can facilitate more rigorous comparisons between models, driving improvements in their design and performance. The insights gained from the evaluation of existing models can inform future research directions, particularly in enhancing memory and perception in interactive environments. Furthermore, the publicly available leaderboard encourages collaboration and competition within the research community, potentially accelerating advancements in the development of robust interactive agents.

Authors: Jianjie Fang, Yingshan Lei, Qin Wan, Ziyou Wang, Yuchao Huang, Yongyan Xu, Baining Zhao, Weichen Zhang et al.  
Source: arXiv:2605.03941  
URL: [https://arxiv.org/abs/2605.03941v1](https://arxiv.org/abs/2605.03941v1)
