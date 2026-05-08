---
title: "Edge-specific signal propagation on mature chromophore-region 3D mechanism graphs for fluorescent protein quantum-yield prediction"
date: 2026-05-07 17:51:41 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.06644v1"
arxiv_id: "2605.06644"
authors: ["Yuchen Xiong", "Swee Keong Yeap", "Steven Aw Yoong Kit"]
slug: edge-specific-signal-propagation-on-mature-chromophore-regio
summary_word_count: 439
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in accurately predicting the quantum yield (QY) of fluorescent proteins, which is influenced by the mature chromophore's three-dimensional microenvironment rather than solely by sequence identity. Existing models, including protein language models and emission-band averages, fail to capture the local physical interactions affecting specific chromophore regions. This work proposes a novel approach to model these interactions more effectively.

**Method**  
The authors introduce a chromophore-centered mechanism graph algorithm for QY prediction. The methodology involves converting Protein Data Bank (PDB) structures into typed 3D residue graphs, which are then registered to a mature chromophore state. The graph is partitioned into three regions: phenolate, bridge, and imidazolinone. A channel-signal-region propagation technique is employed to transform these representations, resulting in 121 enrichment features. After eliminating identity shortcuts, 52 non-identity features are utilized for band-specific regression using ExtraTrees. This approach allows for intrinsic interpretability of the features, as each encodes a contact channel, seed signal, and target chromophore region.

**Results**  
On a benchmark of 531 proteins, the proposed method achieved a random cross-validation performance of R = 0.772 ± 0.008 and MAE = 0.131 ± 0.002, outperforming several model-based baselines: Band mean (R = 0.632), ESM-C (R = 0.734), and SaProt (R = 0.731). The method also excelled in bright screening tasks, achieving a Bright P@5 score of 0.704. Notably, under homology control, the method demonstrated significant advantages in the remote similarity bucket (<50%), with R = 0.697 compared to 0.633, 0.575, and 0.408 for the other models. The selected features revealed band-specific mechanisms, such as aromatic packing and clamp asymmetry in GFP-like proteins, charge/clamp balance in Red proteins, and flexibility-risk/bulky-contact features in Far-red proteins.

**Limitations**  
The authors acknowledge that their approach may be limited by the quality and diversity of the PDB structures used, as well as potential biases in the training dataset. Additionally, while the method shows promise in predicting QY, it may not generalize well to proteins outside the benchmark set. The reliance on specific feature engineering may also limit the model's adaptability to other protein classes or chromophore types.

**Why it matters**  
This work has significant implications for the field of protein engineering and fluorescence applications. By providing a more nuanced understanding of how local interactions influence QY, it opens avenues for the design of fluorescent proteins with tailored properties. The intrinsic interpretability of the model enhances its utility for researchers aiming to manipulate chromophore environments for improved fluorescence characteristics. Furthermore, the methodology could be adapted for other protein properties, potentially advancing the predictive capabilities in protein design and synthetic biology.

Authors: Yuchen Xiong, Swee Keong Yeap, Steven Aw Yoong Kit  
Source: arXiv:2605.06644  
URL: https://arxiv.org/abs/2605.06644v1
