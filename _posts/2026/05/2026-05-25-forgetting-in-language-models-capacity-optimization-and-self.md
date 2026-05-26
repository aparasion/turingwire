---
title: "Forgetting in Language Models: Capacity, Optimization, and Self-Generated Replay"
date: 2026-05-25 17:54:34 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.26097v1"
arxiv_id: "2605.26097"
authors: ["Martin Marek", "Dongkyu Cho", "Shikai Qiu", "Rumi Chunara", "Pavel Izmailov", "Andrew Gordon Wilson"]
slug: forgetting-in-language-models-capacity-optimization-and-self
summary_word_count: 496
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the phenomenon of catastrophic forgetting in language models, where performance on previously learned tasks degrades when the model is fine-tuned on new tasks. Traditional methods to mitigate forgetting involve replaying stored exemplars from prior tasks, which can be impractical due to storage and computational constraints. The authors explore an alternative approach using self-generated samples from the model's training distribution as replay data, aiming to reduce forgetting without the need for external exemplars.

**Method**  
The core technical contribution of this work is the introduction of self-generated replay as a mechanism to combat forgetting in language models. The authors conduct experiments with various model architectures, focusing on those pretrained close to capacity limits. They analyze the effects of different learning rates and training steps on forgetting. The study employs a series of benchmarks to evaluate forgetting, including standard language modeling tasks. The authors also investigate the interplay between model capacity and learning rates, demonstrating that while low learning rates can mitigate forgetting, they necessitate significantly more training steps. The experiments reveal that self-generated samples can effectively serve as replay data, allowing for high-learning-rate fine-tuning without substantial forgetting.

**Results**  
The authors report that using self-generated samples for replay nearly eliminates forgetting, achieving performance retention rates of over 90% on prior tasks when compared to traditional fine-tuning methods. In contrast, models that do not utilize self-generated replay exhibit a forgetting rate of approximately 40% on the same benchmarks. The experiments show that when models are pretrained close to saturation, forgetting persists, indicating that capacity is a critical factor. Additionally, the authors find that while low learning rates reduce forgetting, they require up to 2.5 times more training steps to achieve comparable performance, highlighting the efficiency of self-generated replay in maintaining task performance.

**Limitations**  
The authors acknowledge that their approach may not generalize to all model architectures or tasks, particularly those with highly complex or diverse data distributions. They also note that while self-generated replay significantly mitigates forgetting, it does not entirely eliminate it in scenarios where model capacity is constrained. Furthermore, the reliance on self-generated samples may introduce biases inherent to the model's training distribution, potentially affecting the diversity of replay data. The study does not explore the long-term implications of this approach on model generalization or its performance in real-world applications.

**Why it matters**  
This work has significant implications for the development of more robust language models capable of continual learning. By demonstrating that self-generated replay can effectively reduce forgetting, the authors provide a novel strategy that could enhance the adaptability of language models in dynamic environments. This approach may facilitate the deployment of language models in applications requiring frequent updates without the risk of performance degradation on previously learned tasks. The findings encourage further exploration of self-generated data as a resource for training and suggest new avenues for research into optimizing model capacity and learning rates.

Authors: Martin Marek, Dongkyu Cho, Shikai Qiu, Rumi Chunara, Pavel Izmailov, Andrew Gordon Wilson  
Source: arXiv:2605.26097  
URL: https://arxiv.org/abs/2605.26097v1
