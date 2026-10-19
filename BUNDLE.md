# Bundle de variantes – Pulsera Sueño Luminoso (Mariposa azul)

Inspirado en el bloque "Bundle & Save" de veloisse.com (app Kaching Bundles), hecho a medida en el tema, sin apps.
El pack se forma con las variantes del mismo producto (opción "Producto": Pulsera / Collar / Anillo, 52,50 € cada una).

| Opción | Piezas que entran al carrito | Descuento | Precio |
|---|---|---|---|
| Pulsera | Pulsera | – | 52,50 € |
| Pulsera + Collar · MÁS VENDIDO (preseleccionada) | Pulsera + Collar | 20 % | 84,00 € (antes 105,00 €) |
| Set completo · MEJOR OFERTA | Pulsera + Collar + Anillo | 30 % | 110,25 € (antes 157,50 €) |

## Cómo funciona
- Tema sin publicar **"Lia Femme – v10 bundle mariposa (Claude)"**:
  - `blocks/lf-bundle.liquid` (copia en `tema/blocks/`): tarjetas con miniaturas de cada pieza. Al pulsar
    "Agregar al carrito" mete todas las piezas del pack en una sola petición y abre el carrito de Upcart.
    Oculta el selector de variantes y la cantidad; en los packs oculta también el pago exprés (solo compraría 1 pieza).
  - `templates/product.bundle-mariposa.json`: plantilla asignada solo a esta pulsera.
- Descuentos automáticos de Shopify (el bloque solo muestra el precio):
  - "Compra 2 y ahorra 20%" (ya existía, toda la tienda, 2+ artículos) → Pulsera + Collar.
  - "Set Sueño Luminoso -30% (pulsera + collar + anillo)" (solo este producto, 3+ piezas) → Set completo.
    Si se cumplen los dos, Shopify aplica el mejor (30 %).

## Lo que tienes que hacer tú
- [ ] Publicar la pulsera en el canal **Tienda online** (ahora da 404).
- [ ] Revisar y **publicar** el tema "v10 bundle mariposa".
- [ ] Opcional: borrar en el editor de código del tema los archivos de prueba `templates/product.lf-test.json`
      y `blocks/lf-dbg.liquid` (no se ven en la tienda; la API no deja borrarlos).
- Textos, piezas, % y opción preseleccionada: editor del tema → producto → bloque "LF · Bundle de variantes".
  Si cambias un %, cambia también el descuento automático en Shopify → Descuentos.
