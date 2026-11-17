# Integra la agenda en vivo, la cinta superior y las animaciones en plantilla.html
import os
H = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(H, "plantilla.html")
s = open(p, encoding="utf-8").read()
assert "id=\"agenda\"" not in s, "ya integrada"

# ---------- CSS ----------
a = s.index(".talks{display:grid"); b = s.index(".share{")
css = r""".marquee{position:relative;z-index:2;background:rgba(0,0,0,.35);border-bottom:2px solid var(--gold);overflow:hidden;white-space:nowrap}
.marquee div{display:inline-flex;gap:34px;padding:9px 0;animation:mq 30s linear infinite;font-weight:800;font-size:12px;letter-spacing:.22em;color:var(--gold-light)}
.marquee span.r{color:#ff6a60}
@keyframes mq{to{transform:translateX(-50%)}}
.now{max-width:min(920px,100%);margin:0 auto 14px;display:none;align-items:center;gap:14px;background:linear-gradient(90deg,rgba(224,53,43,.95),rgba(176,32,24,.95));
  border:2px solid #fff;border-radius:18px;padding:10px 18px;box-shadow:0 12px 30px rgba(224,53,43,.35);animation:slide .6s cubic-bezier(.2,1.4,.4,1)}
.now.on{display:flex}
.now img{width:46px;height:46px;border-radius:50%;object-fit:cover;border:2px solid var(--gold-light);flex:none}
.now small{display:block;font-weight:900;font-size:11px;letter-spacing:.2em;opacity:.9}
.now b{font-family:var(--serif);font-size:clamp(17px,2.4vw,22px);font-weight:900;line-height:1.15}
@keyframes slide{from{opacity:0;transform:translateY(-14px)}}

.agenda{--tw:168px;position:relative;max-width:900px;margin:0 auto}
.agenda .rail{position:absolute;left:calc(var(--tw) + 21px);top:14px;bottom:14px;width:4px;border-radius:4px;background:rgba(239,208,142,.22)}
.agenda .fill{position:absolute;left:0;top:0;width:100%;height:0;border-radius:4px;background:linear-gradient(180deg,#FFF1C9,#C9973F);box-shadow:0 0 14px rgba(239,208,142,.8);transition:height 1.2s ease}
.ag{position:relative;display:grid;grid-template-columns:var(--tw) 1fr;column-gap:52px;align-items:center;margin:12px 0;transition:opacity .5s}
.ag .t{text-align:right;font-weight:700;font-size:14px;color:var(--gold-light);white-space:nowrap}
.ag .dot2{position:absolute;left:calc(var(--tw) + 23px);top:50%;width:16px;height:16px;margin:-8px 0 0 -8px;border-radius:50%;background:var(--gold);border:3px solid var(--navy-deep);transition:.4s}
.ag.big .dot2{width:28px;height:28px;margin:-14px 0 0 -14px;background:var(--gold-grad);box-shadow:0 0 0 4px rgba(201,151,63,.25)}
.ag .lbl{display:flex;align-items:center;flex-wrap:wrap;gap:10px;font-weight:600;font-size:16px;opacity:.8}
.ag .lbl svg{width:22px;height:22px;flex:none}
.ag .pill{justify-self:end;background:var(--gold-grad);color:var(--navy);border:3px solid var(--gold-dark);border-radius:16px;padding:7px 14px;text-align:center;box-shadow:0 8px 18px rgba(0,0,0,.3)}
.ag .pill b{display:block;font-weight:900;font-size:26px;line-height:1}
.ag .pill span{font-weight:800;font-size:12px;letter-spacing:.14em}
.misa{display:inline-flex;align-items:center;gap:12px;background:var(--cream);color:var(--navy);border:3px solid var(--gold);border-radius:999px;padding:7px 26px 7px 8px;width:fit-content}
.misa i{width:40px;height:40px;border-radius:50%;background:var(--gold-grad);display:grid;place-items:center;font-style:normal;font-weight:900;font-size:22px}
.misa b{font-family:var(--serif);font-weight:900;font-size:28px}
.card{position:relative;display:flex;gap:18px;align-items:center;background:var(--cream);color:var(--navy);border-radius:24px;padding:14px 20px 14px 14px;border:2px solid var(--gold-light);
  overflow:hidden;box-shadow:var(--shadow);transition:transform .35s cubic-bezier(.2,1.4,.4,1),box-shadow .35s,border-color .35s}
.card:hover{transform:translateY(-4px) scale(1.015);border-color:var(--gold)}
.card:before{content:attr(data-n);position:absolute;right:12px;top:-14px;font-family:var(--serif);font-weight:900;font-size:110px;color:var(--gold);opacity:.13;line-height:1}
.card .ph{position:relative;flex:none;width:104px;height:104px}
.card .ph img{width:100%;height:100%;border-radius:50%;object-fit:cover;border:4px solid var(--gold)}
.card .ph:after{content:"";position:absolute;inset:-7px;border-radius:50%;border:2px dashed var(--gold);animation:spin 16s linear infinite}
.card small{font-weight:800;font-size:11px;letter-spacing:.22em;color:var(--gold-dark)}
.card h3{font-family:var(--serif);font-weight:900;font-size:25px;line-height:1.1;margin:3px 0 4px}
.card p{font-family:var(--serif);font-style:italic;font-size:15px;color:var(--gold-dark);line-height:1.3}
.card .who{display:inline-block;margin-top:8px;background:var(--navy);color:var(--gold-light);font-weight:800;font-size:13px;padding:5px 14px;border-radius:999px}
.badge{position:absolute;top:10px;right:12px;z-index:2;display:none;align-items:center;gap:7px;border-radius:999px;padding:5px 12px;font-weight:900;font-size:11px;letter-spacing:.16em}
.ag.past{opacity:.42}
.ag.past .dot2{background:var(--gold);border-color:var(--gold)}
.ag.past .dot2:after{content:"✓";position:absolute;inset:0;display:grid;place-items:center;font-size:12px;font-weight:900;color:var(--navy)}
.ag.now .dot2{background:var(--red);border-color:#fff;width:30px;height:30px;margin:-15px 0 0 -15px;animation:pingr 1.3s infinite}
@keyframes pingr{0%{box-shadow:0 0 0 0 rgba(224,53,43,.7)}80%,100%{box-shadow:0 0 0 18px rgba(224,53,43,0)}}
.ag.now .card{border:3px solid #fff;box-shadow:0 0 0 6px rgba(224,53,43,.55),0 0 40px rgba(224,53,43,.45)}
.ag.now .badge.n{display:inline-flex;background:var(--red);color:#fff}
.ag.now .badge.n .dot{width:9px;height:9px}
.ag.next .badge.x{display:inline-flex;background:var(--navy);color:var(--gold-light);border:2px solid var(--gold)}
.ag.now .lbl{opacity:1;color:#fff;font-weight:800}
.ag .inline{display:none;font-weight:900;font-size:11px;letter-spacing:.16em;border-radius:999px;padding:4px 10px;margin-left:6px}
.ag.now .inline.n{display:inline-block;background:var(--red);color:#fff}
.ag.next .inline.x{display:inline-block;background:var(--navy);color:var(--gold-light);border:1px solid var(--gold)}
.reveal{opacity:0;transform:translateY(40px) scale(.97);transition:opacity .8s ease,transform .8s cubic-bezier(.2,1,.3,1)}
.reveal.in{opacity:1;transform:none}
.ag.past.reveal.in{opacity:.42}
@media (max-width:640px){
  .agenda{--tw:74px}.ag{column-gap:34px}.ag .t{font-size:11px;white-space:normal}.ag .pill{padding:5px 8px;border-radius:12px}.ag .pill b{font-size:18px}.ag .pill span{font-size:9px}
  .ag .lbl{font-size:14px}.card{padding:12px 12px 12px 10px;gap:12px}.card .ph{width:68px;height:68px}.card h3{font-size:19px}.card p{font-size:13px}.card:before{font-size:80px}
  .misa b{font-size:22px}.misa i{width:32px;height:32px;font-size:18px}.badge{top:6px;right:8px;font-size:9px;padding:4px 9px}
}
"""
s = s[:a] + css + s[b:]

