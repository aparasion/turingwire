---
title: "MAGIC: Multimodal Alignment & Grounding-aware Instruction Coreset for Vision-Language Models"
date: 2026-05-25 16:22:09 +0000
category: research
subcategory: training_methods
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.26004v1"
arxiv_id: "2605.26004"
authors: ["Shristi Das Biswas", "Kaushik Roy"]
slug: magic-multimodal-alignment-grounding-aware-instruction-cores
summary_word_count: 432
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiencies in the instruction tuning of large vision-language models (LVLMs) due to the reliance on extensive multimodal datasets that often contain redundant samples, low visual dependency, and imbalanced multimodal reasoning behaviors. The authors highlight that traditional methods of dataset selection, such as uniform subsampling or naive score-based selection, lead to suboptimal training subsets. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose MAGIC, a training-free, forward-only coreset selection method that constructs compact and behaviorally faithful subsets for multimodal instruction tuning. MAGIC leverages three intrinsic signals derived from a pretrained vision-language model:  
1. **Multimodal Gain**: Quantifies the improvement in likelihood from incorporating visual input.  
2. **Bridging Relevance**: Measures the sharpness of answer-token grounding across visual tokens.  
3. **Skill-Neuron Signatures**: Characterizes the functional computation elicited by each sample based on the top-activated feed-forward neurons.  

The selection process is executed in a three-stage pipeline:  
1. Filtering out low-gain examples.  
2. Ranking the remaining candidates using a normalized quality objective.  
3. Allocating budget bucket-wise over discrete neuron signatures to ensure comprehensive coverage of latent multimodal skills.  

This approach circumvents the need for backpropagation, auxiliary selector training, and costly clustering in continuous activation spaces, making it efficient and easily integrable into existing VLM architectures.

**Results**  
MAGIC demonstrates significant performance improvements over strong baselines when evaluated on the LLaVA-665K and Vision-Flan datasets, as well as in transfer settings to larger models (LLaVA-1.5-7B and -13B). Specifically, under matched 20% budget constraints, MAGIC achieves a relative performance of 100.3% on LLaVA-665K and 101.6% on Vision-Flan-186K compared to full finetuning. Additionally, it results in a 73.7% reduction in wall-clock run time, indicating substantial efficiency gains.

**Limitations**  
The authors acknowledge that MAGIC's performance is contingent on the quality of the pretrained VLM from which the intrinsic signals are derived. They do not address potential limitations related to the generalizability of the selected coreset across diverse multimodal tasks or the impact of dataset biases on the intrinsic signals. Furthermore, the method's reliance on specific neuron activations may limit its applicability to models with different architectures or training paradigms.

**Why it matters**  
MAGIC's introduction of a novel coreset selection methodology has significant implications for the efficiency of instruction tuning in LVLMs. By reducing the computational burden while maintaining or enhancing performance, MAGIC paves the way for more scalable and effective training processes in multimodal AI systems. This work could influence future research on dataset optimization and multimodal reasoning, potentially leading to advancements in the deployment of LVLMs in real-world applications.

Authors: Shristi Das Biswas, Kaushik Roy  
Source: arXiv:2605.26004  
URL: [https://arxiv.org/abs/2605.26004v1](https://arxiv.org/abs/2605.26004v1)
