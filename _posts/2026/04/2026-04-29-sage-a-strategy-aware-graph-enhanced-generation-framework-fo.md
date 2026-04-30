---
title: "SAGE: A Strategy-Aware Graph-Enhanced Generation Framework For Online Counseling"
date: 2026-04-29 12:56:44 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.26630v1"
arxiv_id: "2604.26630"
authors: ["Eliya Naomi Aharon", "Meytal Grimland", "Avi Segal", "Loona Ben Dayan", "Inbar Shenfeld", "Yossi Levi Belz"]
slug: sage-a-strategy-aware-graph-enhanced-generation-framework-fo
summary_word_count: 455
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inadequacy of general-purpose Large Language Models (LLMs) in effectively integrating structured clinical knowledge and real-time psychological frameworks for mental health counseling. The authors highlight that existing LLMs lack the capability for nuanced clinical reasoning, which is essential for safety and therapeutic effectiveness in high-stakes environments like online counseling. This work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The core technical contribution of this work is the SAGE (Strategy-Aware Graph-Enhanced) framework, which employs a heterogeneous graph structure to unify conversational dynamics with a psychologically grounded lexicon. The architecture consists of two main components: a Next Strategy Classifier and a Graph-Aware Attention mechanism. The Next Strategy Classifier identifies the most appropriate therapeutic intervention based on the context of the conversation. The Graph-Aware Attention mechanism then integrates graph-derived structural signals into soft prompts, conditioning the LLM to generate contextually relevant and clinically informed responses. The training process and compute resources utilized are not disclosed in the paper.

**Results**  
SAGE demonstrates significant improvements over baseline models in both strategy prediction and the quality of recommended responses. The authors report that SAGE achieves a 15% increase in accuracy for strategy prediction compared to a standard LLM baseline. In terms of response quality, SAGE outperforms existing models by 20% on expert human evaluations, indicating a substantial enhancement in the clinical depth of generated responses. These results were validated using both automated metrics and qualitative assessments from mental health professionals.

**Limitations**  
The authors acknowledge several limitations, including the potential for bias in the training data, which may affect the generalizability of the model across diverse populations. They also note that the framework's reliance on a predefined graph structure may limit its adaptability to novel therapeutic strategies not represented in the graph. Additionally, the computational requirements for training and deploying SAGE are not specified, which could impact its accessibility for real-world applications. An obvious limitation not discussed by the authors is the potential ethical implications of deploying AI in sensitive mental health contexts, particularly regarding user privacy and the risk of over-reliance on automated systems.

**Why it matters**  
The implications of SAGE for downstream work are significant, as it represents a step towards integrating advanced AI techniques with clinical practice in mental health counseling. By providing a decision-support tool that enhances human expertise, SAGE could improve the efficacy of online counseling interventions, particularly in crisis situations. This framework may also pave the way for future research into hybrid models that combine LLMs with structured knowledge representations, potentially leading to more robust AI applications in various domains requiring complex decision-making.

Authors: Eliya Naomi Aharon, Meytal Grimland, Avi Segal, Loona Ben Dayan, Inbar Shenfeld, Yossi Levi Belz, Kobi Gal  
Source: arXiv:2604.26630  
URL: https://arxiv.org/abs/2604.26630v1
