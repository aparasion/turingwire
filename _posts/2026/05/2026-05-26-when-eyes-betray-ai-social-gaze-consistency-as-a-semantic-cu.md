---
title: "When Eyes Betray AI: Social Gaze Consistency as a Semantic Cue for AI-Generated Image Detection"
date: 2026-05-26 17:50:17 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.27348v1"
arxiv_id: "2605.27348"
authors: ["Kim Jihyeon", "Sohee Kim", "Soosan Lee", "Souhwan Jung", "James Matthew Rehg", "Hyesong Choi"]
slug: when-eyes-betray-ai-social-gaze-consistency-as-a-semantic-cu
summary_word_count: 480
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of detecting AI-generated images, particularly in scenarios where generative models have effectively minimized low-level artifacts such as pixel fingerprints and frequency anomalies. Existing detection methods primarily focus on these low-level cues, which are less effective in person-centric and partial-edit contexts. The authors propose Social Gaze Consistency as a novel semantic cue that leverages the coherence of gaze direction, head-eye alignment, and pupil placement among interacting individuals, thus filling a gap in the literature regarding high-level semantic detection strategies.

**Method**  
The authors introduce three core mechanisms to operationalize Social Gaze Consistency for AI-generated image detection:  
1. **Controlled Diagnostic Dataset**: They create a dataset with region-specific perturbations of gaze-consistent imagery, ensuring strict pair-level grouping to prevent generator-fingerprint memorization. This approach emphasizes the importance of semantic coherence over mere augmentation techniques.  
2. **Block-Compositional Caption Supervision**: This method employs a fixed 5-block reasoning skeleton across 1,250 macro-combined captions, decoupling reasoning consistency from surface diversity. This allows for a more robust training signal that emphasizes semantic alignment.  
3. **Cross-architecture Validation**: The authors demonstrate that the proposed supervision method enhances a vision-language model (FakeVLM) by +3.7 percentage points on the COCOAI Interaction subset (from 67.8% to 71.5% balanced accuracy) and +1.3 percentage points on the COCOAI Person subset (from 83.0% to 84.3%). They also report consistent improvements on a vision-only backbone (Effort), indicating the backbone-agnostic nature of the cue.

**Results**  
The proposed method yields significant improvements in detection performance across multiple benchmarks. Specifically, the FakeVLM model achieves a balanced accuracy of 71.5% on the COCOAI Interaction subset and 84.3% on the COCOAI Person subset, outperforming baseline models. The simultaneous rise in real- and fake-class recalls suggests that the method avoids the common pitfall of "predict-all-fake" artifacts, indicating a more nuanced detection capability. The authors provide a mechanistic account of their findings, detailing how their training approach transfers effectively across different generative models.

**Limitations**  
The authors acknowledge that their approach may be limited by the specific nature of the gaze consistency cue, which may not generalize to all types of AI-generated imagery. Additionally, the reliance on a single inpainter (FLUX.1-Fill) for training may restrict the method's applicability to other generative architectures. The paper does not address potential biases in the dataset or the implications of gaze consistency in diverse cultural contexts.

**Why it matters**  
This work has significant implications for the field of AI-generated content detection, particularly as generative models continue to evolve. By introducing a high-level semantic cue, the authors provide a new avenue for improving detection methodologies that can complement existing low-level artifact detection techniques. The findings suggest that incorporating semantic understanding into detection frameworks can enhance robustness against increasingly sophisticated generative models, paving the way for more reliable content verification systems in various applications, including media integrity and digital forensics.

Authors: Kim Jihyeon, Sohee Kim, Soosan Lee, Souhwan Jung, James Matthew Rehg, Hyesong Choi  
Source: arXiv:2605.27348  
URL: [https://arxiv.org/abs/2605.27348v1](https://arxiv.org/abs/2605.27348v1)
