---
title: "GradeLegal: Automated Grading for German Legal Cases"
date: 2026-05-20 12:09:49 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.21076v1"
arxiv_id: "2605.21076"
authors: ["Abdullah Al Zubaer", "Lorenz Wendlinger", "Simon Alexander Nonn", "Michael Granitzer", "Jelena Mitrovic"]
slug: gradelegal-automated-grading-for-german-legal-cases
summary_word_count: 479
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in automated grading methodologies for German legal exam solutions, particularly in the context of increasing volumes of submissions and a shortage of qualified graders. The authors highlight the critical nature of this task, as state exam grades significantly impact career trajectories in Germany. Despite the practical importance, there is a lack of systematic studies in the literature on effective grading methods for legal exams, particularly using large language models (LLMs).

**Method**  
The authors conduct a systematic evaluation of 27 proprietary and open-source LLMs to assess their effectiveness in grading German legal case solutions in the domains of criminal and public law. The core technical contribution involves the exploration of various prompting strategies that incrementally incorporate task-related information, such as sample solutions and grading rubrics. The evaluation metric used is the quadratic weighted kappa (QWK), which quantifies the agreement between LLM-generated grades and expert human grades. The study finds that reasoning-oriented LLMs can achieve a QWK of up to 0.91 in public law when provided with a sample solution and grading rubric, while performance in criminal law is lower, with a QWK of 0.60. Additionally, the authors explore ensembling techniques, which improve grading agreement by up to 0.15 over the best individual model, suggesting that model selection and prompt design are critical for effective grading.

**Results**  
The results indicate that LLMs can approximate expert grading in public law with a QWK of 0.91, significantly outperforming the 0.60 achieved in criminal law. The study demonstrates that ensembling methods can enhance grading agreement, providing a viable alternative to stronger closed-source models. The findings underscore the importance of effective prompt design and model selection, as these factors are crucial for achieving reliable automated grading outcomes.

**Limitations**  
The authors acknowledge several limitations, including the potential biases inherent in the training data of the LLMs, which may affect grading consistency. They also note that the performance in criminal law is notably lower, indicating that this domain presents a more complex grading challenge. Furthermore, the study does not address the scalability of the proposed methods in real-world grading scenarios or the potential need for human oversight in ambiguous cases. The reliance on specific LLM architectures may also limit generalizability to other legal contexts or languages.

**Why it matters**  
This work has significant implications for the future of legal education and assessment, particularly in jurisdictions facing similar challenges of volume and grader shortages. By demonstrating the feasibility of LLMs for automated grading, the study paves the way for scalable feedback mechanisms that could enhance student learning and self-assessment. The findings also contribute to the broader discourse on the application of AI in high-stakes evaluation contexts, highlighting the need for careful model selection and prompt engineering to ensure reliability and fairness in automated grading systems.

Authors: Abdullah Al Zubaer, Lorenz Wendlinger, Simon Alexander Nonn, Michael Granitzer, Jelena Mitrovic  
Source: arXiv:2605.21076  
URL: https://arxiv.org/abs/2605.21076v1
