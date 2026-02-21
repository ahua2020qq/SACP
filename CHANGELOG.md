# SACP 协议更新日志

本文档记录SACP协议的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [1.0.0] - 2026-02-20

### 新增
- 🎉 发布SACP V1.0正式版
- 📋 定义7种核心数据结构：task, report, output, message, approval, schedule, metric
- 🔌 定义RESTful API主动调用规范
- 🔔 定义Webhook事件推送规范
- 🔒 内置安全规范（签名、加密、数据隔离）
- 🧩 支持extend字段灵活扩展
- 📚 提供完整的协议文档
- 🐍 提供Python SDK示例

### 文档
- 添加协议规范文档 (sacp-v1.0.md)
- 添加README说明文档
- 添加作者信息和版权声明
- 采用CC BY 4.0开源协议

---

## [未来版本规划]

### [1.5.0] - 规划中
- 🏗️ 计划增加行业扩展字段（财务、医疗等）
- 📊 计划增强metric数据指标类
- 🔧 计划优化批量同步性能

### [2.0.0] - 规划中
- 🔙 计划引入事件溯源机制
- 📦 计划优化批量同步功能
- 🚀 计划推出更多语言SDK

---

**版权声明：**
Copyright (c) 2026 山野小娃 (Jorney Ruan)
本文档遵循 CC BY 4.0 协议
