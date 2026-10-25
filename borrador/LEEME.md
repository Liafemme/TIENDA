# Borrador: reseñas, confianza en el checkout y barra de descuento

**Estado: aplicado en una COPIA SIN PUBLICAR del tema** («Lia Femme – v11 reseñas + confianza + tramos
(BORRADOR Claude)», id 210952454475). El tema publicado («v10 bundle mariposa») no se ha tocado.
Vista previa: https://liafemme.com/?preview_theme_id=210952454475
No se ha creado ningún descuento ni cambiado Judge.me, Upcart o el checkout.

- `tema/`: archivos del tema tal y como quedarían (misma ruta que en Shopify).
- `original/`: copia de los archivos actuales que se modifican, para comparar.
- `imagenes/`: banner del checkout, sellos para el carrito de Upcart y una vista previa en móvil.

---

## Cambio de descuentos (pedido el 25/10)

Aplicado en la copia del tema (textos, anuncios, popup, ficha, tarjetas, pack de la pulsera y barra del carrito):
- Código de bienvenida: **BIENVENIDA10 · 10 % · un solo uso por clienta** (antes BIENVENIDA15 · 15 %).
- Por cantidad: **2 prendas -15 % · 3 prendas -20 % · 4 o más -25 %** (antes 2 prendas -20 %).

Pendiente en Shopify → Descuentos (cambia la tienda en vivo, se hace al publicar la copia):
1. «Bienvenida 15% primera compra (código antiguo)» (código BIENVENIDA10): bajar a 10 % y renombrar. Ya es de un uso por clienta.
2. BIENVENIDA15: desactivar.
3. «Compra 2 y ahorra 20%»: bajar a 15 % y renombrar.
4. Crear «Compra 3 y ahorra 20%» y «Compra 4 y ahorra 25%» (automáticos, todos los productos, sin combinar).
5. Decidir qué pasa con «Set Sueño Luminoso -30%» (supera el tope del 25 %).

## Antes de nada: 3 cosas que he encontrado

1. **Ningún producto tiene reseñas todavía en Judge.me** (los 50 productos activos tienen la nota vacía).
   Todo lo que he preparado lee las reseñas **reales** de Judge.me y **se oculta solo** mientras no haya.
   No he puesto ninguna reseña inventada: en España/UE (Directiva Ómnibus) es ilegal mostrar reseñas
   falsas o importadas del proveedor como si fueran de tus clientas.
   → Para que esto sirva hay que conseguir reseñas: Judge.me → *Solicitudes de reseña* (email automático
   X días después de la entrega, pidiendo foto, con un pequeño descuento como premio por la foto).
2. **El widget de reseñas de Judge.me de la ficha está desactivado y configurado con «datos de ejemplo»**
   (`review_data: sample_data`). No lo he tocado. Al publicar hay que activarlo y cambiar a datos reales
   del producto (ver paso 4). Si se activa tal cual, enseñaría reseñas falsas.
3. La sección de testimonios de la ficha tiene una errata: «Opiniones de nuestras **prendras**».

## Lo que NO se puede hacer en tu plan (Basic) y qué propongo a cambio

Shopify **solo deja añadir textos o bloques en las páginas de pago (junto a «Pagar ahora») a las tiendas
Shopify Plus**. En Basic no hay forma (ni con apps) de poner el microtexto de garantía ni la nota media
al lado de «Pagar ahora». Lo que sí he preparado:

- **Todo eso justo debajo del botón «Finalizar compra» del carrito** (último paso antes del pago).
- **Banner del checkout** (`imagenes/checkout-banner-2000x240.png`) con envío gratis · 30 días · pago
  seguro, que sí se puede subir en Basic: *Ajustes → Checkout → Personalizar → Encabezado → Banner*.
  Ojo: Shopify recorta el banner en móvil; revísalo en la vista previa del editor antes de guardar.
- El método de envío ya se llama «Envío GRATIS con seguimiento» (hecho en la ronda anterior).

---

## 1. Reseñas con foto y nota media

| Dónde | Qué | Archivo |
|---|---|---|
| Ficha, bajo el título | Estrellas + nota + nº de reseñas; al tocar baja al widget de Judge.me (con fotos) | `blocks/lf-rating.liquid` (nuevo) y `templates/product.json` |
| Portada, tras la barra de confianza | Sección «Lo que dicen nuestras clientas»: nota media de la tienda + tarjetas con foto | `sections/lf-reviews.liquid` (nuevo) y `templates/index.json` |
| Tarjetas de producto (portada, relacionados) | Estrellas pequeñas + nº de reseñas | `snippets/lf-product-card.liquid` |
| Carrito (antesala del checkout) | Nota media de la tienda bajo «Finalizar compra» | `snippets/lf-cart-trust.liquid` |

