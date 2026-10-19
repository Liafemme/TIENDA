# Bundle por cantidad – Pulsera Sueño Luminoso (Mariposa azul)

Inspirado en el bloque "Bundle & Save" de veloisse.com (app Kaching Bundles), hecho a medida en el tema, sin apps.

## Qué se ha hecho
- **Tema nuevo (sin publicar):** "Lia Femme – v10 bundle mariposa (Claude)", copia del tema publicado.
  - `blocks/lf-bundle.liquid` (copia en `tema/blocks/`): 3 opciones encima de "Añadir al carrito".
  - `templates/product.bundle-mariposa.json`: plantilla del producto con el bloque y la caja "-20% x2" ocultada (el bundle ya lo muestra).
- **Producto:** asignada la plantilla `bundle-mariposa` (solo esta pulsera la usa).
- **Descuento automático nuevo:** "Pulsera mariposa: 3 por -30%" (solo esta pulsera, mínimo 3 unidades).
  El de 2 unidades lo cubre el que ya existía, "Compra 2 y ahorra 20%" (toda la tienda).

| Opción | Unidades | Descuento | Precio (52,50 €/ud) |
|---|---|---|---|
| 1 pulsera | 1 | – | 52,50 € |
| 2 pulseras · MÁS VENDIDO (preseleccionada) | 2 | 20 % | 84,00 € (ahorras 21,00 €) |
| 3 pulseras · MEJOR PRECIO | 3 | 30 % | 110,25 € (ahorras 47,25 €) |

## Lo que tienes que hacer tú
- [ ] Publicar la pulsera en el canal **Tienda online** (ahora mismo no está en ningún canal y da 404).
- [ ] Revisar y **publicar** el tema "v10 bundle mariposa" (Tienda online → Temas).
- Textos, % y opción preseleccionada se cambian en el editor del tema → producto → bloque "LF · Bundle por cantidad".
  Si cambias un %, cambia también el descuento automático en Shopify → Descuentos.
