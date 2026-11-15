import math,json,collections,sys
R=4.41
def pretty(eur):
    x=eur*R
    step=5 if x<150 else 10
    return round(math.ceil((x+0.01)/step)*step-0.01,2)
rows=[l.split() for l in open('data.txt')]
out=[];tab=collections.OrderedDict()
for pid,p,c in rows:
    if p=='VAR': continue
    pp=pretty(float(p)); item={"productId":"gid://shopify/Product/"+pid,"price":{"amount":f"{pp:.2f}","currencyCode":"PLN"}}
    if c!='-':
        cc=pretty(float(c))
        if cc>pp: item["compareAtPrice"]={"amount":f"{cc:.2f}","currencyCode":"PLN"}
    out.append(item); tab[(p,c)]=(pp,item.get("compareAtPrice",{}).get("amount"))
print(len(out))
for k,v in sorted(tab.items(),key=lambda kv: float(kv[0][0])): print(k,v)
json.dump(out[:115],open('b1.json','w'),separators=(',',':')); json.dump(out[115:],open('b2.json','w'),separators=(',',':'))
