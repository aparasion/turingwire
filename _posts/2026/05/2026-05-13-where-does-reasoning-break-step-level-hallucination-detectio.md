---
title: "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry"
date: 2026-05-13 16:48:48 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13772v1"
arxiv_id: "2605.13772"
authors: ["Tyler Alvarez", "Ali Baheri"]
slug: where-does-reasoning-break-step-level-hallucination-detectio
summary_word_count: 447
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in existing hallucination detection methods for large language models (LLMs) during multi-step reasoning tasks. Traditional detectors typically evaluate outputs at the trace level, providing a single confidence score for the entire output without localizing the initial error. This limitation hinders the ability to identify where reasoning breaks down, particularly in complex tasks requiring multiple reasoning steps.

**Method**  
The authors propose a novel approach that frames hallucination detection as a property of the hidden-state trajectory generated during a single forward pass of the model. They introduce a label-conditioned teacher model that utilizes a contrastive PCA framework to analyze the hidden states, focusing on geometric transition features to score each reasoning step. Specifically, the teacher model computes seven geometric features that capture the transport cost of hidden-state transitions, identifying excursions from a stable manifold of correct reasoning. The student model, a BiLSTM distilled from the teacher, operates on raw hidden states without requiring inference-time labels. The authors demonstrate that contrastive PCA serves as the optimal projection for separating the first error from correct states based on transport margins. The training process involves a single forward pass, allowing for efficient first error localization.

**Results**  
The proposed models were evaluated on several benchmarks: ProcessBench, PRM800K, HaluEval, and TruthfulQA. Both the teacher and student models significantly outperformed baseline methods, including entropy-based, probing-based, and attention-based detectors. The teacher model exhibited stable transferability across different language models and datasets, while the student model's performance deteriorated under distribution shifts, a phenomenon predicted by the authors' distillation theory. The results indicate that the proposed method effectively captures the dynamics of step-level hallucination detection, with the teacher model achieving superior performance metrics across all evaluated benchmarks.

**Limitations**  
The authors acknowledge that the student model's performance is sensitive to distribution shifts, which may limit its practical deployment in real-world scenarios. Additionally, the reliance on a label-conditioned teacher model may introduce challenges in environments where labeled data is scarce. The paper does not extensively discuss the computational overhead associated with the contrastive PCA framework or the scalability of the proposed method to larger models or more complex reasoning tasks.

**Why it matters**  
This work has significant implications for the development of more robust hallucination detection mechanisms in LLMs, particularly in applications requiring reliable multi-step reasoning. By framing hallucination detection in terms of hidden-state dynamics, the authors provide a new perspective that could lead to improved methodologies for error localization and correction in LLM outputs. The identification of the transport margin as a critical factor for deployment under distribution shifts highlights an important area for future research, potentially guiding the design of more resilient models.

Authors: Tyler Alvarez, Ali Baheri  
Source: arXiv:2605.13772  
URL: https://arxiv.org/abs/2605.13772v1
