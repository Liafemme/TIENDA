# Diagnóstico Lia Femme – por qué no se paga (7 oct 2026)

Datos reales de Shopify, últimos 30 días.

## Embudo
| Paso | Sesiones | % |
|---|---|---|
| Visitas | 5.780 | |
| Añaden al carrito | 245 | 4,2 % (correcto) |
| Llegan al checkout | 83 | 34 % del carrito (correcto) |
| **Pagan** | **2** | **2,4 % del checkout (lo normal es 40-50 %)** |

- Móvil: 80 checkouts → 1 pago. Casi todo el tráfico es Facebook/Instagram en móvil.
- Solo 18 checkouts abandonados tienen email: unas 65 de 83 personas se van en la **primera pantalla** del checkout, sin escribir nada.
- Shopify Payments sí cobra (los pedidos reales entraron por ahí): no es un fallo técnico, es de **confianza y opciones de pago**.

## Fallos encontrados (por orden de impacto)

1. **Las políticas publicadas son las antiguas y contradicen la web.** La web dice "Envío gratis · Devolución 30 días", pero el enlace del pie del checkout y de la ficha abre:
   - "TENGA EN CUENTA QUE NO REALIZAMOS DEVOLUCIONES GRATUITAS, SE APLICAN CARGOS"
   - "nuestros productos se envían desde Asia", "no es posible un reembolso"
   - "debido al COVID-19", "puede demorar hasta 40 días hábiles", "no podemos cancelarlo"
   - Términos: "Este sitio web es operado por **Tienda**"
   → Los textos nuevos de `politicas/` **no se han pegado** todavía en Ajustes → Políticas.
2. **No hay PayPal ni pago a plazos (Klarna) ni Bizum** (pendiente en `CHECKOUT.md`). En España, con tienda nueva y tráfico de Facebook, la clienta que no conoce la marca no mete su tarjeta: quiere PayPal o pagar en 3 plazos.
3. **Cero prueba social:** ninguna app de reseñas, ni estrellas, ni fotos de clientas.
4. **Señales de tienda poco seria:** solo un Gmail como contacto, sin nombre de empresa / NIF / dirección (aviso legal obligatorio en España), redes sociales vacías en el pie.
5. **Catálogo incoherente:** tienda "Femme" con zapatos y prendas de hombre (colección `moda-hombre`, "Zapatos Tomás", "Mocasines Álvaro", "Camiseta Henley"…). Producto de 285,95 € (Vestido Verona) junto a productos de 30-50 €.
6. **Oferta sin urgencia real:** tachados permanentes (-35 % en todo, siempre), tres mensajes de descuento a la vez y ningún motivo para comprar *hoy* (sin fecha de fin, sin stock limitado, sin regalo).

## Plan (por orden)
1. Pegar `politicas/devoluciones.html` y `politicas/envios.html` en Ajustes → Políticas y sustituir los Términos de servicio (quitar "Tienda").
2. Activar PayPal + Klarna (Ajustes → Pagos).
3. Instalar app de reseñas (Judge.me gratis) e importar/solicitar reseñas reales.
4. Añadir aviso legal con titular, NIF y dirección; contacto con email de dominio (hola@liafemme.com) y WhatsApp.
5. Ocultar productos de hombre y el vestido de 285,95 €.
6. Una sola oferta clara con fecha de fin (p. ej. "Rebajas de otoño -20 % hasta el domingo") en lugar de tachado permanente + 3 códigos.
7. Activar emails de checkout abandonado (1 h y 24 h, con el código en el 2º).
