# Construye index.html (transmisión) y grabaciones.html con las imágenes incrustadas
import base64, os
from urllib.parse import quote
H = os.path.dirname(os.path.abspath(__file__))
VID = "d2ptmrR9mEE"
LIST = "PLEhdyJ7Hr4Og"
WAMSG = quote("¡Hola! Quiero hacer mi donación al Colegio Véritas por las grabaciones del Congreso Educar con alma.")
IMGS = [("emblema", "emblema.jpg"), ("sello", "sello.png"), ("wilson", "wilson.jpg"), ("santiago", "santiago.jpg"),
        ("yuliana", "yuliana.jpg"), ("rodrigo", "rodrigo.jpg"), ("jg", "jg.png")]

def build(src, dst):
    s = open(os.path.join(H, src), encoding="utf-8").read()
    s = s.replace("__VID__", VID).replace("__LIST__", LIST).replace("__WAMSG__", WAMSG)
    for n, f in IMGS:
        mime = "image/png" if f.endswith("png") else "image/jpeg"
        s = s.replace(f"__IMG_{n}__", f"data:{mime};base64," + base64.b64encode(open(os.path.join(H, f), "rb").read()).decode())
    assert "__IMG_" not in s and "__VID__" not in s and "__LIST__" not in s and "__WAMSG__" not in s
    out = os.path.join(os.path.dirname(H), dst)
    open(out, "w", encoding="utf-8").write(s)
    print(out, round(len(s) / 1024), "KB")

build("plantilla.html", "index.html")
build("grabaciones.html", "grabaciones.html")
