#!/usr/bin/env python3
"""Generate docs/zh/sequences/vinyasa-full-flow.md from figures/video/catalog.csv"""
import csv, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
CAT = os.path.join(D, 'figures', 'video', 'catalog.csv')
OUT = os.path.join(D, 'zh', 'sequences', 'vinyasa-full-flow.md')

SECTIONS = [  # (first_order, last_order, title, note)
 (1, 5,  '一 · 坐姿调息与热身',   '坐稳、呼吸，再用侧展、颈侧、扭转唤醒脊柱。'),
 (6, 16, '二 · 四角板凳序列',     '建立手掌根基，猫牛、穿针、虎式的动态与平衡。'),
 (17,29, '三 · 山式与拜日式过渡', '从山式出发，一次完整的 Vinyasa：手臂上举→前屈→平板→四柱→上犬→下犬。'),
 (30,49, '四 · 站立序列',         '战士、三角、金字塔、新月、龙式、神猴、鸽子——单侧完整走一遍。'),
 (50,57, '五 · 平衡挑战',         '幻椅起势，飞机、抱膝、站立抓脚、4 字平衡。'),
 (58,68, '六 · 坐姿拉伸',         '头碰膝、马里奇、半莲花、指南针，反桌与狂野收尾。'),
 (69,82, '七 · 大休息与倒立',     '仰卧束角、大休息；之后是轮式、犁式、肩倒立、头倒立的进出过程。'),
]
# slugs that already have a pose card in zh/poses/
CARDS = {'mountain':'mountain','down-dog':'downward-dog','triangle':'triangle',
         'pyramid-dyn':'pyramid','extended-side-angle':'extended-side-angle',
         'revolved-triangle':'revolved-triangle'}

def tc(s): s=int(s); return f'{s//60}:{s%60:02d}'

rows = list(csv.DictReader(open(CAT, encoding='utf-8')))
n_still = sum(r['type']=='still' for r in rows); n_clip = len(rows)-n_still

css = """<style>
.flow-intro{background:#eef4f1;border-left:4px solid #5E8B7E;border-radius:8px;padding:.8rem 1rem;margin:1rem 0 1.5rem;font-size:.93rem}
.flow-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px;margin:.6rem 0 2rem}
.flow-card{background:#fff;border:1px solid #e3e9e6;border-radius:12px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.05)}
.flow-card .m{aspect-ratio:16/9;background:#1f2a27;position:relative}
.flow-card .m img,.flow-card .m video{width:100%;height:100%;object-fit:cover;display:block}
.flow-card .m .tag{position:absolute;top:6px;left:6px;font-size:.68rem;padding:1px 7px;border-radius:99px;background:rgba(0,0,0,.55);color:#fff;letter-spacing:.04em}
.flow-card .m .tag.clip{background:#c2410c}
.flow-card .b{padding:.55rem .7rem .65rem}
.flow-card .n{font-weight:700;font-size:.95rem;color:#243b35;line-height:1.3}
.flow-card .n small{color:#8a938d;font-weight:400;margin-right:.35rem}
.flow-card .t{font-size:.76rem;color:#8a938d;margin-top:.2rem;font-variant-numeric:tabular-nums}
.flow-card .s{margin-top:.4rem;font-size:.74rem}
.flow-card .s a{color:#3C6A5E;font-weight:600;text-decoration:none;border-bottom:1px dashed #5E8B7E}
.flow-card .s .todo{color:#b45309;background:#fff7e6;border-radius:6px;padding:1px 6px}
.flow-sec{margin-top:2.2rem}.flow-sec h2{border-bottom:2px solid #5E8B7E;padding-bottom:.3rem}
.flow-sec p.note{color:#5b6b66;font-size:.9rem;margin:.3rem 0 .6rem}
@media (max-width:480px){.flow-grid{grid-template-columns:repeat(2,1fr);gap:9px}}
</style>"""

out = []
out.append('# 完整流瑜伽串联 · 动作锚点库\n')
out.append('<p class="pose-sanskrit">Vinyasa Full Flow · Pose Anchor Library</p>\n')
out.append(f"""<div class="flow-intro">
这一页把一整堂流瑜伽课按<b>练习顺序</b>铺开：每个动作是一个"锚点"——来自我自己的练习录像（侧面机位），
<b>定帧</b>用于静态体式，<b>动图</b>用于过渡与动态练习。共 <b>{len(rows)}</b> 个锚点（{n_still} 定帧 · {n_clip} 动图）。<br>
🔗 已写好体式卡的动作可点击进入；标 <span style="color:#b45309">讲解待补充</span> 的，讲解会逐步补进体式库。
时间码为「来源视频 分:秒」，s1 = 第一段（41 分）、s2 = 第二段（25 分）。
</div>
""")

for a,b,title,note in SECTIONS:
    sec = [r for r in rows if a <= int(r['order']) <= b]
    if not sec: continue
    out.append(f'<div class="flow-sec">\n\n## {title}\n\n<p class="note">{note}</p>\n<div class="flow-grid">')
    for r in sec:
        o, slug, zh, typ, vid = r['order'], r['slug'], r['zh'], r['type'], r['video']
        t = tc(r['start']) + (f"–{tc(r['end'])}" if typ=='clip' else '')
        if typ == 'still':
            media = f'<img src="figures/video/{slug}.jpg" alt="{zh}" loading="lazy">' \
                    f'<span class="tag">定帧</span>'
        else:
            media = (f'<video src="figures/video/clips/{slug}.mp4" autoplay muted loop playsinline preload="metadata"></video>'
                     f'<span class="tag clip">动图</span>')
        if slug in CARDS:
            status = f'<a href="#/zh/poses/{CARDS[slug]}">体式卡 →</a>'
        else:
            status = '<span class="todo">讲解待补充</span>'
        out.append(f'<div class="flow-card"><div class="m">{media}</div>'
                   f'<div class="b"><div class="n"><small>{int(o):02d}</small>{zh}</div>'
                   f'<div class="t">s{vid} {t}</div><div class="s">{status}</div></div></div>')
    out.append('</div>\n\n</div>\n')

out.append('\n---\n\n<p style="font-size:.85rem;color:#8a938d">素材：<code>figures/video/</code>（定帧 .jpg，动图 <code>clips/*.mp4</code>）· 源数据：<code>figures/video/catalog.csv</code> · 改动时间码后运行 <code>build_flow_index.py</code> 即可重生成本页。</p>\n')

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(css + '\n\n' + '\n'.join(out))
print('wrote', os.path.relpath(OUT, D), '|', len(rows), 'anchors')
