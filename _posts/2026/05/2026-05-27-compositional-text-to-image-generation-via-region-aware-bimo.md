---
title: "Compositional Text-to-Image Generation Via Region-aware Bimodal Direct Preference Optimization"
date: 2026-05-27 15:27:13 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.28615v1"
arxiv_id: "2605.28615"
authors: ["Zhuohan Liu", "Wujian Peng", "Yitong Chen", "Zuxuan Wu"]
slug: compositional-text-to-image-generation-via-region-aware-bimo
summary_word_count: 451
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing text-to-image (T2I) models in generating images that accurately reflect complex compositional prompts, which include intricate attribute bindings, object relationships, and counting. Despite advancements in T2I technology, the ability to generate images that align with such detailed prompts remains insufficient. The authors present this work as a preprint, indicating that it has not yet undergone peer review.

**Method**  
The authors introduce BiDPO, a novel framework designed to enhance compositional text-to-image generation. The core technical contributions include:

1. **Dataset Construction**: The authors developed a large-scale preference dataset named BiComp, which is constructed with stringent quality control measures to ensure high-quality annotations for training.
   
2. **Model Architecture**: BiDPO extends the Diffusion Direct Preference Optimization (DPO) framework, enabling the joint optimization of image and text preferences. This approach allows the model to better align generated images with complex textual descriptions.

3. **Region-Level Guidance**: To improve fine-grained alignment, the authors implement a region-aware guidance mechanism that focuses on specific image regions relevant to compositional concepts. This method enhances the model's ability to generate images that accurately reflect the specified attributes and relationships in the prompts.

4. **Training Compute**: While specific compute resources are not disclosed, the framework's reliance on a large-scale dataset and the complexity of the joint optimization suggest significant computational requirements.

**Results**  
BiDPO demonstrates substantial improvements in compositional fidelity compared to prior methods. The authors report that their approach consistently outperforms established baselines across multiple benchmarks, although specific metrics and baseline models are not detailed in the abstract. The results indicate a marked enhancement in the model's ability to generate images that adhere to complex prompts, suggesting a significant effect size in terms of performance improvement.

**Limitations**  
The authors acknowledge several limitations, including potential biases in the BiComp dataset that could affect generalization. They also note that while the region-aware guidance improves alignment, it may not fully capture all nuances of complex prompts. Additionally, the scalability of the approach in real-world applications and its performance on unseen data remain areas for further investigation. The lack of peer review may also imply that the findings should be interpreted with caution until validated by the community.

**Why it matters**  
The implications of this work are significant for downstream applications in T2I generation, particularly in fields requiring high fidelity in visual representation of complex textual descriptions, such as content creation, gaming, and virtual reality. The introduction of preference-based fine-tuning offers a flexible and scalable alternative to traditional methods, potentially paving the way for more sophisticated T2I systems that can handle intricate user inputs. This research could inspire further exploration into preference-based learning paradigms in generative models.

Authors: Zhuohan Liu, Wujian Peng, Yitong Chen, Zuxuan Wu  
Source: arXiv:2605.28615  
URL: https://arxiv.org/abs/2605.28615v1
