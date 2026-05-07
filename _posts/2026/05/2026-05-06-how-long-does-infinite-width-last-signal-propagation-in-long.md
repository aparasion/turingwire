---
title: "How Long Does Infinite Width Last? Signal Propagation in Long-Range Linear Recurrences"
date: 2026-05-06 16:44:44 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.05113v1"
arxiv_id: "2605.05113"
authors: ["Mariia Seleznova"]
slug: how-long-does-infinite-width-last-signal-propagation-in-long
summary_word_count: 464
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the understanding of signal propagation in linear recurrent models, particularly in the context of finite-width architectures. Existing theories predominantly focus on the infinite-width limit, leaving a lack of clarity regarding the accuracy of this approximation as the recurrent depth \( t \) increases alongside the width \( n \). This is particularly relevant for modern recurrent sequence models that operate with long input sequences, where both \( t \) and \( n \) can be large. The authors aim to delineate the conditions under which the infinite-width approximation holds and when it fails, thereby providing insights into the stability of standard initialization schemes in recurrent networks.

**Method**  
The authors derive exact finite-width formulas for the hidden state signal energies in linear recurrences initialized with complex Gaussian distributions. They categorize the joint depth-width scaling regimes into three distinct phases:  
1. **Subcritical Regime**: \( t = o(\sqrt{n}) \) - The infinite-width approximation remains valid.  
2. **Critical Regime**: \( t \sim c\sqrt{n} \) - Deviations from infinite-width predictions become significant, leading to a nontrivial joint scaling limit.  
3. **Supercritical Regime**: \( t \gg \sqrt{n} \) - Finite-width effects dominate, indicating a breakdown of the infinite-width theory.  
The analysis reveals that finite-width effects accumulate more rapidly with depth in recurrent models compared to feedforward architectures, suggesting qualitatively different signal propagation dynamics.

**Results**  
The study provides a comprehensive characterization of the scaling regimes, demonstrating that the infinite-width approximation is valid up to a depth of \( t \sim c\sqrt{n} \). The authors illustrate that in the supercritical regime, the signal propagation behavior diverges significantly from the predictions made under the infinite-width assumption. While specific numerical results and effect sizes are not detailed in the abstract, the identification of these regimes is critical for understanding the operational limits of recurrent models.

**Limitations**  
The authors acknowledge that their findings are specific to linear recurrent models and may not generalize to non-linear architectures or other types of recurrent networks. Additionally, the reliance on complex Gaussian initialization may limit the applicability of the results to practical scenarios where different initialization strategies are employed. The paper does not address the implications of these findings on training dynamics or performance metrics in real-world applications.

**Why it matters**  
This work has significant implications for the design and analysis of recurrent neural networks, particularly in understanding the limitations of infinite-width approximations in practical settings. By clarifying the conditions under which these approximations hold, the findings can inform the development of more robust initialization schemes and training strategies for deep recurrent models. Furthermore, the insights into the distinct signal propagation behaviors in recurrent versus feedforward architectures could lead to novel approaches in model architecture and training methodologies, enhancing the performance of sequence-based tasks.

Authors: Mariia Seleznova  
Source: arXiv:2605.05113  
URL: https://arxiv.org/abs/2605.05113v1
