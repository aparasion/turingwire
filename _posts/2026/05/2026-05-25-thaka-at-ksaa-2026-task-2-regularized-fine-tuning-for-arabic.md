---
title: "Thaka at KSAA-2026 Task 2: Regularized Fine-Tuning for Arabic Speech Diacritization"
date: 2026-05-25 15:07:48 +0000
category: research
subcategory: multimodal
company: "OpenAI"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2605.25928v1"
arxiv_id: "2605.25928"
authors: ["Meshal Alamr", "Hassan Alqaeri", "Abdullah Aldahlawi"]
slug: thaka-at-ksaa-2026-task-2-regularized-fine-tuning-for-arabic
summary_word_count: 423
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the challenge of Arabic speech diacritization, specifically in the context of the KSAA-2026 Shared Task, where the goal is to generate fully diacritized Arabic text from speech audio and undiacritized transcripts. The task is particularly challenging due to the limited dataset of only 2,327 training samples and the restriction against using external data. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors propose a system that fine-tunes the CATT-Whisper model, which integrates a pretrained CATT text encoder with a frozen Whisper speech encoder. The core technical contributions include the application of R-Drop consistency regularization to enhance model robustness, the use of Optuna for hyperparameter optimization with a focus on high weight decay, and the implementation of Focal Loss to address class imbalance in the training data. During inference, the model employs Monte Carlo Dropout, averaging 200 stochastic forward passes across four model checkpoints to refine softmax probability estimates, thereby improving prediction accuracy.

**Results**  
The proposed system achieves a Word Error Rate (WER) of 23.26% on the primary leaderboard metric, which includes case endings and no-diacritic positions. This performance places the system first among all participants in the KSAA-2026 Task 2, demonstrating a significant improvement over baseline models, although specific baseline WERs are not disclosed in the paper. The results indicate the effectiveness of the regularization techniques and the multimodal architecture in handling the complexities of Arabic diacritization.

**Limitations**  
The authors acknowledge several limitations, including the reliance on a small training dataset, which may affect the generalizability of the model. Additionally, the use of a frozen speech encoder may limit the model's ability to adapt to variations in speech patterns. The paper does not discuss potential biases in the training data or the implications of using only a single language, which could restrict the applicability of the findings to other languages or dialects.

**Why it matters**  
This work contributes to the field of automatic speech recognition (ASR) and natural language processing (NLP) by providing a novel approach to Arabic diacritization, a task that is critical for accurate text representation and understanding in Arabic. The techniques developed, particularly the regularization strategies and the integration of multimodal models, have broader implications for improving ASR systems in low-resource languages. Furthermore, the success of the approach in a competitive setting highlights the potential for similar methodologies to be applied to other speech and text processing tasks, paving the way for advancements in multilingual ASR systems.

Authors: Meshal Alamr, Hassan Alqaeri, Abdullah Aldahlawi  
Source: arXiv:2605.25928  
URL: https://arxiv.org/abs/2605.25928v1
