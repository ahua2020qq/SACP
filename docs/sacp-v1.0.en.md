<!--
Copyright (c) 2026 山野小娃 (Jorney Ruan)

This document is licensed under CC BY 4.0. You are free to share and adapt, provided you give appropriate credit.
-->

# SACP (Structured AI Collaboration Protocol) V1.0 Specification

## 1. Protocol Overview

### 1.1 Positioning
SACP (Structured AI Collaboration Protocol) is an open, extensible, and standardized AI-native collaboration protocol. It defines structured data models, interaction specifications, and security guidelines for cross-system and cross-software collaboration in AI-driven scenarios. Any software (traditional office software, AI tools, business systems, developer tools) that follows this protocol can achieve seamless AI collaboration, data interoperability, and unified result storage, breaking down data silos in the AI era.

### 1.2 Goals
- Solve the industry pain points of disordered AI outputs, inconsistent formats, and cross-system incompatibility.
- Provide an out-of-the-box standardized solution for AI collaboration, reducing development and integration costs.
- Build an open AI collaboration ecosystem to enable "one standardization, all-scenario collaboration."

### 1.3 Applicable Scenarios
- Traditional software: OA systems, expense reimbursement, travel management, ERP, CRM, knowledge bases, etc.
- AI-native tools: Large model applications, AI execution tools (e.g., OpenClaw), AI knowledge bases, BI data analysis tools, etc.
- Developer tools: Code hosting, CI/CD, project management tools, etc.
- Personal productivity tools: To-do lists, calendars, note-taking apps, etc.

## 2. Core Design Principles

1. **Strict Core, Weakly Invasive Extension**: Core data models are strictly standardized to ensure interoperability; extension fields are completely open to accommodate personalized needs without breaking the core structure.
2. **Security by Design**: The protocol natively defines data security, permission isolation, and encryption guidelines to avoid security risks in AI collaboration from the root.
3. **100% Backward Compatibility**: All version iterations of the protocol are fully backward compatible with core data models; existing integrators do not need to modify code to adapt to new versions.
4. **Minimal Integration Effort**: The protocol provides standardized APIs and multi-language SDKs; integrators only need to convert data formats to achieve protocol adaptation, minimizing development costs.

## 3. Core Data Model Specifications (Mandatory)

SACP defines seven core standardized data structures. All integrators must strictly follow them as the foundation for cross-system collaboration. Each structure contains mandatory core fields and an optional extension field `extend`. Mandatory fields cannot be modified or omitted; extension fields can be customized as needed.

### 3.1 Common Fields
All seven structures include the following common fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Data type, one of: `task`/`report`/`output`/`message`/`approval`/`schedule`/`metric` |
| `title` | string | Yes | Title, max 100 characters |
| `create_time` | string | Yes | Creation time in ISO 8601 format: `yyyy-MM-dd HH:mm:ss` |
| `update_time` | string | Yes | Update time in ISO 8601 format |
| `creator` | string | No | Creator ID/identifier |
| `source` | string | No | Source system identifier, e.g., `OpenClaw`/`EnterpriseOA` |
| `extend` | object | No | Standardized extension field for personalized needs without affecting core structure |

### 3.2 Detailed Specifications for the Seven Core Structures

#### 3.2.1 `task`
**Purpose**: Represents tasks, to-dos, development tasks, etc.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | string | Yes | Detailed task description |
| `priority` | string | Yes | Priority: `high`/`medium`/`low` |
| `status` | string | Yes | Status: `todo`/`doing`/`confirm`/`done`/`archived` |
| `progress` | integer | Yes | Progress percentage, 0-100 |
| `from_command` | string | No | Original command that generated this task |
| `output_expect` | string | No | Expected output or deliverable description |

#### 3.2.2 `report`
**Purpose**: Represents analysis reports, proposal documents, summaries, knowledge assets, etc.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `tags` | array[string] | No | List of tags |
| `outline` | array[string] | No | Outline (list of chapter titles) |
| `summary` | string | No | Abstract/introduction |
| `content` | string | Yes | Full content in Markdown format |
| `from_task` | string | No | Associated task ID (if generated from a task) |

#### 3.2.3 `output`
**Purpose**: Represents deliverables such as code, files, images, links.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `category` | string | Yes | Category: `code`/`file`/`image`/`link` |
| `content` | string | Conditional | When `category` is `code` or `link`, contains code text or URL; may be empty for other categories |
| `language` | string | No | Programming language (recommended when `category=code`) |
| `url` | string | Conditional | When `category` is `file`/`image`, this is the file access URL; when `category` is `link`, this is the link address |
| `file_size` | integer | No | File size in bytes, only for `file`/`image` |
| `from_task` | string | No | Associated task ID |

#### 3.2.4 `message`
**Purpose**: Represents short notifications, status reminders, etc., without carrying core business data.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `text` | string | Yes | Notification content, max 2 lines (recommended ≤140 characters) |

#### 3.2.5 `approval`
**Purpose**: Represents various approval requests (reimbursement, leave, contracts, etc.).

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `apply_type` | string | Yes | Application type, e.g., `reimbursement`/`leave`/`contract` |
| `applicant` | string | Yes | Applicant ID |
| `approver_list` | array[string] | Yes | List of approver IDs (in order) |
| `current_approver` | string | No | Current pending approver ID |
| `status` | string | Yes | Status: `pending`/`approving`/`approved`/`rejected`/`cancelled` |
| `content` | string | Yes | Description of the application |
| `amount` | number | No | Monetary amount (e.g., reimbursement, procurement) |
| `start_time` | string | No | Start time (e.g., leave) |
| `end_time` | string | No | End time (e.g., leave) |

