---
title: "Patch-Effect Graph Kernels for LLM Interpretability"
date: 2026-05-07 16:03:47 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.06480v1"
arxiv_id: "2605.06480"
authors: ["Ruben Fernandez-Boullon", "David N. Olivieri"]
slug: patch-effect-graph-kernels-for-llm-interpretability
summary_word_count: 441
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of mechanistic interpretability in transformer models, specifically focusing on the difficulty of systematically comparing high-dimensional activation patching datasets across various prompts and task families. Existing methods struggle to provide a coherent framework for analyzing these datasets, leading to inefficiencies in identifying causal circuits within model computations.

**Method**  
The authors propose a novel framework that reformulates mechanistic analysis as a graph machine-learning problem. They represent activation-patching profiles as patch-effect graphs, which encapsulate the relationships between model components. Three distinct graph-construction methods are introduced: 
1. **Direct-influence via causal mediation** - captures direct causal relationships between activations.
2. **Partial-correlation** - identifies correlations while controlling for other variables, thus isolating specific influences.
3. **Co-influence** - assesses the joint influence of multiple components on the output.

The authors apply graph kernels to analyze these constructed graphs, allowing for the extraction of structural features that can be used for downstream classification tasks. The evaluation is conducted on the GPT-2 Small model, specifically targeting the Indirect Object Identification (IOI) task and related tasks.

**Results**  
The proposed patch-effect graphs demonstrate superior performance in preserving discriminative structural signals compared to traditional global graph-shape descriptors. Specifically, localized edge-slot features yield higher classification accuracy, outperforming baseline methods. The authors report that the causal mediation (CI) and partial-correlation (PC) methods identify candidate edges that correspond to stronger activation-influence effects than random or low-rank candidates. The framework's effectiveness is validated against rigorous controls, including prompt-only and raw patch-effect comparisons, establishing that graph features effectively compress structured patching signals. The results indicate that the proposed method provides a more nuanced understanding of model behavior, with implications for future mechanistic interpretability research.

**Limitations**  
The authors acknowledge that their approach may be limited by the complexity of the underlying model architecture and the potential for overfitting when interpreting high-dimensional graphs. Additionally, the reliance on specific tasks (IOI and related tasks) may restrict the generalizability of the findings. The paper does not address the computational overhead associated with graph construction and analysis, which could be significant for larger models or datasets.

**Why it matters**  
This work has significant implications for the field of interpretability in large language models (LLMs). By providing a structured framework for analyzing activation patching through graph representations, it enables researchers to systematically compare and evaluate mechanistic insights across diverse tasks. The ability to separate robust slice-discriminative evidence from broader causal claims enhances the rigor of interpretability studies, potentially leading to more reliable insights into model behavior and decision-making processes. This framework could serve as a foundation for future research aimed at improving the transparency and accountability of LLMs.

Authors: Ruben Fernandez-Boullon, David N. Olivieri  
Source: arXiv:2605.06480  
URL: [https://arxiv.org/abs/2605.06480v1](https://arxiv.org/abs/2605.06480v1)
