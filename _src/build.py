import base64, os
H = os.path.dirname(os.path.abspath(__file__))
VID = "d2ptmrR9mEE"
s = open(os.path.join(H, "plantilla.html"), encoding="utf-8").read().replace("__VID__", VID)
for n, f in [("emblema", "emblema.jpg"), ("sello", "sello.png"), ("wilson", "wilson.jpg"), ("santiago", "santiago.jpg"), ("yuliana", "yuliana.jpg"), ("rodrigo", "rodrigo.jpg"), ("jg", "jg.png")]:
    mime = "image/png" if f.endswith("png") else "image/jpeg"
    s = s.replace(f"__IMG_{n}__", f"data:{mime};base64," + base64.b64encode(open(os.path.join(H, f), "rb").read()).decode())
assert "__IMG_" not in s and "__VID__" not in s
out = os.path.join(os.path.dirname(H), "index.html")
open(out, "w", encoding="utf-8").write(s)
print(out, round(len(s) / 1024), "KB")
