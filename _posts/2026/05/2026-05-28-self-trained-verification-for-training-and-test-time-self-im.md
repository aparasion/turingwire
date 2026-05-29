---
title: "Self-Trained Verification for Training- and Test-Time Self-Improvement"
date: 2026-05-28 17:40:45 +0000
category: research
subcategory: reasoning
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.30290v1"
arxiv_id: "2605.30290"
authors: ["Chen Henry Wu", "Aditi Raghunathan"]
slug: self-trained-verification-for-training-and-test-time-self-im
summary_word_count: 458
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing verification-refinement (V-R) loops and self-training methods in reasoning models, particularly their inability to effectively catch self-generated errors due to a lack of training signal for the verifier. The authors highlight that current approaches stall when verifier scores inflate without corresponding accuracy improvements, and self-training often incorporates poor-quality self-generated data. This work aims to enhance the verification process, which is critical for both training and test-time self-improvement.

**Method**  
The authors introduce a novel approach called self-trained verification (STV), which leverages the asymmetry between a model's ability to identify errors when provided with a reference solution versus when it operates independently. The STV framework trains the verifier to imitate a more informed version of itself, effectively creating a supervision target that enhances its performance. At test time, STV is integrated into V-R loops, significantly improving their efficacy on challenging tasks. Additionally, the authors propose a training methodology termed verifier-in-the-loop training (ViL), where the generator is trained using reinforcement learning (RL) with feedback from the STV verifier. This dual approach allows for a more robust training process, capitalizing on the improved verification capabilities.

**Results**  
The implementation of STV leads to substantial performance gains on various benchmarks. Specifically, it approximately doubles the accuracy on hard math problems and achieves a 14x improvement on scientific reasoning tasks, increasing pass rates from 1.5% to 21%. In the context of ViL, starting from an RL-converged generator, the authors report a 33% increase in pass@1 metrics. Notably, the generator's standalone pass@1 performance, without the verifier at test time, improves by 30% relative to the convergence point of standard RL methods. These results demonstrate the effectiveness of STV and ViL in enhancing reasoning capabilities in complex problem domains.

**Limitations**  
The authors acknowledge that the proposed methods may still be limited by the quality of the reference solutions used for training the verifier. Additionally, the reliance on RL for generator training may introduce variability based on the initial conditions and hyperparameter settings. The paper does not address potential scalability issues when applying STV and ViL to larger datasets or more complex reasoning tasks, nor does it explore the generalizability of the approach across different model architectures.

**Why it matters**  
This work has significant implications for the future of reasoning models, particularly in enhancing their ability to self-improve through better verification mechanisms. By demonstrating that improved verification can lead to substantial gains in both training and test-time performance, the authors pave the way for more effective self-training methodologies. The insights gained from STV and ViL could inform the design of next-generation reasoning systems, potentially transforming how models are trained to handle complex tasks that require high levels of accuracy and reliability.

Authors: Chen Henry Wu, Aditi Raghunathan  
Source: arXiv:2605.30290  
URL: https://arxiv.org/abs/2605.30290v1
