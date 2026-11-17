// ---- hora (Colombia). Para probar: añade ?hora=10:30 a la dirección ----
const DAY = "2026-11-16";
const qh = new URLSearchParams(location.search).get("hora");
const at = hm => new Date(`${DAY}T${hm.padStart(5, "0")}:00-05:00`).getTime();
function nowMs() { return qh ? at(qh) : Date.now(); }

// ---- cinta superior ----
const MQ = ["<span class='r'>● EN VIVO</span>", "EDUCAR CON ALMA", "LUNES 16 DE NOVIEMBRE", "1ER CONGRESO SOBRE FAMILIA Y CRIANZA CATÓLICA", "INVITA COLEGIO VÉRITAS", "TEATRO VALERIO ANTONIO · MARINILLA"];
document.getElementById("mq").innerHTML = [...MQ, ...MQ, ...MQ, ...MQ].map(t => t.startsWith("<") ? t : `<span>${t}</span>`).join("");

// ---- agenda ----
const IC = {
  door: "M5 21V4a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v17M3 21h18M14 12h.01",
  cup: "M4 8h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5V8zm13 1h1.5a2.5 2.5 0 0 1 0 5H17M7 3v2M11 3v2",
  food: "M7 3v8M5 3v5a2 2 0 0 0 4 0V3M7 11v10M17 3c-2 0-3 2-3 5s1 4 3 4v9",
  star: "M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z",
};
const AG = [
  { s: "7:00", e: "8:00", k: "min", t: "7:00 – 8:00 a. m.", l: "Apertura del teatro y registro", ic: "door" },
  { s: "8:00", e: "9:00", k: "misa", t: "8:00 a. m.", l: "Santa Misa" },
  { s: "9:00", e: "10:00", k: "min", t: "9:00 a. m.", l: "Break", ic: "cup" },
  { s: "10:00", e: "11:00", k: "talk", h: "10:00", ap: "A. M.", n: 1, title: "Lo que mi casa me enseñó", sub: "Así me educaron en mi hogar: con el alma", who: "Rodrigo Jaramillo", img: "__IMG_rodrigo__" },
  { s: "11:00", e: "12:30", k: "talk", h: "11:00", ap: "A. M.", n: 2, title: "¿Para qué educamos?", sub: "Principios antropológicos, teológicos y filosóficos de la educación", who: "Wilson Tamayo", img: "__IMG_wilson__" },
  { s: "12:30", e: "13:30", k: "min", t: "12:30 p. m.", l: "Almuerzo", ic: "food" },
  { s: "13:30", e: "14:30", k: "talk", h: "1:30", ap: "P. M.", n: 3, title: "¿Estamos criando bien?", sub: "Aciertos y desaciertos de los modelos de crianza modernos", who: "Santiago Correa", img: "__IMG_santiago__" },
  { s: "14:30", e: "14:45", k: "min", t: "2:30 p. m.", l: "Break", ic: "cup" },
  { s: "14:45", e: "16:00", k: "talk", h: "2:45", ap: "P. M.", n: 4, title: "Educar con alma", sub: "Principios para una crianza católica en casa", who: "Yuliana Ramírez", img: "__IMG_yuliana__" },
  { s: "16:00", e: "16:30", k: "min", t: "4:00 p. m.", l: "Cierre", ic: "star" },
];
const agEl = document.getElementById("agenda");
AG.forEach((it, i) => {
  const d = document.createElement("div");
  d.className = "ag reveal" + (it.k !== "min" ? " big" : "");
  d.style.transitionDelay = (i % 3) * 0.08 + "s";
  const inl = '<span class="inline n">● AHORA</span><span class="inline x">A CONTINUACIÓN</span>';
  if (it.k === "min")
    d.innerHTML = `<div class="t">${it.t}</div><span class="dot2"></span><div class="lbl"><svg viewBox="0 0 24 24" fill="none" stroke="#C9973F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="${IC[it.ic]}"/></svg>${it.l}${inl}</div>`;
  else if (it.k === "misa")
    d.innerHTML = `<div class="t" style="font-weight:900;font-size:16px;color:#fff">${it.t}</div><span class="dot2"></span><div class="lbl"><span class="misa"><i>✝</i><b>${it.l}</b></span>${inl}</div>`;
  else
    d.innerHTML = `<div class="pill"><b>${it.h}</b><span>${it.ap}</span></div><span class="dot2"></span>
      <article class="card" data-n="0${it.n}"><span class="badge n"><span class="dot"></span>EN VIVO AHORA</span><span class="badge x">A CONTINUACIÓN</span>
        <div class="ph"><img src="${it.img}" alt=""></div>
        <div><small>CONFERENCIA ${it.n}</small><h3>${it.title}</h3><p>${it.sub}</p><span class="who">${it.who}</span></div></article>`;
  agEl.appendChild(d);
  it.el = d;
});
const fill = document.getElementById("fill"), nowbar = document.getElementById("nowbar");
function agenda() {
  const now = nowMs();
  const dayStart = at("6:00"), dayEnd = at("23:59");
  let cur = null, next = null, lastDone = null;
  AG.forEach(it => {
    it.el.classList.remove("past", "now", "next");
    if (now < dayStart) return; // antes del día: agenda neutra
    if (now >= at(it.e)) { it.el.classList.add("past"); lastDone = it; }
    else if (now >= at(it.s)) { it.el.classList.add("now"); cur = it; }
    else if (!next) next = it;
  });
  if (next && now <= dayEnd) next.el.classList.add("next");
  // la línea dorada se llena hasta la actividad en curso
  const ref = cur || lastDone, rail = agEl.querySelector(".rail");
  if (ref) {
    const dot = ref.el.querySelector(".dot2");
    fill.style.height = Math.max(0, dot.getBoundingClientRect().top + dot.offsetHeight / 2 - rail.getBoundingClientRect().top) + "px";
  } else fill.style.height = "0px";
  // barra "ahora en vivo" sobre el video
  if (cur) {
    const txt = cur.k === "talk" ? `Conferencia ${cur.n}: ${cur.title} — ${cur.who}` : cur.l;
    if (nowbar.dataset.k !== cur.s) {
      nowbar.innerHTML = `${cur.img ? `<img src="${cur.img}" alt="">` : '<span class="dot" style="width:14px;height:14px;flex:none"></span>'}<div><small>AHORA EN VIVO</small><b>${txt}</b></div>`;
      nowbar.dataset.k = cur.s; nowbar.classList.remove("on"); void nowbar.offsetWidth;
    }
    nowbar.classList.add("on");
  } else nowbar.classList.remove("on");
}
agenda(); setInterval(agenda, 15000); addEventListener("resize", agenda);

// ---- aparición al hacer scroll ----
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { threshold: .12 });
document.querySelectorAll(".reveal").forEach(n => io.observe(n));
setTimeout(agenda, 1200);
