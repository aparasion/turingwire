---
title: "Fine-tuning with Hierarchical Prompting for Robust Propaganda Classification Across Annotation Schemas"
date: 2026-05-13 15:19:46 +0000
category: research
subcategory: other
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.13663v1"
arxiv_id: "2605.13663"
authors: ["Lukas St\u00e4helin", "Veronika Solopova", "Max Upravitelev", "David Kaplan", "Ariana Sahitaj", "Premtim Sahitaj"]
slug: fine-tuning-with-hierarchical-prompting-for-robust-propagand
summary_word_count: 415
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of propaganda detection in social media, which is complicated by noisy, short texts and low inter-annotator agreement. The authors introduce a novel intent-focused taxonomy of propaganda techniques and compare it against an established schema with higher agreement. The work aims to fill the gap in understanding how different classification schemas and prompting strategies affect model performance in this domain.

**Method**  
The authors propose a hierarchical prompting method (HiPP) that first predicts fine-grained propaganda techniques before aggregating them into broader categories. They evaluate this approach using four language models: GPT-4.1-nano, Phi-4 14B, Qwen2.5-14B, and Qwen3-14B. The models are fine-tuned on the newly created HQP dataset, which features intent-based labels for propaganda techniques. The training process emphasizes the importance of fine-tuning, which transforms weak zero-shot performance into competitive results. The study systematically explores three dimensions: model portfolio, schema effects, and prompting strategy, revealing methodological differences that are obscured when using base models.

**Results**  
The results indicate that fine-tuning significantly enhances model performance across different schemas. The Qwen models (Qwen2.5-14B and Qwen3-14B) achieve the highest overall performance, while Phi-4 14B consistently outperforms GPT-4.1-nano. Specifically, the HiPP method shows marked improvements on the more ambiguous, low-agreement taxonomy, demonstrating its effectiveness in handling complex classification tasks. The authors report that fine-tuned models outperform zero-shot baselines by substantial margins, although exact effect sizes are not disclosed. The HQP dataset serves as a challenging benchmark for future research, providing a richer understanding of propaganda's strategic goals.

**Limitations**  
The authors acknowledge that their approach may still struggle with highly ambiguous texts and that the performance gains are contingent on the quality of the fine-tuning dataset. They do not address potential biases in the dataset or the generalizability of their findings across different languages or cultural contexts. Additionally, the reliance on large language models may limit accessibility for researchers with fewer computational resources.

**Why it matters**  
This work has significant implications for the field of natural language processing, particularly in the context of misinformation and propaganda detection. By introducing a new taxonomy and demonstrating the effectiveness of hierarchical prompting, the authors provide a framework that can enhance the robustness of classification systems in real-world applications. The HQP dataset not only serves as a benchmark but also encourages further exploration of intent-based classification, potentially influencing future research directions in social media analysis and automated content moderation.

Authors: Lukas Stähelin, Veronika Solopova, Max Upravitelev, David Kaplan, Ariana Sahitaj, Premtim Sahitaj, Charlott Jakob, Sebastian Möller et al.  
Source: arXiv:2605.13663  
URL: https://arxiv.org/abs/2605.13663v1
