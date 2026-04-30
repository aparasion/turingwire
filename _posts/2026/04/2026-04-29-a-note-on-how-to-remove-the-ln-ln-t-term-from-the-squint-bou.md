---
title: 'A Note on How to Remove the $\ln\ln T$ Term from the Squint Bound'
date: 2026-04-29 17:40:25 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2604.26926v1"
arxiv_id: "2604.26926"
authors: ["Francesco Orabona"]
slug: a-note-on-how-to-remove-the-ln-ln-t-term-from-the-squint-bou
summary_word_count: 354
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a gap in the theoretical understanding of the Squint algorithm's performance, specifically the presence of the $\ln \ln T$ term in its data-independent bound. The work builds on prior research by Orabona and Pál (2016), which introduced shifted KT potentials to mitigate this term in the context of parameter-free learning with expert bounds. This note is a preprint and has not undergone peer review.

**Method**  
The core technical contribution involves a reformulation of the Krichevsky–Trofimov (KT) algorithm's prior, which is shown to be equivalent to the application of shifted KT potentials. By modifying the prior, the author demonstrates that the $\ln \ln T$ term can be effectively removed from the Squint algorithm's data-independent bound. The paper does not disclose specific architectural details, loss functions, or training compute, as it focuses on theoretical advancements rather than empirical implementations.

**Results**  
The author provides a theoretical proof that the modified prior leads to a tighter bound for the Squint algorithm, eliminating the $\ln \ln T$ term. While specific numerical results or comparisons against established baselines are not presented in this note, the theoretical implications suggest improved performance in scenarios where the Squint algorithm is applied, particularly in contexts where the $\ln \ln T$ term would otherwise hinder its effectiveness.

**Limitations**  
The author acknowledges that the work is primarily theoretical and does not include empirical validation of the proposed modifications. Additionally, the implications of the modified prior on practical implementations of the Squint algorithm remain unexplored. The paper does not address potential computational overhead introduced by the new prior or its impact on convergence rates in practice.

**Why it matters**  
This work has significant implications for the theoretical foundations of online learning algorithms, particularly in the context of expert advice frameworks. By removing the $\ln \ln T$ term, the findings could lead to more efficient algorithms in practice, enhancing their applicability in real-world scenarios where data independence is a concern. The insights gained from this note may also inspire further research into the optimization of other online learning algorithms, potentially leading to broader advancements in the field.

Authors: Francesco Orabona  
Source: arXiv:2604.26926  
URL: https://arxiv.org/abs/2604.26926v1
