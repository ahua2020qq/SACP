<!--
Copyright (c) 2026 山野小娃

本文档采用 CC BY 4.0 协议。您可以自由分享和修改，但需保留署名。
-->

# SACP 结构化AI协同协议 V1.1 规范

## 版本信息

- **版本号**: v1.1
- **发布日期**: 2026-03-20
- **基于版本**: v1.0 (2026-02-20)
- **更新类型**: 功能扩展（完全向下兼容）

---

## 1. 更新概述

### 1.1 核心更新

SACP v1.1 在 v1.0 的基础上，新增 **第8种核心数据结构 `workflow`（工作流编排）**，实现了从"数据标准化"到"流程自动化"的关键跃迁。

**主要特性**：
- 新增 `workflow` 数据结构，支持跨系统的业务流程编排
- 定义节点依赖关系和触发条件
- 支持工作流状态监控和可视化
- 完全向下兼容 v1.0 的所有数据结构

### 1.2 设计目标

- **流程标准化**: 让 AI 能够理解、生成、执行业务流程
- **自动化闭环**: 实现跨系统的链式自动化协作
- **生态扩展**: 支持工作流模板的积累和复用

---

## 2. 新增数据结构：workflow

### 2.1 核心定位

`workflow` 是一种**工作流编排类**数据结构，用于定义多个 SACP 数据实体之间的依赖关系、触发条件和执行顺序。

**解决的问题**：
- v1.0 的7种数据结构（task、report、output、message、approval、schedule、metric）是孤立的
- 缺少描述"如何让这些数据流动起来"的标准化机制
- AI 无法理解复杂业务流程的执行逻辑

### 2.2 通用字段

继承 SACP 通用字段规范：

| 字段名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `type` | string | 是 | 固定为 `workflow` |
| `title` | string | 是 | 工作流标题，不超过100字符 |
| `create_time` | string | 是 | 创建时间，ISO 8601格式：`yyyy-MM-dd HH:mm:ss` |
| `update_time` | string | 是 | 更新时间，ISO 8601格式 |
| `creator` | string | 否 | 创建人ID/标识 |
| `source` | string | 否 | 数据来源系统标识 |
| `extend` | object | 否 | 扩展字段 |

### 2.3 workflow 专用字段

| 字段名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `steps` | array[object] | 是 | 工作流步骤列表 |
| `steps[].id` | string | 是 | 步骤唯一标识 |
| `steps[].type` | string | 是 | 步骤类型：`task`/`report`/`output`/`message`/`approval`/`schedule`/`metric` |
| `steps[].title` | string | 是 | 步骤标题 |
| `steps[].depends_on` | array[string] | 否 | 依赖的步骤ID列表（必须完成后才能执行当前步骤） |
| `steps[].trigger` | string | 否 | 触发条件表达式（详见2.4节） |
| `steps[].config` | object | 是 | 步骤配置对象（包含对应数据类型的所有必填字段） |
| `steps[].timeout` | integer | 否 | 超时时间（秒），0表示不超时，默认86400（24小时） |
| `steps[].retry_policy` | object | 否 | 重试策略（详见2.5节） |
| `status` | string | 是 | 工作流状态：`pending`/`running`/`paused`/`completed`/`failed` |
| `current_step` | string | 否 | 当前执行到的步骤ID |
| `started_at` | string | 否 | 开始执行时间 |
| `completed_at` | string | 否 | 完成时间 |
| `error_message` | string | 否 | 失败时的错误信息 |

### 2.4 触发条件表达式

触发条件用于定义步骤的自动执行条件。

**语法格式**：
```
[步骤ID].[字段名] [操作符] [值]
```

**支持的操作符**：
- `==` 等于
- `!=` 不等于
- `>` 大于
- `>=` 大于等于
- `<` 小于
- `<=` 小于等于
- `contains` 包含（字符串）
- `!contains` 不包含（字符串）

**触发时机**：
- 当依赖步骤（`depends_on`）全部完成时，评估触发条件
- 触发条件为 `true` 时，自动执行当前步骤
- 如果未定义 `trigger`，依赖步骤完成后立即执行

**示例**：
```json
"trigger": "step1.status == 'done'"
"trigger": "step3.status == 'approved'"
"trigger": "step5.metric_value > 1000"
"trigger": "step2.message contains '紧急'"
```

### 2.5 重试策略

当步骤执行失败时，可配置重试策略。

**重试策略对象**：
```json
{
  "max_retries": 3,           // 最大重试次数，默认0
  "retry_interval": 60,        // 重试间隔（秒），默认60
  "backoff_multiplier": 2.0,   // 退避乘数，每次重试间隔翻倍，默认1.0
  "retry_on": ["timeout", "error"]  // 重试触发条件：timeout/error，默认["error"]
}
```

---

## 3. 状态机

### 3.1 workflow 状态流转

```
pending → running → completed
                    ↘ failed
              ↘ paused → running
```

