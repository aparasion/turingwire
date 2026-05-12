---
title: "The Last Word Often Wins: A Format Confound in Chain-of-Thought Corruption Studies"
date: 2026-05-11 16:26:50 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.10799v1"
arxiv_id: "2605.10799"
authors: ["Gabriel Garcia"]
slug: the-last-word-often-wins-a-format-confound-in-chain-of-thoug
summary_word_count: 491
classification_confidence: 0.75
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the evaluation of chain-of-thought (CoT) faithfulness in language models, specifically in corruption studies. These studies traditionally assess the computational importance of various positions in a CoT by measuring accuracy when steps are corrupted. The authors identify a systematic confound: existing benchmarks often focus on chains that conclude with explicit answer statements, leading to misleading conclusions about where computation occurs versus where the answer is simply presented.

**Method**  
The authors conduct a series of experiments to demonstrate the format confound in CoT corruption studies. They employ a within-dataset format ablation on the GSM8K benchmark, where they remove only the terminal answer statement while preserving the reasoning chain. This manipulation reveals a dramatic collapse in suffix sensitivity, quantified as approximately 19 times at a model size of 3 billion parameters (N=300, p=0.022). They also perform conflicting-answer experiments across five architecture families at 7 billion parameters, observing that accuracy drops to near-zero (≤0.02) when the answer is incorrect. The followed-wrong rate varies from 0.63 to 1.00 across model sizes from 3B to 7B, with attenuation observed at larger scales (0.300 at Phi-4-14B, ~0.01 at 32B). A replication study at 7B confirms a 9.3x attenuation (N=76, p=7.8e-3), and similar patterns are observed on the MATH benchmark with a 10.9x suffix-survival recovery for DeepSeek-R1-7B. Generation-time probes reveal that the answer is not determined early in the generation process (early commitment <5%), yet model outputs consistently follow the explicit answer text during consumption. The format-determination effect persists through 14B (8.5x ratio, p=0.001) and diminishes at 32B.

**Results**  
The findings indicate that the removal of answer suffixes leads to a significant drop in accuracy, with a 19x collapse in suffix sensitivity at 3B and near-zero accuracy at 7B in conflicting-answer scenarios. The authors provide strong statistical evidence for their claims, with p-values consistently below 0.05 across multiple experiments. The replication studies further validate the results, demonstrating that the format confound is a robust phenomenon across different model architectures and sizes.

**Limitations**  
The authors acknowledge that their proposed three-prerequisite protocol for corruption-based faithfulness studies may not be universally applicable to all datasets or model architectures. Additionally, the focus on specific benchmarks like GSM8K and MATH may limit the generalizability of the findings. They do not address potential implications of the confound on other evaluation metrics or the broader landscape of model interpretability.

**Why it matters**  
This work has significant implications for the evaluation of language models, particularly in the context of CoT reasoning. By highlighting the format confound, the authors call for a reevaluation of existing benchmarks and methodologies used in corruption studies. Their proposed protocol aims to establish a more rigorous standard for assessing model faithfulness, which could lead to improved understanding and trust in AI systems' reasoning capabilities. This research encourages further exploration into the nuances of model outputs and their dependence on formatting, potentially influencing future model design and evaluation strategies.

Authors: Gabriel Garcia  
Source: arXiv:2605.10799  
URL: [https://arxiv.org/abs/2605.10799v1](https://arxiv.org/abs/2605.10799v1)
