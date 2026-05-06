---
title: "Towards accurate extreme event likelihoods from diffusion model climate emulators"
date: 2026-05-05 14:28:20 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.LG"
source_url: "https://arxiv.org/abs/2605.03802v1"
arxiv_id: "2605.03802"
authors: ["Peter Manshausen", "Noah Brenowitz", "Julius Berner", "Karthik Kashinath", "Mike Pritchard"]
slug: towards-accurate-extreme-event-likelihoods-from-diffusion-mo
summary_word_count: 433
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the gap in accurately estimating the likelihood of extreme weather events, specifically Tropical Cyclones (TCs), using diffusion model climate emulators. While existing models provide atmospheric state generation, they lack robust methodologies for quantifying the probability of extreme events under specific boundary conditions. The authors propose a novel approach leveraging the diffusion model "Climate in a Bottle" (cBottle) to enhance the understanding of extreme event likelihoods, which is critical for climate scenario planning and adaptation.

**Method**  
The core technical contribution is the application of the cBottle diffusion model to generate atmospheric states conditioned on solar position and sea surface temperatures. The authors utilize the model's ability to approximate the probability density of atmospheric states to derive likelihoods for extreme events. By guiding the model towards states indicative of TCs, they compute odds ratios comparing the probability densities of guided versus unguided states. This allows for importance sampling from the TC distribution, which significantly reduces the standard error of probability estimates compared to traditional Monte Carlo methods. The training compute specifics are not disclosed, but the methodology emphasizes the probabilistic nature of the diffusion model outputs.

**Results**  
The authors present preliminary results demonstrating that the guided model significantly increases the likelihood of generating TCs compared to the unguided model. While specific numerical results are not detailed in the abstract, the use of odds ratios indicates a quantifiable improvement in the probability estimates for TCs. The authors suggest that their approach yields a more accurate representation of extreme event likelihoods, which could enhance the reliability of climate predictions. The results are positioned as early findings that could catalyze further research into probabilistic climate modeling.

**Limitations**  
The authors acknowledge several limitations, including the nascent stage of their methodology and the need for further validation against real-world data. They do not address potential biases in the training data or the generalizability of the model across different climatic conditions. Additionally, the reliance on the diffusion model's assumptions may limit the applicability of the results to other extreme weather phenomena beyond TCs.

**Why it matters**  
This work has significant implications for climate science and risk assessment, as it provides a framework for quantifying the likelihood of extreme weather events using advanced machine learning techniques. By improving the accuracy of extreme event likelihood estimates, this research can inform better decision-making in climate adaptation strategies and disaster preparedness. The findings encourage further exploration of probabilistic approaches in climate modeling, potentially leading to more resilient infrastructure and policies in the face of climate change.

Authors: Peter Manshausen, Noah Brenowitz, Julius Berner, Karthik Kashinath, Mike Pritchard  
Source: arXiv:2605.03802  
URL: [https://arxiv.org/abs/2605.03802v1](https://arxiv.org/abs/2605.03802v1)
