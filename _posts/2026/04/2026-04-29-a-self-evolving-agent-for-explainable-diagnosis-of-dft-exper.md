---
title: "A self-evolving agent for explainable diagnosis of DFT-experiment band-gap mismatch"
date: 2026-04-29 14:11:03 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2604.26703v1"
arxiv_id: "2604.26703"
authors: ["Yue Li", "Bijun Tang"]
slug: a-self-evolving-agent-for-explainable-diagnosis-of-dft-exper
summary_word_count: 453
classification_confidence: 0.85
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in the capability of standard density functional theory (DFT) to accurately classify the electronic ground states of correlated and structurally complex materials. DFT often misclassifies semiconductors as metallic, leading to significant discrepancies between theoretical predictions and experimental results. The challenge lies in the manual extraction of non-idealities—such as magnetic ordering, electron correlation, alternative polymorphs, or defects—that contribute to these mismatches. Automating this diagnosis process has not been effectively achieved in the literature.

**Method**  
The authors propose XDFT, a self-evolving agent designed to automate the diagnosis of DFT-experiment band-gap mismatches. XDFT operates in a closed-loop system where it draws candidate hypotheses from a curated catalogue of known non-idealities. It executes corresponding first-principles tests to evaluate these hypotheses and updates a global Bayesian posterior based on the outcomes of these tests. The architecture leverages Bayesian inference to assess the usefulness of each hypothesis iteratively. The training compute specifics are not disclosed, but the method is validated on a benchmark of 124 materials, focusing on the identification of resolving mechanisms for mismatch cases.

**Results**  
XDFT successfully identifies resolving mechanisms for 70 out of 90 mismatch cases, achieving a success rate of 78%. This performance significantly outperforms a uniform-random baseline (19%) and a static large language model (LLM) ordering (20%). The internal Bayesian posterior aligns well with empirical performance over the benchmark timeline, indicating that the agent's self-assessment is reliable. The resolved cases are categorized into a tri-partite element-class taxonomy, which the authors distill into a concise four-line static rule. Each diagnosed material is returned with a corrected protocol and mechanistic attribution, while unresolved cases are flagged for further experimental investigation.

**Limitations**  
The authors acknowledge that the performance of XDFT is contingent on the quality and comprehensiveness of the curated hypothesis catalogue. Additionally, the method may not generalize well to materials outside the benchmark set, as it has not been tested on a broader range of compounds. The reliance on first-principles tests may also introduce computational overhead, which could limit scalability. Furthermore, the study does not address the potential biases in the hypothesis selection process or the implications of the Bayesian prior used.

**Why it matters**  
The development of XDFT has significant implications for materials science, particularly in the context of accelerating the discovery of new semiconductors and correlated materials. By automating the diagnosis of DFT mismatches, researchers can save time and resources, allowing for more efficient exploration of complex materials. The ability to provide mechanistic attributions and corrected protocols enhances the interpretability of DFT results, fostering a more robust integration of theoretical predictions with experimental validation. This work lays the groundwork for future advancements in self-evolving agents in computational materials science.

Authors: Yue Li, Bijun Tang  
Source: arXiv:2604.26703  
URL: https://arxiv.org/abs/2604.26703v1
