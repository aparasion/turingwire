---
title: "Confidence and Calibration of Activation Oracles for Reliable Interpretation of Language Model Internals"
date: 2026-05-25 17:08:47 +0000
category: research
subcategory: interpretability
company: "Oracle"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.26045v1"
arxiv_id: "2605.26045"
authors: ["Federico Torrielli", "Peter Schneider-Kamp", "Lukas Galke Poech"]
slug: confidence-and-calibration-of-activation-oracles-for-reliabl
summary_word_count: 450
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses a significant gap in the interpretability of language models, specifically focusing on the uncertainty quantification (UQ) of activation oracles. While activation oracles have shown promise in making model activations interpretable, the confidence associated with their outputs remains underexplored. The authors aim to enhance the reliability of these interpretations by evaluating various methods for estimating and calibrating the confidence of activation oracles.

**Method**  
The authors investigate six distinct methods for estimating the confidence of activation oracles, focusing on their calibration performance. The methods include bootstrap mode frequency and answer-word log-probability, among others. The evaluation is conducted on a dataset comprising 6,000 samples per oracle, utilizing different verbalizers and context prompts. The calibration of confidence scores is assessed using Expected Calibration Error (ECE) as the primary metric. The bootstrap mode frequency method is identified as the best-performing approach, achieving an ECE of 5.7% compared to 25.5% for the answer-word log-probability on the Qwen3-8B model, and 10.3% versus 13.1% on the Qwen3.6-27B model. The authors also highlight that the log-probability baseline can serve as a rapid triage signal, providing a cost-effective alternative for initial assessments.

**Results**  
The results demonstrate that the bootstrap mode frequency method significantly outperforms the answer-word log-probability in terms of calibration, with a notable reduction in ECE. Specifically, the bootstrap method achieves an ECE of 5.7% on Qwen3-8B, while the log-probability method yields an ECE of 25.5%. For the Qwen3.6-27B model, the bootstrap method achieves an ECE of 10.3%, compared to 13.1% for the log-probability method. These results indicate a clear advantage in using the bootstrap mode frequency for reliable confidence estimation in activation oracles.

**Limitations**  
The authors acknowledge that their study is limited to the specific activation oracle methods evaluated and the models used (Qwen3-8B and Qwen3.6-27B). They do not explore the generalizability of their findings across other model architectures or tasks. Additionally, the reliance on ECE as a sole metric may overlook other aspects of calibration and uncertainty quantification. The study also does not address potential biases in the dataset or the implications of using different verbalizers and context prompts.

**Why it matters**  
This work has significant implications for the field of model interpretability, particularly in enhancing the reliability of activation oracles. By providing a systematic evaluation of confidence estimation methods, the authors contribute to the development of more robust interpretability tools for language models. Improved calibration of confidence scores can lead to better decision-making in applications where model outputs are critical, such as in healthcare or legal domains. Furthermore, the findings may inform future research on uncertainty quantification in machine learning, paving the way for more transparent and accountable AI systems.

Authors: Federico Torrielli, Peter Schneider-Kamp, Lukas Galke Poech  
Source: arXiv:2605.26045  
URL: https://arxiv.org/abs/2605.26045v1
