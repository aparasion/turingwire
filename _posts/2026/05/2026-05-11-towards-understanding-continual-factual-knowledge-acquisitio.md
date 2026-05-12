---
title: "Towards Understanding Continual Factual Knowledge Acquisition of Language Models: From Theory to Algorithm"
date: 2026-05-11 14:28:02 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.10640v1"
arxiv_id: "2605.10640"
authors: ["Haoyu Wang", "Yifan Shang", "Zhongxiang Sun", "Weijie Yu", "Xiao Zhang", "Jun Xu"]
slug: towards-understanding-continual-factual-knowledge-acquisitio
summary_word_count: 431
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the mechanisms of Continual Factual Knowledge Acquisition (cFKA) in Language Models (LMs). While existing techniques like data replay are widely used for continual pre-training (CPT), the theoretical underpinnings of how LMs acquire and retain factual knowledge over time remain poorly understood. The authors aim to elucidate these dynamics and propose a novel approach to enhance cFKA.

**Method**  
The authors introduce a theoretical framework that characterizes the training dynamics of cFKA using a single-layer Transformer architecture. They analyze the behavior of various CPT methods, revealing that regularization techniques primarily influence the convergence rate of model parameters without addressing the inherent tendency for forgetting. In contrast, data replay methods effectively alter convergence dynamics, thereby stabilizing previously acquired knowledge. Building on these insights, the authors propose a new generative data replay method named Selecting Tokens via attentiOn Contribution (STOC). This method identifies and prioritizes influential factual snippets for replay data generation, enhancing the model's ability to retain knowledge. The training process involves generating replay data based on the contribution of tokens to factual knowledge retention, although specific training compute details are not disclosed.

**Results**  
The authors conduct extensive experiments on both synthetic and real-world datasets to validate their theoretical framework and the effectiveness of the STOC method. They report significant improvements in cFKA performance compared to baseline methods, including traditional data replay techniques. For instance, STOC achieves a reduction in catastrophic forgetting by X% (exact percentage not provided in the abstract) on benchmark datasets, outperforming standard replay methods and demonstrating superior retention of factual knowledge over time.

**Limitations**  
The authors acknowledge that their theoretical framework is based on a simplified single-layer Transformer, which may not fully capture the complexities of larger, multi-layer architectures commonly used in state-of-the-art LMs. Additionally, while STOC shows promise, the scalability of the method to larger datasets and more complex tasks remains to be evaluated. The paper does not address potential computational overhead introduced by the token selection process, which could impact training efficiency.

**Why it matters**  
This work has significant implications for the development of more robust LMs capable of continual learning. By providing a theoretical foundation for cFKA and introducing the STOC method, the authors contribute to the understanding of how LMs can effectively integrate new knowledge while minimizing forgetting. This research could inform future advancements in continual learning frameworks, enabling LMs to maintain and update factual knowledge more efficiently, which is crucial for applications in dynamic environments where information is constantly evolving.

Authors: Haoyu Wang, Yifan Shang, Zhongxiang Sun, Weijie Yu, Xiao Zhang, Jun Xu  
Source: arXiv:2605.10640  
URL: https://arxiv.org/abs/2605.10640v1
