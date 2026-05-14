---
title: "EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents"
date: 2026-05-13 17:58:52 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13841v1"
arxiv_id: "2605.13841"
authors: ["Tara Bogavelli", "Gabrielle Gauthier Melan\u00e7on", "Katrina Stankiewicz", "Oluwanifemi Bamgbose", "Fanny Riols", "Hoang H. Nguyen"]
slug: eva-bench-a-new-end-to-end-framework-for-evaluating-voice-ag
summary_word_count: 450
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of voice agents, which are increasingly utilized in enterprise applications. Existing benchmarks fail to jointly tackle two critical challenges: the generation of realistic simulated conversations and the comprehensive measurement of quality across various voice-specific failure modes. The authors present EVA-Bench, an end-to-end evaluation framework designed to fill this void. This work is a preprint and has not yet undergone peer review.

**Method**  
EVA-Bench orchestrates bot-to-bot audio conversations through dynamic multi-turn dialogues, employing automatic simulation validation to identify user simulator errors and regenerate conversations as needed. The framework introduces two composite metrics: EVA-A (Accuracy) and EVA-X (Experience). EVA-A assesses task completion, faithfulness, and audio-level speech fidelity, while EVA-X evaluates conversation progression, spoken conciseness, and turn-taking timing. These metrics facilitate direct comparisons across different agent architectures. The framework encompasses 213 scenarios across three enterprise domains and includes a controlled perturbation suite to test robustness against accent and noise variations. The evaluation metrics include pass@1, pass@k, and pass^k, which differentiate between peak and reliable performance.

**Results**  
The authors evaluated 12 systems across three architectures using EVA-Bench. Key findings include: (1) no system achieved a score exceeding 0.5 on both EVA-A pass@1 and EVA-X pass@1, indicating a significant performance ceiling; (2) there is a substantial divergence between peak and reliable performance, with a median gap of 0.44 on EVA-A between pass@k and pass^k; (3) robustness to accent and noise perturbations revealed considerable vulnerabilities, with mean performance drops of up to 0.314 across different architectures, systems, and metrics. These results highlight the limitations of current voice agents in handling real-world conversational challenges.

**Limitations**  
The authors acknowledge that EVA-Bench, while comprehensive, may not cover all possible conversational scenarios or failure modes. Additionally, the reliance on simulated conversations may not fully capture the complexities of human-agent interactions. The framework's performance metrics, while informative, may require further refinement to account for nuanced conversational dynamics. The authors do not address potential biases in the training data or the generalizability of the results across different languages or cultural contexts.

**Why it matters**  
EVA-Bench represents a significant advancement in the evaluation of voice agents, providing a structured framework that can facilitate the development of more robust and effective conversational AI systems. By exposing the limitations of current architectures and highlighting performance gaps, this work lays the groundwork for future research aimed at improving voice agent capabilities. The open-source release of the framework and benchmark data encourages further exploration and innovation in the field, potentially leading to more reliable and user-friendly voice agents in enterprise applications.

Authors: Tara Bogavelli, Gabrielle Gauthier Melançon, Katrina Stankiewicz, Oluwanifemi Bamgbose, Fanny Riols, Hoang H. Nguyen, Raghav Mehndiratta, Lindsay Devon Brin et al.  
Source: arXiv:2605.13841  
URL: [https://arxiv.org/abs/2605.13841v1](https://arxiv.org/abs/2605.13841v1)