**状态说明**：
- `pending`: 待执行，已创建但未开始
- `running`: 执行中，正在执行某个步骤
- `paused`: 已暂停，人工暂停或等待外部触发
- `completed`: 已完成，所有步骤执行成功
- `failed`: 已失败，某个步骤执行失败且重试次数用尽

### 3.2 步骤状态

每个步骤内部也有独立状态：
- `pending`: 待执行
- `running`: 执行中
- `completed`: 已完成
- `failed`: 已失败
- `skipped`: 已跳过（前置步骤失败导致）

---

## 4. 完整示例

### 4.1 差旅报销流程

```json
{
  "type": "workflow",
  "title": "差旅报销流程",
  "create_time": "2026-03-20 14:00:00",
  "update_time": "2026-03-20 14:00:00",
  "creator": "user_12345",
  "source": "AI助手",
  "steps": [
    {
      "id": "step1",
      "type": "task",
      "title": "收集差旅发票",
      "config": {
        "description": "收集本次差旅的所有发票和凭证",
        "priority": "高",
        "status": "todo",
        "progress": 0,
        "output_expect": "发票扫描件和费用明细表"
      },
      "timeout": 86400
    },
    {
      "id": "step2",
      "type": "report",
      "title": "生成报销报告",
      "depends_on": ["step1"],
      "trigger": "step1.status == 'done'",
      "config": {
        "tags": ["报销", "差旅"],
        "summary": "2026年3月北京出差费用报销",
        "content": "# 差旅费用报销\\n\\n## 费用明细\\n- 交通费：¥2,500\\n- 住宿费：¥1,800\\n- 餐费：¥600\\n\\n**总计：¥4,900**"
      },
      "timeout": 3600
    },
    {
      "id": "step3",
      "type": "approval",
      "title": "主管审批",
      "depends_on": ["step2"],
      "trigger": "step2.created != null",
      "config": {
        "apply_type": "报销",
        "applicant": "user_12345",
        "approver_list": ["manager_001", "finance_001"],
        "approval_data": {
          "amount": 4900,
          "category": "差旅费",
          "description": "北京出差3天"
        },
        "current_step": 0,
        "status": "pending"
      },
      "timeout": 86400,
      "retry_policy": {
        "max_retries": 0
      }
    },
    {
      "id": "step4",
      "type": "schedule",
      "title": "财务打款",
      "depends_on": ["step3"],
      "trigger": "step3.status == 'approved'",
      "config": {
        "start_time": "2026-03-21 10:00:00",
        "end_time": "2026-03-21 10:30:00",
        "location": "财务系统",
        "participants": ["finance_001"],
        "reminder_type": "email",
        "reminder_time": "1hour"
      },
      "timeout": 3600
    },
    {
      "id": "step5",
      "type": "message",
      "title": "通知申请人",
      "depends_on": ["step4"],
      "trigger": "step4.status == 'done'",
      "config": {
        "text": "您的差旅报销已批准，款项将在1-2个工作日打入您的工资卡"
      }
    }
  ],
  "status": "pending",
  "extend": {
    "company": "某科技公司",
    "department": "研发部",
    "workflow_template_id": "expense_travel_001"
  }
}
```

### 4.2 软件开发流程

```json
{
  "type": "workflow",
  "title": "功能开发流程",
  "create_time": "2026-03-20 09:00:00",
  "update_time": "2026-03-20 09:00:00",
  "steps": [
    {
      "id": "dev_task",
      "type": "task",
      "title": "开发新功能",
      "config": {
        "description": "实现用户登录功能",
        "priority": "高",
        "status": "todo",
        "progress": 0
      }
    },
    {
      "id": "unit_test",
      "type": "output",
      "title": "单元测试",
      "depends_on": ["dev_task"],
      "trigger": "dev_task.status == 'done'",
      "config": {
        "category": "code",
        "content": "function testLogin() { ... }",
        "language": "javascript"
      }
    },
    {
      "id": "code_review",
      "type": "approval",
      "title": "代码审查",
      "depends_on": ["unit_test"],
      "trigger": "unit_test.created != null",
      "config": {
        "apply_type": "代码审查",
        "applicant": "developer_001",
        "approver_list": ["tech_lead_001"],
        "approval_data": {
          "pr_url": "https://github.com/repo/pull/123",
          "files_changed": 5
        },
        "current_step": 0,
        "status": "pending"
      }
    },
    {
      "id": "deploy",
      "type": "schedule",
      "title": "部署上线",
      "depends_on": ["code_review"],
      "trigger": "code_review.status == 'approved'",
      "config": {
        "start_time": "2026-03-20 18:00:00",
        "end_time": "2026-03-20 19:00:00",
        "location": "生产环境",
        "participants": ["devops_001"],
        "reminder_type": "push",
        "reminder_time": "30min"
      }
    },
    {
      "id": "notify",
      "type": "message",
      "title": "发布通知",
      "depends_on": ["deploy"],
      "trigger": "deploy.status == 'done'",
      "config": {
        "text": "新功能已上线：用户登录功能"
      }
    }
  ],
  "status": "pending"
}
```

---

## 5. 实施指南

### 5.1 系统要求

实现 SACP v1.1 workflow 的系统需要具备：

