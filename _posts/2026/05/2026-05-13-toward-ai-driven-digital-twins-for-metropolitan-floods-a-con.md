---
title: "Toward AI-Driven Digital Twins for Metropolitan Floods: A Conditional Latent Dynamics Network Surrogate of the Shallow Water Equations"
date: 2026-05-13 16:41:14 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: major
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.13761v1"
arxiv_id: "2605.13761"
authors: ["Phillip Si", "Yuan Qiu", "Omar Sallam", "Jeremy Feinstein", "Ziang He", "Eugene Yan"]
slug: toward-ai-driven-digital-twins-for-metropolitan-floods-a-con
summary_word_count: 461
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the need for efficient hydrodynamic surrogates in AI-driven digital twins for metropolitan flood forecasting. Current GPU-accelerated solvers for the two-dimensional shallow water equations (SWE) are computationally intensive, requiring approximately 55 minutes for a 96-hour simulation on a large metropolitan basin (Des Plaines River basin with 4.2 million active cells). This latency renders real-time applications impractical. The authors propose a novel approach to overcome this limitation, presenting the Conditional Latent Dynamics Network (CLDNet) as a surrogate model for rapid flood forecasting. This work is a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the CLDNet architecture, which employs a low-dimensional latent neural ordinary differential equation (ODE) driven by rainfall inputs. The model features a coordinate-based decoder that is conditioned on static terrain attributes (elevation, slope, Manning roughness), allowing it to reconstruct depth and discharge at arbitrary query points. This pointwise decoding mechanism decouples memory usage from grid size, enabling efficient handling of irregular watersheds. The training is conducted on a single compute node, facilitating metropolitan-scale applications. The model is evaluated on a synthetic benchmark with 250,000 cells and a case study involving 114 real-rainfall Stage IV storms in the Des Plaines basin, validated against USGS gauge data.

**Results**  
CLDNet demonstrates significant performance improvements over baseline models. It achieves a relative root-mean-squared error reduction of approximately 50% compared to an unconditional baseline. On the Texas benchmark, CLDNet outperforms both a variational autoencoder combined with ConvLSTM and Fourier Neural Operator (FNO) baselines, which are constrained by their reliance on Cartesian grids and are not applicable to the irregular Des Plaines watershed. The model reaches a critical success index of approximately 86% at the 0.5 m inundation threshold and produces a full 96-hour basin-wide forecast in about 29 seconds, resulting in a speedup of approximately 115 times compared to traditional solvers.

**Limitations**  
The authors acknowledge that the model's performance is contingent on the quality of the input rainfall data and the static terrain features used for conditioning. Additionally, while the model is validated against historical flood events, its generalizability to other geographic regions or extreme weather scenarios remains untested. The reliance on synthetic data for initial training may also introduce biases that could affect real-world applicability.

**Why it matters**  
The development of CLDNet has significant implications for real-time flood forecasting and management in urban environments. By drastically reducing computation time while maintaining accuracy, this approach enables more frequent updates and better integration of observational data into flood models. The ability to handle irregular watersheds natively expands the applicability of AI-driven digital twins in diverse geographic contexts, paving the way for enhanced disaster preparedness and response strategies.

Authors: Phillip Si, Yuan Qiu, Omar Sallam, Jeremy Feinstein, Ziang He, Eugene Yan, Peng Chen  
Source: arXiv:2605.13761  
URL: [https://arxiv.org/abs/2605.13761v1](https://arxiv.org/abs/2605.13761v1)
