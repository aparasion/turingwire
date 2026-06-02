---
title: "PaSBench-Video: A Streaming Video Benchmark for Proactive Safety Warning"
date: 2026-06-01 16:14:01 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2606.02443v1"
arxiv_id: "2606.02443"
authors: ["Yusong Zhao", "Yuejin Xie", "Youliang Yuan", "Junjie Hu", "Jitian Guo", "Yujiu Yang"]
slug: pasbench-video-a-streaming-video-benchmark-for-proactive-saf
summary_word_count: 385
classification_confidence: 0.70
source_truncated: false
layout: post
description: "This paper introduces PaSBench-Video, a benchmark for evaluating proactive safety warnings in video-capable multimodal large language models."
---

**Problem**  
The paper addresses a significant gap in the evaluation of video-capable multimodal large language models (MLLMs) for proactive safety warnings. Existing benchmarks fail to assess the temporal precision of warnings, do not account for false positives in safe scenarios, and rely on static inputs. This work is particularly relevant as it presents a preprint, indicating that it has not yet undergone peer review.

**Method**  
The authors propose PaSBench-Video, a comprehensive benchmark consisting of 740 videos categorized into 481 risk and 259 no-risk clips across four domains: driving, healthcare, daily life, and industrial production. Each risk video is annotated with frame-level risk onset and accident boundaries, allowing for a nuanced evaluation of model performance. The benchmark requires models to observe videos causally and generate warnings that are both temporally calibrated and content-correct. The authors evaluate 13 MLLMs, focusing on their ability to produce accurate warnings while minimizing false positives.

**Results**  
The evaluation reveals that no model surpasses 20.0% on the strictest metric of the benchmark. The results indicate a strong correlation (Pearson correlation of 0.64) between recall and false-positive rates, suggesting that improved detection capabilities lead to increased false alarms in safe clips. Performance varies significantly by domain; models achieve moderate recall with low false-positive rates in daily life scenarios, where risks are often anomalous. Conversely, in driving scenarios, models tend to issue warnings indiscriminately due to the similarity between routine and hazardous scenes.

**Limitations**  
The authors acknowledge several limitations, including the potential for domain-specific biases in model performance and the challenge of accurately annotating risk onset in complex video scenarios. They also note that the benchmark does not encompass all possible real-world situations, which may limit the generalizability of the findings. Additionally, the reliance on existing MLLMs may not fully capture the potential of future architectures designed specifically for proactive safety monitoring.

**Why it matters**  
The introduction of PaSBench-Video has significant implications for the development of safety-critical applications utilizing MLLMs. By providing a structured framework for evaluating the temporal and contextual accuracy of safety warnings, this benchmark can guide future research in improving model robustness and reliability in real-world scenarios. The findings underscore the necessity for models to move beyond scene-level activity recognition and incorporate reasoning about emerging risks. This work lays the groundwork for advancing proactive safety systems, as discussed in [arXiv cs.AI](https://arxiv.org/abs/2606.02443v1).
