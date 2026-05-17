---
title: "New math benchmark reveals AI models confidently solve problems that have no solution"
date: 2026-05-17 08:56:52 +0000
category: research
subcategory: evaluation_benchmarks
company: "Google DeepMind"
secondary_companies: []
impact: major
source_publisher: "The Decoder"
source_url: "https://the-decoder.com/new-math-benchmark-reveals-ai-models-confidently-solve-problems-that-have-no-solution/"
arxiv_id: ""
authors: []
slug: new-math-benchmark-reveals-ai-models-confidently-solve-probl
summary_word_count: 438
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of AI models' mathematical reasoning capabilities, particularly their ability to discern solvable from unsolvable problems. The authors introduce SOOHAK, a novel benchmark comprising 439 handwritten mathematical tasks, of which 99 are intentionally unsolvable. This work is presented as a preprint and has not undergone peer review, highlighting the need for further validation in the community.

**Method**  
The core technical contribution is the SOOHAK benchmark, designed to rigorously assess AI models' performance on both solvable and unsolvable mathematical tasks. The benchmark includes a diverse set of handwritten problems, which are critical for evaluating generalization in AI systems. The evaluation focuses on the performance of Google's Gemini 3 Pro, which is reported to achieve a 30% success rate on research-level problems. The study emphasizes that while increased computational resources enhance models' problem-solving capabilities, they do not improve the models' ability to recognize unsolvable tasks. The authors do not disclose specific details regarding the architecture, loss functions, or training compute used for Gemini 3 Pro, which limits the reproducibility of their findings.

**Results**  
The results indicate that no AI model, including Gemini 3 Pro, surpasses a 50% success rate in identifying unsolvable tasks within the SOOHAK benchmark. Specifically, Gemini 3 Pro leads with a 30% success rate on research-level problems, but this performance starkly contrasts with its inability to effectively recognize broken tasks. The findings suggest a critical disparity between the models' confidence in providing solutions and their actual understanding of problem solvability, underscoring a fundamental limitation in current AI capabilities.

**Limitations**  
The authors acknowledge that the benchmark's reliance on handwritten tasks may introduce variability in model performance due to differences in handwriting recognition. Additionally, the lack of detailed information regarding the training methodologies and architectures of the evaluated models limits the ability to draw comprehensive conclusions about the underlying reasons for their performance. An obvious limitation not discussed by the authors is the potential bias introduced by the selection of tasks, which may not represent the full spectrum of mathematical reasoning challenges.

**Why it matters**  
This work has significant implications for the development of AI systems in mathematical reasoning and problem-solving. By highlighting the gap between performance on solvable tasks and the ability to recognize unsolvable ones, the study calls for a reevaluation of how AI models are trained and assessed. It suggests that future research should focus not only on enhancing problem-solving capabilities but also on improving models' understanding of problem constraints. This could lead to more robust AI systems that are better equipped to handle complex reasoning tasks in real-world applications.

Authors: unknown  
Source: arXiv: [id]  
URL: https://the-decoder.com/new-math-benchmark-reveals-ai-models-confidently-solve-problems-that-have-no-solution/
