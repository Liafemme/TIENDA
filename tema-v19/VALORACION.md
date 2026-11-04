# Valoración en la ficha de producto (tema v19)

Tema: "Lia Femme – v19 estrellas sobre el título (Claude)" (id 211870155083), sin publicar.

Muestra ★★★★★ 4,7 de 5 en 23 reseñas (cuadros negros, texto subrayado en Playfair Display),
encima del título del producto (en móvil, justo debajo de la foto). Valores fijos,
sin apps, CSV ni metacampos. Se editan en el bloque "Valoración" del editor de temas
(nota media y número de reseñas).

Archivos en Shopify:
- blocks/lf-rating-header.liquid: el bloque de la valoración.
- templates/product.lf-test.json: se añade el bloque (product.json y
  product.bundle-mariposa.json ya lo tenían encima del título).
- La línea "Envío gratis · 30 días para devolver" se ha quitado.
- blocks/lf-trust-line.liquid y snippets/lf-trust-line.liquid quedaron sin uso
  (no se pueden borrar desde la API; se pueden eliminar en el editor de código).

Los productos nuevos usan product.json por defecto, así que lo heredan automáticamente.
