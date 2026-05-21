---
title: "Manga109-v2026: Revisiting Manga109 Annotations for Modern Manga Understanding"
date: 2026-05-20 13:49:13 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21182v1"
arxiv_id: "2605.21182"
authors: ["Jeonghun Baek", "Atsuyuki Miyai", "Shota Onohara", "Hikaru Ikuta", "Kiyoharu Aizawa"]
slug: manga109-v2026-revisiting-manga109-annotations-for-modern-ma
summary_word_count: 426
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of the existing Manga109 dataset, which has become a cornerstone for AI research in manga understanding, OCR, and translation. The authors identify that the current dataset suffers from transcription errors and coarse annotations that hinder its effectiveness for modern AI applications. Specifically, they highlight five categories of annotation issues: transcription errors, missing text regions, overlapping dialogue and onomatopoeia, and under-segmented speech balloons. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a revised dataset, Manga109-v2026, which involves a two-pronged approach to improve the quality of dialogue text annotations. First, they employ an OCR-based issue detection system to automatically identify problematic annotations. Following this, a manual revision process is conducted to correct the identified issues. The result is a comprehensive revision of approximately 29,000 dialogue annotations, ensuring that the new dataset aligns more closely with the requirements of contemporary OCR and multimodal understanding tasks. The authors emphasize the importance of preserving the expressive structures characteristic of manga during this revision process.

**Results**  
While specific quantitative results comparing Manga109-v2026 to its predecessor are not detailed in the abstract, the authors assert that their revisions significantly enhance the dataset's utility for modern AI applications. They suggest that the improved annotations will lead to better performance in downstream tasks such as OCR and multimodal understanding, although exact performance metrics against named baselines on specific benchmarks are not provided in the abstract.

**Limitations**  
The authors acknowledge that their approach may not completely eliminate all annotation issues, as the manual revision process is inherently limited by human error and subjectivity. Additionally, the reliance on OCR for initial issue detection may introduce its own inaccuracies, particularly in complex or stylized text typical of manga. The paper does not discuss the potential impact of these limitations on the overall performance of AI systems trained on the revised dataset.

**Why it matters**  
The revision of the Manga109 dataset to create Manga109-v2026 is significant for the field of AI research focused on manga. By addressing the annotation issues that have plagued the original dataset, this work enhances the dataset's applicability for training and evaluating AI models in OCR and multimodal understanding tasks. Improved annotations can lead to more accurate and robust AI systems capable of understanding the unique characteristics of manga, thereby advancing research in this culturally rich medium. This work sets a precedent for future dataset revisions in other domains where annotation quality is critical.

Authors: Jeonghun Baek, Atsuyuki Miyai, Shota Onohara, Hikaru Ikuta, Kiyoharu Aizawa  
Source: arXiv:2605.21182  
URL: [https://arxiv.org/abs/2605.21182v1](https://arxiv.org/abs/2605.21182v1)
