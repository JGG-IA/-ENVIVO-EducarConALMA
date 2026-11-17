# Lee la lista de YouTube descargada (pl.html) y guarda videos.json (id, título, duración)
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
src = sys.argv[1]
h = open(src, encoding="utf-8").read()
i = h.index("ytInitialData")
start = h.index("{", i)
d, _ = json.JSONDecoder().raw_decode(h[start:])
out, seen = [], set()

def walk(o):
    if isinstance(o, dict):
        if "lockupViewModel" in o:
            r = o["lockupViewModel"]
            vid = r.get("contentId")
            title = (((r.get("metadata") or {}).get("lockupMetadataViewModel") or {}).get("title") or {}).get("content", "")
            dur = ""
            for m in re.finditer(r'"text":\s*"(\d{1,2}:\d{2}(?::\d{2})?)"', json.dumps(r, ensure_ascii=False)):
                dur = m.group(1); break
            if vid and len(vid) == 11 and vid not in seen:
                seen.add(vid); out.append({"id": vid, "title": title, "dur": dur})
        if "playlistVideoRenderer" in o:
            r = o["playlistVideoRenderer"]
            vid = r["videoId"]
            if vid not in seen:
                seen.add(vid)
                out.append({"id": vid, "title": "".join(x.get("text", "") for x in r["title"].get("runs", [])),
                            "dur": r.get("lengthText", {}).get("simpleText", "")})
        for v in o.values(): walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)

walk(d)
for v in out: print(v)
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
