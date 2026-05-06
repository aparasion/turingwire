---
title: "Robustness and Transferability of Pix2Geomodel for Bidirectional Facies Property Translation in a Complex Reservoir"
date: 2026-05-05 16:16:39 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.03919v1"
arxiv_id: "2605.03919"
authors: ["Abdulrahman Al-Fakih", "Nabil Sariah", "Ardiansyah Koeshidayatullah", "Sherif Hanafy", "SanLinn I. Kaka"]
slug: robustness-and-transferability-of-pix2geomodel-for-bidirecti
summary_word_count: 417
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of conventional geostatistical workflows in reservoir geomodeling, particularly in scenarios with sparse conditioning data and significant geological heterogeneity. The study evaluates the robustness and transferability of the Pix2Geomodel framework, specifically its ability to perform bidirectional facies-property translation in a complex reservoir dataset with reduced vertical support. The challenge lies in maintaining accurate facies-property relationships under constrained data conditions, which is critical for effective subsurface characterization.

**Method**  
The core technical contribution is the application of the Pix2Pix model, which employs a U-Net architecture as the generator and a PatchGAN discriminator for image-to-image translation tasks. The dataset consists of aligned two-dimensional slices extracted from a reference reservoir model, which includes facies, porosity, permeability, and clay volume (VCL). The authors augmented the dataset using consistent geometric transformations to create paired image datasets for six bidirectional tasks: facies to porosity, facies to permeability, facies to VCL, porosity to facies, permeability to facies, and VCL to facies. The model's performance was evaluated using image-based metrics, visual comparisons, and variogram-based spatial-continuity validation, ensuring a comprehensive assessment of its capabilities.

**Results**  
The Pix2Geomodel demonstrated strong performance across the evaluated tasks. The facies to porosity translation achieved a pixel accuracy of 0.9326 and a frequency-weighted intersection over union (IoU) of 0.8807, indicating high fidelity in preserving the geological architecture. The VCL to facies task yielded a mean pixel accuracy of 0.8506 and a mean IoU of 0.7049. These results suggest that the model effectively captures the dominant spatial-continuity trends and geological features, outperforming traditional methods in the context of complex reservoir modeling.

**Limitations**  
The authors acknowledge that the study is limited by the specific characteristics of the dataset used, which may not generalize to all reservoir types. Additionally, the reliance on image-based metrics may overlook certain aspects of geological realism that are critical in subsurface applications. The model's performance in extreme geological scenarios or with even sparser data remains untested, which could impact its robustness in practical applications.

**Why it matters**  
The findings of this study have significant implications for downstream work in reservoir modeling and subsurface characterization. By demonstrating the effectiveness of Pix2Geomodel in translating facies properties under challenging conditions, this research provides a practical framework for rapid and accurate geomodeling. The ability to transfer knowledge across different reservoir datasets enhances the potential for improved decision-making in resource extraction and management, ultimately contributing to more efficient and sustainable practices in the field.

Authors: Abdulrahman Al-Fakih, Nabil Sariah, Ardiansyah Koeshidayatullah, Sherif Hanafy, SanLinn I. Kaka  
Source: arXiv:2605.03919  
URL: https://arxiv.org/abs/2605.03919v1
