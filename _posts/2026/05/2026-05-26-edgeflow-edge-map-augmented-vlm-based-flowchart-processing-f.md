---
title: "EdgeFlow: Edge-Map Augmented VLM-Based Flowchart Processing for Industrial Requirements Engineering"
date: 2026-05-26 17:40:47 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.27332v1"
arxiv_id: "2605.27332"
authors: ["Zhifei Dou", "Shabnam Hassani", "Ou Wei"]
slug: edgeflow-edge-map-augmented-vlm-based-flowchart-processing-f
summary_word_count: 443
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in converting static flowchart images into machine-readable formats for industrial requirements engineering (RE). While Vision Language Models (VLMs) have shown potential in this domain, they often struggle with topology-critical visual details, which are essential for accurate flowchart interpretation. The authors present EdgeFlow, a method that enhances VLM performance without the need for annotated training data or domain-specific fine-tuning. This work is a preprint and has not yet undergone peer review.

**Method**  
EdgeFlow introduces a novel approach that augments the input to a VLM with a Canny edge map, which serves as a structural prior. This edge map is deterministically extracted from the flowchart images, providing critical topological information that the VLM can leverage during the conversion process. The architecture remains based on existing VLMs, but the integration of the edge map is the core technical contribution. The authors do not disclose specific details regarding the training compute or the exact VLM architecture used, focusing instead on the augmentation technique. The method is evaluated on the IndusReqFlow dataset, which consists of real-world flowchart data relevant to industrial RE.

**Results**  
EdgeFlow demonstrates significant improvements over off-the-shelf VLMs on the IndusReqFlow dataset. Specifically, it achieves a node-level F1 score improvement of 17.39 percentage points and an edge-level F1 score improvement of 16.94 percentage points. Additionally, at the path level, EdgeFlow improves path F1 by 11.06 percentage points. These results indicate that EdgeFlow effectively enhances the topology-preserving conversion of flowcharts to the Mermaid format, which is crucial for model-based testing. However, cross-dataset evaluations on a public synthetic benchmark did not yield significant improvements, suggesting that the method's effectiveness may be limited to the specific characteristics of the industrial dataset used.

**Limitations**  
The authors acknowledge that the lack of significant improvement on synthetic benchmarks indicates a need for more diverse datasets that incorporate industrial data for comprehensive evaluation. They do not address potential limitations related to the generalizability of the edge map augmentation across different types of flowcharts or the scalability of the method to larger datasets. Additionally, the reliance on a specific edge detection technique (Canny) may limit the method's applicability to flowcharts with varying styles or complexities.

**Why it matters**  
The implications of this work are significant for the field of requirements engineering, particularly in automating the conversion of visual representations into machine-readable formats. By providing a training-free method that enhances VLM performance, EdgeFlow opens avenues for more efficient model-based testing and requirements analysis in industrial contexts. The findings underscore the necessity for diverse evaluation benchmarks, which could inform the development of future VLM-based tools tailored for industrial applications.

Authors: Zhifei Dou, Shabnam Hassani, Ou Wei  
Source: arXiv:2605.27332  
URL: [https://arxiv.org/abs/2605.27332v1](https://arxiv.org/abs/2605.27332v1)
