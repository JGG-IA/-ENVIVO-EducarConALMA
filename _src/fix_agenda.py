# Corrige: choque de la clase .now y horas en celular
import os, re
H = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(H, "plantilla.html")
s = open(p, encoding="utf-8").read()

# 1) la barra "ahora en vivo" pasa a llamarse .nowbar
s = s.replace(".now{max-width:min(920px,100%)", ".nowbar{max-width:min(920px,100%)")
s = s.replace(".now.on{display:flex}", ".nowbar.on{display:flex}")
s = s.replace(".now img{", ".nowbar img{").replace(".now small{", ".nowbar small{").replace(".now b{", ".nowbar b{")
s = s.replace('<div class="now" id="nowbar"></div>', '<div class="nowbar" id="nowbar"></div>')

# 2) horas en dos renglones (hora / a. m.)
s = s.replace(".ag .t{text-align:right;font-weight:700;font-size:14px;color:var(--gold-light);white-space:nowrap}",
              ".ag .t{text-align:right;font-weight:800;font-size:17px;line-height:1.1;color:var(--gold-light);white-space:nowrap}"
              ".ag .t small{display:block;font-size:11px;font-weight:700;letter-spacing:.12em;opacity:.85}")
for hm, ap in [("7:00 – 8:00", "a. m."), ("8:00", "a. m."), ("9:00", "a. m."), ("12:30", "p. m."), ("2:30", "p. m."), ("4:00", "p. m.")]:
    s = s.replace(f't: "{hm} {ap}"', f't: "{hm}<small>{ap.upper()}</small>"')
s = s.replace('<div class="t" style="font-weight:900;font-size:16px;color:#fff">', '<div class="t" style="color:#fff">')

# 3) celular más holgado
old = s[s.index("@media (max-width:640px){\n  .agenda{--tw:74px}"):]
old = old[:old.index("\n}\n") + 3]
new = """@media (max-width:640px){
  .agenda{--tw:58px}.ag{column-gap:26px}.ag .t{font-size:13px}.ag .t small{font-size:9px}
  .ag .pill{padding:5px 6px;border-radius:12px}.ag .pill b{font-size:16px}.ag .pill span{font-size:8px;letter-spacing:.08em}
  .ag .lbl{font-size:14px}.card{padding:12px 10px 12px 10px;gap:10px}.card .ph{width:58px;height:58px}.card .ph img{border-width:3px}.card .ph:after{display:none}
  .card h3{font-size:18px}.card p{font-size:12.5px}.card .who{font-size:11px;padding:4px 10px}.card:before{font-size:70px}.card small{font-size:9px;letter-spacing:.16em}
  .misa{padding:5px 16px 5px 5px;gap:8px}.misa b{font-size:20px}.misa i{width:30px;height:30px;font-size:16px}
  .badge{position:static;margin-bottom:6px;font-size:9px;padding:3px 9px}.card>div:last-child{min-width:0}
  .ag.big .dot2{width:22px;height:22px;margin:-11px 0 0 -11px}.ag.now .dot2{width:24px;height:24px;margin:-12px 0 0 -12px}
}
"""
s = s.replace(old, new)
# en celular, las insignias van arriba del texto dentro de la tarjeta
s = s.replace('<article class="card" data-n="0${it.n}"><span class="badge n"><span class="dot"></span>EN VIVO AHORA</span><span class="badge x">A CONTINUACIÓN</span>\n        <div class="ph"><img src="${it.img}" alt=""></div>\n        <div><small>',
              '<article class="card" data-n="0${it.n}">\n        <div class="ph"><img src="${it.img}" alt=""></div>\n        <div><span class="badge n"><span class="dot"></span>EN VIVO AHORA</span><span class="badge x">A CONTINUACIÓN</span><small>')
s = s.replace(".badge{position:absolute;top:10px;right:12px;z-index:2;display:none;", ".badge{position:static;margin:0 0 6px;z-index:2;display:none;width:fit-content;")
s = s.replace(".ag.now .badge.n{display:inline-flex;", ".ag.now .badge.n{display:flex;").replace(".ag.next .badge.x{display:inline-flex;", ".ag.next .badge.x{display:flex;")
assert "nowbar{max-width" in s and "<small>A. M.</small>" in s and 'class="badge n"' in s
open(p, "w", encoding="utf-8").write(s)
print("ok")
