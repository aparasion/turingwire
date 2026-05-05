---
title: "Static Analysis of Recursive SHACL"
date: 2026-05-04 16:29:29 +0000
category: research
subcategory: theory
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02787v1"
arxiv_id: "2605.02787"
authors: ["Anouk Oudshoorn", "Magdalena Ortiz", "Mantas Simkus"]
slug: static-analysis-of-recursive-shacl
summary_word_count: 437
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the static analysis of SHACL (Shapes Constraint Language) documents, specifically the lack of tools to compare the validity of different SHACL documents. Prior research has primarily focused on the implications of shape expressions without considering the complexities introduced by recursive shape definitions and targets. The authors highlight that the problem of determining whether all graphs validating one SHACL document also validate another is undecidable under both supported and stable model semantics. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a novel approach to tackle the containment problem for SHACL documents by leveraging the well-founded semantics. They introduce a translation of SHACL under this semantics into the full hybrid mu-calculus, which allows for a more structured analysis of recursive shapes. The key technical contribution is the development of a worst-case optimal automata-based decision procedure that operates in single exponential time. This method contrasts with the undecidability results under other semantics, providing a practical solution for specific cases of SHACL documents.

**Results**  
The authors demonstrate that under well-founded semantics, the containment problem is decidable in single exponential time, which is a significant improvement over the undecidable cases presented in other semantics. While specific numerical results or comparisons against named baselines are not provided in the abstract, the authors imply that their method offers a more efficient decision-making process for SHACL document validation compared to existing approaches. The implications of this result suggest a more robust framework for static analysis in RDF data validation.

**Limitations**  
The authors acknowledge that their results are limited to the well-founded semantics and do not extend to the supported and stable model semantics, where the containment problem remains undecidable. Additionally, the paper does not address the practical implementation challenges that may arise when applying their theoretical findings to real-world SHACL documents. There is also no discussion on the scalability of their approach when applied to large datasets or complex recursive structures.

**Why it matters**  
This work has significant implications for the development of static analysis tools in the Semantic Web and RDF data validation. By establishing a decidable framework for comparing SHACL documents, the authors pave the way for enhanced validation services that can ensure data compliance more effectively. This could lead to improved data integrity and interoperability in systems that rely on RDF and SHACL for data representation and validation. Furthermore, the connection between well-founded semantics and fixed point modal logic opens new avenues for research in logic-based reasoning and automated verification in knowledge representation.

Authors: Anouk Oudshoorn, Magdalena Ortiz, Mantas Simkus  
Source: arXiv:2605.02787  
URL: https://arxiv.org/abs/2605.02787v1
