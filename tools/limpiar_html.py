"""Limpia el HTML de las descripciones: quita estilos/atributos basura y spans vacíos,
conservando estructura, enlaces, imágenes y tablas."""
import json, sys, re
from bs4 import BeautifulSoup, Comment

KEEP = {"a": {"href", "target", "rel"}, "img": {"src", "alt", "width", "height"},
        "th": {"scope", "colspan", "rowspan"}, "td": {"colspan", "rowspan"},
        "iframe": {"src", "width", "height", "allowfullscreen", "frameborder"}}

def clean(html):
    s = BeautifulSoup(html or "", "html.parser")
    for c in s.find_all(string=lambda t: isinstance(t, Comment)):
        c.extract()
    for t in s.find_all(True):
        allowed = KEEP.get(t.name, set())
        for a in list(t.attrs):
            if a not in allowed or t.attrs[a] in ("undefined", ""):
                del t.attrs[a]
    for t in s.find_all(["span", "font", "div", "section"]):
        t.unwrap()
    for t in s.find_all(["td", "th"]):
        txt = t.get_text(" ", strip=True)
        if not t.find("img"):
            t.clear(); t.append(txt)
    for t in s.find_all(["p", "h3", "h4", "h5"]):
        if not t.get_text(strip=True) and not t.find("img"):
            t.decompose()
    out = str(s)
    out = re.sub(r">\s+<", "><", out)
    return out.strip()

if __name__ == "__main__":
    data = json.load(open(sys.argv[1]))
    for p in data:
        p["clean"] = clean(p["descriptionHtml"])
    json.dump(data, open(sys.argv[2], "w"), ensure_ascii=False)
    print(sum(len(p["descriptionHtml"]) for p in data), "->", sum(len(p["clean"]) for p in data))
