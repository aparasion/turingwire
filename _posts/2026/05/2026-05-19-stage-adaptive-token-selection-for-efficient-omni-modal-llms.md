---
title: "Stage-adaptive Token Selection for Efficient Omni-modal LLMs"
date: 2026-05-19 15:55:16 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.20035v1"
arxiv_id: "2605.20035"
authors: ["Zijie Xin", "Jie Yang", "Ruixiang Zhao", "Tianyi Wang", "Fengyun Rao", "Jing Lyu"]
slug: stage-adaptive-token-selection-for-efficient-omni-modal-llms
summary_word_count: 409
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the computational inefficiency in omni-modal large language models (om-LLMs) due to the processing of dense non-textual tokens, specifically in the context of audio-visual understanding. Existing token selection methods are limited as they either focus solely on visual inputs or apply fixed per-modality ratios for pruning, neglecting the dynamic nature of token importance across different layers of the model. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce SEATS (Stage-adaptive Token Selection), a training-free method designed to enhance the efficiency of om-LLM inference. SEATS operates in two stages: 

1. **Pre-LLM Token Selection**: It employs attention-weighted diversity selection to eliminate spatiotemporal redundancy before the tokens are fed into the LLM.
2. **In-LLM Token Pruning**: Within the LLM, SEATS progressively prunes tokens across blocks, dynamically adjusting the retention budget between modalities based on query relevance scores. In the late layers, it completely removes non-textual tokens once cross-modal fusion is achieved.

The method leverages an analysis of layer-wise token dependencies, revealing that visual and audio dependencies diminish with depth, allowing for more aggressive pruning in later layers.

**Results**  
SEATS was evaluated on the Qwen2.5-Omni and Qwen3-Omni benchmarks. The method demonstrated a significant reduction in computational overhead, achieving a 9.3x reduction in FLOPs and a 4.8x speedup in prefill time while retaining 96.3% of the original model's performance. These results indicate that SEATS effectively balances efficiency and performance, outperforming existing token selection strategies that do not adapt to layer-wise token importance.

**Limitations**  
The authors acknowledge that SEATS is a training-free approach, which may limit its adaptability compared to methods that incorporate training-based token selection. Additionally, the analysis of layer-wise dependencies may not generalize across all om-LLMs, and the method's performance on other architectures or datasets remains untested. The reliance on query relevance scores for dynamic budget allocation may also introduce variability based on the specific tasks or modalities involved.

**Why it matters**  
The development of SEATS has significant implications for the deployment of om-LLMs in resource-constrained environments, where computational efficiency is paramount. By effectively reducing the number of tokens processed without sacrificing performance, SEATS paves the way for more scalable omni-modal applications, such as real-time audio-visual processing and interactive AI systems. This work encourages further exploration into adaptive token selection strategies that can enhance the efficiency of large-scale models across various modalities.

Authors: Zijie Xin, Jie Yang, Ruixiang Zhao, Tianyi Wang, Fengyun Rao, Jing Lyu, Xirong Li  
Source: arXiv:2605.20035  
URL: [https://arxiv.org/abs/2605.20035v1](https://arxiv.org/abs/2605.20035v1)
