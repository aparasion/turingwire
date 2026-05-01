---
title: "Representation Fréchet Loss for Visual Generation"
date: 2026-04-30 17:59:51 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2604.28190v1"
arxiv_id: "2604.28190"
authors: ["Jiawei Yang", "Zhengyang Geng", "Xuan Ju", "Yonglong Tian", "Yue Wang"]
slug: representation-frechet-loss-for-visual-generation
summary_word_count: 451
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of using Fréchet Distance (FD) as a training objective for generative models, which has historically been deemed impractical due to computational constraints. The authors identify a gap in the literature regarding effective optimization of FD in representation spaces, particularly in the context of visual generation tasks. They propose a novel approach that separates the population size used for FD estimation from the batch size used for gradient computation, thereby enabling practical application of FD in training.

**Method**  
The core technical contribution is the introduction of the FD-loss, which allows for the effective optimization of Fréchet Distance in representation spaces. The authors utilize a population size of 50,000 for FD estimation while employing a smaller batch size of 1,024 for gradient updates. This decoupling facilitates the training of generative models without the need for teacher distillation, adversarial training, or per-sample targets. The experiments leverage the Inception feature space for evaluation, demonstrating that post-training a base generator with FD-loss can significantly enhance visual quality. The authors also introduce FDr$^k$, a multi-representation metric that accounts for the discrepancies in visual quality rankings produced by traditional FID metrics.

**Results**  
The application of FD-loss yields notable improvements in visual quality, achieving a Fréchet Inception Distance (FID) of 0.72 on the ImageNet dataset at a resolution of 256x256 pixels using a one-step generator. This performance is benchmarked against existing state-of-the-art models, demonstrating that the FD-loss approach can transform multi-step generators into competitive one-step generators. The authors highlight that traditional FID metrics can misrank visual quality, as modern representations may produce superior samples despite yielding higher FID scores. This finding underscores the necessity for alternative evaluation metrics like FDr$^k$.

**Limitations**  
The authors acknowledge that their approach may not generalize across all generative tasks or datasets, as the effectiveness of FD-loss is demonstrated primarily within the context of visual generation using the Inception feature space. They do not address potential computational overhead associated with estimating FD over large populations, nor do they explore the implications of using different representation spaces beyond Inception. Additionally, the reliance on a specific architecture for evaluation may limit the applicability of their findings to other generative frameworks.

**Why it matters**  
This work has significant implications for the field of generative modeling, particularly in how distance metrics are utilized for training and evaluation. By demonstrating that FD can be effectively optimized in representation spaces, the authors open avenues for further research into distributional distances as both training objectives and evaluation metrics. The introduction of FDr$^k$ encourages the exploration of alternative representations, potentially leading to advancements in visual quality and model robustness in generative tasks.

Authors: Jiawei Yang, Zhengyang Geng, Xuan Ju, Yonglong Tian, Yue Wang  
Source: arXiv:2604.28190  
URL: [https://arxiv.org/abs/2604.28190v1](https://arxiv.org/abs/2604.28190v1)
