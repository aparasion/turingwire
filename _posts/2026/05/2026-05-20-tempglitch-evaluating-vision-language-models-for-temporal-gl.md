---
title: "TempGlitch: Evaluating Vision-Language Models for Temporal Glitch Detection in Gameplay Videos"
date: 2026-05-20 17:32:26 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21443v1"
arxiv_id: "2605.21443"
authors: ["Yakun Yu", "Ashley Wiens", "Adri\u00e1n Barahona-R\u00edos", "Benedict Wilkins", "Saman Zadtootaghaj", "Nabajeet Barman"]
slug: tempglitch-evaluating-vision-language-models-for-temporal-gl
summary_word_count: 487
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of vision-language models (VLMs) for gameplay video quality assurance, specifically in the context of temporal glitch detection. Existing literature predominantly focuses on static visual anomalies, assessing models based on single-frame analysis. The authors argue that this approach neglects the complexity of temporal glitches, which manifest through changes across multiple frames. A preliminary study conducted by the authors indicates that temporal glitches present a more formidable challenge for VLMs compared to spatial glitches. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce TempGlitch, a benchmark designed specifically for evaluating temporal glitch detection in gameplay videos. TempGlitch encompasses five distinct types of temporal glitches, with a balanced dataset that includes paired glitch-free videos for reliable binary evaluation. The evaluation involves 12 VLMs, both proprietary and open-weight, across various frame-sampling configurations. The models are assessed on their ability to detect temporal glitches, with a focus on their performance in distinguishing between glitchy and non-glitchy video segments. The authors do not disclose specific architectural details, loss functions, or training compute used for the VLMs evaluated.

**Results**  
The evaluation results reveal that the current state of VLMs performs near chance levels on the TempGlitch benchmark. The models exhibit two primary failure modes: overly conservative behavior, where they fail to detect most glitches, and overly sensitive behavior, where they incorrectly flag clean videos as glitchy. The authors report that increasing frame density and model size does not consistently improve detection performance. These findings highlight the inadequacy of existing VLMs in handling temporal reasoning tasks, with no model achieving significant effect sizes over chance performance.

**Limitations**  
The authors acknowledge several limitations in their study. Firstly, the benchmark is limited to five types of temporal glitches, which may not encompass the full spectrum of potential gameplay anomalies. Additionally, the reliance on binary evaluation may oversimplify the complexity of glitch detection. The authors also note that the performance of VLMs may vary significantly based on the specific architecture and training data used, which they do not control for in their evaluation. An obvious limitation not discussed is the potential for overfitting to the benchmark due to its controlled nature, which may not generalize to real-world scenarios.

**Why it matters**  
The introduction of TempGlitch has significant implications for future research in automated gameplay quality assurance and VLM capabilities. By providing a focused testbed for temporal reasoning, this work encourages the development of more sophisticated models that can effectively handle temporal dynamics in video data. The findings underscore the need for improved methodologies in evaluating VLMs, particularly in contexts where temporal information is critical. This research could pave the way for advancements in both VLM architectures and training paradigms, ultimately enhancing the robustness of AI systems in real-time video analysis.

Authors: Yakun Yu, Ashley Wiens, Adrián Barahona-Ríos, Benedict Wilkins, Saman Zadtootaghaj, Nabajeet Barman, Cor-Paul Bezemer  
Source: arXiv:2605.21443  
URL: https://arxiv.org/abs/2605.21443v1
