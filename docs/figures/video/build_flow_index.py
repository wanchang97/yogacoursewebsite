#!/usr/bin/env python3
"""Generate docs/{zh,en,de}/sequences/vinyasa-full-flow.md from figures/video/catalog.csv
Notes: notes/<slug>.md (zh), notes/en/<slug>.md, notes/de/<slug>.md"""
import csv, os, re, html
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
CAT = os.path.join(D, 'figures', 'video', 'catalog.csv')
NOTES = os.path.join(D, 'figures', 'video', 'notes')   # notes/<slug>.md = 讲解 for that anchor

def inline(t):
    t = html.escape(t, quote=False)
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)

def md2html(txt):
    # tiny markdown: paragraphs, "- " bullet lists, **bold**
    out, ul = [], False
    for line in txt.strip().splitlines():
        line = line.rstrip()
        if line.startswith('- '):
            if not ul: out.append('<ul>'); ul = True
            out.append(f'<li>{inline(line[2:])}</li>'); continue
        if ul: out.append('</ul>'); ul = False
        if line: out.append(f'<p>{inline(line)}</p>')
    if ul: out.append('</ul>')
    return ''.join(out)

def load_note(slug, lang='zh'):
    p = os.path.join(NOTES, slug + '.md') if lang == 'zh' else os.path.join(NOTES, lang, slug + '.md')
    return md2html(open(p, encoding='utf-8').read()) if os.path.exists(p) else None

