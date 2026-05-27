---
title: "Can Retrieval Heads See Images? Multimodal Retrieval Heads in Long-Context Vision-Language Models"
date: 2026-05-26 16:24:29 +0000
category: research
subcategory: multimodal
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.27243v1"
arxiv_id: "2605.27243"
authors: ["Aaron Branson Cigres Li", "Zhaowei Wang", "Yu Zhao", "Yiming Du", "Haobo Li", "Xiyu Ren"]
slug: can-retrieval-heads-see-images-multimodal-retrieval-heads-in
summary_word_count: 491
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in understanding how retrieval heads in vision-language models (VLMs) can effectively locate and utilize visual evidence in long-context scenarios. While previous research has focused on retrieval mechanisms in large language models (LLMs) using text-based evidence, the application of these methods to images remains underexplored. The authors aim to investigate the role of multimodal retrieval heads in VLMs, particularly in the context of interleaved text and images, which is critical for tasks involving complex documents and videos.

**Method**  
The authors propose a novel multimodal retrieval head detection method that quantifies the attention from question tokens to both textual and visual evidence. This method identifies the sparsity and importance of retrieval heads within the model architecture. The study reveals that only 4.4-10.2% of attention heads are responsible for 50% of the positive retrieval-score mass. The authors conduct experiments where they mask the top 5% of selected heads, leading to significant performance drops on benchmarks: MMLongBench-Doc scores plummet from 48.2% to 5.7%, and SlideVQA from 71.2% to 8.9%. In contrast, random-head masking results in minimal performance degradation. The analysis also indicates that while some retrieval heads are shared across modalities, they exhibit dynamic behavior, with image retrieval heads being more variable than text retrieval heads as context length and modality change. Additionally, the authors demonstrate that these heads can be utilized for ranking visually rich documents without further training, achieving improvements in Recall@1 on MMDocIR: 7.7/7.4 macro/micro points for page retrieval and 6.3/6.8 points for layout retrieval compared to the strongest reported baseline.

**Results**  
The core findings indicate that multimodal retrieval heads are both sparse and crucial for effective retrieval in VLMs. The performance metrics highlight the significant impact of these heads on model efficacy, with the following results:  
- MMLongBench-Doc: 48.2% to 5.7% (top-5% head masking)  
- SlideVQA: 71.2% to 8.9% (top-5% head masking)  
- MMDocIR Recall@1 improvements: 7.7/7.4 macro/micro points for page retrieval, 6.3/6.8 points for layout retrieval.

**Limitations**  
The authors acknowledge that their findings are limited to the specific architectures and datasets used in their experiments. They do not explore the generalizability of the multimodal retrieval head detection method across different VLM architectures or other modalities. Additionally, the reliance on attention scores may not capture all aspects of head importance, and the dynamic behavior of heads across varying contexts could introduce variability in performance that is not fully addressed.

**Why it matters**  
This work has significant implications for the design and training of future vision-language models, particularly in applications requiring robust retrieval capabilities across multimodal data. Understanding the role of retrieval heads can inform model architecture choices and training strategies, potentially leading to more efficient and effective VLMs for complex tasks involving long-context reasoning. The findings also pave the way for further research into optimizing retrieval mechanisms in multimodal settings.

Authors: Aaron Branson, Cigres Li, Zhaowei Wang, Yu Zhao, Yiming Du, Haobo Li, Xiyu Ren, Ginny Wong, Simon See et al.  
Source: arXiv:2605.27243  
URL: https://arxiv.org/abs/2605.27243v1
