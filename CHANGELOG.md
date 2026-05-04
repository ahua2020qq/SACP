# SACP 协议更新日志 | SACP Protocol Changelog

本文档记录SACP协议的所有重要变更。
This document records all important changes to the SACP protocol.

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
Versioning based on [Semantic Versioning](https://semver.org/lang/zh-CN/).

---

## [1.1.0] - 2026-03-20

### 新增 | Added
- 🎉 发布SACP V1.1功能扩展版 | Released SACP V1.1 feature extension version
- 🔄 新增第8种核心数据结构：workflow（工作流编排）| Added 8th core data structure: workflow (orchestration)
- 🔗 支持步骤依赖关系定义 | Support step dependency definition
- ⚡ 支持触发条件表达式 | Support trigger condition expressions
- 📊 支持工作流状态监控 | Support workflow status monitoring
- 🔁 支持步骤重试策略 | Support step retry policy
- ⏱️ 支持步骤超时控制 | Support step timeout control
- 📈 支持工作流可视化（规范定义）| Support workflow visualization (specification defined)
- ✅ 完全向下兼容v1.0 | Fully backward compatible with v1.0

### 文档 | Documentation
- 添加v1.1协议规范文档 | Added v1.1 protocol specification documentation (sacp-v1.1.md)
- 添加workflow完整示例 | Added complete workflow examples
- 添加状态机定义 | Added state machine definition
- 添加触发条件表达式语法 | Added trigger condition expression syntax
- 添加实施指南 | Added implementation guide
- 添加API扩展建议 | Added API extension recommendations

### 设计原则 | Design Principles
- 从"数据标准化"到"流程自动化"的关键跃迁 | Key leap from "data standardization" to "process automation"
- AI原生的工作流编排框架 | AI-native workflow orchestration framework
- 支持工作流模板积累和复用 | Support workflow template accumulation and reuse
- 企业级流程自动化解决方案 | Enterprise process automation solution

---

## [1.0.0] - 2026-02-20

### 新增 | Added
- 🎉 发布SACP V1.0正式版 | Released SACP V1.0 official version
- 📋 定义7种核心数据结构 | Defined 7 core data structures: task, report, output, message, approval, schedule, metric
- 🔌 定义RESTful API主动调用规范 | Defined RESTful API active invocation specification
- 🔔 定义Webhook事件推送规范 | Defined Webhook event push specification
- 🔒 内置安全规范（签名、加密、数据隔离）| Built-in security specifications (signature, encryption, data isolation)
- 🧩 支持extend字段灵活扩展 | Support flexible extension via extend fields
- 📚 提供完整的协议文档 | Provided complete protocol documentation
- 🐍 提供Python SDK示例 | Provided Python SDK example

### 文档 | Documentation
- 添加协议规范文档 | Added protocol specification documentation (sacp-v1.0.zh.md & sacp-v1.0.en.md)
- 添加README说明文档 | Added README documentation
- 添加作者信息和版权声明 | Added author information and copyright notice
- 采用CC BY 4.0开源协议 | Adopted CC BY 4.0 open source license

---

## [未来版本规划 | Future Versions]

### [1.2.0] - 规划中 | Planning
- 🔣 支持复杂触发条件（AND/OR/NOT逻辑运算）| Support complex trigger conditions (AND/OR/NOT logic)
- 🎨 添加workflow可视化DSL | Add workflow visualization DSL
- 📊 添加工作流性能监控指标 | Add workflow performance monitoring metrics
- 🔧 添加工作流调试工具 | Add workflow debugging tools

### [1.3.0] - 规划中 | Planning
- 📦 建立工作流模板市场 | Establish workflow template marketplace
- 🤖 支持AI自动生成workflow | Support AI-generated workflow
- 🌐 添加workflow分享机制 | Add workflow sharing mechanism
- 📝 添加最佳实践案例库 | Add best practice case library

### [1.5.0] - 规划中 | Planning
- 🏗️ 计划增加行业扩展字段（财务、医疗等）| Plan to add industry extension fields (finance, healthcare, etc.)
- 📊 计划增强metric数据指标类 | Plan to enhance metric data structure
- 🔧 计划优化批量同步性能 | Plan to optimize batch sync performance

### [2.0.0] - 规划中 | Planning
- 🔙 计划引入事件溯源机制 | Plan to introduce event sourcing mechanism
- 📦 计划优化批量同步功能 | Plan to optimize batch sync functionality
- 🚀 计划推出更多语言SDK | Plan to release more language SDKs

---

**版权声明 | Copyright:**
Copyright (c) 2026 山野小娃
本文档遵循 CC BY 4.0 协议 | This document follows CC BY 4.0 license
