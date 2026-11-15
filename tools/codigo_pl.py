# Reemplazos de textos fijos en español del código del tema (archivos lf-*)
import sys,os
R={
"blocks__lf-bundle.liquid":[
 ("No se ha podido añadir el pack. Inténtalo de nuevo.","Nie udało się dodać zestawu. Spróbuj ponownie."),
 ('"default": "Elige tu pack y ahorra"','"default": "Wybierz zestaw i oszczędzaj"'),
 ('"default": "Set completo: Pulsera + Collar + Anillo"','"default": "Pełny zestaw: Bransoletka + Naszyjnik + Pierścionek"'),
 ('"default": "Pulsera, Collar, Anillo"','"default": "Bransoletka, Naszyjnik, Pierścionek"'),
 ('"default": "Pulsera + Collar"','"default": "Bransoletka + Naszyjnik"'),
 ('"default": "Pulsera, Collar"','"default": "Bransoletka, Naszyjnik"'),
 ('"default": "Pulsera"','"default": "Bransoletka"'),
 ('"default": "Brilla en la oscuridad"','"default": "Świeci w ciemności"'),
 ('"default": "Ahorras [ahorro]"','"default": "Oszczędzasz [ahorro]"'),
 ('"default": "Más vendido"','"default": "Bestseller"'),
 ('"default": "Conjunto a juego"','"default": "Dopasowany komplet"'),
 ('"default": "Mejor oferta"','"default": "Najlepsza oferta"'),
 ('"default": "El anillo a mitad de precio"','"default": "Pierścionek za pół ceny"'),
],
"blocks__lf-buybox.liquid":[
 ("Ahorras {{ save","Oszczędzasz {{ save"),
 ("'ene,feb,mar,abr,may,jun,jul,ago,sep,oct,nov,dic'","'sty,lut,mar,kwi,maj,cze,lip,sie,wrz,paź,lis,gru'"),
 ("Pídelo hoy y recíbelo entre el <strong>","Zamów dziś, a otrzymasz między <strong>"),
 ("</strong> y el <strong>","</strong> a <strong>"),
 ("· Envío gratis con seguimiento</span>","· Darmowa wysyłka z numerem śledzenia</span>"),
 ('aria-label="Métodos de pago"','aria-label="Metody płatności"'),
 ('"default":"<strong>Compra 2 y ahorra un 15%</strong> · se aplica solo en el carrito"','"default":"<strong>Kup 2 i oszczędź 15%</strong> · nalicza się samo w koszyku"'),
 ('"default":"30 días para devoluciones"','"default":"30 dni na zwrot"'),
 ('"default":"Pago 100% seguro y cifrado"','"default":"100% bezpieczna i szyfrowana płatność"'),
 ('"default":"Atención por email en menos de 24 h"','"default":"Odpowiedź e-mailem w ciągu 24 h"'),
],
"blocks__lf-offer.liquid":[
 ("Tu precio en tu primera compra:","Twoja cena przy pierwszych zakupach:"),
 ("Código <b>{{ bs.hw_code }}</b> ya activado: se aplica solo en el carrito, no tienes que copiar nada.","Kod <b>{{ bs.hw_code }}</b> już aktywny: nalicza się sam w koszyku, nie musisz niczego kopiować."),
 ("Llévate 2 prendas y paga <strong","Kup 2 produkty i zapłać <strong"),
 ("</strong> cada una</span>","</strong> za sztukę</span>"),
 ("% BIENVENIDA</span>","% NA START</span>"),
 ('"default": "BIENVENIDA10"','"default": "WITAJ10"'),
 ('"default": "3 prendas: -20% · 4 o más: -25%"','"default": "3 produkty: -20% · 4 lub więcej: -25%"'),
],
"blocks__lf-rating-header.liquid":[
 ('aria-label="{{ rating_txt_short }} de 5 estrellas"','aria-label="{{ rating_txt_short }} na 5 gwiazdek"'),
 ("{{ rating_txt_short }} de 5 en {{ count }} {% if count == 1 %}reseña{% else %}reseñas{% endif %}","{{ rating_txt_short }} na 5 · {{ count }} {% if count == 1 %}opinia{% else %}opinii{% endif %}"),
],
"blocks__lf-card-save.liquid":[('"default": "Ahorras"','"default": "Oszczędzasz"')],
"blocks__lf-trust-line.liquid":[('"default": "Envío gratis · 30 días para devolver"','"default": "Darmowa wysyłka · 30 dni na zwrot"')],
"sections__lf-footer.liquid":[('aria-label="Métodos de pago"','aria-label="Metody płatności"')],
"sections__lf-hw-bar.liquid":[('aria-label="Tiempo restante de la oferta de hoy"','aria-label="Czas do końca dzisiejszej oferty"')],
"snippets__lf-hw-countdown.liquid":[('aria-label="Tiempo restante de la oferta de hoy"','aria-label="Czas do końca dzisiejszej oferty"')],
"sections__lf-liq-hero.liquid":[(">Mejor precio<",">Najlepsza cena<")],
"sections__lf-newsletter.liquid":[
 ("¡Gracias! Ya estás en la lista.","Dziękujemy! Jesteś już na liście."),
 ('placeholder="Tu email"','placeholder="Twój e-mail"'),
 ("Puedes darte de baja en cualquier momento. Consulta nuestra <a","Możesz wypisać się w każdej chwili. Zobacz naszą <a"),
 (">política de privacidad</a>",">politykę prywatności</a>"),
],
"snippets__lf-autodiscount.liquid":[
 ('aria-label="Cerrar"','aria-label="Zamknij"'),
 ("🎁 Bienvenida a Lia Femme","🎁 Witaj w Lia Femme"),
 ("Un regalo para ti<br><span>-10% en tu primera compra</span>","Prezent dla Ciebie<br><span>-10% na pierwsze zakupy</span>"),
 ("Código <strong>{{ code }}</strong> · ya activado","Kod <strong>{{ code }}</strong> · już aktywny"),
 ("Se aplica solo en el carrito, no tienes que copiar nada.<br>Y si te llevas más, ahorras más: <strong>2 prendas -15%, 3 prendas -20% y 4 o más -25%</strong>.","Nalicza się sam w koszyku, nie musisz niczego kopiować.<br>A im więcej kupisz, tym więcej oszczędzasz: <strong>2 produkty -15%, 3 produkty -20%, 4 lub więcej -25%</strong>."),
 (">¡Lo quiero!<",">Chcę!<"),
 ("Envío gratis con seguimiento · 30 días para devoluciones","Darmowa wysyłka z numerem śledzenia · 30 dni na zwrot"),
],
"snippets__lf-card-offer.liquid":[("Black Friday · Llévate 2: <strong>","Black Friday · Kup 2: <strong>")],
"snippets__lf-cart-trust.liquid":[
 ("<span>Envío gratis</span>","<span>Darmowa wysyłka</span>"),
 ("<span>30 días para devolver</span>","<span>30 dni na zwrot</span>"),
 ("<span>Atención 24 h</span>","<span>Odpowiedź w 24 h</span>"),
 ('aria-label="Métodos de pago"','aria-label="Metody płatności"'),
 ("Pago 100% seguro y cifrado. Si no te encanta, tienes 30 días para devolverlo.","100% bezpieczna i szyfrowana płatność. Jeśli nie pokochasz zakupu, masz 30 dni na zwrot."),
 ("<strong>Envío gratis</strong>con seguimiento","<strong>Darmowa wysyłka</strong>z numerem śledzenia"),
 ("<strong>30 días</strong>para devolver","<strong>30 dni</strong>na zwrot"),
 ("<strong>Atención 24 h</strong>por email, en español","<strong>Odpowiedź w 24 h</strong>e-mailem"),
 ("Compra tranquila en Lia Femme","Spokojne zakupy w Lia Femme"),
 ("Si te llega dañado o no es lo que pediste, te lo cambiamos o te devolvemos el dinero sin coste.","Jeśli produkt dotrze uszkodzony lub niezgodny z zamówieniem, wymienimy go lub zwrócimy pieniądze bez kosztów."),
 ("Reembolso en un máximo de 14 días, con el mismo método de pago.","Zwrot pieniędzy w ciągu maksymalnie 14 dni, tą samą metodą płatności."),
 ("Número de seguimiento por email en cuanto sale tu pedido.","Numer śledzenia e-mailem, gdy tylko zamówienie zostanie wysłane."),
],
"snippets__lf-cart-upsell.liquid":[(">Añadir</button>",">Dodaj</button>"),("default: 'Completa tu look'","default: 'Dopełnij swój look'")],
"snippets__lf-piedras.liquid":[
 ("<span>Elige tus piedras</span>","<span>Wybierz kamienie</span>"),
 ("Elige 2 piedras para añadir al carrito","Wybierz 2 kamienie, aby dodać do koszyka"),
 ('data-prop1="Piedra 1" data-prop2="Piedra 2"','data-prop1="Kamień 1" data-prop2="Kamień 2"'),
 ('"Enero", "color": "#8e1b2e", "sub": "Granate"','"Styczeń", "color": "#8e1b2e", "sub": "Granat"'),
 ('"Febrero", "color": "#8f5fc4", "sub": "Amatista"','"Luty", "color": "#8f5fc4", "sub": "Ametyst"'),
 ('"Marzo", "color": "#86d3e3", "sub": "Aguamarina"','"Marzec", "color": "#86d3e3", "sub": "Akwamaryn"'),
 ('"Abril", "color": "#eef3f6", "sub": "Diamante"','"Kwiecień", "color": "#eef3f6", "sub": "Diament"'),
 ('"Mayo", "color": "#1d9a5b", "sub": "Esmeralda"','"Maj", "color": "#1d9a5b", "sub": "Szmaragd"'),
 ('"Junio", "color": "#d9c8e6", "sub": "Alejandrita"','"Czerwiec", "color": "#d9c8e6", "sub": "Aleksandryt"'),
 ('"Julio", "color": "#cf1340", "sub": "Rubí"','"Lipiec", "color": "#cf1340", "sub": "Rubin"'),
 ('"Agosto", "color": "#a5c43a", "sub": "Peridoto"','"Sierpień", "color": "#a5c43a", "sub": "Perydot"'),
 ('"Septiembre", "color": "#1f4fbf", "sub": "Zafiro"','"Wrzesień", "color": "#1f4fbf", "sub": "Szafir"'),
 ('"Octubre", "color": "#f08ab6", "sub": "Turmalina"','"Październik", "color": "#f08ab6", "sub": "Turmalin"'),
 ('"Noviembre", "color": "#f0a11d", "sub": "Topacio"','"Listopad", "color": "#f0a11d", "sub": "Topaz"'),
 ('"Diciembre", "color": "#3aa6d8", "sub": "Circón"','"Grudzień", "color": "#3aa6d8", "sub": "Cyrkon"'),
],
"snippets__lf-stars.liquid":[("}} de {{ scale }} estrellas","}} na {{ scale }} gwiazdek")],
"snippets__lf-store-rating.liquid":[("{% if total == 1 %}reseña{% else %}reseñas{% endif %}","{% if total == 1 %}opinia{% else %}opinii{% endif %}")],
"snippets__lf-tier-bar.liquid":[
 ("Añade <strong>{{ missing }} {% if missing == 1 %}prenda{% else %}prendas{% endif %} más</strong> y ahorra un <strong>{{ next_pct }}%</strong> en todo el pedido","Dodaj jeszcze <strong>{{ missing }} {% if missing == 1 %}produkt{% else %}produkty{% endif %}</strong> i oszczędź <strong>{{ next_pct }}%</strong> na całym zamówieniu"),
 ("¡Genial! Tienes el <strong>máximo descuento: -{{ cur_pct }}%</strong>","Świetnie! Masz <strong>maksymalny rabat: -{{ cur_pct }}%</strong>"),
 ("{% if forloop.last %}+{% endif %} prendas</span>","{% if forloop.last %}+{% endif %} prod.</span>"),
 ("Estás ahorrando <strong>","Oszczędzasz <strong>"),
],
"snippets__lf-trust-line.liquid":[("default: 'Envío gratis · 30 días para devolver'","default: 'Darmowa wysyłka · 30 dni na zwrot'")],
}
src,dst=sys.argv[1],sys.argv[2]
os.makedirs(dst,exist_ok=True)
for fn,pairs in R.items():
    c=open(os.path.join(src,fn)).read()
    for a,b in pairs:
        n=c.count(a)
        if n==0: print("NO ENCONTRADO",fn,"|",a[:60])
        c=c.replace(a,b)
    open(os.path.join(dst,fn),"w").write(c)
print("ok",len(R))
