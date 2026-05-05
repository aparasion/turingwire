---
title: "Triple Spectral Fusion for Sensor-based Human Activity Recognition"
date: 2026-05-04 15:42:58 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02743v1"
arxiv_id: "2605.02743"
authors: ["Ye Zhang", "Longguang Wang", "Qing Gao", "Chaocan Xiang", "Mohammed Bennamoun", "Yulan Guo"]
slug: triple-spectral-fusion-for-sensor-based-human-activity-recog
summary_word_count: 410
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations in sensor-based human activity recognition (HAR) systems, particularly the challenges in fusing heterogeneous sensor data from Inertial Measurement Units (IMUs) and establishing long-term context correlations. Despite advancements in learning-based methods, existing approaches struggle with temporal information fusion due to the complexity of integrating diverse data types. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel framework called Triple Spectral Fusion (TSF) for HAR, which employs an adaptive complementary filtering technique to suppress noise and organizes IMU sensors into posture and motion modality nodes. The framework treats IMU nodes as a dynamic heterogeneous graph, applying adaptive filtering in the Fourier, graph Fourier, and wavelet domains to facilitate effective multi-sensor fusion. Specifically, the adaptive filtering in the graph Fourier domain merges both homogeneous and heterogeneous node information, while the adaptive wavelet frequency selection reduces context redundancy and shortens feature lengths. This multi-domain approach enhances timestamp-based graph aggregation and improves long-term context correlation.

**Results**  
The proposed TSF framework was evaluated on ten benchmark datasets, demonstrating superior performance compared to several baseline methods. The authors report significant improvements in accuracy metrics, achieving up to a 12% increase in F1-score and a 10% increase in accuracy over state-of-the-art methods such as CNNs and LSTMs. The results indicate that the TSF framework effectively captures complex temporal dependencies and context correlations, outperforming traditional HAR approaches.

**Limitations**  
The authors acknowledge several limitations, including the reliance on the quality of sensor data, which can affect the robustness of the framework. Additionally, the complexity of the proposed method may lead to increased computational overhead, which could limit its applicability in real-time scenarios. The paper does not address the scalability of the framework to larger datasets or its performance in diverse environmental conditions, which are critical for practical deployment.

**Why it matters**  
The implications of this work are significant for the field of HAR, as it introduces a robust framework for fusing heterogeneous sensor data and improving context correlation. The TSF framework's ability to enhance the accuracy of activity recognition systems can lead to advancements in various applications, including smart health monitoring, human-computer interaction, and context-aware computing. By addressing the challenges of temporal information fusion, this research paves the way for more sophisticated and reliable HAR systems, potentially influencing future research directions and applications in sensor-based technologies.

Authors: Ye Zhang, Longguang Wang, Qing Gao, Chaocan Xiang, Mohammed Bennamoun, Yulan Guo  
Source: arXiv:2605.02743  
URL: https://arxiv.org/abs/2605.02743v1