Piezas comunes: `snippets/lf-stars.liquid` (estrellas con relleno parcial) y
`snippets/lf-store-rating.liquid` (media ponderada de todas las reseñas reales; con más de 50 productos
la calcula con los 50 primeros, limitación de Shopify).

La sección de portada **no lleva reseñas de ejemplo**: las tarjetas se rellenan en el editor copiando
reseñas reales de Judge.me (foto de la clienta, nombre, estrellas, texto, producto). Sin tarjetas ni
reseñas, la sección no aparece.

## 2. Confianza en el carrito / checkout

`snippets/lf-cart-trust.liquid`, debajo del botón de pagar:
- Microtexto: «🔒 Pago 100% seguro y cifrado. Si no te encanta, tienes 30 días para devolverlo.»
- Tres sellos: Envío gratis con seguimiento · 30 días para devolver · Pago seguro (tarjeta, Apple Pay, Google Pay).
- Nota media real (solo cuando haya reseñas).

## 3. Barra de progreso del descuento por cantidad

`snippets/lf-tier-bar.liquid`, encima del total del carrito. Dice cuántas prendas faltan para el
siguiente tramo, marca los tramos conseguidos y enseña **el ahorro real** del carrito.

Tramos propuestos (se cambian en una línea de `blocks/_cart-summary.liquid`: `tiers: '2:15,3:20,4:25'`):

| Prendas | Descuento | ¿Existe ya en Shopify? |
|---|---|---|
| 2 | -15% | Existe al 20 %: hay que bajarlo a 15 % |
| 3 | -20% | **No, hay que crearlo** |
| 4 o más | -25% | **No, hay que crearlo** |

**Decide tú los porcentajes** (dependen de tu margen). La barra solo informa: el descuento lo aplica
Shopify, así que antes de publicar hay que crear los descuentos automáticos de 3 y 4 prendas
(*Descuentos → Crear → Importe de descuento en productos → Automático → Cantidad mínima de artículos*).
Como no se combinan entre sí, Shopify aplica automáticamente el mayor. Si prefieres solo 2 tramos,
dejamos `tiers: '2:20'`... aunque entonces la barra pierde gracia; con 3 tramos funciona mucho mejor.

### Importante: tu carrito lateral es de Upcart

La app **Upcart está activa** y sustituye al carrito lateral del tema, así que la mayoría de clientas
ve el carrito de Upcart, no el del tema. Lo de arriba aparece en la página `/cart`. Para el carrito
lateral, lo mismo se configura dentro de Upcart (lo dejo descrito, sin tocarlo):
- **Barra de tramos**: Upcart → *Rewards* (ahora desactivado) → por **número de artículos**, con los
  mismos tramos y porcentajes. Si se usa, conviene pausar el descuento «Compra 2 y ahorra 20%» de
  Shopify para no tener dos sistemas de descuento a la vez.
- **Sellos de confianza**: Upcart → *Trust badges* → subir `imagenes/sellos-confianza-1200x200.png`.

---

## Cómo lo publicaríamos (cuando lo apruebes)

1. Duplicar el tema publicado y aplicar los archivos de `tema/` **en la copia** (no en el publicado).
2. Revisar la copia con su enlace de vista previa (móvil y ordenador): ficha, portada y carrito con 1, 2, 3 y 4 prendas.
3. Crear los descuentos de 3 y 4 prendas (si los apruebas).
4. En el editor de la copia, en la ficha: activar el widget de Judge.me y cambiar «datos de ejemplo»
   por los del producto. Corregir la errata «prendras».
5. Cuando haya reseñas, añadir tarjetas en «LF · Reseñas con foto» de la portada.
6. Publicar la copia. Banner del checkout y Upcart, desde sus pantallas.

Archivos que cambian respecto al tema actual:
- Nuevos: `blocks/lf-rating.liquid`, `sections/lf-reviews.liquid`, `snippets/lf-stars.liquid`,
  `snippets/lf-store-rating.liquid`, `snippets/lf-tier-bar.liquid`, `snippets/lf-cart-trust.liquid`.
- Modificados: `blocks/_cart-summary.liquid` (bloque del carrito, 4 líneas), `snippets/lf-product-card.liquid`,
  `templates/product.json` (1 bloque), `templates/index.json` (1 sección).
