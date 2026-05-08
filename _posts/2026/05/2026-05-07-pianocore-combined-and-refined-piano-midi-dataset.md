---
title: "PianoCoRe: Combined and Refined Piano MIDI Dataset"
date: 2026-05-07 17:41:07 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.06627v1"
arxiv_id: "2605.06627"
authors: ["Ilya Borovik"]
slug: pianocore-combined-and-refined-piano-midi-dataset
summary_word_count: 392
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing symbolic music datasets used in music information retrieval (MIR) tasks, which often suffer from a narrow range of composers, lack of performance variety, absence of note-level alignments, and inconsistent naming conventions. The authors present PianoCoRe, a comprehensive and refined piano MIDI dataset that consolidates major open-source piano corpora. This work is a preprint and has not yet undergone peer review.

**Method**  
PianoCoRe comprises 250,046 performances of 5,625 pieces from 483 composers, totaling 21,763 hours of music. The dataset is released in tiered subsets:  
- **PianoCoRe-C**: For large-scale analysis and pre-training.  
- **PianoCoRe-B**: A deduplicated version for similar applications.  
- **PianoCoRe-A/A***: The note-aligned subset, which includes 157,207 performances aligned to 1,591 scores, representing the largest open-source collection of its kind.  

The authors introduce two key technical contributions:  
1. A **MIDI quality classifier** designed to detect corrupted and score-like transcriptions, enhancing the dataset's integrity.  
2. **RAScoP** (Refinement and Alignment of Score Performance), an alignment refinement pipeline that corrects temporal alignment errors and interpolates missing notes, thereby reducing temporal noise and eliminating tempo outliers.

**Results**  
The refinement process using RAScoP significantly improves the quality of the dataset. The expressive performance rendering model trained on PianoCoRe exhibits enhanced robustness to unseen pieces, outperforming models trained on smaller or raw datasets. While specific numerical results and comparisons to baseline models are not detailed in the abstract, the qualitative improvements suggest substantial effect sizes in terms of performance consistency and alignment accuracy.

**Limitations**  
The authors acknowledge that while PianoCoRe significantly enhances the quality and variety of piano MIDI datasets, it may still be limited by the inherent biases of the original corpora it consolidates. Additionally, the dataset's reliance on MIDI format may not capture the full expressiveness of live performances. The paper does not address potential issues related to the generalizability of the expressive performance rendering model across different musical genres or instruments.

**Why it matters**  
PianoCoRe serves as a foundational resource for advancing research in expressive piano performance and MIR tasks. By providing a large-scale, high-quality dataset with refined alignments, it enables researchers to develop more sophisticated models for music generation, performance analysis, and other MIR applications. The introduction of RAScoP and the MIDI quality classifier also sets a precedent for future work in dataset refinement and quality assurance in music datasets.

Authors: Ilya Borovik  
Source: arXiv:2605.06627  
URL: [https://arxiv.org/abs/2605.06627v1](https://arxiv.org/abs/2605.06627v1)
