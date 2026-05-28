---
title: "OpenURMA: A Clean-Room Open Implementation of the Unified Bus Protocol"
date: 2026-05-27 16:38:57 +0000
category: research
subcategory: efficiency_inference
company: "null"
secondary_companies: ["Huawei"]
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.28717v1"
arxiv_id: "2605.28717"
authors: ["Bojie Li"]
slug: openurma-a-clean-room-open-implementation-of-the-unified-bus
summary_word_count: 473
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of modern datacenter RDMA (Remote Direct Memory Access) implementations, specifically focusing on the inefficiencies introduced by the Queue Pair over PCIe abstraction inherited from InfiniBand. The authors highlight that existing NICs (Network Interface Cards) managing RoCE (RDMA over Converged Ethernet) or InfiniBand maintain extensive per-connection state, leading to significant latency due to multiple PCIe round trips. The work presents OpenURMA as a clean-room open implementation of Huawei's Unified Bus (UB) protocol, which is a public specification set to be released in 2025. This implementation aims to provide a transparent alternative to proprietary solutions, enabling researchers to explore UB's potential without the constraints of closed silicon.

**Method**  
OpenURMA's core technical contribution is the comprehensive implementation of the UB's transport and transaction layers across three distinct tiers: synthesizable RTL (Register Transfer Level) on the Alveo U50 FPGA, a cycle-level two-node SystemC simulator, and a gem5 full-system scaffold. The architecture decouples per-application endpoint state from per-host transport state, allowing for reduced connection context growth and optional ordering. The implementation leverages native CPU load/store operations to access remote memory via an on-chip bus controller, significantly enhancing performance. The authors provide a controlled comparison against a matched OpenRoCE (RoCEv2 RC) baseline, ensuring that the evaluation is rigorous and reproducible.

**Results**  
The results demonstrate that OpenURMA's load/store path achieves an end-to-end latency of approximately 500 ns for a canonical 64-byte remote fetch operation, which is 4.37 times lower than the matched baseline of 2186 ns. Additionally, OpenURMA sustains a throughput that is 2.80 times higher than that of the RoCEv2 RC implementation. The resource utilization on the Alveo U50 FPGA is also noteworthy, with the implementation fitting within approximately 14% of the available LUTs (Look-Up Tables), indicating efficient use of hardware resources.

**Limitations**  
The authors acknowledge that their implementation is a clean-room effort and may not capture all optimizations present in proprietary implementations. They do not address potential scalability issues when deploying OpenURMA in larger, more complex datacenter environments. Furthermore, the performance metrics are based on specific configurations and workloads, which may not generalize across all use cases. The paper does not discuss the implications of integrating OpenURMA with existing datacenter architectures or the potential overhead of transitioning from current RDMA protocols.

**Why it matters**  
The implications of OpenURMA are significant for the future of RDMA in datacenters. By providing an open-source alternative to proprietary solutions, it enables researchers and engineers to explore new optimizations and applications of the Unified Bus protocol without the constraints of closed systems. This work could catalyze further research into efficient memory access patterns and network protocols, potentially leading to advancements in high-performance computing and large-scale data processing. The findings also highlight the importance of protocol design in reducing latency and improving throughput, which are critical factors in modern datacenter performance.

Authors: Bojie Li  
Source: arXiv:2605.28717  
URL: https://arxiv.org/abs/2605.28717v1
