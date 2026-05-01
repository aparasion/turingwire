---
title: "WindowsWorld: A Process-Centric Benchmark of Autonomous GUI Agents in Professional Cross-Application Environments"
date: 2026-04-30 12:13:27 +0000
category: research
subcategory: evaluation_benchmarks
company: null
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.CL"
source_url: "https://arxiv.org/abs/2604.27776v1"
arxiv_id: "2604.27776"
authors: ["Jinchao Li", "Yunxin Li", "Chenrui Zhao", "Zhenran Xu", "Baotian Hu", "Min Zhang"]
slug: windowsworld-a-process-centric-benchmark-of-autonomous-gui-a
summary_word_count: 458
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses a significant gap in the evaluation of GUI agents, specifically the lack of benchmarks that assess their performance in complex, multi-application workflows typical of professional environments. Existing benchmarks, such as OSWorld, primarily focus on isolated tasks within single applications, which does not reflect the real-world scenarios where users must coordinate across multiple applications. The authors present WindowsWorld, a novel benchmark designed to systematically evaluate GUI agents on multi-step tasks that require interaction across various applications, thus filling this critical void in the literature. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The WindowsWorld benchmark employs a multi-agent framework informed by 16 distinct occupations to generate a diverse set of tasks. The benchmark consists of 181 tasks, each with an average of 5.0 sub-goals, executed within a simulated environment that encompasses 17 common desktop applications. The tasks are categorized into four difficulty levels, with 78% of them requiring interaction across multiple applications. The methodology includes intermediate inspection and human review to refine the tasks, ensuring they accurately reflect professional workflows. The evaluation of GUI agents is conducted using leading large models, with a focus on their ability to handle conditional judgment and reasoning across three or more applications.

**Results**  
The experimental results reveal that all tested computer-use agents exhibit poor performance on multi-application tasks, achieving a success rate of less than 21%. This performance is significantly lower than that observed in simpler, single-application tasks. Specifically, agents struggle with tasks that necessitate conditional reasoning across multiple applications, often stalling at early sub-goals. Additionally, the agents demonstrate low execution efficiency, frequently failing to complete tasks despite exceeding human-defined step limits. These findings highlight the inadequacy of current GUI agents in handling complex, real-world workflows.

**Limitations**  
The authors acknowledge several limitations, including the potential biases introduced by the task selection process and the simulated environment, which may not fully capture the nuances of real-world application interactions. They also note that the benchmark does not account for variations in user expertise or the impact of different operating systems. An additional limitation not explicitly mentioned is the reliance on a fixed set of applications, which may not generalize to all professional environments.

**Why it matters**  
The introduction of WindowsWorld has significant implications for the development and evaluation of autonomous GUI agents. By providing a structured framework for assessing multi-application capabilities, this benchmark encourages researchers to focus on improving agents' performance in complex workflows, which is essential for real-world applicability. The findings underscore the need for advancements in conditional reasoning and task execution efficiency, guiding future research directions in the field of AI-driven automation in professional settings.

Authors: Jinchao Li, Yunxin Li, Chenrui Zhao, Zhenran Xu, Baotian Hu, Min Zhang  
Source: arXiv:2604.27776  
URL: [https://arxiv.org/abs/2604.27776v1](https://arxiv.org/abs/2604.27776v1)
