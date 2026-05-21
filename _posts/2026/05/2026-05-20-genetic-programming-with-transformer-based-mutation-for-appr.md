---
title: "Genetic Programming with Transformer-Based Mutation for Approximate Circuit Design"
date: 2026-05-20 11:42:10 +0000
category: research
subcategory: training_methods
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.21055v1"
arxiv_id: "2605.21055"
authors: ["Ondrej Galeta", "Lukas Sekanina"]
slug: genetic-programming-with-transformer-based-mutation-for-appr
summary_word_count: 427
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations in the evolutionary design and optimization of approximate arithmetic circuits, specifically within the framework of Cartesian Genetic Programming (CGP). Traditional mutation operators in CGP often lead to stagnation, hindering the exploration of the design space. The authors propose a novel transformer-based mutation operator to enhance the diversity and effectiveness of circuit design, filling a gap in the literature regarding the integration of advanced machine learning techniques into evolutionary algorithms for circuit design.

**Method**  
The core technical contribution is the introduction of a transformer-based mutation operator that is integrated into a hybrid CGP framework. This operator is alternated with a standard mutation operator to maintain diversity in the population of circuit designs. The transformer is trained using a dataset composed of thousands of CGP chromosomes, which represent various approximate multipliers. The training scheme is designed to optimize the mutation process by leveraging the transformer’s ability to learn complex patterns in circuit design. The authors do not disclose specific details about the training compute but emphasize the computational demands of both the training and evolutionary processes.

**Results**  
The proposed method demonstrates significant improvements over existing state-of-the-art designs from the EvoApproxLib library. For various target error constraints, the approximate multipliers evolved using the transformer-based mutation operator achieve superior trade-offs in terms of area, delay, and power consumption compared to the best-known designs. The authors report that their approach yields a reduction in error rates while maintaining competitive performance metrics, although specific numerical results and effect sizes are not detailed in the abstract.

**Limitations**  
The authors acknowledge that both the training of the transformer and the evolutionary design process are computationally intensive, which may limit the scalability of their approach. They do not address potential overfitting of the transformer to the training data or the generalizability of the learned mutation patterns to other types of circuits. Additionally, the reliance on a hybrid mutation strategy may complicate the interpretability of the evolutionary process, as it combines two distinct mutation mechanisms.

**Why it matters**  
This work has significant implications for the field of approximate circuit design, particularly in the context of leveraging machine learning to enhance evolutionary algorithms. By integrating transformer-based mutation, the authors provide a novel approach that could lead to the development of more efficient and innovative circuit designs, potentially resulting in patentable technologies. The findings may inspire further research into hybrid methodologies that combine machine learning with traditional optimization techniques, paving the way for advancements in automated circuit design and other areas of hardware optimization.

Authors: Ondrej Galeta, Lukas Sekanina  
Source: arXiv:2605.21055  
URL: [https://arxiv.org/abs/2605.21055v1](https://arxiv.org/abs/2605.21055v1)
