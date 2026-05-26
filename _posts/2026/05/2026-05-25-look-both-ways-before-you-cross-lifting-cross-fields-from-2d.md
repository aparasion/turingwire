---
title: "Look Both Ways Before You Cross: Lifting Cross Fields From 2D Visual Priors"
date: 2026-05-25 17:23:23 +0000
category: research
subcategory: other
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.26062v1"
arxiv_id: "2605.26062"
authors: ["Dale Decatur", "Jacob Serfaty", "Oded Stein", "Amir Vaxman", "Rana Hanocka"]
slug: look-both-ways-before-you-cross-lifting-cross-fields-from-2d
summary_word_count: 405
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in generating cross fields on 3D meshes using 2D visual priors, a task that has not been effectively tackled in existing literature. The authors propose CrossLift, a method that leverages advanced text-to-image synthesis techniques to derive explicit per-pixel directional information from 2D images, which is then back-projected onto 3D mesh surfaces. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
CrossLift operates by extracting directional signals from 2D images, which are synthesized to align with quad meshes. The core technical contribution involves two key interpolation steps on the mesh surface: the first interpolation is performed within individual views, while the second aggregates information across multiple views. The authors introduce a custom confidence-based weighting scheme for candidate directions during these interpolations, which helps resolve conflicts between competing directional signals on the same mesh face and facilitates smooth interpolation for occluded areas. The method is modular, allowing integration with various 2D visual priors, and includes applications for texture-aligned quad meshing and interactive design using user-drawn lines.

**Results**  
CrossLift demonstrates significant improvements over existing methods in generating semantically aligned quad meshes. The authors report that their method produces superior results on a diverse set of organic and mechanical shapes, although specific quantitative metrics (e.g., F1 scores, IoU) against named baselines are not detailed in the abstract. The qualitative results indicate enhanced alignment with visual features compared to traditional approaches, suggesting a strong effect size in practical applications.

**Limitations**  
The authors acknowledge that their method's performance may vary depending on the quality of the 2D visual priors used, as well as the complexity of the input shapes. They do not discuss potential computational overhead associated with the dual interpolation process or the scalability of the method to highly complex meshes. Additionally, the reliance on user-drawn lines for interactive design may introduce variability based on user skill and intent.

**Why it matters**  
The implications of CrossLift extend to various fields, including computer graphics, CAD, and AR/VR applications, where accurate mesh representation is crucial. By enabling the generation of semantically aligned quad meshes from 2D images, this work opens avenues for improved texture mapping, surface modeling, and user-driven design processes. The modular nature of the method suggests potential for integration into existing workflows, enhancing the capabilities of tools used in 3D modeling and animation.

Authors: Dale Decatur, Jacob Serfaty, Oded Stein, Amir Vaxman, Rana Hanocka  
Source: arXiv:2605.26062v1  
URL: https://arxiv.org/abs/2605.26062v1
