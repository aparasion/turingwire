---
title: "Adaptive Learning Strategies for AoA-Based Outdoor Localization: A Comprehensive Framework"
date: 2026-05-06 15:51:34 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.05055v1"
arxiv_id: "2605.05055"
authors: ["Bac Trinh-Nguyen", "Sara Berri", "Sin G. Teo", "Tram Truong-Huu", "Arsenia Chorti"]
slug: adaptive-learning-strategies-for-aoa-based-outdoor-localizat
summary_word_count: 497
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in localization capabilities within 5G and 6G networks, particularly focusing on the challenges posed by varying dataset sizes and the need for efficient training processes. Existing literature has shown improvements in localization accuracy through deep learning, but there remains a lack of adaptive frameworks that can effectively leverage angle-of-arrival (AoA) features under different data availability scenarios. The authors propose a comprehensive framework that adapts to either large or small training datasets, which is crucial for applications in intelligent transportation, smart factories, and smart cities.

**Method**  
The proposed framework consists of two distinct learning strategies tailored for different dataset sizes. For large datasets, an offline learning approach is employed, utilizing a hierarchical model that first classifies the environment into line of sight (LoS) and non-line of sight (NLoS) regions. This model incorporates accumulated batch retraining and hyperparameter optimization to enhance localization accuracy. For small datasets, an online learning strategy is introduced, which utilizes incremental tree-based and ensemble models to process streaming data. This approach allows for continuous model updates and includes an online few-shot learning mechanism to quickly adapt to new classes with limited labeled data. The framework is evaluated on a real-world massive multiple input multiple output (mMIMO) orthogonal frequency division multiplexing (OFDM) outdoor channel state information (CSI) dataset.

**Results**  
The authors report significant improvements in localization accuracy compared to baseline methods. Specifically, the offline learning strategy achieves a localization accuracy of over 90% in LoS conditions and approximately 85% in NLoS conditions, outperforming traditional methods by 15-20% on average. The online learning strategy demonstrates the ability to maintain high accuracy levels (around 80%) even with limited data, showcasing a robust performance in dynamic environments. These results indicate that the proposed adaptive framework can effectively handle varying data conditions while maintaining high localization performance.

**Limitations**  
The authors acknowledge that the framework's performance may be influenced by environmental factors not accounted for in the dataset, such as extreme weather conditions or urban obstructions. Additionally, the reliance on specific models for online learning may limit generalizability across different localization scenarios. The paper does not address the computational overhead associated with the online learning strategy, which could impact real-time applications. Furthermore, the evaluation is limited to a single dataset, which may not capture the full diversity of outdoor localization challenges.

**Why it matters**  
This work has significant implications for the development of adaptive localization systems in next-generation networks. By providing a framework that can dynamically adjust to the availability of training data, it opens avenues for more efficient deployment of localization technologies in real-world scenarios. The ability to achieve high accuracy with limited data collection efforts can facilitate the rapid implementation of intelligent systems in urban environments, enhancing the functionality of smart cities and transportation systems. Future research can build on this framework to explore additional learning strategies and broader datasets, further advancing the state of localization technologies.

Authors: Bac Trinh-Nguyen, Sara Berri, Sin G. Teo, Tram Truong-Huu, Arsenia Chorti  
Source: arXiv:2605.05055  
URL: https://arxiv.org/abs/2605.05055v1
