# Agrega a la página principal el acceso a "Ver grabaciones"
import os
H = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(H, "plantilla.html")
s = open(p, encoding="utf-8").read()
assert "grabaciones.html" not in s, "ya agregado"

css = """.rec{position:relative;display:flex;align-items:center;justify-content:center;gap:14px;max-width:min(920px,100%);margin:0 auto 16px;padding:16px 22px;border-radius:22px;
  background:var(--gold-grad);color:var(--navy);border:3px solid #FFF1C9;box-shadow:0 14px 34px rgba(0,0,0,.35),0 0 0 0 rgba(239,208,142,.6);overflow:hidden;isolation:isolate;
  animation:recring 2.2s infinite;transition:transform .25s}
.rec:hover{transform:translateY(-3px) scale(1.01)}
.rec:after{content:"";position:absolute;inset:0;background:linear-gradient(110deg,transparent 30%,rgba(255,255,255,.6) 45%,transparent 60%);transform:translateX(-120%);animation:recsweep 3s ease-in-out infinite;z-index:-1}
@keyframes recsweep{60%,100%{transform:translateX(120%)}}
@keyframes recring{70%{box-shadow:0 14px 34px rgba(0,0,0,.35),0 0 0 16px rgba(239,208,142,0)}}
.rec .pb{flex:none;width:52px;height:52px;border-radius:50%;background:var(--navy);display:grid;place-items:center;box-shadow:0 0 0 4px rgba(19,41,77,.2)}
.rec .pb svg{width:22px;margin-left:4px}
.rec small{display:block;font-weight:800;font-size:12px;letter-spacing:.2em;opacity:.8}
.rec b{display:block;font-family:var(--serif);font-weight:900;font-size:clamp(22px,3.6vw,32px);line-height:1.05}
.rec .go{flex:none;font-weight:900;font-size:26px}
.tool.gold{background:var(--gold-grad);color:var(--navy);border-color:#FFF1C9;font-weight:900}
"""
s = s.replace(".tools{", css + ".tools{", 1)

btn = """  <a class="rec" href="grabaciones.html">
    <span class="pb"><svg viewBox="0 0 24 24"><path d="M6 3.5v17a1 1 0 0 0 1.5.86l14-8.5a1 1 0 0 0 0-1.72l-14-8.5A1 1 0 0 0 6 3.5z" fill="#EFD08E"/></svg></span>
    <span><small>¿TE LO PERDISTE? YA ESTÁN DISPONIBLES</small><b>Ver grabaciones del congreso</b></span><span class="go">→</span>
  </a>
"""
s = s.replace('  <div class="nowbar" id="nowbar"></div>', btn + '  <div class="nowbar" id="nowbar"></div>', 1)
s = s.replace('  <div class="tools">', '  <div class="tools">\n    <a class="tool gold" href="grabaciones.html"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M4 5h11v14H4zM16 9l5-3v12l-5-3z"/></svg>Ver grabaciones</a>', 1)
# al terminar el evento, el aviso de arriba lleva a las grabaciones
s = s.replace("""st.innerHTML = '<span class="live" style="background:#13294D;border:2px solid #C9973F;box-shadow:none">GRACIAS POR ACOMPAÑARNOS · MIRA LA GRABACIÓN</span>';""",
              """st.innerHTML = '<a href="grabaciones.html" class="live" style="background:#13294D;border:2px solid #C9973F;box-shadow:none">GRACIAS POR ACOMPAÑARNOS · VER GRABACIONES →</a>';""")
assert s.count("grabaciones.html") >= 3, s.count("grabaciones.html")
open(p, "w", encoding="utf-8").write(s)
print("ok", s.count("grabaciones.html"))
