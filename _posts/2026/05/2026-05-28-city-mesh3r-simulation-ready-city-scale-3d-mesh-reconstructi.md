---
title: "City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images"
date: 2026-05-28 17:53:26 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.30310v1"
arxiv_id: "2605.30310"
authors: ["Sayan Paul", "Sourav Ghosh", "Siddharth Katageri", "Soumyadip Maity", "Sanjana Sinha", "Brojeshwar Bhowmick"]
slug: city-mesh3r-simulation-ready-city-scale-3d-mesh-reconstructi
summary_word_count: 441
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in city-scale 3D surface reconstruction from multi-view images, particularly for applications in simulation. Existing methods, such as Neural Radiance Fields (NeRF) and Gaussian Splatting, struggle with generating complete and accurate 3D meshes due to issues like incomplete geometry and noisy surfaces. The authors highlight that scaling small-scale reconstruction techniques to urban environments is computationally prohibitive. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce City-Mesh3R, a novel end-to-end framework for reconstructing watertight surface meshes from large unordered image collections. The method employs a divide-and-conquer strategy, which includes several key components: 

1. **Topological Image Clustering**: This step organizes images into clusters based on their spatial relationships, facilitating efficient processing.
2. **Sparse Structure from Motion (SfM)**: Each cluster undergoes independent sparse SfM to generate a sparse city map without exhaustive feature matching.
3. **Map Merging**: The sparse maps from different clusters are merged to create a comprehensive representation of the city.
4. **Geometry-Aware Camera Selection**: The city map is spatially partitioned to optimize camera selection for dense reconstruction.
5. **Dense Surface Reconstruction**: This step generates detailed surface meshes, followed by curvature-aware adaptive vertex density remeshing to refine the geometry.

The entire process is designed to be scalable and efficient, allowing for the reconstruction of large urban scenes in a distributed manner.

**Results**  
City-Mesh3R was evaluated on city-scale reconstruction datasets, demonstrating significant improvements over existing baselines. The authors report that their method produces high-fidelity watertight meshes with regular geometry, effectively capturing fine surface details. While specific quantitative metrics are not disclosed in the abstract, the qualitative results indicate a marked enhancement in mesh quality compared to traditional methods.

**Limitations**  
The authors acknowledge that their approach may still face challenges in extremely complex urban environments where occlusions and varying lighting conditions could affect image quality. Additionally, the reliance on clustering may introduce biases based on the distribution of images, potentially impacting the final mesh quality. The paper does not discuss the computational resources required for the end-to-end processing, which could be a concern for practical applications.

**Why it matters**  
The development of City-Mesh3R has significant implications for urban planning, simulation, and virtual reality applications. By providing a scalable solution for city-scale 3D reconstruction, this framework can facilitate more accurate simulations of urban environments, enhancing the fidelity of analyses in fields such as urban design, disaster response, and autonomous navigation. The end-to-end nature of the method also suggests potential for integration into real-time systems, paving the way for future advancements in 3D reconstruction technologies.

Authors: Sayan Paul, Sourav Ghosh, Siddharth Katageri, Soumyadip Maity, Sanjana Sinha, Brojeshwar Bhowmick  
Source: arXiv:2605.30310  
URL: https://arxiv.org/abs/2605.30310v1
