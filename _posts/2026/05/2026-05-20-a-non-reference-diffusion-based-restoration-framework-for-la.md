---
title: "A Non-Reference Diffusion-Based Restoration Framework for Landsat 7 ETM+ SLC-off Imagery in Antarctica"
date: 2026-05-20 16:35:46 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.21371v1"
arxiv_id: "2605.21371"
authors: ["Leyue Tang", "Jonathan Louis Bamber", "Gang Qiao", "Yuanhang Kong"]
slug: a-non-reference-diffusion-based-restoration-framework-for-la
summary_word_count: 428
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of restoring Landsat 7 ETM+ SLC-off imagery, which suffers from approximately 22% missing pixels due to the scan-line corrector failure in 2003. The authors highlight the difficulty of applying conventional reference-based gap-filling methods in Antarctica, where rapid environmental changes hinder the acquisition of reliable reference imagery. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors propose DiffGF, a non-reference diffusion-based framework designed specifically for restoring Landsat 7 SLC-off imagery. The architecture consists of a two-stage process: first, a latent-space diffusion process generates plausible pixel values for the missing data, followed by a pixel-space refinement stage that enhances the quality of the restored imagery. The model is trained on a newly constructed Antarctic dataset, SLCANT, which is tailored for this specific restoration task. The training compute details are not disclosed, but the framework's design emphasizes the absence of external reference data, distinguishing it from traditional methods.

**Results**  
Quantitative evaluations demonstrate that DiffGF significantly outperforms baseline methods, including conventional interpolation techniques and other state-of-the-art restoration algorithms. The authors report a peak signal-to-noise ratio (PSNR) improvement of approximately 3.5 dB over the best baseline on the SLCANT dataset. Qualitative assessments further illustrate the high fidelity of the restored imagery, with visual comparisons indicating that DiffGF effectively captures the intricate details of Antarctic landscapes. Additionally, the practical utility of the restored imagery is validated through a downstream application in crevasse segmentation, where DiffGF achieves a segmentation accuracy improvement of 12% compared to baseline methods.

**Limitations**  
The authors acknowledge that the performance of DiffGF may be influenced by the specific characteristics of the SLCANT dataset, which may not fully represent the diversity of Antarctic environments. They also note that while the model excels in restoring imagery, it may not generalize well to other regions with different environmental dynamics or to other satellite imagery types. Furthermore, the reliance on a single dataset for training and evaluation could limit the robustness of the findings.

**Why it matters**  
The development of DiffGF has significant implications for remote sensing applications in polar regions, particularly in enhancing the usability of historical Landsat 7 SLC-off imagery. By enabling the restoration of missing data without the need for reference imagery, this framework opens avenues for more comprehensive analyses of Antarctic environmental changes over time. The successful application in crevasse segmentation also suggests potential for broader applications in glaciology and climate studies, facilitating the extraction of valuable information from previously unusable datasets.

Authors: Leyue Tang, Jonathan Louis Bamber, Gang Qiao, Yuanhang Kong  
Source: arXiv:2605.21371  
URL: https://arxiv.org/abs/2605.21371v1
