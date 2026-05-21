---
title: "Stream3D: Sequential Multi-View 3D Generation via Evidential Memory"
date: 2026-05-20 17:55:16 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.21472v1"
arxiv_id: "2605.21472"
authors: ["Kaichen Zhou", "Zeyang Bai", "Xinhai Chang", "Mengyu Wang", "Paul Liang", "Fangneng Zhan"]
slug: stream3d-sequential-multi-view-3d-generation-via-evidential-
summary_word_count: 411
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in generating temporally consistent 3D reconstructions from long monocular video streams using existing view-conditioned 3D generators, such as SAM 3D, TRELLIS, and Hunyuan3D. These models typically operate on single frames, leading to significant temporal inconsistencies when applied independently to each frame in a streaming context. The authors propose Stream3D, a novel approach that does not require retraining existing models, thus filling a critical need for efficient streaming 3D generation. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
Stream3D introduces a training-free streaming mechanism that leverages a compact evidential memory to enhance a frozen view-conditioned 3D generator. The architecture maintains a constant cross-chunk memory that selectively caches the most informative historical frames based on an evidence score mechanism. This memory dynamically updates as the stream progresses, ensuring that only a fixed number of informative frames are retained, which prevents linear growth in memory usage with increasing sequence length. The method does not require architectural changes, retraining, or auxiliary losses, making it a lightweight solution for real-time applications.

**Results**  
Stream3D was evaluated against latent-transport baselines, including KV-cache reuse and flow-based feature editing, on both realistic and synthetic streaming benchmarks. The results demonstrate that Stream3D significantly outperforms these baselines across various photometric and geometric metrics. Specific performance metrics were not disclosed in the abstract, but the authors claim substantial improvements in both quality and consistency of the generated 3D reconstructions, indicating a marked effect size over the baseline methods.

**Limitations**  
The authors acknowledge that while Stream3D effectively addresses temporal inconsistency, it may still be limited by the inherent capabilities of the underlying view-conditioned 3D generator. Additionally, the reliance on a fixed-size memory could potentially lead to loss of information from earlier frames in very long sequences. The paper does not discuss the computational overhead associated with the evidence score mechanism or the potential impact of varying frame rates in the input streams.

**Why it matters**  
The implications of Stream3D are significant for applications in robotics, augmented reality, and any domain requiring real-time 3D reconstruction from video streams. By enabling consistent 3D generation without the need for retraining, this approach can facilitate the deployment of existing models in dynamic environments, enhancing their utility in practical scenarios. Furthermore, the evidential memory mechanism could inspire future research into memory-efficient architectures for sequential data processing in other domains.

Authors: Kaichen Zhou, Zeyang Bai, Xinhai Chang, Mengyu Wang, Paul Liang, Fangneng Zhan  
Source: arXiv:2605.21472v1  
URL: https://arxiv.org/abs/2605.21472v1
