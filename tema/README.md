# Tema v7 – hero con marca de fondo

Archivos subidos al tema **"Lia Femme – v6 descuentos 15/20 (Claude)"** (sin publicar),
que es una copia del tema publicado "Lia Femme" a 7 oct 2026.

| Archivo | Qué hace |
|---|---|
| `blocks/lf-offer.liquid` | Recuadro bajo el precio en la ficha: "Tu precio hoy: X € (-10% BIENVENIDA)" y "Llévate 2 y paga X € cada una (-15%)". |
| `snippets/lf-card-offer.liquid` | Línea "Con tu 10%: X €" bajo el precio de cada tarjeta de producto. |
| `snippets/lf-product-card.liquid` | Tarjetas de la portada: añade la línea anterior. |
| `blocks/price.liquid` | Bloque de precio de Horizon: añade la línea anterior en colecciones, búsqueda y relacionados (no en el precio principal de la ficha). |
| `snippets/lf-autodiscount.liquid` | Sigue aplicando BIENVENIDA10 solo; sustituye el aviso pequeño por un popup "¡Ups! Tienes un regalo" (1 vez cada 24 h, nunca en el carrito). |
| `templates/product.json` | Coloca `lf-offer` justo debajo del precio y quita la promo duplicada del bloque de confianza. |

Clientas con sesión iniciada y pedidos previos no ven el 10% (el código es de un solo uso por cliente): ven solo la oferta de 2 prendas.

Si cambias los descuentos en Shopify, cambia los porcentajes en el bloque "LF · Precio con descuento" (editor del tema → ficha de producto) y en `lf-card-offer.liquid`.

## v7 (hero)
`sections/lf-hero.liquid`: nombre "LIA FEMME" grande y translúcido detrás del texto de la portada, con línea "Moda femenina". Ajustable en el editor (texto, opacidad 10–70%, arriba/centro, mostrar u ocultar). Maquetas en `previews/`.
