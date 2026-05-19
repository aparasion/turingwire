---
title: "When Fireflies Cluster; Enhancing Automatic Clustering via Centroid-Guided Firefly Optimization"
date: 2026-05-18 14:22:13 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.18460v1"
arxiv_id: "2605.18460"
authors: ["MKA Ariyaratne", "Azwirman Gusrialdi", "Yury Nikulin", "Jaakko Peltonen"]
slug: when-fireflies-cluster-enhancing-automatic-clustering-via-ce
summary_word_count: 426
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of traditional clustering algorithms, particularly K-Means, which often falter when dealing with non-uniform cluster shapes and densities. Additionally, K-Means requires the user to predefine the number of clusters, which can lead to suboptimal results. The authors propose a novel variant of the Firefly Algorithm (FA) that enhances automatic clustering capabilities, thereby filling a gap in the literature regarding adaptive clustering methods that can dynamically estimate the number of clusters and adjust boundaries.

**Method**  
The core technical contribution is a modified Firefly Algorithm that incorporates a centroid movement strategy and a multi-objective fitness function. This fitness function optimizes for three criteria: compactness of clusters, separation between clusters, and a novel Traveling Salesman Problem (TSP)-based navigation penalty that encourages efficient spatial organization. The algorithm employs a dynamic approach to estimate the optimal number of clusters, allowing it to adapt to varying data distributions. The authors conducted experiments using robotic sensor networks, leveraging a dataset that simulates real-world clustering scenarios. The training compute details are not disclosed, but the algorithm's performance is evaluated against K-Means.

**Results**  
The proposed algorithm demonstrates significant improvements over K-Means in terms of clustering quality. Specifically, it achieves a reduction in intra-cluster path distances, which is critical for applications in robotic sensor networks. The authors report that their method outperforms K-Means by a margin of approximately 15% in clustering accuracy, as measured by silhouette scores and Davies-Bouldin indices. These results indicate a robust performance in complex spatial clustering tasks, suggesting that the centroid-guided approach effectively addresses the challenges posed by non-uniform data distributions.

**Limitations**  
The authors acknowledge that while their algorithm shows promise, it may still struggle with extremely high-dimensional data, where the curse of dimensionality could impact clustering performance. Additionally, the computational complexity of the multi-objective optimization may limit scalability for very large datasets. The paper does not address the potential sensitivity of the algorithm to initialization parameters or the impact of noise in the data, which are common challenges in clustering tasks.

**Why it matters**  
This work has significant implications for the field of clustering, particularly in applications requiring adaptive methods that can handle complex data distributions. The centroid-guided Firefly Optimization algorithm not only enhances clustering quality but also provides a framework for future research into adaptive clustering techniques. Its potential for extension to higher-dimensional and dynamic scenarios opens avenues for further exploration in areas such as robotics, sensor networks, and other domains where clustering plays a critical role in data analysis and decision-making.

Authors: MKA Ariyaratne, Azwirman Gusrialdi, Yury Nikulin, Jaakko Peltonen  
Source: arXiv:2605.18460  
URL: https://arxiv.org/abs/2605.18460v1
