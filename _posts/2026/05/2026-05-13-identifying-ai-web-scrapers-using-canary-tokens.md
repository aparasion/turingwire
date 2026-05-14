---
title: "Identifying AI Web Scrapers Using Canary Tokens"
date: 2026-05-13 15:53:57 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.13706v1"
arxiv_id: "2605.13706"
authors: ["Steven Seiden", "Triss Ren", "Caroline Zhang", "Taein Kim", "Enze Liu", "Emily Wenger"]
slug: identifying-ai-web-scrapers-using-canary-tokens
summary_word_count: 452
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in reliable identification of web scrapers that feed data to large language models (LLMs). Current methods for identifying scrapers rely on voluntary disclosures, isolated experiments, or crowd-sourced reports, which lack scalability and reliability. The authors propose a novel technique to automate the identification of LLM-related scrapers, which is particularly relevant given the ethical, legal, and stability concerns associated with large-scale web scraping. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The authors introduce a method that utilizes dynamic websites to serve unique canary tokens to each visiting scraper. The core of the approach involves prompting various LLMs to generate outputs based on the content of these dynamic sites. By analyzing the outputs for the presence of the unique canary tokens, the authors can infer which LLMs have been exposed to specific scrapers. The experiments were conducted across 22 production LLM systems, demonstrating the method's applicability across a diverse set of models. The architecture of the dynamic websites and the mechanism for token generation are not detailed in the abstract, but the approach emphasizes the automated nature of the identification process.

**Results**  
The results indicate that the proposed method can reliably identify the relationship between scrapers and LLMs. The authors report successful identification of several scrapers that are not publicly disclosed, showcasing the effectiveness of their approach. While specific numerical performance metrics or effect sizes are not provided in the abstract, the implication is that the method outperforms existing identification techniques, which are characterized as unreliable and non-scalable.

**Limitations**  
The authors acknowledge that their method relies on the assumption that LLMs will generate outputs containing the canary tokens when exposed to the corresponding scrapers. This may not hold true for all LLMs or in all contexts, potentially limiting the generalizability of the findings. Additionally, the paper does not address the potential for scrapers to evade detection by ignoring or filtering out canary tokens. The scalability of the method in real-world scenarios, particularly with respect to the volume of traffic and the diversity of scrapers, is also not discussed in detail.

**Why it matters**  
This work has significant implications for web scraping governance and the ethical use of data in training LLMs. By providing a reliable method for identifying scrapers, website owners can better enforce access control mechanisms, such as the Robots Exclusion Protocol, to mitigate the negative impacts of unwanted scraping. Furthermore, this research opens avenues for future work in scraper detection and the development of more robust web scraping policies, potentially influencing how LLMs are trained and the data sources they utilize.

Authors: Steven Seiden, Triss Ren, Caroline Zhang, Taein Kim, Enze Liu, Emily Wenger  
Source: arXiv:2605.13706  
URL: [https://arxiv.org/abs/2605.13706v1](https://arxiv.org/abs/2605.13706v1)
