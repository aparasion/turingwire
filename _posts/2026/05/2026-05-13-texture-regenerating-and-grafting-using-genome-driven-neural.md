---
title: "Texture Regenerating and Grafting Using Genome-Driven Neural Cellular Automata"
date: 2026-05-13 14:57:32 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.13630v1"
arxiv_id: "2605.13630"
authors: ["Mirela-Magdalena Catrina", "Ioana Cristina Plajer", "Alexandra B\u0103icoianu"]
slug: texture-regenerating-and-grafting-using-genome-driven-neural
summary_word_count: 439
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in multi-texture synthesis capabilities, particularly the lack of robust self-regeneration mechanisms in existing texture generation methods. Traditional approaches often fail to adaptively repair damaged textures or seamlessly combine multiple textures without extensive retraining. The authors propose a novel methodology leveraging Neural Cellular Automata (NCAs) to facilitate these processes, which is crucial for dynamic and adaptive systems in both computer graphics and broader applications.

**Method**  
The core technical contribution is a new training methodology for NCAs that emphasizes genome-driven mechanisms for texture regeneration and grafting. The authors introduce a versatile grafting technique that allows for the combination of distinct textures during the inference phase. This is achieved by initializing the NCA's genome channels with specific parameters that enable the synthesis of complex textures with fluid transitions. The training process involves a dataset of diverse textures, although specific details regarding the dataset size and composition are not disclosed. The authors do not specify the compute resources used for training, but the focus on genome-driven initialization suggests a novel approach to managing the NCA's state during texture synthesis.

**Results**  
The authors report significant improvements in texture quality and regeneration capabilities compared to baseline methods, although specific quantitative metrics (e.g., PSNR, SSIM) and named baselines are not provided in the abstract. The results indicate that the proposed method can generate high-quality textures with seamless transitions, outperforming traditional texture synthesis techniques in terms of adaptability and self-repair. The qualitative results demonstrate the effectiveness of the grafting technique, showcasing the ability to blend textures without retraining, which is a notable advancement in the field.

**Limitations**  
The authors acknowledge that their approach may be limited by the complexity of the textures used in training, which could affect the generalizability of the model to unseen textures. Additionally, the reliance on precise initialization of genome channels may pose challenges in practical applications where such initialization is not feasible. The paper does not address potential computational inefficiencies during the inference phase when combining multiple textures, nor does it explore the scalability of the method to larger or more complex texture datasets.

**Why it matters**  
This work has significant implications for the fields of computer graphics and autonomous systems, where dynamic texture synthesis and self-repair capabilities are increasingly important. The introduction of NCAs for texture regeneration and grafting opens new avenues for research in adaptive systems, potentially influencing areas such as virtual reality, game design, and material science. The ability to seamlessly combine textures without retraining could lead to more efficient workflows in graphics rendering and enhance the realism of synthetic environments.

Authors: Mirela-Magdalena Catrina, Ioana Cristina Plajer, Alexandra Băicoianu  
Source: arXiv:2605.13630  
URL: [https://arxiv.org/abs/2605.13630v1](https://arxiv.org/abs/2605.13630v1)
