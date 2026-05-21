---
title: "E-ReCON: An Energy- and Resource-Efficient Precision-Configurable Sparse nvCIM Macro for Conventional and Spiking Neural Edge Inference"
date: 2026-05-20 05:18:27 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.NE"
source_url: "https://arxiv.org/abs/2605.20717v1"
arxiv_id: "2605.20717"
authors: ["Ankit Kumar Tenwar", "Mukul Lokhande", "Santosh Kumar Vishvakarma"]
slug: e-recon-an-energy-and-resource-efficient-precision-configura
summary_word_count: 401
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in energy and resource efficiency for digital compute-in-memory (DCIM) architectures tailored for edge-AI inference, particularly focusing on the limitations of existing ReRAM-based designs. The authors present E-ReCON, a precision-configurable sparse macro that enhances performance for both conventional convolutional neural networks (CNNs) and spiking neural networks (SNNs). This work is a preprint and has not undergone peer review.

**Method**  
E-ReCON utilizes a compact 3T1R ReRAM bitcell, occupying only 0.85 µm², which enables reliable AND-based in-memory multiplication. The architecture incorporates an interleaved 10T/28T adder tree, which reduces transistor count and power consumption by 37% and 28%, respectively, compared to a conventional 28T RCA-based design. The macro is implemented in a 65 nm CMOS process at 1.2 V, achieving a minimum latency of 0.48 ns and a throughput of 2.31-3.1 TOPS. Energy efficiency reaches up to 419 TOPS/W. The design supports 40% pruning, maintaining 99.8% of original accuracy while significantly reducing multiply-accumulate (MAC) operations and computation cycles. For SNN workloads, the AND-type bitcell facilitates efficient spike-weight multiplication, with a 2A2W configuration achieving accuracy comparable to the FP32 baseline across various networks.

**Results**  
E-ReCON demonstrates impressive performance metrics on standard benchmarks: it achieves 97.81% accuracy on MNIST/A-Z, 93.23% on CIFAR-10, and 96.51% on SVHN using LeNet-5, AlexNet, and CNN-8 models. For SNNs, the architecture maintains high accuracy across VGG-8, VGG-16, and ResNet-18 on CIFAR-10, CIFAR-100, and ImageNet-1K datasets, with performance improvements in latency and energy efficiency of 30-40% over prior ADC-based ReRAM-CIM designs. 

**Limitations**  
The authors acknowledge that while E-ReCON shows significant improvements in energy efficiency and latency, the architecture's performance may be sensitive to variations in process, voltage, and temperature (PVT) conditions, as well as ReRAM variability. Additionally, the scalability of the architecture for larger models or more complex tasks is not fully explored. The paper does not address potential trade-offs in precision or the impact of increased sparsity on inference speed.

**Why it matters**  
E-ReCON represents a significant advancement in the design of energy-efficient computing architectures for edge-AI applications, particularly in the context of IoT and biomedical sensing. Its ability to support both CNN and SNN workloads with high accuracy and low energy consumption positions it as a viable solution for next-generation neuromorphic applications. The findings could influence future research in DCIM architectures, particularly in optimizing for energy efficiency and performance in resource-constrained environments.

Authors: Ankit Kumar Tenwar, Mukul Lokhande, Santosh Kumar Vishvakarma  
Source: arXiv:2605.20717  
URL: [https://arxiv.org/abs/2605.20717v1](https://arxiv.org/abs/2605.20717v1)
