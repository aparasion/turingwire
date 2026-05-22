---
title: "More Context, Larger Models, or Moral Knowledge? A Systematic Study of Schwartz Value Detection in Political Texts"
date: 2026-05-21 15:46:54 +0000
category: research
subcategory: interpretability
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.22641v1"
arxiv_id: "2605.22641"
authors: ["V\u00edctor Yeste", "Paolo Rosso"]
slug: more-context-larger-models-or-moral-knowledge-a-systematic-s
summary_word_count: 426
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the challenge of detecting Schwartz values in political texts, which is complicated by implicit cues that rely on surrounding arguments and nuanced distinctions between similar values. The authors identify a gap in understanding how contextual information and explicit moral knowledge can enhance sentence-level value detection, particularly in the context of varying model architectures and input formats.

**Method**  
The study employs a systematic approach using the ValuesML/Touché ValueEval format to evaluate different input configurations: sentence-level, window-based, and full-document contexts. It contrasts no-retrieval-augmented generation (no-RAG) settings with retrieval-augmented settings that utilize a curated moral knowledge base. The models tested include supervised DeBERTa-v3-base and DeBERTa-v3-large encoders, as well as zero-shot large language models (LLMs) ranging from 12 billion to 123 billion parameters. The authors implement early fusion techniques for integrating retrieved knowledge, comparing them against late-fusion and cross-attention RAG variants. The training compute specifics are not disclosed, but the focus is on evaluating the impact of context and moral knowledge retrieval on model performance.

**Results**  
The findings reveal that full-document context enhances the performance of supervised DeBERTa encoders, yielding improvements of 3.8 to 4.8 macro-F1 points over sentence-only inputs. However, this benefit does not extend uniformly to zero-shot LLMs, indicating a nuanced relationship between context and model architecture. The integration of retrieved moral knowledge consistently improves performance across all model families and context conditions, particularly under early fusion. Notably, scaling from DeBERTa-v3-base to DeBERTa-v3-large and from 12B to larger LLMs does not guarantee performance gains. Early fusion outperforms late-fusion and cross-attention RAG methods for encoders. Per-value analyses indicate that context and retrieval are particularly beneficial for values that are socially situated or conceptually confusable.

**Limitations**  
The authors acknowledge that while their findings provide insights into the interplay of context, knowledge, and model architecture, they do not explore the effects of different moral knowledge bases or the potential for overfitting in larger models. Additionally, the study does not address the computational efficiency of the various approaches, which could impact practical deployment. The reliance on specific datasets may also limit the generalizability of the results.

**Why it matters**  
This research has significant implications for value-sensitive natural language processing (NLP), suggesting that practitioners should evaluate the interplay of context, moral knowledge, and model architecture rather than assuming that longer inputs or larger models will yield universal improvements. The insights gained from this study can inform future work in political text analysis, ethical AI, and the development of more nuanced NLP systems that account for moral dimensions in language understanding.

Authors: Víctor Yeste, Paolo Rosso  
Source: arXiv:2605.22641  
URL: [https://arxiv.org/abs/2605.22641v1](https://arxiv.org/abs/2605.22641v1)
