# 信源可靠性管理

## 降级规则

当某个网站被发现发布**二手加工内容**（未经核实直接转载/编造信息，将传闻写成事实），该网站的可靠性等级降级：

1. 不直接采纳该网站的报道作为事实来源
2. 不引用该网站作为信息的 primary source
3. 用英文一手源或其他可靠中文源替代

---

## 🔴 不可信（禁止直接采纳）

| 网站 | 降级原因 | 降级日期 |
|------|---------|---------|
| 腾讯新闻 (news.qq.com) | 将匿名爆料写成"OpenAI官方确认"，GPT-6传闻层层加码 | 2026-04-16 |
| CSDN (blog.csdn.net) | 转载匿名爆料无交叉验证，将"据传"升级为"正式发布" | 2026-04-16 |
| 知乎专栏 (zhuanlan.zhihu.com) | 转载科技博主匿名爆料，未标注"传闻/未确认" | 2026-04-16 |
| 新浪财经/科技 (sina.cn / k.sina.cn) | 自相矛盾报道（GPT-6代号写成"海伦"vs其他源"Spud"），编造内容 | 2026-04-16 |
| 搜狐科技 (sohu.com) | 转载二手信息未核实 | 2026-04-16 |

---

## 🟡 有限信任（需交叉验证）

| 网站 | 说明 |
|------|------|
| 36氪 (36kr.com) | 行业分析可靠，但产品发布类消息需追溯一手源 |
| 钛媒体 (tmtpost.com) | 同上 |

---

## 🟢 可信（可直接采纳）

### 英文一手源（优先级最高）

- TechCrunch AI (techcrunch.com/category/artificial-intelligence/)
- VentureBeat AI (venturebeat.com/ai/)
- MIT Technology Review (technologyreview.com/topic/artificial-intelligence/)
- The Rundown AI (therundown.ai/)
- Futurepedia (futurepedia.io/)
- Product Hunt AI (producthunt.com/topics/artificial-intelligence)
- Hugging Face Blog/Models (huggingface.co/)
- arXiv cs.AI (arxiv.org/list/cs.AI/recent)
- GitHub Trending (github.com/trending)
- Papers With Code (huggingface.co/papers/trending)
- OpenAI Blog (openai.com/blog)
- Google AI Blog (blog.google/technology/ai/)
- Anthropic Blog (anthropic.com/blog)
- Meta AI Blog (ai.meta.com/blog)
- Apple Newsroom (apple.com/newsroom)

### 中文可信源

- 财联社 AI 频道 (cls.cn) — 实时快讯，通常有原始出处
- 雪球科技板块 (xueqiu.com) — 用户讨论为主，观点类可参考
- 码农财经 (manong.info) — 技术向翻译，标注原文链接

---

## 使用规则

1. **产品发布/重大公告类消息**：必须追溯至公司官方博客或高管社交媒体确认，二手媒体报道一律标注"[传闻]"
2. **降级名单中的网站**：仅可用于发现线索，但不能作为信息来源标注，必须用一手源替代
3. **中英文来源比例**：每次至少包含 3-4 条英文源内容
4. **信源标注**：每条新闻的来源必须是实际信息的原始出处，不是转载媒体