#### 3.2.6 `schedule`
**Purpose**: Represents meetings, reminders, recurring tasks, etc.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | string | No | Detailed description |
| `start_time` | string | Yes | Start time |
| `end_time` | string | Yes | End time |
| `status` | string | Yes | Status: `scheduled`/`ongoing`/`completed`/`cancelled` |
| `priority` | string | No | Priority: `high`/`medium`/`low` |
| `remind_time` | string | No | Reminder time (ISO 8601) |
| `cycle_rule` | string | No | Recurrence rule, e.g., `daily`/`weekly on Monday`/`monthly on 1st` |
| `participant_list` | array[string] | No | List of participant IDs |

#### 3.2.7 `metric`
**Purpose**: Represents statistical data such as operational metrics, financial figures, project progress.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `stat_cycle` | string | Yes | Statistical period, e.g., `2026-02` (monthly), `2026-W08` (weekly) |
| `data_source` | string | No | Source system of the data |
| `metric_list` | array[object] | Yes | Array of metrics, each containing `name` (metric name), `value` (numeric value), `unit` (unit) |

## 4. Interaction Specifications

SACP defines two standardized interaction modes to cover all collaboration scenarios. Integrators can implement as needed.

### 4.1 Mode 1: RESTful API (Active Invocation)

All APIs share the common prefix: `/api/v1/sacp/`. All requests must use HTTPS and include protocol authentication headers.

#### 4.1.1 Authentication
- Each integrator generates a `SACP-API-Key` and `SACP-API-Secret` for identity authentication.
- All requests must include the following headers:
  - `X-SACP-API-Key`: The integrator's API Key
  - `X-SACP-Signature`: SHA256 signature generated from `request body + timestamp + API Secret` to prevent tampering
  - `X-SACP-Timestamp`: Current timestamp, valid within 10 minutes

#### 4.1.2 Core API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/data/write` | POST | Write a single standardized data item (any of the seven types) |
| `/data/batch-write` | POST | Batch write multiple data items (mixed types allowed) |
| `/data/list` | GET | Paginated query of data list by type, time range, keywords |
| `/data/detail` | GET | Retrieve full details of a single data item by ID |
| `/data/update` | PUT | Update status or content of a data item |
| `/data/delete` | DELETE | Delete a data item |

### 4.2 Mode 2: Webhook Event Push

The protocol defines a standardized event push mechanism for real-time data synchronization between systems without polling.

#### 4.2.1 Supported Event Types
- `data.create`: Triggered when new data is created
- `data.update`: Triggered when data is updated
- `data.delete`: Triggered when data is deleted
- `status.change`: Triggered when status of a task/approval/schedule changes

#### 4.2.2 Push Specifications
- Integrators must configure a Webhook receiver URL, event types, and a push signature secret.
- Push payloads contain the standardized SACP data structure, including event type, trigger time, and full data details.
- Push requests must include a signature header; receivers must verify the signature to prevent malicious pushes.
- Failed pushes must implement a retry mechanism: up to 3 retries with 1-minute intervals.

## 5. Security Specifications (Mandatory)

1. **Transport Security**: All API requests and Webhook pushes must use HTTPS; plain HTTP is prohibited.
2. **Data Isolation**: Integrators must implement strict data isolation between different users/tenants to prevent unauthorized access.
3. **Signature Verification**: All requests and pushes must undergo signature verification to prevent tampering and replay attacks.
4. **Least Privilege**: API Keys must be assigned with minimal necessary permissions; support IP whitelisting and QPS rate limiting.
5. **Sensitive Data Handling**: The protocol prohibits transmitting sensitive information such as users' LLM API keys or passwords; only business data for collaboration is allowed.
6. **Audit Logging**: Integrators must retain complete logs of API calls and Webhook pushes for compliance and troubleshooting, with a retention period of at least 6 months.

## 6. Extension Guidelines

1. All extensions must be placed in the `extend` field; core fields must not be modified.
2. Extension field names must be clear, unambiguous, and free of special characters.
3. Extensions must not affect the parsing of core structures; if an integrator cannot recognize an extension, they must still parse the core fields correctly.
4. Industry-common extensions may be incorporated into the standardized specification through future protocol iterations.

## 7. Official Implementations and Open Source Ecosystem

1. **Official Reference Implementation**: [ClawSync](https://github.com/ahua2020qq/clawsync) is the first complete implementation of the SACP protocol, providing full support for all protocol capabilities.
2. **Multi-language SDKs**: Official SDKs for Python, Node.js, Java, Go, etc., to reduce integration effort.
3. **Open Source Licenses**:
   - SACP protocol specification: Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) – free to share and adapt with attribution.
   - Official SDKs and reference implementation: Licensed under the [MIT License](https://opensource.org/licenses/MIT).

## 8. Versioning Rules

- Version format: `MAJOR.MINOR.PATCH`
- **MAJOR version**: Incremented when core data models change in a backward-incompatible way.
- **MINOR version**: Incremented when new APIs or extensions are added in a backward-compatible way.
- **PATCH version**: Incremented for bug fixes and documentation improvements that are backward-compatible.

---

**Author:** 山野小娃 (Jorney Ruan)
**Copyright:** Copyright (c) 2026 山野小娃 (Jorney Ruan)
**License:** This document is licensed under CC BY 4.0. You are free to share and adapt, provided you give appropriate credit.
