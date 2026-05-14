---
title: "Neurosymbolic Auditing of Natural-Language Software Requirements"
date: 2026-05-13 17:43:13 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13817v1"
arxiv_id: "2605.13817"
authors: ["Bethel Hall", "William Eiers"]
slug: neurosymbolic-auditing-of-natural-language-software-requirem
summary_word_count: 435
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the inadequacies in the auditing of natural-language software requirements, particularly in safety-critical domains such as medical devices. Traditional methods often fail to capture ambiguities, inconsistencies, and underspecifications in requirements, which can lead to erroneous formal models and unsafe implementations. The authors propose a novel approach that leverages large language models (LLMs) in conjunction with satisfiability modulo theories (SMT) solvers to systematically audit these requirements.

**Method**  
The core technical contribution is the VERIMED pipeline, which integrates LLMs with SMT solvers to translate natural-language requirements into formal logic. The process involves generating multiple formalizations of the same requirement to detect ambiguity through stochastic variation. The authors employ bidirectional SMT equivalence checking to identify inconsistencies and ambiguities, which manifest as SMT-inequivalent formalizations. The pipeline also utilizes counterexample-guided repair, where the granularity of symbolic feedback is crucial. The authors report that concrete SMT counterexamples significantly enhance the accuracy of requirement verification, achieving a verified accuracy of 98.5% on a hemodialysis question-answering benchmark, compared to 55.4% without such feedback.

**Results**  
The experimental evaluation demonstrates that VERIMED effectively reduces ambiguity in software requirements. On a dataset of open-source hemodialysis safety requirements, the LLM-based approach significantly outperformed traditional methods. The authors report that the stochastic variation in formalizations serves as a reliable indicator of ambiguity, and the use of SMT solvers allows for rigorous auditing of requirements. The results indicate a marked improvement in the identification of safety violations and inconsistencies, showcasing the potential of the neurosymbolic approach in enhancing requirement quality.

**Limitations**  
The authors acknowledge that the effectiveness of the approach may be contingent on the quality of the LLM and the SMT solver used. They also note that while the method shows promise in the medical domain, its generalizability to other safety-critical domains remains to be validated. Additionally, the reliance on stochastic variation may introduce noise, potentially leading to false positives in ambiguity detection. The paper does not address the computational overhead associated with generating multiple formalizations or the scalability of the approach for larger requirement sets.

**Why it matters**  
This work has significant implications for the field of software engineering, particularly in the development of safety-critical systems. By providing a systematic method for auditing natural-language requirements, the authors contribute to the ongoing efforts to enhance the reliability and safety of software systems. The integration of LLMs with formal verification techniques represents a promising direction for future research, potentially leading to more robust methodologies for requirement analysis and verification. This approach could pave the way for improved safety standards in various domains, including healthcare, automotive, and aerospace.

Authors: Bethel Hall, William Eiers  
Source: arXiv:2605.13817  
URL: https://arxiv.org/abs/2605.13817v1
