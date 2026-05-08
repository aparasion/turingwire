---
title: "Patch2Vuln: Agentic Reconstruction of Vulnerabilities from Linux Distribution Binary Patches"
date: 2026-05-07 17:22:22 +0000
category: research
subcategory: agents_robotics
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.06601v1"
arxiv_id: "2605.06601"
authors: ["Isaac David", "Arthur Gervais"]
slug: patch2vuln-agentic-reconstruction-of-vulnerabilities-from-li
summary_word_count: 458
classification_confidence: 0.80
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the gap in automated vulnerability reconstruction from binary patches in Linux distributions, specifically focusing on the challenge of interpreting security updates when only binary artifacts are available. The authors highlight that existing literature primarily emphasizes source code analysis, leaving a significant void in methodologies that can operate solely on binary-level evidence. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the development of Patch2Vuln, a local, resumable pipeline designed to extract and analyze binary patches. The pipeline operates on pairs of Executable and Linkable Format (ELF) binaries, utilizing tools such as Ghidra and Ghidriff for binary differencing. The process involves several steps: extracting old and new ELF pairs, computing diffs, ranking changed functions, and constructing candidate dossiers. An offline language-model agent is then employed to generate a preliminary audit, a bounded validation plan, and a final audit. The evaluation is conducted on 25 Ubuntu `.deb` package pairs, comprising 20 security-update pairs and five negative controls, with results validated against private source-patch and binary-function ground truth.

**Results**  
Patch2Vuln successfully localizes a verified security-relevant patch function in 10 out of 20 security-update pairs, achieving an acceptance rate of 50%. Furthermore, it assigns an accepted final root-cause class in 11 of the 20 pairs, indicating a 55% success rate in classifying vulnerabilities. Oracle diagnostics reveal that six pairs fail to provide actionable insights due to limitations in the binary differencing or ranking processes, while one additional context-export miss is noted. A separate bounded validation pass yields two target-level minimized behavioral differentials for the tcpdump utility, although no crash, timeout, sanitizer finding, or memory-corruption proof is produced. All five negative controls are correctly classified as unknown, with no validation differentials generated.

**Limitations**  
The authors acknowledge that the effectiveness of Patch2Vuln is constrained by the coverage of binary diffs and the limitations of local behavioral validation. Specifically, the model's performance is hindered when the binary differ or ranker fails to identify the relevant functions. Additionally, the reliance on a limited dataset of 25 pairs may affect the generalizability of the findings. The absence of a comprehensive evaluation across diverse Linux distributions and binary formats is another notable limitation.

**Why it matters**  
This research has significant implications for the field of automated vulnerability analysis, particularly in environments where source code is not accessible. By demonstrating the feasibility of reconstructing vulnerabilities from binary patches, Patch2Vuln opens avenues for further exploration into agentic models that can enhance security auditing processes. The findings suggest that improving binary differencing techniques and expanding behavioral validation methods could lead to more robust vulnerability detection systems, ultimately contributing to better security practices in software development and deployment.

Authors: Isaac David, Arthur Gervais  
Source: arXiv:2605.06601  
URL: [https://arxiv.org/abs/2605.06601v1](https://arxiv.org/abs/2605.06601v1)
