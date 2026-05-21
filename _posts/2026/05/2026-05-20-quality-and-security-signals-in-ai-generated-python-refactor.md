---
title: "Quality and Security Signals in AI-Generated Python Refactoring Pull Requests"
date: 2026-05-20 17:43:36 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.21453v1"
arxiv_id: "2605.21453"
authors: ["Mohamed Almukhtar", "Anwar Ghammam", "Hua Ming"]
slug: quality-and-security-signals-in-ai-generated-python-refactor
summary_word_count: 442
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in empirical evidence regarding the quality and security implications of AI-generated refactoring contributions in real-world software projects. Specifically, it investigates how AI agents' refactoring edits impact maintainability, code quality, and security when integrated into GitHub repositories. The study focuses on Python refactoring pull requests (PRs) from the AIDev dataset, an area that has not been extensively explored in existing literature.

**Method**  
The authors employ an empirical analysis of Python refactoring PRs using PyQu, a machine learning-based quality assessment tool tailored for Python code. The study quantifies changes across five quality attributes: usability, readability, maintainability, complexity, and security. Additionally, they utilize static analysis tools Pylint and Bandit to assess code quality and security issues before and after the refactoring changes. The analysis includes a taxonomy of 24 recurring change operations derived from the observed diffs, which are mapped to the lint and security findings they most frequently affect. The dataset comprises a significant number of PRs, although the exact size and training compute are not disclosed.

**Results**  
The findings reveal that, on average, agentic commits improve a quality attribute in 22.5% of the analyzed changes, with usability improvements occurring most frequently at 36.5%. However, 24.17% of modified files introduce new Pylint issues, primarily related to convention-level violations such as long lines, while 4.7% introduce new security findings from Bandit. Notably, despite these mixed outcomes, a high developer acceptance rate is observed, with 73.5% of the analyzed PRs being merged, including those that introduce new lint or security issues, often alongside the resolution of existing problems.

**Limitations**  
The authors acknowledge the mixed results regarding the quality improvements and the introduction of new issues, indicating a need for enhanced quality and security gating in AI-driven development workflows. They do not discuss the potential biases in the AIDev dataset or the limitations of the PyQu tool in capturing all dimensions of code quality. Additionally, the study does not explore the long-term effects of these changes on code maintainability or the potential for cumulative technical debt.

**Why it matters**  
This research highlights the dual nature of AI-generated refactoring contributions, showcasing both their potential benefits and risks. The findings underscore the necessity for improved tooling and processes to ensure that AI-driven development does not compromise code quality or security. The taxonomy of change operations provides a framework for future research and tool development aimed at enhancing the reliability of AI contributions in software engineering. This work lays the groundwork for further exploration into the integration of AI in development workflows, emphasizing the importance of quality assurance mechanisms in automated coding practices.

Authors: Mohamed Almukhtar, Anwar Ghammam, Hua Ming  
Source: arXiv:2605.21453  
URL: [https://arxiv.org/abs/2605.21453v1](https://arxiv.org/abs/2605.21453v1)
