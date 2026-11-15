# Cambio de marca: Lia Femme → Zofia Nowak

## Ya hecho (por Claude, vía API)
- [x] Logo final: **opción 1 (clásico elegante)** en la cabecera (`zofia-nowak-logo-cabecera.png`) y **monograma C** (Z | N) como icono de la pestaña (`zofia-nowak-icono.png`).
- [x] Tema duplicado **"Zofia Nowak – v26 nuevo nombre y logo (Claude)"** con logo, favicon y todos los textos "Lia Femme" → "Zofia Nowak" (hero, "Dlaczego warto kupować w sklepie Zofia Nowak", Club Zofia Nowak, popup de bienvenida, carrito, slider, reseñas, plantillas de producto y colecciones). Copia de los archivos en `tema-zofia-nowak/`.
- [x] Página "O nas" actualizada.
- [x] SEO (título y descripción) de 15 colecciones actualizado.
- [x] Correos (`liafemme23@gmail.com`, `info@liafemme.com`) y dominio `liafemme.com` **sin tocar**, como pediste.

## Hazlo tú (Shopify no lo permite por API con los permisos actuales)
1. [ ] **Publicar el tema**: Tienda online → Temas → "Zofia Nowak – v26…" → Publicar.
2. [ ] **Nombre de la tienda**: Ajustes → General → Nombre de la tienda → `Zofia Nowak`.
   (Esto cambia el título de la pestaña, el © del pie, los emails a clientes, el checkout y Shop Pay.)
3. [ ] **Políticas** (Ajustes → Políticas, botón `<>` para HTML):
   - Política de privacidad → pegar `politicas/politica-privacidad.html`
   - Términos del servicio → pegar `politicas/terminos-servicio.html`
   (Reembolso, envío y contacto no mencionan "Lia Femme": no hace falta tocarlas.)
4. [ ] **Logo del checkout**: Ajustes → Checkout → Personalizar → Logo → elegir `zofia-nowak-logo-cabecera.png`.
5. [ ] **Logo de emails**: Ajustes → Notificaciones → Personalizar plantillas de email → Logo → `zofia-nowak-logo-cabecera.png`.
6. [ ] **Apps**: Judge.me (nombre de respuesta "Lia Femme" → Zofia Nowak), Klaviyo (nombre del remitente/plantillas).
7. [ ] Opcional: nombre interno del menú "Menu Lia Femme (nowe)" (solo lo ves tú en el admin).

- [x] **Productos**: proveedor "Lia Femme" → "Zofia Nowak" en 216 productos (los 10 de Paola Milano no se tocan), SEO de ~140 productos y 21 descripciones actualizadas. 7 textos SEO que seguían en español, traducidos al polaco. Copia de los datos originales en `backup-productos/`.
- [x] **Código de la cuenta atrás**: `LIAFEMME` no existía en Shopify; cambiado por `WITAJ10` (activo, -10%) en el tema v26.

## Usos del monograma
- Foto de perfil de Instagram / TikTok / Facebook: `logo/propuestas/monograma-c.png` (o el sello `monograma-b.png`).
