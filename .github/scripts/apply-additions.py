#!/usr/bin/env python3
"""One-shot helper: add 7 Michael Heckert templates to catalog.json. Idempotent by bot_id."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
# Wait: if script is at .github/scripts/, parents[0]=scripts, [1]=.github, [2]=repo root. Yes.

path = ROOT / "catalog.json"
data = json.loads(path.read_text())

AUTHOR = {
    "name": "Michael",
    "handle": "michaelheckert",
    "url": "https://x.com/michaelheckert",
}

def src_share(bot_id):
    return {"catalog": "x.ai share page", "url": f"https://x.ai/bot/{bot_id}"}

def src_post(url):
    return {"catalog": "author post", "url": url}

entries = [
    {
        "slug": "stick-cut",
        "name": "Stick Cut by Michael",
        "author": AUTHOR,
        "summary": "Turns a two-sided concept into a looping stick-figure explainer for X, Reels, or TikTok. You post it.",
        "summary_zh": "把正反两面的概念做成可循环的简笔画解说视频，用于 X、Reels 或 TikTok，由你自己发布。",
        "official_summary": "Turns a two-sided concept into a looping stick-figure explainer for X, Reels, or TikTok. You post it.",
        "import": "https://x.ai/bot/rET0A-uXf1XKqb_z5vjwl",
        "bot_id": "rET0A-uXf1XKqb_z5vjwl",
        "category": "content-publishing",
        "tags": ["video", "explainer", "content", "stick-figure"],
        "origin": "https://x.com/MichaelHeckert/status/2115100364940943710",
        "sources": [src_share("rET0A-uXf1XKqb_z5vjwl"), src_post("https://x.com/MichaelHeckert/status/2115100364940943710")],
        "first_seen": "2026-11-13",
        "checked": "2026-11-13",
        "link_status": 200,
        "license": "CC0-1.0",
    },
    {
        "slug": "covered",
        "name": "Covered by Michael",
        "author": AUTHOR,
        "summary": "Finds free repairs, replacements, and warranty claims you're already owed, and drafts the claim. You file it.",
        "summary_zh": "找出你已有物品可免费维修、更换或保修索赔的机会，并起草索赔内容，由你自己提交。",
        "official_summary": "Covered finds the free repairs, replacements, and warranty claims you're already owed on the stuff you own, and drafts the claim. You file it.",
        "import": "https://x.ai/bot/JE8skJITEDqsPpFOZUsBh",
        "bot_id": "JE8skJITEDqsPpFOZUsBh",
        "category": "personal-admin",
        "tags": ["warranty", "recall", "money", "claims"],
        "origin": "https://x.com/MichaelHeckert/status/2113712551670456582",
        "sources": [src_share("JE8skJITEDqsPpFOZUsBh"), src_post("https://x.com/MichaelHeckert/status/2113712551670456582")],
        "first_seen": "2026-11-13",
        "checked": "2026-11-13",
        "link_status": 200,
        "license": "CC0-1.0",
    },
    {
        "slug": "distill",
        "name": "Distill by Michael",
        "author": AUTHOR,
        "summary": "One source in, ten ranked ready-to-post drafts out, in your voice. Nothing posts without your OK.",
        "summary_zh": "一份来源进去，按你的语气输出十条排序好的待发草稿，未经你同意不会发布。",
        "official_summary": "One source in, ten ranked ready-to-post drafts out, in your voice. Nothing posts without your OK.",
        "import": "https://x.ai/bot/dPj7ysFWJ-nTtWPwiZlih",
        "bot_id": "dPj7ysFWJ-nTtWPwiZlih",
        "category": "content-publishing",
        "tags": ["content", "repurpose", "social", "drafts"],
        "origin": "https://x.com/MichaelHeckert/status/2113827903469461659",
        "sources": [src_share("dPj7ysFWJ-nTtWPwiZlih"), src_post("https://x.com/MichaelHeckert/status/2113827903469461659")],
        "first_seen": "2026-11-13",
        "checked": "2026-11-13",
        "link_status": 200,
        "license": "CC0-1.0",
    },
    {
        "slug": "undercut",
        "name": "Undercut by Michael",
        "author": AUTHOR,
        "summary": "Drop in a bill. See what new customers pay near you, plus the exact script to get your price down. You make the call.",
        "summary_zh": "丢进一张账单，看看附近新客户在付多少，并给出降价话术，由你自己打电话。",
        "official_summary": "Drop in a bill. See what new customers pay near you, plus the exact script to get your price down. You make the call.",
        "import": "https://x.ai/bot/mzY8PRsWQZCuKuTEFQteB",
        "bot_id": "mzY8PRsWQZCuKuTEFQteB",
        "category": "finance-ops",
        "tags": ["bills", "negotiation", "money"],
        "sources": [src_share("mzY8PRsWQZCuKuTEFQteB"), {"catalog": "@michaelheckert on X", "url": "https://x.com/michaelheckert"}],
        "first_seen": "2026-11-13",
        "checked": "2026-11-13",
        "link_status": 200,
        "license": "CC0-1.0",
    },
    {
        "slug": "cut-man",
        "name": "Cut Man by Michael",
        "author": AUTHOR,
        "summary": "Finds money leaks like unused subscriptions and surprise renewals, and keeps you on track to cut them. Nothing cancels without your OK.",
        "summary_zh": "找出未使用的订阅和意外续费等金钱漏洞，并帮你跟进削减，未经同意不会取消任何项目。",
        "official_summary": "Finds money leaks in your business, like unused subscriptions, surprise renewals, and wasted spend, and keeps you on track to cut them. For solo...",
        "import": "https://x.ai/bot/8q0BDryA7qBsMmrXGoypO",
        "bot_id": "8q0BDryA7qBsMmrXGoypO",
        "category": "finance-ops",
        "tags": ["subscriptions", "spend", "money"],
        "sources": [src_share("8q0BDryA7qBsMmrXGoypO"), {"catalog": "@michaelheckert on X", "url": "https://x.com/michaelheckert"}],
        "first_seen": "2026-11-13",
        "checked": "2026-11-13",
        "link_status": 200,
        "license": "CC0-1.0",
    },
    {
        "slug": "sponsor-scout",
        "name": "Sponsor Scout by Michael",
        "author": AUTHOR,
        "summary": "Finds brands already sponsoring people like you, finds the real way in, and drafts the pitch. You hit send.",
        "summary_zh": "找出已经在赞助类似创作者的品牌，找到真正的对接路径并起草提案，由你自己发送。",
        "official_summary": "Finds brands already sponsoring people like you, finds the real way in, and drafts the pitch. You hit send. Built for fighters, athletes, newsletter...",
        "import": "https://x.ai/bot/HK7rbeEuMNDD3_RbYyvx6",
        "bot_id": "HK7rbeEuMNDD3_RbYyvx6",
        "category": "customer-sales",
        "tags": ["sponsorship", "athletes", "outreach"],
        "sources": [src_share("HK7rbeEuMNDD3_RbYyvx6"), {"catalog": "@michaelheckert on X", "url": "https://x.com/michaelheckert"}],
        "first_seen": "2026-11-13",
        "checked": "2026-11-13",
        "link_status": 200,
        "license": "CC0-1.0",
    },
    {
        "slug": "scorecard",
        "name": "Scorecard by Michael",
        "author": AUTHOR,
        "summary": "Scores your last week on X like a fight card against your 4-week baseline, plus 3 data-backed fixes.",
        "summary_zh": "每周一像拳赛记分卡一样，对照你过去四周的基线为上周的 X 表现打分，并给出 3 条有数据支撑的改进建议。",
        "official_summary": "Every Monday, judges your last week on X like a fight: a fight-card image scored with X's open-source ranking weights against your own 4-week baseline,...",
        "import": "https://x.ai/bot/tEsWijg6kaDbi-3aY6who",
        "bot_id": "tEsWijg6kaDbi-3aY6who",
        "category": "content-publishing",
        "tags": ["x", "analytics", "growth", "weekly"],
        "sources": [src_share("tEsWijg6kaDbi-3aY6who"), {"catalog": "@michaelheckert on X", "url": "https://x.com/michaelheckert"}],
        "first_seen": "2026-11-13",
        "checked": "2026-11-13",
        "link_status": 200,
        "license": "CC0-1.0",
    },
]

existing_ids = {e.get("bot_id") for e in data["entries"]}
added = []
for e in entries:
    if e["bot_id"] in existing_ids:
        print(f"skip existing {e['slug']}")
        continue
    data["entries"].append(e)
    existing_ids.add(e["bot_id"])
    added.append(e["slug"])

from collections import Counter
c = Counter(e["category"] for e in data["entries"])
data["counts"]["live"] = len(data["entries"])
data["counts"]["by_category"] = {k: c[k] for k in data["counts"]["by_category"]}
path.write_text(json.dumps(data, ensure_ascii=False, indent=2))
print("added:", added, "live:", data["counts"]["live"])
