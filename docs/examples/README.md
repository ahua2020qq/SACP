# SACP 数据结构示例 | SACP Data Structure Examples

本目录包含SACP协议定义的7种核心数据结构的JSON示例。
This directory contains JSON examples for the 7 core data structures defined in the SACP protocol.

## 示例列表 | Example List

### 1. task.json - 任务执行类
**用途 | Purpose**: 表示需要执行的任务、待办事项、开发任务等
Represents tasks, to-dos, development tasks, etc.

**关键字段 | Key Fields**:
- `priority`: 优先级 (high/medium/low)
- `status`: 状态 (todo/doing/confirm/done/archived)
- `progress`: 进度 (0-100)

### 2. report.json - 文档报告类
**用途 | Purpose**: 表示分析报告、方案文档、总结、知识沉淀等
Represents analysis reports, proposal documents, summaries, knowledge assets, etc.

**关键字段 | Key Fields**:
- `content`: Markdown格式的完整内容
- `tags`: 标签列表
- `outline`: 大纲

### 3. output.json - 成果交付类
**用途 | Purpose**: 表示代码、文件、图片、链接等交付物
Represents deliverables such as code, files, images, links

**关键字段 | Key Fields**:
- `category`: 类别 (code/file/image/link)
- `content`: 代码文本或URL
- `language`: 代码语言

### 4. message.json - 通知消息类
**用途 | Purpose**: 用于简短通知、状态提醒等，不承载核心业务数据
Used for short notifications, status reminders, without carrying core business data

**关键字段 | Key Fields**:
- `text`: 通知内容 (不超过140字符)

### 5. approval.json - 审批流程类
**用途 | Purpose**: 表示各类审批申请（报销、请假、合同等）
Represents various approval requests (reimbursement, leave, contracts, etc.)

**关键字段 | Key Fields**:
- `apply_type`: 申请类型
- `approver_list`: 审批人列表
- `amount`: 涉及金额

### 6. schedule.json - 日程待办类
**用途 | Purpose**: 表示会议、提醒、周期任务等
Represents meetings, reminders, recurring tasks, etc.

**关键字段 | Key Fields**:
- `start_time` / `end_time`: 开始/结束时间
- `participant_list`: 参与人列表
- `cycle_rule`: 周期性规则

### 7. metric.json - 数据指标类
**用途 | Purpose**: 表示运营指标、财务数据、项目进度等统计数据
Represents statistical data such as operational metrics, financial figures, project progress

**关键字段 | Key Fields**:
- `stat_cycle`: 统计周期 (如 2026-02)
- `metric_list`: 指标数组 (name/value/unit)

## 使用方法 | Usage

```bash
# 查看示例
cat examples/task.json

# 使用Python SDK写入
from sacp_client import SACPClient
import json

client = SACPClient(base_url, api_key, api_secret)

# 读取并写入示例数据
with open('examples/task.json', 'r') as f:
    data = json.load(f)
    result = client.write(data)
```

## 注意事项 | Notes

- 所有示例中的时间字段都使用ISO 8601格式
- 所有结构都包含通用字段：type, title, create_time, update_time
- extend字段可根据实际需求自定义
- 必填字段不可省略

---

**Copyright (c) 2026 山野小娃 (Jorney Ruan)**
**Licensed under CC BY 4.0**
