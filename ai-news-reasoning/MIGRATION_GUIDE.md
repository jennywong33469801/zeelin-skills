# AI日报流水线 Skill + 模板 迁移指南

## 组合结构

```
ai-news-reasoning/
├── SKILL.md                      # 推理引擎（7条推理链）
├── ai-daily-template.toml        # 格式参数模板
├── references/
│   ├── source_reliability.md     # 信源可靠性名单
│   └── four_domains.md           # 四大领域关键词
├── scripts/
│   └── date_utils.py             # VOL编号推算脚本
└── assets/
    └── html_template.html        # HTML排版参考模板
```

---

## 迁移到新领域的步骤

### Step 1：新建领域目录

```
skills/
├── ai-news-reasoning/          # 推理引擎（不改）
├── new-domain-reasoning/        # 新领域推理（复制后改名）
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── assets/
└── new-domain-template.toml     # 新格式模板（新建）
```

### Step 2：改 SKILL.md

只需改 3 处：

1. **description**（触发词）：替换 "AI日报" → "XX日报"
2. **推理链 R4**：替换 `references/four_domains.md` → 新领域关键词文件
3. **推理链 R7**：替换 `ai-daily-template.toml` → 新模板路径

### Step 3：改 four_domains.md

替换四个领域的关键词表：
- AIGC → 新能源：锂电池、光伏、储能、碳中和...
- AIGC → 医疗：药物研发、手术机器人、医疗AI...
- AIGC → Crypto：DeFi、NFT、Layer2、链上数据...

### Step 4：改 ai-daily-template.toml

换皮不变骨：
- 颜色、品牌名
- 标签体系（如"大模型/产品" → "车型/电池技术"）
- 排版尺寸
- 封面图 prompt 风格

### Step 5：改 source_reliability.md

换行业对应的可信信源清单。

---

## 快速启动命令

```bash
# 查看今天 VOL 编号
python skills/ai-news-reasoning/scripts/date_utils.py info

# 验证某个 VOL 对应的日期
python skills/ai-news-reasoning/scripts/date_utils.py check_vol 111
```

---

## 复用清单

| 推理链 | 改动量 | 说明 |
|--------|--------|------|
| R1 信源分级 | 换清单 | 优先级结构不变 |
| R2 可靠性管理 | 换名单 | 降级规则不变 |
| R3 信噪比三档 | **不改** | 完全通用 |
| R4 领域过滤 | 换关键词 | 完全通用 |
| R5 VOL推算 | 换起始日期 | 脚本复用 |
| R6 封面图 | 换prompt | 映射表可复用 |
| R7 HTML排版 | 换模板 | 微信渲染规则通用 |