SPANS = [(1,5),(6,16),(17,29),(30,49),(50,57),(58,68),(69,82)]
L = {
 'zh': dict(
  sections=[('一 · 坐姿调息与热身','坐稳、呼吸，再用侧展、颈侧、扭转唤醒脊柱。'),
            ('二 · 四角板凳序列','建立手掌根基，猫牛、穿针、虎式的动态与平衡。'),
            ('三 · 山式与拜日式过渡','从山式出发，一次完整的 Vinyasa：手臂上举→前屈→平板→四柱→上犬→下犬。'),
            ('四 · 站立序列','战士、三角、金字塔、新月、龙式、神猴、鸽子——单侧完整走一遍。'),
            ('五 · 平衡挑战','幻椅起势，飞机、抱膝、站立抓脚、4 字平衡。'),
            ('六 · 坐姿拉伸','头碰膝、马里奇、半莲花、指南针，反桌与狂野收尾。'),
            ('七 · 大休息与倒立','仰卧束角、大休息；之后是轮式、犁式、肩倒立、头倒立的进出过程。')],
  title='完整流瑜伽串联 · 动作锚点库', sub='Vinyasa Full Flow · Pose Anchor Library',
  intro=lambda n,ns,nc: f"""这一页把一整堂流瑜伽课按<b>练习顺序</b>铺开：每个动作是一个"锚点"——来自我自己的练习录像（侧面机位），
<b>定帧</b>用于静态体式，<b>动图</b>用于过渡与动态练习。共 <b>{n}</b> 个锚点（{ns} 定帧 · {nc} 动图）。<br>
🔗 已写好体式卡的动作可点击进入；有讲解的动作点「▸ 讲解」展开；标 <span style="color:#b45309">讲解待补充</span> 的，讲解会逐步补进体式库。
时间码为「来源视频 分:秒」，s1 = 第一段（41 分）、s2 = 第二段（25 分）。""",
  still='定帧', clip='动图', card='体式卡 →', todo='讲解待补充', ex='讲解',
  foot='素材：<code>figures/video/</code>（定帧 .jpg，动图 <code>clips/*.mp4</code>）· 源数据：<code>figures/video/catalog.csv</code> · 讲解写在 <code>figures/video/notes/&lt;slug&gt;.md</code>（英文 <code>notes/en/</code>、德文 <code>notes/de/</code>）。改动时间码或讲解后运行 <code>build_flow_index.py</code> 即可重生成本页。'),
 'en': dict(
  sections=[('1 · Seated breathing & warm-up','Settle, breathe, then wake up the spine with side stretches, neck stretches and twists.'),
            ('2 · Tabletop sequence','Build the foundation of the hands; cat–cow, thread the needle and tiger in motion and balance.'),
            ('3 · Mountain pose & sun salutation','From mountain pose, one full vinyasa: arms up → fold → plank → chaturanga → up-dog → down dog.'),
            ('4 · Standing sequence','Warriors, triangle, pyramid, crescent, dragon, splits, pigeon — one full side.'),
            ('5 · Balance challenge','Starting from chair: airplane, knee hug, standing hand to toe, figure-four balance.'),
            ('6 · Seated stretches','Head-to-knee, Marichyasana, half lotus, compass, finishing with reverse tabletop and wild thing.'),
            ('7 · Relaxation & inversions','Reclined bound angle and savasana; then entering and leaving wheel, plow, shoulder stand and headstand.')],
  title='Full Vinyasa Flow · Pose Anchor Library', sub='完整流瑜伽串联 · 动作锚点库',
  intro=lambda n,ns,nc: f"""This page lays out a full vinyasa class in <b>practice order</b>. Each pose is an "anchor" taken from my own practice recording (side view):
<b>stills</b> for held poses, <b>clips</b> for transitions and dynamic movements. <b>{n}</b> anchors in total ({ns} stills · {nc} clips).<br>
🔗 Poses with a pose card link to it (currently in Chinese); open "▸ Guide" for cues on each pose.
Timecodes are "source video min:sec", s1 = part one (41 min), s2 = part two (25 min).""",
  still='still', clip='clip', card='Pose card (中文) →', todo='guide coming soon', ex='Guide',
  foot='Media: <code>figures/video/</code> (stills .jpg, clips <code>clips/*.mp4</code>) · Data: <code>figures/video/catalog.csv</code> · Guides: <code>figures/video/notes/en/&lt;slug&gt;.md</code>. Run <code>build_flow_index.py</code> after editing to regenerate this page.'),
 'de': dict(
  sections=[('1 · Sitzende Atemübung & Aufwärmen','Ankommen, atmen, dann die Wirbelsäule mit Seitdehnung, Nacken und Drehung wecken.'),
            ('2 · Vierfüßler-Sequenz','Das Fundament der Hände aufbauen; Katze–Kuh, Nadel einfädeln und Tiger – dynamisch und in Balance.'),
            ('3 · Berghaltung & Sonnengruß','Aus der Berghaltung ein ganzer Vinyasa: Arme hoch → Vorbeuge → Brett → Chaturanga → Up-Dog → Down-Dog.'),
            ('4 · Stehende Sequenz','Krieger, Dreieck, Pyramide, Halbmond, Drache, Spagat, Taube – eine ganze Seite.'),
            ('5 · Balance-Herausforderung','Aus dem Stuhl: Flugzeug, Knie umarmen, stehende Hand zum Zeh, Vierer-Balance.'),
            ('6 · Sitzende Dehnung','Kopf-zu-Knie, Marichyasana, halber Lotus, Kompass, zum Schluss umgekehrter Tisch und wilde Haltung.'),
            ('7 · Endentspannung & Umkehrhaltungen','Liegender gebundener Winkel und Savasana; danach Rad, Pflug, Schulterstand und Kopfstand – hinein und heraus.')],
  title='Vinyasa-Flow · Anker-Bibliothek', sub='完整流瑜伽串联 · Vinyasa Full Flow',
  intro=lambda n,ns,nc: f"""Diese Seite zeigt eine ganze Vinyasa-Stunde in <b>Übungsreihenfolge</b>. Jede Haltung ist ein „Anker“ aus meiner eigenen Übungsaufnahme (Seitenansicht):
<b>Standbilder</b> für gehaltene Haltungen, <b>Clips</b> für Übergänge und dynamische Bewegungen. Insgesamt <b>{n}</b> Anker ({ns} Standbilder · {nc} Clips).<br>
🔗 Haltungen mit Asana-Karte sind verlinkt (zurzeit auf Chinesisch); öffne „▸ Anleitung“ für die Hinweise zu jeder Haltung.
Zeitangaben: „Quellvideo Min:Sek“, s1 = Teil eins (41 Min), s2 = Teil zwei (25 Min).""",
  still='Standbild', clip='Clip', card='Asana-Karte (中文) →', todo='Anleitung folgt', ex='Anleitung',
  foot='Material: <code>figures/video/</code> (Standbilder .jpg, Clips <code>clips/*.mp4</code>) · Daten: <code>figures/video/catalog.csv</code> · Anleitungen: <code>figures/video/notes/de/&lt;slug&gt;.md</code>. Nach Änderungen <code>build_flow_index.py</code> ausführen, um diese Seite neu zu erzeugen.'),
}
# slugs that already have a pose card in zh/poses/
CARDS = {'mountain':'mountain','down-dog':'downward-dog','triangle':'triangle',
         'pyramid-dyn':'pyramid','extended-side-angle':'extended-side-angle',
         'revolved-triangle':'revolved-triangle'}

