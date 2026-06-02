---
title: "Bridging the Sim-to-Real Gap in Semiconductor Visual Program Synthesis via Input Binarization"
date: 2026-06-01 16:06:20 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.02434v1"
arxiv_id: "2606.02434"
authors: ["Yusuke Ohtsubo", "Kota Dohi", "Koichiro Yawata", "Koki Takeshita", "Tatsuya Sasaki"]
slug: bridging-the-sim-to-real-gap-in-semiconductor-visual-program
summary_word_count: 414
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper introduces a visual program synthesis framework that utilizes input binarization to bridge the sim-to-real gap in semiconductor inspection tasks."
---

**Problem**  
The paper addresses the challenge of obtaining sufficient real training data for semiconductor inspection, which is costly and difficult to acquire. Existing generative models, such as diffusion models and GANs, fail to ensure the nanometer-scale geometric accuracy required for metrology tasks. The authors propose a novel approach to mitigate the domain gap that arises when applying a Vision-Language Model (VLM) trained on synthetic data to real-world Scanning Electron Microscope (SEM) images. This work is presented as a preprint and has not undergone peer review.

**Method**  
The core technical contribution is a visual program synthesis framework that leverages a VLM to convert inspection images into editable Domain-Specific Language (DSL) code, which describes circuit geometries. This allows for precise control over the generation of training data. The VLM is trained exclusively on synthetic data rendered in DSL, which leads to a domain gap when processing real SEM images. To address this, the authors introduce an input binarization strategy that abstracts SEM-specific textures and noise, enabling the model to concentrate on the underlying geometric structures. The method emphasizes the importance of geometric fidelity in training data for effective model performance.

**Results**  
The proposed input binarization technique significantly enhances model performance on the MIIC dataset. The mean Dice coefficient, a measure of overlap between predicted and ground truth geometries, improves from 0.4393 with raw inputs to 0.5256 with binarized inputs. This represents a notable increase in performance, demonstrating that the abstraction of texture can effectively reduce the sim-to-real gap in the context of semiconductor visual program synthesis.

**Limitations**  
The authors acknowledge that their approach relies heavily on the quality of the synthetic data used for training the VLM. If the synthetic data does not accurately represent the complexities of real-world scenarios, the model's performance may still be compromised. Additionally, the input binarization method may not generalize well to other domains outside semiconductor inspection, limiting its applicability. The paper does not discuss potential computational costs associated with the binarization process or the scalability of the proposed framework.

**Why it matters**  
This work has significant implications for the field of semiconductor inspection, particularly in enhancing the efficiency and accuracy of training data generation. By bridging the sim-to-real gap, the proposed framework can facilitate the development of more robust inspection systems, ultimately leading to improved semiconductor manufacturing processes. The findings contribute to ongoing research in visual program synthesis and domain adaptation, as highlighted in related works on generative models and their applications in industrial settings, as published in [arXiv cs.AI](https://arxiv.org/abs/2606.02434v1).
