---
title: "Rethinking Visual Attribution for Chest X-ray Reasoning in Large Vision Language Models"
date: 2026-05-19 17:46:40 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.20158v1"
arxiv_id: "2605.20158"
authors: ["Guangzhi Xiong", "Qiao Jin", "Sanchit Sinha", "Zhiyong Lu", "Aidong Zhang"]
slug: rethinking-visual-attribution-for-chest-x-ray-reasoning-in-l
summary_word_count: 410
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the capability of Large Vision Language Models (LVLMs) to provide trustworthy visual attributions in medical contexts, specifically for chest X-ray (CXR) reasoning. Existing visual attribution methods lack verification against ground-truth annotations, leading to concerns about the reliability of model explanations in clinical settings. The authors highlight that current methods do not adequately confirm whether the visual evidence cited by LVLMs corresponds to the actual reasoning behind their predictions.

**Method**  
The authors introduce a causal evaluation framework that filters CXR-VQA samples to retain only those where expert-annotated regions are confirmed to be causally responsible for the model's predictions through counterfactual editing. They evaluate 11 attribution methods across six open-source LVLMs, utilizing two output modes: direct answers and step-by-step reasoning. To improve upon existing methods, they propose MedFocus, a novel concept-based attribution technique that employs unbalanced optimal transport to localize clinically relevant anatomical regions. MedFocus assesses the causal impact of these regions on model outputs via targeted interventions, producing attributions at spatial, concept, and token levels. The training compute and specific datasets used for the evaluation are not disclosed.

**Results**  
MedFocus demonstrates significant improvements over existing attribution methods. The authors report that traditional methods often fail to identify the correct visual evidence used by LVLMs, while MedFocus successfully localizes relevant anatomical regions and provides more accurate attributions. Although specific numerical results and effect sizes are not detailed in the abstract, the authors assert that MedFocus outperforms prior methods, indicating a substantial enhancement in the reliability of visual attributions for medical applications.

**Limitations**  
The authors acknowledge that their framework is limited to CXR reasoning and may not generalize to other medical imaging modalities or domains. Additionally, the reliance on expert annotations for causal verification may introduce bias, as the quality and consistency of these annotations can vary. The study does not address the computational efficiency of MedFocus compared to existing methods, which could impact its practical deployment in clinical settings.

**Why it matters**  
This work is significant as it advances the interpretability of LVLMs in medical applications, a critical factor for clinical trustworthiness. By providing a more reliable method for visual attribution, MedFocus could enhance the integration of AI in healthcare, facilitating better decision-making and patient outcomes. The implications extend to future research on model interpretability, potentially influencing the development of more robust and clinically applicable AI systems in medical imaging.

Authors: Guangzhi Xiong, Qiao Jin, Sanchit Sinha, Zhiyong Lu, Aidong Zhang  
Source: arXiv:2605.20158v1  
URL: https://arxiv.org/abs/2605.20158v1
