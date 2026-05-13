---
title: "From Web to Pixels: Bringing Agentic Search into Visual Perception"
date: 2026-05-12 17:59:51 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.12497v1"
arxiv_id: "2605.12497"
authors: ["Bokang Yang", "Xinyi Sun", "Kaituo Feng", "Xingping Dong", "Dongming Wu", "Xiangyu Yue"]
slug: from-web-to-pixels-bringing-agentic-search-into-visual-perce
summary_word_count: 452
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in visual perception research, particularly in scenarios where the identification of a target object requires external knowledge rather than relying solely on the image or pre-trained model knowledge. The authors formalize this challenge as "Perception Deep Research," which is particularly relevant in open-world settings where objects may not be directly visible or identifiable without additional context. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a novel benchmark called WebEye, which is designed to facilitate the evaluation of visual perception tasks that require knowledge-intensive queries. WebEye comprises 120 images, 473 annotated object instances, 645 unique question-answer pairs, and 1,927 task samples. It encompasses three distinct task views: Search-based Grounding, Search-based Segmentation, and Search-based Visual Question Answering (VQA). The core technical contribution is the Pixel-Searcher, an agentic search-to-pixel workflow that integrates evidence acquisition, identity resolution, and visual instance binding. This architecture allows for the dynamic resolution of hidden target identities, linking them to precise bounding boxes, segmentation masks, or grounded answers. The training methodology and computational resources utilized for training Pixel-Searcher are not explicitly disclosed in the paper.

**Results**  
Pixel-Searcher demonstrates superior performance across all three task views in the WebEye benchmark, outperforming existing open-source models. While specific quantitative results are not detailed in the abstract, the authors indicate that their method achieves the strongest performance metrics compared to named baselines. The primary failure modes identified include challenges in evidence acquisition, identity resolution, and the binding of visual instances, suggesting areas for further improvement.

**Limitations**  
The authors acknowledge several limitations, including the reliance on external evidence for object identification, which may not always be available or easily accessible. Additionally, the performance of Pixel-Searcher is contingent on the quality of the external knowledge sources and the complexity of the queries posed. The dataset's relatively small size (120 images) may also limit the generalizability of the findings. Furthermore, the paper does not address potential biases in the dataset or the implications of using web-sourced knowledge, which could affect the robustness of the model in diverse real-world applications.

**Why it matters**  
This work has significant implications for advancing visual perception systems, particularly in open-world scenarios where contextual knowledge is crucial for accurate object identification and localization. By formalizing the challenge and providing a structured benchmark, the authors pave the way for future research that integrates external knowledge into visual perception tasks. The introduction of the Pixel-Searcher workflow could inspire new methodologies that enhance the capabilities of AI systems in understanding and interacting with complex environments, ultimately leading to more intelligent and adaptable agents.

Authors: Bokang Yang, Xinyi Sun, Kaituo Feng, Xingping Dong, Dongming Wu, Xiangyu Yue  
Source: arXiv:2605.12497  
URL: [https://arxiv.org/abs/2605.12497v1](https://arxiv.org/abs/2605.12497v1)
