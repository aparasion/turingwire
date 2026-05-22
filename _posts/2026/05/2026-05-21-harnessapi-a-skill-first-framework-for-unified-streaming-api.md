---
title: "HarnessAPI: A Skill-First Framework for Unified Streaming APIs and MCP Tools"
date: 2026-05-21 17:03:44 +0000
category: research
subcategory: efficiency_inference
company: "Anthropic"
secondary_companies: []
impact: notable
source_publisher: "arXiv cs.AI"
source_url: "https://arxiv.org/abs/2605.22733v1"
arxiv_id: "2605.22733"
authors: ["Edwin Jose"]
slug: harnessapi-a-skill-first-framework-for-unified-streaming-api
summary_word_count: 443
classification_confidence: 0.70
source_truncated: false
layout: post
---

**Problem**  
This paper addresses the inefficiencies in the deployment of Python functions as tools for large language models (LLMs), specifically the redundancy in creating separate HTTP endpoints for human-facing clients and MCP (Multi-Client Protocol) tool registrations for agent runtimes. The authors highlight that existing implementations require maintaining divergent codebases for routing, validation, serialization, and schema management, leading to increased complexity and potential drift as the underlying code evolves. This work is presented as a preprint and has not yet undergone peer review.

**Method**  
The core technical contribution is the HarnessAPI framework, which consolidates the deployment process into a single source of truth: a typed skill folder. The framework utilizes a single `handler.py` file along with Pydantic schemas to automatically generate a streaming HTTP endpoint that supports Server-Sent Events (SSE), an interactive OpenAPI/Swagger UI, and a zero-configuration MCP tool, all from a single process. The framework employs dual-mode content negotiation, allowing the same handler to serve both SSE-streaming and JSON-returning clients without modifications to the handler code. A dynamic code-generation mechanism ensures that Pydantic type annotations are correctly propagated to FastMCP's inspection layer, addressing a limitation in naive closure-based registration. HarnessAPI is built as a subclass of FastAPI, leveraging its middleware, dependency injection, and deployment capabilities.

**Results**  
The authors conducted a comparative analysis using six representative skills and reported a 74% reduction in framework-facing boilerplate code when using HarnessAPI compared to a manually maintained dual-stack implementation (FastAPI server + FastMCP server). This significant reduction in boilerplate suggests a more efficient development process and potentially lower maintenance overhead. The paper does not provide specific performance metrics such as latency or throughput, focusing instead on the reduction of code complexity.

**Limitations**  
The authors acknowledge that while HarnessAPI simplifies the deployment process, it may not address all edge cases in complex applications where custom routing or validation logic is required. Additionally, the reliance on Pydantic for type validation may introduce limitations in scenarios where more complex data structures are involved. The paper does not discuss the performance implications of the generated endpoints or the scalability of the framework under high load, which are critical factors for production environments.

**Why it matters**  
HarnessAPI has significant implications for the development of LLM tools, as it streamlines the deployment process and reduces the cognitive load on developers by minimizing code duplication. By providing a unified framework for both HTTP and MCP tool registrations, it encourages best practices in code maintenance and promotes consistency across different deployment environments. This framework could serve as a foundation for future work in building more sophisticated LLM applications, potentially influencing the design of similar tools in the ecosystem.

Authors: Edwin Jose  
Source: arXiv:2605.22733  
URL: [https://arxiv.org/abs/2605.22733v1](https://arxiv.org/abs/2605.22733v1)
