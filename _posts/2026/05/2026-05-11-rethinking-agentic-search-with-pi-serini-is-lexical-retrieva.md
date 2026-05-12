---
title: "Rethinking Agentic Search with Pi-Serini: Is Lexical Retrieval Sufficient?"
date: 2026-05-11 16:58:57 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.10848v1"
arxiv_id: "2605.10848"
authors: ["Tz-Huan Hsu", "Jheng-Hong Yang", "Jimmy Lin"]
slug: rethinking-agentic-search-with-pi-serini-is-lexical-retrieva
summary_word_count: 442
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the capability gap in the integration of lexical retrieval systems with large language models (LLMs) in agentic search contexts. As LLMs become increasingly capable, the necessity of sophisticated retrieval mechanisms is questioned. The authors investigate whether a traditional lexical retriever, specifically BM25, can effectively support LLMs in deep research tasks, particularly in scenarios requiring reasoning and tool use.

**Method**  
The core technical contribution is the introduction of Pi-Serini, a search agent that combines BM25 with advanced LLMs, specifically gpt-5.5. Pi-Serini is equipped with three tools for retrieving, browsing, and reading documents, facilitating a comprehensive search experience. The authors conducted controlled ablation studies to assess the impact of BM25 tuning and retrieval depth on performance metrics. The tuning of BM25 parameters led to significant improvements in answer accuracy and evidence recall, with the authors reporting an 18.0% increase in answer accuracy and an 11.1% increase in surfaced evidence recall compared to the default BM25 configuration. Additionally, increasing retrieval depth yielded a 25.3% improvement in surfaced evidence recall over shallow retrieval settings.

**Results**  
On the BrowseComp-Plus benchmark, Pi-Serini achieved an answer accuracy of 83.1% and a surfaced evidence recall of 94.7%. These results surpass those of existing search agents that utilize dense retrievers, demonstrating the effectiveness of a well-tuned lexical retriever in conjunction with a capable LLM. The performance metrics indicate that the combination of BM25 and gpt-5.5 can yield superior results in deep research tasks, challenging the assumption that dense retrieval methods are inherently superior.

**Limitations**  
The authors acknowledge that their findings are contingent on the specific configurations of BM25 and the capabilities of gpt-5.5. They do not explore the performance of Pi-Serini with other LLMs or retrieval methods, which may limit generalizability. Additionally, the study does not address the computational efficiency of the proposed system compared to dense retrieval methods, which could be a critical factor in practical applications. The reliance on a single benchmark (BrowseComp-Plus) may also restrict the robustness of the conclusions drawn.

**Why it matters**  
This work has significant implications for the design of search agents in AI research and applications. By demonstrating that a well-configured lexical retriever can effectively complement advanced LLMs, the authors challenge the prevailing notion that dense retrieval systems are necessary for high-performance search tasks. This could lead to a reevaluation of resource allocation in developing search technologies, potentially favoring simpler, more interpretable systems that leverage existing lexical retrieval techniques. The findings encourage further exploration of hybrid models that combine the strengths of both lexical and dense retrieval approaches, paving the way for more efficient and effective research tools.

Authors: Tz-Huan Hsu, Jheng-Hong Yang, Jimmy Lin  
Source: arXiv cs.AI  
URL: https://arxiv.org/abs/2605.10848v1
