# ZeeLin Skills

AI 内容创作相关 Skill 合集，用于 ZeeLin AI 微信公众号运营与 New Age 短视频项目。

## 目录

### ai-news-reasoning
**AI 日报推理引擎** — 垂直领域日报/周报内容生成的底层推理库。

包含：
- R1 信源分级采集（五大优先级）
- R2 可靠性管理（信源黑/白名单）
- R3 信噪比三档过滤（信号/背景/噪音）
- R4 领域关键词过滤（四大领域）
- R5 VOL 编号推算
- R6 封面图提示词生成
- R7 HTML 排版渲染

可迁移到新能源、医疗、crypto 等其他垂直领域。

### zeelin-ai-headline-brief
**AI 头部简讯编排层** — 微信公众号「ZeeLin AI 头部简讯」的 Skill。

- 接收用户请求，判断任务模式（日报/周报/专题）
- 格式化输出（公众号/HTML/纯文本）
- 自动调用 ai-news-reasoning 推理引擎
- 支持每日快讯 + 每周深度总结两种模式

## 编排架构

```
用户请求
    ↓
zeelin-ai-headline-brief（编排层）
    ↓ 自动调用
ai-news-reasoning（推理引擎层）
    ↓
VOL 编号 + 封面图 + HTML 渲染
    ↓
公众号发布
```

## 使用前提

- WorkBuddy Claw 环境（AppID: wx6f0f119975e5cbbe）
- 将本仓库克隆到 `~/.workbuddy/skills/`

## 维护者

huabo / 华博
