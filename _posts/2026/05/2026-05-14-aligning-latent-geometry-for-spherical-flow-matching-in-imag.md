---
title: "Aligning Latent Geometry for Spherical Flow Matching in Image Generation"
date: 2026-05-14 17:59:37 +0000
category: research
subcategory: efficiency_inference
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CV"
source_url: "https://arxiv.org/abs/2605.15193v1"
arxiv_id: "2605.15193"
authors: ["Tuna Han Salih Meral", "Kaan Oktay", "Hidir Yesiltepe", "Adil Kaan Akan", "Pinar Yanardag"]
slug: aligning-latent-geometry-for-spherical-flow-matching-in-imag
summary_word_count: 444
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This preprint addresses the limitations of existing latent flow matching techniques in image generation, which typically transport Gaussian noise to variational autoencoder (VAE) latents along linear paths. The authors identify that both endpoints of these paths concentrate in thin spherical shells, leading to inefficiencies as Euclidean chords can exit these shells. This work highlights the need for a method that maintains the integrity of the latent space geometry during the generation process.

**Method**  
The authors propose a novel approach that decomposes each latent token into radial and angular components. They demonstrate through component-swap probes that the perceptual and semantic content of the decoded images is predominantly carried by the angular direction, while the radial component contributes minimally. To align the latent geometry, the method involves projecting data latents onto a fixed token radius and utilizing the radial projection of Gaussian noise as a spherical prior. The decoder is fine-tuned with the encoder frozen, and the authors replace traditional linear interpolation with spherical linear interpolation (slerp). This ensures that the generated paths remain on the sphere at every timestep, with velocity targets defined purely by angular components. The method operates under matched training conditions and does not require any auxiliary encoder or representation-alignment objectives.

**Results**  
The proposed method demonstrates a consistent improvement in class-conditional image generation, as measured by the Fréchet Inception Distance (FID) on the ImageNet-256 benchmark. Specifically, the authors report a reduction in FID scores across various image tokenizers, indicating enhanced image quality and diversity. While exact numerical improvements are not disclosed in the abstract, the consistent performance across different configurations suggests a significant effect size compared to baseline methods that utilize traditional linear interpolation.

**Limitations**  
The authors acknowledge that their approach may not generalize to all types of latent spaces or architectures beyond the diffusion models tested. Additionally, the reliance on fixed token radii may limit flexibility in certain applications. The paper does not address potential computational overhead introduced by the spherical interpolation process, nor does it explore the implications of this method on other generative tasks outside of image generation.

**Why it matters**  
This work has significant implications for the field of generative modeling, particularly in enhancing the quality of image generation through improved latent space alignment. By maintaining the geometric integrity of the latent space, the proposed method could lead to advancements in various applications, including style transfer, image synthesis, and other tasks that rely on high-fidelity image generation. The findings encourage further exploration of spherical geometries in latent spaces, potentially influencing future architectures and training methodologies in generative models.

Authors: Tuna Han Salih Meral, Kaan Oktay, Hidir Yesiltepe, Adil Kaan Akan, Pinar Yanardag  
Source: arXiv cs.CV  
URL: [https://arxiv.org/abs/2605.15193v1](https://arxiv.org/abs/2605.15193v1)
