---
title: "NeuroAgent: LLM Agents for Multimodal Neuroimaging Analysis and Research"
date: 2026-05-07 17:13:48 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06584v1"
arxiv_id: "2605.06584"
authors: ["Lujia Zhong", "Yihao Xia", "Jianwei Zhang", "Shuo huang", "Jiaxin Yue", "Mingyang Xia"]
slug: neuroagent-llm-agents-for-multimodal-neuroimaging-analysis-a
summary_word_count: 389
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in automating the preprocessing and analysis of multimodal neuroimaging data, which typically involves complex, modality-specific workflows that are cumbersome and error-prone. The authors highlight the lack of integrated solutions that can handle diverse neuroimaging modalities (sMRI, fMRI, dMRI, PET) and facilitate reproducible scientific analysis. The work is presented as a preprint, indicating it has not yet undergone peer review.

**Method**  
The core technical contribution is the NeuroAgent framework, which utilizes a hierarchical multi-agent architecture combined with a feedback-driven Generate-Execute-Validate (GEV) engine. NeuroAgent automates the generation of executable preprocessing code, error detection, and output validation. The framework employs large language models (LLMs) for intent parsing and code generation, with ablation studies conducted across various LLM backends. The strongest model, Qwen3.5-27B, achieved 100% intent-parsing accuracy and 84.8% correctness in end-to-end preprocessing steps. The system also incorporates a Human-In-The-Loop interface to manage edge cases requiring human intervention.

**Results**  
NeuroAgent was evaluated on a dataset comprising 1,470 subjects from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including 1,000 cognitively normal (CN) and 470 Alzheimer's Disease (AD) subjects. The framework demonstrated an area under the curve (AUC) of 0.9518 for Alzheimer's Disease classification using multimodal data, significantly outperforming single-modality baselines. The results indicate that the automated preprocessing pipeline can effectively reduce manual effort while maintaining high accuracy in downstream analysis.

**Limitations**  
The authors acknowledge that while NeuroAgent automates many preprocessing tasks, it still requires human oversight in certain edge cases, which may limit its applicability in fully automated settings. Additionally, the performance of the framework is contingent on the capabilities of the underlying LLMs, which may vary across different tasks and datasets. The paper does not address potential biases in the training data for the LLMs or the generalizability of the results to other neuroimaging datasets outside of ADNI.

**Why it matters**  
NeuroAgent has significant implications for neuroimaging research by streamlining the preprocessing and analysis of multimodal data, thereby enhancing reproducibility and efficiency. The framework's ability to automate complex workflows can facilitate broader access to neuroimaging analysis tools, potentially accelerating discoveries in neuroscience and clinical applications. Furthermore, the integration of LLMs into scientific workflows may inspire future research on AI-driven automation in other domains of medical imaging and data analysis.

Authors: Lujia Zhong, Yihao Xia, Jianwei Zhang, Shuo Huang, Jiaxin Yue, Mingyang Xia, Yonggang Shi  
Source: arXiv:2605.06584  
URL: [https://arxiv.org/abs/2605.06584v1](https://arxiv.org/abs/2605.06584v1)
