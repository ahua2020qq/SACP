# SACP 协议更新日志 | SACP Protocol Changelog

本文档记录SACP协议的所有重要变更。
This document records all important changes to the SACP protocol.

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
Versioning based on [Semantic Versioning](https://semver.org/lang/zh-CN/).

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
Copyright (c) 2026 山野小娃 (Jorney Ruan)
本文档遵循 CC BY 4.0 协议 | This document follows CC BY 4.0 license