def tc(s): s=int(s); return f'{s//60}:{s%60:02d}'

rows = list(csv.DictReader(open(CAT, encoding='utf-8')))
n_still = sum(r['type']=='still' for r in rows); n_clip = len(rows)-n_still

css = """<style>
.flow-intro{background:#eef4f1;border-left:4px solid #5E8B7E;border-radius:8px;padding:.8rem 1rem;margin:1rem 0 1.5rem;font-size:.93rem}
.flow-grid{display:grid;align-items:start;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px;margin:.6rem 0 2rem}
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
.flow-card details.ex{margin-top:.45rem;font-size:.84rem;color:#3d4a45;line-height:1.6}
.flow-card details.ex summary{cursor:pointer;color:#3C6A5E;font-weight:600;font-size:.76rem;list-style:none}
.flow-card details.ex summary::-webkit-details-marker{display:none}
.flow-card details.ex summary::before{content:'▸ '}
.flow-card details.ex[open] summary::before{content:'▾ '}
.flow-card details.ex p{margin:.4rem 0}.flow-card details.ex ul{margin:.3rem 0;padding-left:1.1rem}
.flow-card details.ex li{margin:.15rem 0}
@media (max-width:480px){.flow-grid{grid-template-columns:repeat(2,1fr);gap:9px}}
</style>"""

def build(lang):
    c = L[lang]
    out = []
    out.append(f"# {c['title']}\n")
    out.append(f'<p class="pose-sanskrit">{c["sub"]}</p>\n')
    out.append('<div class="flow-intro">\n' + c['intro'](len(rows), n_still, n_clip) + '\n</div>\n')
    for (a, b), (title, note) in zip(SPANS, c['sections']):
        sec = [r for r in rows if a <= int(r['order']) <= b]
        if not sec: continue
        out.append(f'<div class="flow-sec">\n\n## {title}\n\n<p class="note">{note}</p>\n<div class="flow-grid">')
        for r in sec:
            o, slug, typ, vid = r['order'], r['slug'], r['type'], r['video']
            name = r.get(lang) or r['zh']
            t = tc(r['start']) + (f"–{tc(r['end'])}" if typ == 'clip' else '')
            if typ == 'still':
                media = f'<img src="figures/video/{slug}.jpg" alt="{html.escape(name)}" loading="lazy"><span class="tag">{c["still"]}</span>'
            else:
                media = (f'<video src="figures/video/clips/{slug}.mp4" autoplay muted loop playsinline preload="metadata"></video>'
                         f'<span class="tag clip">{c["clip"]}</span>')
            nh = load_note(slug, lang)
            if slug in CARDS:
                status = f'<a href="#/zh/poses/{CARDS[slug]}">{c["card"]}</a>'
            elif nh:
                status = ''
            else:
                status = f'<span class="todo">{c["todo"]}</span>'
            if nh:
                status += f'<details class="ex"><summary>{c["ex"]}</summary>{nh}</details>'
            out.append(f'<div class="flow-card"><div class="m">{media}</div>'
                       f'<div class="b"><div class="n"><small>{int(o):02d}</small>{html.escape(name)}</div>'
                       f'<div class="t">s{vid} {t}</div><div class="s">{status}</div></div></div>')
        out.append('</div>\n\n</div>\n')
    out.append(f'\n---\n\n<p style="font-size:.85rem;color:#8a938d">{c["foot"]}</p>\n')
    path = os.path.join(D, lang, 'sequences', 'vinyasa-full-flow.md')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(css + '\n\n' + '\n'.join(out))
    print('wrote', os.path.relpath(path, D), '|', len(rows), 'anchors')

for lang in L:
    build(lang)
