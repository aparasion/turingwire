---
title: "Why Neighborhoods Matter: Traversal Context and Provenance in Agentic GraphRAG"
date: 2026-05-14 17:25:20 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.15109v1"
arxiv_id: "2605.15109"
authors: ["Riccardo Terrenzi", "Maximilian von Zastrow", "Serkan Ayvaz"]
slug: why-neighborhoods-matter-traversal-context-and-provenance-in
summary_word_count: 493
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the understanding of citation faithfulness within Retrieval-Augmented Generation (RAG) systems, specifically in the context of Agentic GraphRAG. Traditional approaches often evaluate citation quality based solely on the support they provide for the generated answer. However, the authors argue that this perspective is insufficient, as it neglects the importance of the entire traversal context within a knowledge graph, including the influence of visited but uncited entities. This work aims to redefine citation faithfulness as a trajectory-level problem, emphasizing the need for a more nuanced evaluation of citations that considers the graph's structure and traversal history.

**Method**  
The authors propose a series of controlled ablation experiments to investigate the impact of various graph entities on the accuracy of generated answers. They systematically isolate, remove, and mask both cited and uncited entities within the knowledge graph to assess their contributions to the final output. The experiments focus on how these manipulations affect the fidelity of the generated answers, thereby providing insights into the role of traversal context and provenance in citation evaluation. The architecture of the Agentic GraphRAG system is not explicitly detailed, but the methodology emphasizes the importance of understanding the relationships and structures within the graph during the retrieval and generation process.

**Results**  
The findings reveal that the removal of cited evidence significantly alters the generated answers, leading to a marked decrease in accuracy. Specifically, the authors report that answers generated without cited entities exhibit a substantial drop in correctness, indicating that citations are often necessary for maintaining factuality. However, the results also demonstrate that citations alone are insufficient; accurate answers frequently depend on the context provided by uncited traversal paths and the overall structure of the knowledge graph. This dual dependency suggests that a comprehensive evaluation of citation faithfulness must incorporate both cited and uncited elements of the traversal.

**Limitations**  
The authors acknowledge that their study is limited by the specific configurations of the knowledge graphs used in their experiments, which may not generalize to all graph structures or domains. Additionally, the reliance on controlled ablation may not capture the full complexity of real-world scenarios where graph traversal is less predictable. They do not address potential scalability issues related to larger graphs or the computational overhead introduced by more complex traversal evaluations.

**Why it matters**  
This work has significant implications for the design and evaluation of RAG systems, particularly those employing knowledge graphs. By advocating for a broader understanding of citation faithfulness that includes traversal context and provenance, the authors encourage future research to develop more robust metrics for citation evaluation. This shift could lead to improved accuracy and reliability in AI-generated responses, enhancing the overall trustworthiness of systems that rely on external evidence for factuality. The insights gained from this study may also inform the development of more sophisticated graph-based retrieval mechanisms in various applications, including natural language processing and knowledge representation.

Authors: Riccardo Terrenzi, Maximilian von Zastrow, Serkan Ayvaz  
Source: arXiv:2605.15109  
URL: [https://arxiv.org/abs/2605.15109v1](https://arxiv.org/abs/2605.15109v1)
