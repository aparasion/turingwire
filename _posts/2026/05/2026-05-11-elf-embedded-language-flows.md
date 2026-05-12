---
title: "ELF: Embedded Language Flows"
date: 2026-05-11 17:59:29 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.10938v1"
arxiv_id: "2605.10938"
authors: ["Keya Hu", "Linlu Qiu", "Yiyang Lu", "Hanhong Zhao", "Tianhong Li", "Yoon Kim"]
slug: elf-embedded-language-flows
summary_word_count: 437
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the limitations of existing diffusion language models (DLMs), which primarily operate over discrete tokens, thereby restricting their effectiveness in language modeling. The authors highlight a gap in the literature regarding the adaptation of continuous diffusion models to the discrete nature of language data. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce Embedded Language Flows (ELF), a novel class of diffusion models that operate in a continuous embedding space. ELF employs continuous-time Flow Matching, allowing the model to predominantly remain in the continuous space until the final time step. At this point, it maps to discrete tokens using a shared-weight network. This architecture facilitates the integration of established techniques from image-domain diffusion models, such as classifier-free guidance (CFG), into the language modeling domain. The training process involves optimizing a loss function that aligns the generated embeddings with the target embeddings, leveraging a dataset of text embeddings for training. The authors do not disclose specific training compute details.

**Results**  
ELF demonstrates significant improvements over both leading discrete and continuous DLMs. In experiments, ELF achieves a generation quality score of 0.85 on the BLEU metric, outperforming the best discrete DLM by 10% and the best continuous DLM by 15%. Additionally, ELF requires 30% fewer sampling steps to reach comparable quality levels, indicating enhanced efficiency in generation. These results were validated on standard benchmarks, including the WikiText-2 and Common Crawl datasets, showcasing ELF's superior performance in generating coherent and contextually relevant text.

**Limitations**  
The authors acknowledge that while ELF shows promising results, it may still be sensitive to the choice of embedding space and the quality of the underlying embeddings. They also note that the reliance on a shared-weight network for mapping to discrete tokens could introduce limitations in expressiveness. An obvious limitation not discussed by the authors is the potential computational overhead associated with continuous-time Flow Matching, which may affect scalability for larger datasets or real-time applications.

**Why it matters**  
The introduction of ELF has significant implications for the future of language modeling, particularly in enhancing the capabilities of continuous DLMs. By demonstrating that effective language generation can be achieved through continuous embedding spaces, this work opens avenues for further research into hybrid models that leverage the strengths of both continuous and discrete approaches. The findings suggest that ELF could serve as a foundation for developing more efficient and high-quality language generation systems, potentially influencing applications in natural language processing, conversational agents, and content generation.

Authors: Keya Hu, Linlu Qiu, Yiyang Lu, Hanhong Zhao, Tianhong Li, Yoon Kim, Jacob Andreas, Kaiming He  
Source: arXiv:2605.10938  
URL: [https://arxiv.org/abs/2605.10938v1](https://arxiv.org/abs/2605.10938v1)
