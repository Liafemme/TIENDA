# Checkout Lia Femme – lista de acciones

Datos (30 días): 79 personas llegaron al checkout y solo 2 pagaron (2,5 %). Lo normal es 40-50 %.

## Ya hecho (por Claude, vía API)
- [x] Método de envío renombrado: "Gratis" → **"Envío GRATIS con seguimiento"** + "Entrega en 7-14 días laborables" (España y UE) / "7-30 días según destino" (internacional).
- [x] Botones de pago exprés (Shop Pay / Apple Pay / Google Pay) activados en la ficha de producto (tema publicado).
- [x] Textos nuevos de políticas listos en `politicas/` (originales guardados en `backup-politicas/`).

## Hazlo tú (Shopify no deja hacerlo por API en el plan Basic)

### 1. Métodos de pago – Ajustes → Pagos (lo más importante)
- [ ] **PayPal**: "Activar PayPal Express Checkout" y conectar tu cuenta PayPal.
- [ ] **Klarna** (paga en 3 plazos): en Shopify Payments → "Métodos de pago" → añadir Klarna. Si no aparece, instalar la app de Klarna.
- [ ] Comprobar que **Shopify Payments está completamente verificado** (sin avisos en rojo en Ajustes → Pagos). Si la cuenta está en revisión, los pagos pueden fallar.
- [ ] Opcional: Bizum (vía app de Redsys/pasarela española) y Google Pay/Apple Pay ya vienen con Shopify Payments.

### 2. Formulario del checkout – Ajustes → Checkout
- [ ] Contacto: **"Teléfono o email"** (deja elegir).
- [ ] Nombre: "Nombre y apellido obligatorios" (está bien). Campo **"Empresa"**: Oculto.
- [ ] Línea de dirección 2: **Opcional**.
- [ ] Teléfono en dirección de envío: **Opcional** (no obligatorio).
- [ ] Activar **"Usar la dirección de envío como dirección de facturación"** por defecto.
- [ ] Activar **autocompletado de direcciones**.
- [ ] Marketing: activar casilla de **suscripción por email** (premarcada NO, pero visible).
- [ ] Propinas: **desactivadas**.

### 3. Diseño del checkout – Ajustes → Checkout → Personalizar
- [ ] Logo: el de Lia Femme (tamaño mediano), alineado al centro.
- [ ] Colores: fondo `#FBF8F4`, botones `#1E1A17`, acento `#9C5B3E`.
- [ ] Tipografía: títulos Playfair Display, texto Inter.
- [ ] Esquinas: redondeadas.
- [ ] Barra lateral / resumen: fondo `#F3EDE5`.

### 4. Políticas – Ajustes → Políticas
- [ ] Pegar `politicas/devoluciones.html` en "Política de reembolso" (botón `<>` para HTML).
- [ ] Pegar `politicas/envios.html` en "Política de envío".

### 5. Recuperar checkouts abandonados – Marketing → Automatizaciones
- [ ] Activar plantilla **"Recuperar checkout abandonado"** (1 email a la 1 h, otro a las 24 h).
- [ ] Opcional: incluir código de descuento en el 2º email (p. ej. 10 %).
- [ ] Activar también **"Recuperar carrito abandonado"** y **"Bienvenida a nuevos suscriptores"**.

### 6. Prueba final
- [ ] Hacer una compra real desde el **móvil** (con tarjeta propia, luego reembolsar) y anotar cualquier paso raro.

---

# Cambio a Polonia (solo mercado polaco)

## Ya hecho (por Claude)
- [x] Mercado **España** desactivado (en borrador). El mercado **Unión Europea** se mantiene.
- [x] Mercado **Polska** activo con moneda **PLN**. Idioma principal de la tienda: **polaco**.
- [x] Políticas de envío y devoluciones traducidas al polaco en `politicas/` (las versiones en español siguen en el historial de git).

## Hazlo tú
### 1. Moneda principal EUR → PLN – Ajustes → Datos de la tienda → Moneda de la tienda
- [ ] Cambiar a **złoty polaco (PLN)**. Si Shopify no deja (pasa cuando ya hay ventas o pagos con Shopify Payments), contactar con el soporte de Shopify.
- [ ] ⚠️ Shopify NO convierte los precios: 51,95 € pasa a ser 51,95 zł. **Avisa a Claude justo después** para reescribir los precios de las 4.839 variantes en złoty terminados en 9 (p. ej. 234 → 239 zł, 297 → 299 zł, 1286 → 1289 zł). Mejor hacerlo de noche, con poco tráfico.

### 2. Políticas – Ajustes → Políticas (botón `<>` para HTML)
- [ ] Pegar `politicas/devoluciones.html` en "Política de reembolso".
- [ ] Pegar `politicas/envios.html` en "Política de envío".
- [ ] Traducir también **Privacidad, Términos del servicio y Contacto** (siguen en español).

### 3. Pagos polacos – Ajustes → Pagos
- [ ] Activar **BLIK** y **Przelewy24** (son los métodos más usados en Polonia).
