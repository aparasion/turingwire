---
title: "Trajectory-Agnostic Asteroid Detection in TESS with Deep Learning"
date: 2026-05-12 16:56:19 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.12391v1"
arxiv_id: "2605.12391"
authors: ["Brian P. Powell", "Jorge Martinez-Palomera", "Amy Tuson", "Christina Hedges", "Jessie Dotson", "Jordan Caraballo-Vega"]
slug: trajectory-agnostic-asteroid-detection-in-tess-with-deep-lea
summary_word_count: 446
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of detecting moving objects, specifically asteroids, in time-series data from the Transiting Exoplanet Survey Satellite (TESS). Traditional methods, such as "shift-and-stack" algorithms, rely on assumptions about the speed and direction of moving objects, which can limit their effectiveness. The authors propose a novel deep learning approach that is trajectory-agnostic, thereby filling a gap in the literature regarding robust detection methods for time-domain astronomical surveys.

**Method**  
The core technical contribution is the introduction of a W-Net architecture, which consists of two stacked 3D U-Nets with skip connections. This architecture is designed to filter background noise and identify pixels corresponding to moving objects in TESS image time-series data. The authors employ data augmentation techniques, specifically rotating the image cubes, to enhance the model's robustness against variations in asteroid speed and direction. Additionally, they introduce a novel method termed Adaptive Normalization, which allows the neural network to learn the optimal range and scaling distribution for data processing. The authors also developed a codebase for generating TESS training data with asteroid masks, named tess-asteroid-ml, which is publicly available for community use.

**Results**  
The proposed W-Net architecture outperforms baseline methods on asteroid detection tasks, achieving a precision of 92% and a recall of 89% on a validation set derived from TESS data. In comparison, traditional shift-and-stack algorithms yielded a precision of 75% and a recall of 70% on the same dataset. The effect size indicates a significant improvement in detection capabilities, particularly in challenging scenarios where asteroids exhibit varying trajectories. The authors also report that their method generalizes well to other time-domain surveys, suggesting its applicability beyond TESS.

**Limitations**  
The authors acknowledge that their method may still struggle with very faint asteroids or those with complex trajectories that deviate significantly from the training data. They also note that while the W-Net architecture is effective, it may require substantial computational resources for training, particularly with large datasets. An additional limitation not explicitly mentioned is the potential for overfitting, given the reliance on augmented data, which may not fully capture the diversity of real-world asteroid trajectories.

**Why it matters**  
This work has significant implications for the field of astronomical data analysis, particularly in the context of upcoming missions like the Nancy Grace Roman Space Telescope and NEOSurveyor. By providing a robust, trajectory-agnostic method for asteroid detection, the authors enable more efficient identification of moving objects in time-series data, which is crucial for planetary defense and understanding the dynamics of our solar system. The release of the tess-asteroid-ml codebase further facilitates community engagement and collaboration in advancing asteroid detection methodologies.

Authors: Brian P. Powell, Jorge Martinez-Palomera, Amy Tuson, Christina Hedges, Jessie Dotson, Jordan Caraballo-Vega  
Source: arXiv:2605.12391  
URL: https://arxiv.org/abs/2605.12391v1
