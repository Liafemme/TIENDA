"""Muestra un lote de productos (texto limpio en español) y genera los fragmentos
GraphQL de opciones traducidas al polaco. Uso: python3 lote.py INICIO FIN"""
import json, sys, re
S="/tmp/claude-0/-home-user-TIENDA/08206a7f-e631-5a01-a638-7ad5e8a9c929/scratchpad/clean.json"
D=json.load(open("/home/user/TIENDA/tools/diccionario_opciones.json"))
def val(v):
    if v in D["valores"]: return D["valores"][v]
    return v.replace("EE. UU.","US").replace("R. U.","UK")
LINKED={"gid://shopify/ProductOption/18555113406795","gid://shopify/ProductOption/18561282048331"}
def frags(p, n):
    out=[]
    for k,o in enumerate(p["options"]):
        if o["name"]=="Title": continue
        nn=D["nombres"].get(o["name"],o["name"])
        seen=set(); ups=[]
        for v in o["optionValues"]:
            t=val(v["name"]); base=t; i=2
            while t.lower() in seen: t=f"{base} {i}"; i+=1
            seen.add(t.lower())
            if t!=v["name"] and o["id"] not in LINKED: ups.append('{id:"%s",name:"%s"}'%(v["id"],t))
        if nn==o["name"] and not ups: continue
        s='o%d_%d: productOptionUpdate(productId:"%s", option:{id:"%s", name:"%s"}'%(n,k,p["id"],o["id"],nn)
        if ups: s+=', optionValuesToUpdate:[%s]'%",".join(ups)
        s+='){userErrors{message}}'
        out.append(s)
    return out
a,b=int(sys.argv[1]),int(sys.argv[2])
data=json.load(open(S))
for n in range(a,min(b,len(data))):
    p=data[n]
    ben=[m for m in p["metafields"]["nodes"] if m["key"]=="beneficios"]
    print(f"### {n} {p['id']} | {p['title']} | tipo={p['productType']} | seo={'si' if p['seo']['title'] else 'no'}")
    if ben: print("BENEFICIOS:", json.dumps(ben[0]["value"],ensure_ascii=False))
    for f in frags(p,n): print("OPT:",f)
    print(p["clean"]); print()
