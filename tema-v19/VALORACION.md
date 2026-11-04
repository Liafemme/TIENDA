# Valoración ilustrativa en la ficha de producto (tema v19)

Tema: "Lia Femme – v19 estrellas sobre el título (Claude)" (id 211870155083), sin publicar.

Muestra ★★★★★ 4,5/5 (estrellas verdes) con la etiqueta "Valoración ilustrativa",
encima del título del producto (en móvil queda justo debajo de la foto).
Es estática: no usa Judge.me, apps, CSV ni metacampos.

Archivos modificados en Shopify:
- blocks/lf-rating-header.liquid: el bloque ahora siempre muestra la valoración estática.
- templates/product.lf-test.json: se añade el bloque (product.json y
  product.bundle-mariposa.json ya lo tenían encima del título).

Los productos nuevos usan product.json por defecto, así que lo heredan automáticamente.
La nota y la etiqueta se pueden cambiar en el editor de temas (bloque "Valoración ilustrativa").
