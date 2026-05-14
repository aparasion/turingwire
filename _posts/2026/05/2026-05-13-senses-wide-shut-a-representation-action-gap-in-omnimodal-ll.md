---
title: "Senses Wide Shut: A Representation-Action Gap in Omnimodal LLMs"
date: 2026-05-13 16:14:44 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13737v1"
arxiv_id: "2605.13737"
authors: ["Trung Nguyen Quang", "Yiming Gao", "Fanyi Pu", "Kaichen Zhang", "Shuo Sun", "Ziwei Liu"]
slug: senses-wide-shut-a-representation-action-gap-in-omnimodal-ll
summary_word_count: 491
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the capabilities of omnimodal large language models (LLMs) regarding their ability to detect and respond to contradictions between textual premises and sensory inputs. While recent models are designed to process and integrate video, audio, and text, the authors highlight that the fundamental task of identifying when a textual claim conflicts with the model's own sensory observations has not been adequately tested. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The authors introduce the IMAVB benchmark, a curated dataset comprising 500 clips from long-form movies, structured in a 2x2 design that varies by target modality (vision or audio) and premise condition (standard or misleading). This allows for the assessment of conflict detection independent of typical multimodal comprehension tasks. The study evaluates eight open-source omnimodal LLMs alongside Gemini 3.1 Pro, focusing on their hidden state representations to identify the Representation-Action Gap. The authors observe two primary failure modes: under-rejection, where models accept misleading premises, and over-rejection, where they incorrectly reject standard premises. The analysis reveals that audio grounding is less effective than visual grounding, and the models exhibit resistance to prompt variations. To mitigate these issues, the authors propose a probe-guided logit adjustment (PGLA) technique, which re-injects the encoded mismatch signal into the decoding process, leading to improved rejection behavior.

**Results**  
The findings indicate a clear Representation-Action Gap, where hidden states can encode premise-perception mismatches, yet the models frequently fail to reject false claims. The performance of the models varies significantly, with the audio modality showing lower accuracy in conflict detection compared to vision. The PGLA intervention consistently enhances rejection behavior across the tested models, demonstrating a quantifiable improvement in handling misleading premises. Specific numerical results are not disclosed in the abstract, but the authors emphasize the behavioral discrepancies and the modality-asymmetric performance.

**Limitations**  
The authors acknowledge that their study is limited by the scope of the IMAVB benchmark, which may not encompass all potential scenarios of premise-perception conflict. Additionally, the reliance on curated movie clips may introduce biases that do not generalize to other forms of multimodal data. The models' resistance to prompt variations suggests a need for further exploration into prompt engineering techniques. The study does not address the computational costs associated with implementing the PGLA method or the scalability of the benchmark.

**Why it matters**  
This research has significant implications for the development of more robust omnimodal LLMs capable of accurately grounding their outputs in sensory inputs. By identifying the Representation-Action Gap, the authors provide a framework for future investigations into multimodal grounding, emphasizing the need for improved translation mechanisms between perception and action. The findings could inform the design of more effective training protocols and architectures that enhance the models' ability to discern and respond to conflicting information, ultimately advancing the field of multimodal AI.

Authors: Trung Nguyen Quang, Yiming Gao, Fanyi Pu, Kaichen Zhang, Shuo Sun, Ziwei Liu  
Source: arXiv:2605.13737  
URL: [https://arxiv.org/abs/2605.13737v1](https://arxiv.org/abs/2605.13737v1)
