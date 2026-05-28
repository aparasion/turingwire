---
title: "Misalignment Between Backpropagation and the Hierarchy of Brain Responses to Images"
date: 2026-05-27 16:20:31 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.28693v1"
arxiv_id: "2605.28693"
authors: ["Jos\u00e9phine Raugel", "Maximilian Seitzer", "Marc Szafraniec", "Huy V. Vo", "J\u00e9r\u00e9my Rapin", "Patrick Labatut"]
slug: misalignment-between-backpropagation-and-the-hierarchy-of-br
summary_word_count: 452
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding the relationship between backpropagation, a fundamental algorithm in deep learning, and the neural mechanisms of the human brain. While prior research has established that forward activations of deep learning models correlate with the cortical hierarchy of visual processing, the correspondence of backpropagated gradients to brain responses remains unexplored. This study investigates whether backpropagation aligns with the spatial and temporal organization of neural responses in the human visual cortex.

**Method**  
The authors employ functional magnetic resonance imaging (fMRI) and magnetoencephalography (MEG) to analyze human brain responses to natural images. They extend standard encoding analyses to map backpropagated gradients from a self-supervised vision model, DINOv3, onto neural data. The study reproduces findings across eight different vision models, focusing on the prediction of fMRI and MEG signals specifically in higher-level visual cortex regions and at later latencies. The analysis involves comparing the spatial and temporal organization of backpropagated gradients with the expected patterns derived from a biologically plausible backpropagation mechanism.

**Results**  
The findings indicate that backpropagated gradients can reliably predict fMRI and MEG signals, particularly in higher-level visual areas, with significant correlations observed at later latencies. However, the authors report that the spatial and temporal organization of these gradients diverges from the expected hierarchies in the human brain. Specifically, the order of gradient computation and their spatial distribution do not align with the established temporal and spatial hierarchies of visual processing in humans. This suggests a fundamental misalignment between the mechanisms of learning in deep networks and those in biological systems.

**Limitations**  
The authors acknowledge that their findings are limited by the specific models and datasets used, which may not generalize to all neural processing scenarios. Additionally, the reliance on fMRI and MEG, which have inherent spatial and temporal resolution limitations, may affect the precision of the observed correlations. The study does not explore the implications of these misalignments for the broader understanding of neural computation or the potential for alternative learning mechanisms in biological systems.

**Why it matters**  
This research has significant implications for both the fields of artificial intelligence and neuroscience. It challenges the assumption that deep learning models, particularly those using backpropagation, operate in a manner analogous to human learning processes. Understanding the discrepancies between artificial and biological learning mechanisms could inform the development of more biologically inspired learning algorithms, potentially leading to advancements in AI that better mimic human cognitive processes. Furthermore, this work may stimulate further investigation into alternative learning paradigms that align more closely with neural mechanisms, thereby enhancing our understanding of both artificial and biological intelligence.

Authors: Joséphine Raugel, Maximilian Seitzer, Marc Szafraniec, Huy V. Vo, Jérémy Rapin, Patrick Labatut, Piotr Bojanowski, Valentin Wyart et al.  
Source: arXiv:2605.28693  
URL: [https://arxiv.org/abs/2605.28693v1](https://arxiv.org/abs/2605.28693v1)
