---
title: "LocateAnything: Fast and High-Quality Vision-Language Grounding with Parallel Box Decoding"
date: 2026-05-26 17:59:12 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.27365v1"
arxiv_id: "2605.27365"
authors: ["Shihao Wang", "Shilong Liu", "Yuanguo Kuang", "Xinyu Wei", "Yangzhou Liu", "Zhiqi Li"]
slug: locateanything-fast-and-high-quality-vision-language-groundi
summary_word_count: 405
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing Vision-Language Models (VLMs) that treat visual grounding and detection as a sequential token generation problem. The conventional approach serializes bounding boxes into multiple 1D tokens, which leads to inefficiencies in decoding due to the independent learning and decoding of these tokens. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel framework called LocateAnything, which utilizes Parallel Box Decoding (PBD) to decode geometric elements—bounding boxes and points—simultaneously as atomic units. This method preserves the geometric coherence of the boxes and allows for significant parallelism during the decoding process. The architecture leverages a scalable data engine and introduces LocateAnything-Data, a dataset comprising over 138 million training samples, enhancing data diversity for improved localization precision. The training compute specifics are not disclosed, but the emphasis on large-scale data suggests a substantial computational investment.

**Results**  
LocateAnything demonstrates a marked improvement in both decoding throughput and localization accuracy compared to established baselines. The paper reports that the PBD approach achieves a decoding throughput that is significantly higher than traditional methods while also enhancing high Intersection over Union (IoU) localization quality across various benchmarks. Specific performance metrics are not detailed in the abstract, but the results indicate a clear advancement in the speed-accuracy trade-off, showcasing the effectiveness of the proposed method against named baselines.

**Limitations**  
The authors acknowledge that while PBD improves efficiency and accuracy, the reliance on large-scale data may introduce challenges related to data quality and annotation consistency. Additionally, the paper does not address potential limitations in the generalizability of the model across different domains or the computational costs associated with training on such a large dataset. The impact of varying data distributions on model performance is also not discussed.

**Why it matters**  
The implications of this work are significant for the fields of visual grounding and detection, as it presents a unified framework that enhances both speed and accuracy. The introduction of Parallel Box Decoding could lead to more efficient real-time applications in areas such as autonomous driving, robotics, and augmented reality, where rapid and precise localization is critical. Furthermore, the development of a large-scale dataset like LocateAnything-Data could serve as a valuable resource for future research, potentially enabling further advancements in VLMs and related tasks.

Authors: Shihao Wang, Shilong Liu, Yuanguo Kuang, Xinyu Wei, Yangzhou Liu, Zhiqi Li, Yunze Man, Guo Chen et al.  
Source: arXiv:2605.27365  
URL: [https://arxiv.org/abs/2605.27365v1](https://arxiv.org/abs/2605.27365v1)
