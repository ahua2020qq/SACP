# SACP: Structured AI Collaboration Protocol

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/version-1.0-blue)](https://github.com/ahua2020qq/SACP/releases/tag/v1.0)

**结构化AI协同协议 (Structured AI Collaboration Protocol)** — 为AI驱动的跨系统协作提供标准化数据模型与交互规范，让AI输出有序，让系统互通无界。

---

## 中文介绍 | [English](#english)

### 为什么需要SACP？

当前AI生成的内容（任务、报告、审批等）多以自然语言散落在各个界面，无法被其他系统直接消费。SACP通过定义**7种标准数据结构**和**安全交互规范**，为AI与软件生态搭建了一座"通用语言"的桥梁。

- **打破数据孤岛**：统一的任务、报告、审批等格式，让OA、ERP、AI工具无缝协作。
- **AI原生设计**：从数据结构到交互模式，全面适配AI驱动场景。
- **安全内置**：签名校验、数据隔离、HTTPS强制，企业级安全基线。
- **与MCP互补**：MCP解决模型与工具的上下文互通，SACP解决系统间AI数据的标准化流转。

### 核心能力

- **7种标准化数据结构**：任务(task)、报告(report)、输出(output)、消息(message)、审批(approval)、日程(schedule)、指标(metric)
- **两种交互模式**：RESTful API（主动调用） + Webhook（事件推送）
- **强制安全规范**：签名、加密、权限最小化
- **灵活扩展**：所有结构均支持`extend`字段，满足个性化需求

### 版本路线

| 版本 | 发布日期   | 核心内容                 | 状态     |
| ---- | ---------- | ------------------------ | -------- |
| v1.0 | 2026-02-20 | 7种核心结构 + 基础交互   | ✅ 已发布 |
| v1.5 | 规划中     | 行业扩展（财务、医疗等） | 🚧 规划中 |
| v2.0 | 规划中     | 事件溯源、批量同步优化   | 🚧 规划中 |

### 快速开始

1. 阅读[协议规范（中文版）](./docs/sacp-v1.0.zh.md)或[English Specification](./docs/sacp-v1.0.en.md)了解数据模型。
2. 参考[API文档](./docs/api-reference.md)对接系统。
3. 查看[示例代码](./docs/examples/)快速上手。
4. 使用官方SDK（[Python](./sdk/python/sacp_client.py)）简化接入。

### 开源协议

- 协议规范：采用 [CC BY 4.0](LICENSE) 协议，可自由分享、演绎，但需保留署名。
- 官方SDK与示例：采用 [MIT](LICENSE-MIT) 协议。

### 生态联动

- [ClawSync](https://github.com/ahua2020qq/clawsync) —— SACP协议的首个官方参考实现，开箱即用的AI协同工作台。

---

<a name="english"></a>
## English | [中文](#中文介绍)

### Why SACP?

AI-generated content (tasks, reports, approvals, etc.) is currently scattered across interfaces in natural language and cannot be directly consumed by other systems. SACP bridges AI and software ecosystems by defining **7 standard data structures** and **secure interaction specifications**.

- **Break Data Silos**: Unified formats for tasks, reports, approvals, etc., enable seamless collaboration between OA, ERP, and AI tools.
- **AI-Native Design**: From data structures to interaction patterns, fully adapted for AI-driven scenarios.
- **Security Built-in**: Signature verification, data isolation, mandatory HTTPS - enterprise-grade security baseline.
- **Complementary to MCP**: MCP solves model-tool context interoperability; SACP solves standardized AI data flow between systems.

### Core Capabilities

- **7 Standardized Data Structures**: task, report, output, message, approval, schedule, metric
- **Two Interaction Modes**: RESTful API (active invocation) + Webhook (event push)
- **Mandatory Security**: Signature, encryption, principle of least privilege
- **Flexible Extension**: All structures support `extend` fields for customization

### Version Roadmap

| Version | Release Date | Core Content                                | Status            |
| ------- | ------------ | ------------------------------------------- | ----------------- |
| v1.0    | 2026-02-20   | 7 core structures + basic interactions      | ✅ Released       |
| v1.5    | Planning     | Industry extensions (finance, healthcare, etc.) | 🚧 Planning    |
| v2.0    | Planning     | Event sourcing, batch sync optimization     | 🚧 Planning    |

### Quick Start

1. Read the [protocol specification (English)](./docs/sacp-v1.0.en.md) or [中文版](./docs/sacp-v1.0.zh.md) to understand data models.
2. Reference the [API documentation](./docs/api-reference.md) for system integration.
3. Check [example code](./docs/examples/) for quick start.
4. Use the official SDK ([Python](./sdk/python/sacp_client.py)) to simplify integration.

### Open Source License

- Protocol specification: Licensed under [CC BY 4.0](LICENSE) — free to share and adapt with attribution.
- Official SDK and examples: Licensed under [MIT](LICENSE-MIT).

### Ecosystem

- [ClawSync](https://github.com/ahua2020qq/clawsync) — The first official reference implementation of SACP protocol, a ready-to-use AI collaboration workspace.

---

## 贡献指南 | Contributing

欢迎通过Issue或PR参与协议完善。/ Contributions via Issues or PRs are welcome!

---

## 作者与维护者 | Author & Maintainer

**作者 | Author:** 山野小娃 (Jorney Ruan)

**联系 | Contact:**
- Email: ahua2020@qq.com
- GitHub: [@ahua2020qq](https://github.com/ahua2020qq)

**版权声明 | Copyright:**
Copyright (c) 2026 山野小娃 (Jorney Ruan)

本协议规范采用 CC BY 4.0 许可证开源。您可以自由地分享、修改和使用本规范，但必须保留原作者署名。
This specification is licensed under CC BY 4.0. You are free to share, modify, and use this specification, provided you retain attribution.

---

*本项目由 山野小娃 (Jorney Ruan) 发起并维护，感谢所有贡献者的支持！*
*This project is initiated and maintained by 山野小娃 (Jorney Ruan). Thanks to all contributors!*