# ---------- HTML ----------
a = s.index("  <!-- PROGRAMA -->"); b = s.index("  <!-- COMPARTIR -->")
html = """  <!-- AGENDA -->
  <section>
    <span class="kicker reveal">AGENDA · LUNES 16 DE NOVIEMBRE</span>
    <h2 class="reveal">Así será el <em class="gold">gran día</em></h2>
    <div class="agenda" id="agenda"><div class="rail"><div class="fill" id="fill"></div></div></div>
  </section>

"""
s = s[:a] + html + s[b:]
s = s.replace('<section>\n    <div class="share">', '<section>\n    <div class="share reveal">')
s = s.replace('<canvas id="sparks"></canvas>', '<canvas id="sparks"></canvas>\n<div class="marquee" aria-hidden="true"><div id="mq"></div></div>', 1)
s = s.replace('  <!-- REPRODUCTOR -->', '  <div class="now" id="nowbar"></div>\n  <!-- REPRODUCTOR -->')

# ---------- JS ----------
js = open(os.path.join(H, "agenda.js"), encoding="utf-8").read()
mark = "// ---- estado: cuenta regresiva hasta el inicio / EN VIVO ----"
s = s.replace(mark, js + "\n" + mark)
s = s.replace("function status() {\n  const now = Date.now();", "function status() {\n  const now = nowMs();")
assert "nowMs()" in s
open(p, "w", encoding="utf-8").write(s)
print("ok")
