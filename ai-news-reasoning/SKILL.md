---
name: AI Daily News Reasoning
description: |
  AI领域日报/周报内容生成推理引擎。当用户需要生成任何垂直领域日报简报时触发。
  包含：信源分级采集、信噪比三档过滤、四大领域关联判断、结构化内容输出、封面图关键词提取、HTML排版渲染全链路推理。
  触发词：生成日报、制作日报、日报流水线、新闻简报、内容采集过滤、周报生成、AI简报、垂直领域日报
  适用场景：(1)新建某领域日报流水线 (2)复用信源过滤逻辑到其他行业 (3)将现有日报扩展到新能源/医疗/crypto等新领域
---

# AI Daily News Reasoning — 推理引擎

## 定位

推理引擎 = 骨架（会盘算），模板 = 皮囊（会打扮）。

两者组合生成完整日报流水线：
```
信源采集 → 过滤判断 → 结构化生成 → 渲染排版 → 发布输出
   ↑                    ↑              ↑
  Skill               Skill         Template
  (推理)              (推理)        (格式)
```

## 核心推理链（7条，可独立使用）

### 推理链 R1 — 信源分级优先级

```
优先级0：国际AI媒体（当日事件首选）
  TechCrunch / VentureBeat / The Verge / Wired / Reuters / MIT Tech Review

优先级1：学术前沿（arXiv cs.AI/cs.LG/cs.CL/cs.CV）
优先级2：开源工具（GitHub Trending，本周star增速>500）
优先级3：社区讨论（Hacker News，points>100且comments>30）
优先级4：模型生态（Hugging Face，本周下载量增速top20）
```

**跨领域复用**：换行业只改信源清单，优先级结构完全不变。

---

### 推理链 R2 — 可靠性动态管理

读取 `references/source_reliability.md` 获取最新降级名单。

```
🟢 可信（直接采纳）→ 英文一手源 / 财联社 / 雪球技术向
🟡 有限信任（需交叉验证）→ 36氪 / 钛媒体（需追溯一手源）
🔴 不可信（禁止直接采纳）→ 腾讯新闻 / CSDN / 新浪财经 / 知乎专栏 / 搜狐科技
```

**降级触发条件**：被发现发布二手加工内容（未经核实将传闻写成事实）。降级后该媒体不能作为 primary source 标注，必须用一手源替代。

---

### 推理链 R3 — 信噪比三档判断

对每条采集到的信息，执行三档评估：

| 等级 | 标准 | 处理 |
|------|------|------|
| 🔴 噪音 | 标题党、旧闻重包装、无实质内容、"天塌了/史诗级/炸裂"类空话 | 直接过滤，不出现在简报 |
| 🟡 背景 | 有一定信息量但非突破性、行业常规更新 | 仅在"背景扫描"一句话提及 |
| 🟢 信号 | 真正的新工具/新方法/新数据、对目标读者有直接价值 | 进入核心简报，附详细摘要 |

**噪音识别黑名单**：
```
"will change everything", "mind-blowing", "game-changer",
"天塌了", "颠覆性", "史诗级", "重磅", "炸裂", "王炸",
"刚刚", "你还不知道？", "看完我沉默了", "XX已死"
```
**不机械过滤**——如果内容本身确实有干货，仍然保留。

---

### 推理链 R4 — 领域关联过滤

读取 `references/four_domains.md` 获取当前领域的关键词和关注重点。

每条新闻判断是否落在指定领域内：
- **AIGC/生成式AI**：文生视频、图片生成、开源模型发布
- **虚拟数字人**：数字主播、数字分身、表情/动作合成
- **AI短视频/短剧**：制作工具更新、工作流优化、产业数据
- **智能传播/舆情**：学术论文、治理政策、平台算法变化

---

### 推理链 R5 — VOL编号+星期自动推算

```
今日日期 → 计算VOL编号（第1期=起始日期）
        → 计算中文星期（WEEKDAY_CN）
        → 格式化日期字符串
```

起始日期由模板配置指定，运行 `scripts/date_utils.py` 自动推算。

---

### 推理链 R6 — 封面图关键词提取+视觉映射

```
头条标题 → 遍历 KEYWORD_VISUAL_MAP 找最长匹配
        → 提取英文单词（3+字母，过滤停用词）
        → 构造 prompt（科技感+目标配色）
        → 调用图生API生成封面图
        → Fallback：CSS方案
```

视觉关键词映射表（可从模板配置读取）：
```
关键词 → 视觉标签
video generation → cinematic, digital art
AI model launch → futuristic, tech blueprint
investment/deal → corporate, financial
robotics → metallic, precision engineering
```

---

### 推理链 R7 — HTML排版渲染

读取 `ai-daily-template.toml` 获取格式参数（颜色/字号/布局/标签体系）。

微信渲染规则（必须遵守）：
- 所有样式用 `style=""` 内联，不使用 `<style>` 块
- 不使用 `class` 属性，微信渲染器会剥离
- 字体：中文用系统默认字体，英文用 Inter/Playfair Display
- 图片：封面图 2:1 比例，宽度 900px

---

## 完整工作流程

```
Step 1 确认任务
  └─ 确认领域/主题、输出模式（日报/周报）、发布平台

Step 2 信源采集（并行）
  ├─ R1: 优先级0 国际媒体（必选）
  ├─ R1: 优先级1 arXiv（周报必选，日报可选）
  ├─ R1: 优先级2 GitHub Trending
  └─ R1: 优先级3 HN / HF

Step 3 过滤与判断（串行）
  ├─ R2: 剔除不可信信源
  ├─ R3: 信噪比三档分级
  └─ R4: 领域关联过滤

Step 4 结构化生成
  ├─ R5: VOL编号 + 星期推算
  └─ 按模板输出 Markdown

Step 5 渲染发布
  ├─ R6: 生成封面图
  ├─ R7: HTML排版（读取模板配置）
  └─ 导出PNG → 发布到目标平台
```

## 跨领域迁移指南

将本推理引擎迁移到新领域（如新能源/医疗/crypto）：

1. **替换信源清单**（references/ 目录新建对应文件）
2. **替换领域定义**（修改 four_domains.md）
3. **替换格式模板**（替换 ai-daily-template.toml）
4. **保留**：R1/R2/R3/R5/R6/R7 全部不变

## 参考文件

- `references/source_reliability.md` — 信源可靠性名单（持续更新）
- `references/four_domains.md` — 当前四大领域关键词定义
- `scripts/date_utils.py` — VOL编号推算脚本
- `ai-daily-template.toml` — 格式参数模板（与本Skill同目录）
