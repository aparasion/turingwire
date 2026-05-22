---
title: "Cross-Species RSA Reveals Conserved Early Visual Alignment but Divergent Higher-Area Rankings Across Human fMRI and Macaque Electrophysiology"
date: 2026-05-21 12:31:18 +0000
category: research
subcategory: alignment_safety
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.22401v1"
arxiv_id: "2605.22401"
authors: ["Nils Leutenegger"]
slug: cross-species-rsa-reveals-conserved-early-visual-alignment-b
summary_word_count: 460
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the generalizability of learning rules across species, specifically between humans and macaques, in the context of visual processing. Prior work established that untrained convolutional neural networks (CNNs) align with human V1 responses, but the authors extend this investigation to macaque electrophysiology, examining whether similar learning rules yield comparable results in early and higher visual areas.

**Method**  
The study evaluates five learning rules: backpropagation (BP), feedback alignment (FA), predictive coding (PC), spike-timing-dependent plasticity (STDP), and a random-weights baseline. The macaque data is sourced from two datasets: MajajHong2015 (focusing on V4/IT with 3,200 stimulus presentations across 88/168 neurons) and FreemanZiemba2013 (targeting V1/V2 with 135 stimuli across 102/103 neurons). The authors employ representational similarity analysis (RSA) using identical model weights from their previous human study. The alignment metrics are quantified using Spearman's rank correlation coefficient (rho), with a focus on early visual cortex (V1/V2) and higher areas (IT).

**Results**  
The findings reveal that all models exhibit significantly higher alignment with macaque early visual cortex (rho = 0.15-0.30 at V1/V2) compared to human fMRI (rho = 0.01-0.08), attributed to the superior signal-to-noise ratio of electrophysiological data. Among the learning rules, STDP and PC yield the highest alignment in macaque V1/V2 (rho ~ 0.30 and 0.28, respectively), aligning with their performance in human V1. However, no correlation in learning rule rankings is observed at IT across species (Kendall's tau = 0.00, p = 1.00), likely due to the limited sample size (n = 5) and differences in stimulus sets. Notably, a pretrained ResNet-50 model (trained on ImageNet) achieves a rho of 0.25 at macaque IT, surpassing all custom CNN conditions (rho = 0.07-0.14), indicating that IT alignment is constrained more by model capacity and training data than by the learning rule itself. The study also discusses noise ceilings, variability across multiple seeds (5 seeds), and a stimulus-control analysis.

**Limitations**  
The authors acknowledge the limited power of their statistical tests due to the small sample size of learning rules (n = 5), which restricts the ability to detect correlations. Additionally, the differences in stimulus sets between species may confound the results, particularly in higher visual areas. The reliance on pretrained models raises questions about the generalizability of findings to untrained architectures.

**Why it matters**  
This research has significant implications for understanding the neural basis of visual processing across species and the effectiveness of various learning rules in neural network architectures. The demonstration of robust early visual alignment suggests that foundational visual processing mechanisms may be conserved, while the divergence in higher-area rankings highlights the influence of model capacity and training data. These insights could inform the design of more effective neural network architectures and learning paradigms that better mimic biological systems.

Authors: Nils Leutenegger  
Source: arXiv:2605.22401  
URL: https://arxiv.org/abs/2605.22401v1
