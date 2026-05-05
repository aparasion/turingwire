---
title: "U-Define: Designing User Workflows for Hard and Soft Constraints in LLM-Based Planning"
date: 2026-05-04 16:05:40 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.02765v1"
arxiv_id: "2605.02765"
authors: ["Christine P Lee", "Xinyu Jessica Wang", "Aws Albarghouthi", "David Porfirio", "Bilge Mutlu"]
slug: u-define-designing-user-workflows-for-hard-and-soft-constrai
summary_word_count: 438
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of current large language model (LLM) systems in user task planning, particularly their black-box nature, which hampers users' ability to enforce reliability and control over generated plans. Existing approaches often rely on rigid hard constraints that fail to accommodate real-world variability, while numeric flexibility weights can confuse users. The authors investigate how to enhance user workflows for applying constraints, aiming to improve the expressiveness of user intent in LLM-generated plans.

**Method**  
The core technical contribution is the U-Define system, which allows users to define constraints in natural language and categorize them into hard rules (mandatory conditions) and soft preferences (flexible guidelines). U-Define employs two distinct verification mechanisms: formal model checking for hard constraints, ensuring that these rules are strictly adhered to, and an LLM-as-judge evaluation for soft constraints, which assesses the degree to which generated plans align with user preferences. The system was evaluated through a combination of technical assessments and user studies involving both general and expert participants, focusing on perceived usefulness, performance, and user satisfaction.

**Results**  
The user studies revealed that the introduction of user-defined constraint types significantly improved perceived usefulness, performance, and satisfaction compared to baseline systems that did not support such flexible constraint definitions. Specific metrics were not disclosed in the abstract, but the qualitative feedback indicated a marked enhancement in usability and alignment with user intent. The authors suggest that the dual verification approach effectively balances the need for strict adherence to hard constraints with the flexibility of soft preferences, leading to more reliable and user-friendly planning workflows.

**Limitations**  
The authors acknowledge that the study's findings are based on user studies with a limited participant pool, which may not fully represent the broader user base. Additionally, the reliance on LLMs for soft constraint evaluation may introduce variability in performance, as the LLM's judgment can be influenced by its training data and inherent biases. The paper does not address potential scalability issues when applying U-Define to more complex planning scenarios or the integration of additional constraint types beyond hard and soft.

**Why it matters**  
This work has significant implications for the design of user-centric AI systems, particularly in domains requiring nuanced decision-making and planning. By enabling users to express constraints in a more intuitive manner, U-Define could enhance the reliability of LLM-generated outputs, fostering greater trust and adoption of AI in critical applications. The insights gained from this research may inform future developments in constraint-based AI systems, paving the way for more sophisticated user interactions and improved performance in real-world tasks.

Authors: Christine P Lee, Xinyu Jessica Wang, Aws Albarghouthi, David Porfirio, Bilge Mutlu  
Source: arXiv:2605.02765  
URL: [https://arxiv.org/abs/2605.02765v1](https://arxiv.org/abs/2605.02765v1)
