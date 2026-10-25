/**
 * LF · Sugerencias del carrito (snippets/lf-cart-upsell.liquid).
 * Se carga una vez desde snippets/cart-drawer.liquid; los botones llegan después al re-renderizar el carrito.
 */
import { CartLinesUpdateEvent } from '@shopify/events';

document.addEventListener('click', async (event) => {
  const button = event.target instanceof Element ? event.target.closest('[data-lf-upsell-add]') : null;
  if (!button || button.disabled) return;
  event.preventDefault();

  const card = button.closest('.lf-upsell__card');
  const select = card?.querySelector('.lf-upsell__select');
  const variantId = select ? select.value : button.dataset.variantId;
  if (!variantId) return;

  button.disabled = true;
  button.classList.add('is-loading');

  const sectionIds = [...document.querySelectorAll('cart-items-component[data-section-id]')].map(
    (el) => el.dataset.sectionId
  );
  const deferred = CartLinesUpdateEvent.createPromise();
  button.dispatchEvent(
    new CartLinesUpdateEvent({
      action: 'add',
      context: 'cart',
      lines: [{ merchandiseId: String(variantId), quantity: 1 }],
      promise: deferred.promise,
    })
  );

  try {
    const response = await fetch(Theme.routes.cart_add_url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify({ items: [{ id: Number(variantId), quantity: 1 }], sections: sectionIds.join(',') }),
    });
    const data = await response.json();
    const cart = await (await fetch(`${Theme.routes.cart_url}.js`, { headers: { Accept: 'application/json' } })).json();
    deferred.resolve({
      cart: CartLinesUpdateEvent.createCartFromAjaxResponse(cart),
      detail: {
        items: cart.items,
        itemCount: 1,
        source: 'lf-cart-upsell',
        sections: data.status ? undefined : data.sections,
        didError: Boolean(data.status),
      },
    });
  } catch (error) {
    deferred.reject(error);
    button.disabled = false;
    button.classList.remove('is-loading');
  }
});