1. **流程引擎**: 能够解析 workflow 定义并执行步骤
2. **状态管理**: 跟踪 workflow 和每个步骤的状态
3. **触发器**: 监听依赖步骤的状态变化，评估触发条件
4. **超时处理**: 检测步骤超时并执行重试或失败处理
5. **事件通知**: 在关键状态变化时发送通知

### 5.2 执行流程

```
1. 接收 workflow 对象
2. 验证步骤定义和依赖关系
3. 初始化状态为 pending
4. 启动工作流（status → running）
5. 找到无依赖的起始步骤
6. 依次执行步骤：
   a. 检查依赖步骤是否完成
   b. 评估触发条件
   c. 创建对应类型的 SACP 对象
   d. 更新步骤状态
   e. 触发下一步骤
7. 所有步骤完成 → status → completed
8. 任何步骤失败 → status → failed
```

### 5.3 API 扩展建议

**创建工作流**：
```
POST /api/sacp/workflows
Content-Type: application/json

{
  "workflow": { ...workflow对象... }
}

Response:
{
  "workflow_id": "wf_20260320_001",
  "status": "pending",
  "created_at": "2026-03-20 14:00:00"
}
```

**查询工作流状态**：
```
GET /api/sacp/workflows/{workflow_id}

Response:
{
  "workflow_id": "wf_20260320_001",
  "status": "running",
  "current_step": "step3",
  "steps": [
    {"id": "step1", "status": "completed"},
    {"id": "step2", "status": "completed"},
    {"id": "step3", "status": "running"},
    {"id": "step4", "status": "pending"},
    {"id": "step5", "status": "pending"}
  ]
}
```

**暂停/恢复工作流**：
```
POST /api/sacp/workflows/{workflow_id}/pause
POST /api/sacp/workflows/{workflow_id}/resume
```

---

## 6. 与 v1.0 的兼容性

SACP v1.1 **完全向下兼容** v1.0：

- v1.0 的所有数据结构（task、report、output、message、approval、schedule、metric）保持不变
- v1.0 的 API 接口保持不变
- v1.0 的实现系统可以继续正常工作
- 新增的 `workflow` 结构是可选的，不影响现有系统

**升级路径**：
- v1.0 系统可以直接升级到 v1.1，无需修改现有代码
- 可以选择性地实现 workflow 功能
- v1.0 和 v1.1 系统可以互相协作

---

## 7. 应用场景

### 7.1 企业流程自动化

- 费用报销流程
- 请假审批流程
- 采购申请流程
- 入职办理流程

### 7.2 软件开发流程

- 代码审查流程
- CI/CD 部署流程
- Bug 修复流程
- 发布管理流程

### 7.3 客户服务流程

- 工单处理流程
- 投诉处理流程
- 售后服务流程
- 客户咨询流程

### 7.4 AI Agent 协作

- 多 Agent 任务分配
- 结果汇总流程
- 质量检查流程
- 自动化测试流程

---

## 8. 最佳实践

### 8.1 工作流设计原则

1. **步骤单一职责**: 每个步骤只做一件事
2. **依赖关系清晰**: 避免循环依赖
3. **错误处理完备**: 为每个步骤定义超时和重试策略
4. **可观测性**: 在关键步骤添加 metric 收集

### 8.2 性能优化

1. **并行执行**: 无依赖关系的步骤可以并行执行
2. **异步处理**: 长时间步骤采用异步模式
3. **缓存优化**: 相同输入的步骤可以缓存结果

### 8.3 安全建议

1. **权限控制**: 每个步骤继承相应数据类型的权限要求
2. **审计日志**: 记录所有状态变更和执行日志
3. **敏感数据**: 审批类步骤的 config 应加密存储

---

## 9. 版本历史

- **v1.1** (2026-03-20): 新增 workflow 工作流编排结构
- **v1.0** (2026-02-20): 初始版本，定义7种核心数据结构

---

## 10. 作者与许可

**作者**: 山野小娃

**联系**: douyacenter@163.com

**许可**: CC BY 4.0

您可以自由分享、修改和使用本规范，但必须保留原作者署名。

---

## 附录A: 触发条件表达式详细语法

### A.1 基本语法

```
[步骤ID].[字段路径] [操作符] [值]
```

### A.2 字段路径

- 步骤状态: `[步骤ID].status`
- 步骤创建时间: `[步骤ID].create_time`
- 步骤配置字段: `[步骤ID].config.[字段名]`

### A.3 值类型

- 字符串: 用单引号包裹，如 `'done'`
- 数字: 直接写，如 `1000`
- 布尔: `true` / `false`
- 时间: ISO 8601格式，如 `'2026-03-20 14:00:00'`

### A.4 高级表达式（v1.2+规划）

未来版本将支持：
- 逻辑运算符: `AND`, `OR`, `NOT`
- 时间比较: `>`, `<`（针对时间字段）
- 正则表达式: `matches`, `!matches`
- 自定义函数: `now()`, `duration()`

---

**SACP v1.1 - 让AI驱动的业务流程标准化、自动化、智能化**
