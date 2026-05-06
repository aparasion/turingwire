---
title: "Reservoir property image slices from the Groningen gas field for image translation and segmentation"
date: 2026-05-05 16:31:11 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.03942v1"
arxiv_id: "2605.03942"
authors: ["Abdulrahman Al-Fakih", "Nabil Sariah", "Ardiansyah Koeshidayatullah", "SanLinn I. Kaka"]
slug: reservoir-property-image-slices-from-the-groningen-gas-field
summary_word_count: 411
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in publicly available geological image datasets that are essential for reproducible benchmarking in reservoir characterization workflows. While machine learning and deep learning approaches are increasingly utilized in geoscience, the lack of high-quality, openly accessible datasets hampers the development and validation of image-based methods for tasks such as segmentation and image translation. The authors aim to fill this void by providing a comprehensive dataset derived from the Groningen gas field's static geological model.

**Method**  
The core technical contribution is the creation of a high-resolution dataset consisting of aligned two-dimensional PNG images that represent various reservoir properties, including facies, porosity, permeability, and water saturation. These images are generated from three-dimensional reservoir grids, ensuring that they are suitable for downstream tasks such as visualization, segmentation, and image-to-image translation. The authors also provide a reproducible software workflow that includes processes for data augmentation, mask generation, and paired-image construction. This workflow is designed to facilitate baseline experiments and ensure that the dataset can be effectively utilized for benchmarking geological image analysis methods.

**Results**  
The dataset comprises a substantial number of image slices, although specific quantitative metrics (e.g., number of images, resolution) are not disclosed in the abstract. The authors emphasize the dataset's utility for benchmarking, but do not provide direct comparisons against existing baselines or performance metrics on standard benchmarks. The focus is on the dataset's potential for supporting various downstream tasks rather than presenting empirical results from specific model evaluations.

**Limitations**  
The authors acknowledge that the dataset is limited to the Groningen gas field, which may restrict its generalizability to other geological contexts. Additionally, while the software workflow is provided, the authors do not detail the computational resources required for processing or the specific configurations used in their experiments. The lack of empirical results comparing the dataset's utility against existing datasets or methods is another notable limitation, as it leaves the effectiveness of the resource somewhat unquantified.

**Why it matters**  
This work is significant as it provides a transparent and reproducible foundation for future research in geoscience and machine learning applications related to reservoir modeling. By offering a high-quality dataset and a comprehensive processing workflow, the authors enable researchers to benchmark their methods against a standardized resource, fostering advancements in image-based geological analysis. The implications extend to improved understanding of cross-domain relationships among reservoir properties, which can enhance predictive modeling and decision-making in resource management.

Authors: Abdulrahman Al-Fakih, Nabil Sariah, Ardiansyah Koeshidayatullah, SanLinn I. Kaka  
Source: arXiv:2605.03942  
URL: [https://arxiv.org/abs/2605.03942v1](https://arxiv.org/abs/2605.03942v1)
