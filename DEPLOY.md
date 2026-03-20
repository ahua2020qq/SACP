# SACP 部署指南

## 域名：douya.green

---

## 方式一：通过 Cloudflare Pages 直接上传（最快）

### 1. 准备文件
确保项目目录包含以下文件：
```
D:\zhipu\sacp\
├── index.html          (主页面 - 动画卡通风格)
├── spec.html           (协议规范文档 - 专业简洁风格)
└── README.md           (项目说明)
```

### 2. 使用 Wrangler CLI 上传

```bash
# 安装 wrangler (如果还没安装)
npm install -g wrangler

# 登录 Cloudflare
wrangler login

# 进入项目目录
cd D:\zhipu\sacp

# 部署到 Cloudflare Pages
wrangler pages publish . --project-name=sacp-protocol
```

### 3. 通过 Web 界面上传（备选）

1. 访问 https://dash.cloudflare.com/
2. 左侧菜单选择 "Workers & Pages"
3. 点击 "Create application" → "Pages" → "Upload assets"
4. 项目名称：`sacp-protocol`
5. 将以下文件拖拽上传：
   - `index.html`
   - `spec.html`
6. 点击 "Deploy site"

---

## 方式二：通过 GitHub + Cloudflare Pages（推荐，支持自动更新）

### 1. 推送到 GitHub

```bash
cd D:\zhipu\sacp

# 初始化 git
git init

# 添加文件
git add index.html spec.html README.md docs/

# 提交
git commit -m "Initial commit: SACP protocol website with internationalization

- Added animated homepage with 9 language support
- Added professional specification document
- Added Chinese and English support"

# 创建 GitHub 仓库后，推送代码
git remote add origin https://github.com/ahua2020qq/sacp.git
git branch -M main
git push -u origin main
```

### 2. 在 Cloudflare Pages 连接 GitHub

1. 访问 https://dash.cloudflare.com/
2. "Workers & Pages" → "Create application" → "Pages" → "Connect to Git"
3. 选择你的 GitHub 仓库
4. 配置构建设置：
   - **Project name**: `sacp-protocol`
   - **Production branch**: `main`
   - **Build command**: (留空)
   - **Build output directory**: `/` (根目录)
5. 点击 "Save and Deploy"

---

## 绑定域名 douya.green

### 1. 在 Cloudflare Pages 项目中添加自定义域名

1. 进入你的 Pages 项目
2. 点击 "Custom domains" 标签
3. 点击 "Set up a custom domain"
4. 输入：`douya.green`
5. 点击 "Continue"

### 2. 配置 DNS 记录

Cloudflare 会自动为你添加以下 DNS 记录：

```
类型: CNAME
名称: douya.green (或 @)
目标: sacp-protocol.pages.dev
代理状态: 已开启 (橙色云朵)
```

### 3. 配置子域名（可选）

如果你想用 `www.douya.green`，添加：

```
类型: CNAME
名称: www
目标: douya.green
代理状态: 已开启 (橙色云朵)
```

---

## 验证部署

### 检查清单

- [ ] 访问 https://douya.green 可以看到主页面
- [ ] 语言切换器工作正常
- [ ] "查看协议规范" 按钮可以打开 spec.html
- [ ] 协议文档页面中英文切换正常
- [ ] 所有动画效果正常显示
- [ ] HTTPS 证书正常（浏览器显示小锁）

---

## 域名配置建议

### 主页（douaya.green）
- 显示动画卡通风格的主页面
- 默认语言：英文

### 协议文档（douya.green/spec.html）
- 专业简洁的协议规范文档
- 支持中英文切换

---

## 部署后的 URL 结构

```
https://douya.green/              → 主页面（动画卡通风格）
https://douya.green/spec.html     → 协议规范文档（专业简洁风格）
https://www.douya.green/          → 同上（如果配置了 www）
```

---

## 更新网站内容

### 方式一（GitHub + 自动部署）
```bash
# 修改文件后
git add .
git commit -m "Update content"
git push
# Cloudflare Pages 会自动检测并重新部署
```

### 方式二（直接上传）
```bash
# 修改文件后重新上传
wrangler pages publish . --project-name=sacp-protocol
```

---

## 故障排除

### 问题 1: 域名无法访问
- 检查 DNS 记录是否正确
- 等待 DNS 传播（可能需要 24-48 小时，通常几分钟）
- 在 Cloudflare DNS 设置中确认域名状态

### 问题 2: HTTPS 证书未生效
- Cloudflare 会自动为你的域名申请证书
- 通常需要几分钟到几小时
- 可以在 Cloudflare SSL/TLS 设置中检查状态

### 问题 3: 页面样式异常
- 确认 index.html 和 spec.html 都已上传
- 检查浏览器控制台是否有错误
- 清除浏览器缓存后重试

---

## 优化建议

### 1. 启用 Cloudflare 优化（免费）
- Brotli 压缩
- HTTP/3
- Auto Minify (HTML, CSS, JS)
- Rocket Loader (自动优化 JavaScript 加载)

### 2. 配置缓存规则
- 为静态内容设置长期缓存
- HTML 文件设置较短的缓存时间

### 3. 添加分析（可选）
- Cloudflare Web Analytics
- Google Analytics
- 或其他分析工具

---

## 联系信息

作者: 山野小娃
Email: douyacenter@163.com

---

## 许可证

CC BY 4.0 - 可自由分享、演绎，但需保留署名
