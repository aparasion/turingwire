---
title: "Does it Really Count? Assessing Semantic Grounding in Text-Guided Class-Agnostic Counting"
date: 2026-05-04 15:55:57 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.02752v1"
arxiv_id: "2605.02752"
authors: ["Giacomo Pacini", "Luca Ciampi", "Nicola Messina", "Nicola Tonellotto", "Giuseppe Amato", "Fabrizio Falchi"]
slug: does-it-really-count-assessing-semantic-grounding-in-text-gu
summary_word_count: 483
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a critical gap in the evaluation of text-guided class-agnostic counting (CAC) models, particularly in their ability to semantically ground textual prompts in visual scenes. Current evaluation protocols predominantly focus on counting accuracy within single-category images, neglecting the essential requirement for models to correctly interpret and align the semantics of the textual input with the visual representation of objects. The authors highlight that existing state-of-the-art CAC models often misalign the textual semantics with visual object representations, leading to unreliable counting outcomes. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel evaluation framework that includes two main contributions: (i) the introduction of PrACo++ (Prompt-Aware Counting++), which consists of two dedicated evaluation protocols—the negative-label test and the distractor test—along with new specialized metrics to assess model robustness and trustworthiness; and (ii) the creation of the MUCCA (MUlti-Category Class-Agnostic counting) dataset, which comprises real-world images annotated with multiple object categories per scene. This contrasts with existing benchmarks that typically focus on single-category images. The evaluation framework emphasizes the importance of semantic grounding in CAC tasks, providing a more comprehensive assessment of model performance.

**Results**  
The authors conducted extensive experiments on 10 state-of-the-art CAC methods, revealing that while these models perform well under traditional counting metrics, they exhibit significant deficiencies in grounding object class descriptions. The results indicate that models struggle with semantic alignment, leading to spurious counting responses. The paper quantitatively analyzes the impact of semantic similarity between prompts on model performance, demonstrating that higher semantic similarity correlates with increased counting errors. Specific performance metrics and effect sizes are not disclosed in the abstract, but the findings suggest a substantial gap between expected and actual model performance in real-world scenarios.

**Limitations**  
The authors acknowledge that their evaluation framework is still in its early stages and may require further refinement to capture the full complexity of semantic grounding in CAC tasks. They also note that the reliance on real-world images in the MUCCA dataset may introduce variability that could affect model performance assessments. Additionally, the paper does not address potential biases in the dataset or the generalizability of the proposed evaluation protocols across different domains or object classes.

**Why it matters**  
This work has significant implications for the development of more robust and semantically aware CAC models. By highlighting the misalignment between textual prompts and visual representations, the authors advocate for a paradigm shift in how CAC models are evaluated and developed. The introduction of the PrACo++ framework and the MUCCA dataset provides a foundation for future research aimed at improving the reliability and trustworthiness of text-guided counting systems in open-world scenarios. This could lead to advancements in applications such as autonomous systems, robotics, and interactive AI, where accurate object counting and semantic understanding are critical.

Authors: Giacomo Pacini, Luca Ciampi, Nicola Messina, Nicola Tonellotto, Giuseppe Amato, Fabrizio Falchi  
Source: arXiv:2605.02752  
URL: https://arxiv.org/abs/2605.02752v1
