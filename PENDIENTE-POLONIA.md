# Cambio a Polonia – estado (14/11/2026)

## Hecho en Shopify
- Mercado **Polska** creado en PLN (Polonia sacada del mercado UE). Idioma polaco activado (sin publicar).
- Método de envío renombrado a polaco: "DARMOWA dostawa z numerem śledzenia".
- 5 páginas traducidas (Kontakt, O nas, Tabela rozmiarów, FAQ, Prywatność).
- 20 colecciones y 6 menús traducidos.
- Descuentos nuevos: **WITAJ10** (10 %) y **WITAJ15** (15 %). Descuentos automáticos renombrados.
- 8 colores (metaobjetos) traducidos.
- **Productos: 142 de 230 traducidos** (título, descripción, SEO, opciones Kolor/Rozmiar y colores). Siguiente: índice 142 (`python3 tools/lote.py 142 149`).

## Falta (lo hago yo)
- Productos 142–229.
- Tema: copia traducida al polaco → **necesito que reconectes la app de Shopify** (pide permisos nuevos para editar temas).

## Falta (lo haces tú en Shopify)
- Ajustes → Idiomas: poner **polaco como idioma predeterminado** (así el checkout y los emails salen en polaco).
- Ajustes → Políticas: pegar `politicas/wysylka.html` (envío) y `politicas/zwroty.html` (reembolso). Privacidad y Términos: "Crear desde plantilla" una vez el idioma esté en polaco.
- Pagos: activar **BLIK** y **Przelewy24** (los métodos que más usan en Polonia).

Copia completa del español en `backup-es/`.
