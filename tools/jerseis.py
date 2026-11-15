import json,sys
COMMON='<ul><li><strong>{f}</strong> – wyjątkowy design, który nie przejdzie niezauważony.</li><li><strong>Ręcznie robiony z troską</strong> – każde oczko opowiada historię.</li><li><strong>Wygoda bez gryzienia</strong> – miękka, delikatna dla skóry przędza, która nie gryzie ani nie podrażnia.</li><li><strong>Miękka, przewiewna dzianina</strong> – stworzona dla komfortu przez cały dzień.</li><li><strong>Twarzowe dopasowanie</strong> – podkreśla sylwetkę i pasuje na każdą okazję.</li></ul><p>Na nieformalne spotkanie, relaksujący wieczór w domu czy wypad na świeże powietrze w warstwach: dzianinowy sweter ze stylem bez wysiłku i wygodą na długo.</p>'
items=json.load(open(sys.argv[1]))
out=[]
for i,(pid,title,h3,name,extra,feat) in enumerate(items):
    html=f'<h3>{h3}</h3><p>Odkryj ciepło, wygodę i ponadczasowe rzemiosło <strong>swetra {name}</strong> z naszej ekskluzywnej kolekcji ręcznie robionych swetrów islandzkich. Miękki splot i otulające dopasowanie sprawiają, że jest idealny na cały sezon, a {extra}</p><p><strong>Dlaczego go pokochasz:</strong></p>'+COMMON.format(f=feat)
    out.append('j%d: productUpdate(product:{id:"gid://shopify/Product/%s", title:%s, seo:{title:%s, description:%s}, descriptionHtml:%s}){userErrors{message}}'%(i,pid,json.dumps(title,ensure_ascii=False),json.dumps(title+" | Lia Femme",ensure_ascii=False),json.dumps(f"Sweter {name} z kolekcji ręcznie robionych swetrów w Lia Femme. Darmowa wysyłka i 30 dni na zwrot.",ensure_ascii=False),json.dumps(html,ensure_ascii=False)))
print("mutation {\n"+"\n".join(out)+"\n}")
