(function(){
  if (customElements.get('lf-piedras')) return;

  // Estado compartido: sobrevive a los re-renderizados de la sección al cambiar de variante
  var state = window.__lfPiedras = window.__lfPiedras || {1: null, 2: null};
  var DROP = 'M20 3C25 13 34 22 34 33a14 14 0 0 1-28 0C6 22 15 13 20 3Z';

  function esc(s){ return String(s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
  function gemSVG(color, id){
    var g = 'lfpzg' + id;
    return '<svg viewBox="0 0 40 50" aria-hidden="true"><defs><radialGradient id="'+g+'" cx="38%" cy="58%" r="70%">'+
      '<stop offset="0" stop-color="#fff" stop-opacity=".85"/><stop offset=".35" stop-color="'+esc(color)+'"/><stop offset="1" stop-color="'+esc(color)+'" stop-opacity=".9"/></radialGradient></defs>'+
      '<path d="'+DROP+'" fill="url(#'+g+')" stroke="rgba(0,0,0,.18)" stroke-width="1"/>'+
      '<path d="M14 30c1-5 3-8 5-11" stroke="#fff" stroke-opacity=".7" stroke-width="1.6" fill="none" stroke-linecap="round"/></svg>';
  }
  function isSilver(){
    var txt = '';
    document.querySelectorAll('variant-picker[data-template-product-match] input:checked, variant-picker[data-template-product-match] select').forEach(function(el){
      txt += ' ' + (el.tagName === 'SELECT' ? (el.options[el.selectedIndex] || {}).text || el.value : el.value);
    });
    return /plata|silver|argent/i.test(txt);
  }
  // Dos lágrimas que forman un corazón, con el engaste en oro o plata
  function heartSVG(c1, c2){
    var metal = isSilver() ? '#c9ccd1' : '#d4a94f';
    function drop(cx, ang, gid){
      return '<g transform="translate('+(cx-20)+' 15) rotate('+ang+' 20 33)"><path d="'+DROP+'" fill="url(#'+gid+')" stroke="'+metal+'" stroke-width="3" stroke-linejoin="round"/></g>';
    }
    function grad(id, color){
      return '<radialGradient id="'+id+'" cx="40%" cy="60%" r="70%"><stop offset="0" stop-color="#fff" stop-opacity=".8"/><stop offset=".4" stop-color="'+esc(color)+'"/><stop offset="1" stop-color="'+esc(color)+'"/></radialGradient>';
    }
    return '<svg viewBox="0 0 160 92" role="img" aria-label="Vista previa del colgante">'+
      '<defs>'+grad('lfpzh1', c1 || '#e9e3dc')+grad('lfpzh2', c2 || '#e9e3dc')+'</defs>'+
      '<path d="M0 6 Q80 40 160 6" stroke="'+metal+'" stroke-width="1.5" fill="none"/>'+
      drop(64, 145, 'lfpzh1')+drop(96, -145, 'lfpzh2')+
      '<circle cx="80" cy="27" r="3" fill="none" stroke="'+metal+'" stroke-width="2"/></svg>';
  }

  var drawer, overlay, active, draft = {1: null, 2: null};

  function cfgOf(el){ try { return JSON.parse(el.querySelector('[data-pz-config]').textContent); } catch(e){ return {stones: []}; } }
  function stoneBy(cfg, name){ for (var i = 0; i < cfg.stones.length; i++) if (cfg.stones[i].name === name) return cfg.stones[i]; return null; }
  function count(s){ return (s[1] ? 1 : 0) + (s[2] ? 1 : 0); }
  function label(st){ return st.sub ? st.name + ' (' + st.sub + ')' : st.name; }

  function buildDrawer(cfg){
    if (drawer) { drawer.remove(); overlay.remove(); }
    overlay = document.createElement('div'); overlay.className = 'lf-pz-overlay'; overlay.hidden = true;
    drawer = document.createElement('div'); drawer.className = 'lf-pz-drawer';
    drawer.setAttribute('role', 'dialog'); drawer.setAttribute('aria-modal', 'true'); drawer.setAttribute('aria-hidden', 'true');
    var sections = [1, 2].map(function(n){
      return '<div class="lf-pz-drawer__section" data-sec="'+n+'"><h3 class="lf-pz-drawer__h">'+esc(cfg['stone'+n])+' *</h3>'+
        '<p class="lf-pz-drawer__err" data-err="'+n+'" hidden>'+esc(cfg.err)+'</p><div class="lf-pz-drawer__grid">'+
        cfg.stones.map(function(st, i){
          return '<button type="button" class="lf-pz-tile" data-slot="'+n+'" data-stone="'+esc(st.name)+'" aria-pressed="false">'+
            gemSVG(st.color, n + '_' + i)+'<span class="lf-pz-tile__name">'+esc(st.name)+'</span>'+
            (st.sub ? '<span class="lf-pz-tile__sub">'+esc(st.sub)+'</span>' : '')+'</button>';
        }).join('')+'</div></div>';
    }).join('');
    drawer.innerHTML =
      '<div class="lf-pz-drawer__head"><div><span class="lf-pz-drawer__title">'+esc(cfg.title)+'</span> <span class="lf-pz__muted" data-dcount>0/2</span></div>'+
      '<button type="button" class="lf-pz-drawer__close" aria-label="Cerrar"><svg width="20" height="20" viewBox="0 0 20 20"><path d="M3 3l14 14M17 3L3 17" stroke="#111" stroke-width="1.4" fill="none"/></svg></button></div>'+
      '<div class="lf-pz-drawer__preview" data-preview></div><div class="lf-pz-drawer__body">'+sections+'</div>'+
      '<div class="lf-pz-drawer__foot"><button type="button" class="lf-pz-drawer__confirm"><span>'+esc(cfg.confirm)+'</span><span data-fcount>0/2</span></button></div>';
    document.body.appendChild(overlay); document.body.appendChild(drawer);

    drawer.addEventListener('click', function(e){
      var t = e.target.closest('.lf-pz-tile');
      if (t) { draft[t.dataset.slot] = t.dataset.stone; renderDrawer(); return; }
      if (e.target.closest('.lf-pz-drawer__close')) close();
      if (e.target.closest('.lf-pz-drawer__confirm')) confirm();
    });
    overlay.addEventListener('click', close);
  }

  function renderDrawer(){
    var cfg = active.cfg, c = count(draft);
    drawer.querySelector('[data-dcount]').textContent = c + '/2';
    drawer.querySelector('[data-fcount]').textContent = c + '/2';
    drawer.querySelectorAll('.lf-pz-tile').forEach(function(t){
      var on = draft[t.dataset.slot] === t.dataset.stone;
      t.classList.toggle('is-selected', on); t.setAttribute('aria-pressed', on);
    });
    [1, 2].forEach(function(n){ if (draft[n]) drawer.querySelector('[data-err="'+n+'"]').hidden = true; });
    var s1 = stoneBy(cfg, draft[1]), s2 = stoneBy(cfg, draft[2]);
    drawer.querySelector('[data-preview]').innerHTML = heartSVG(s1 && s1.color, s2 && s2.color);
  }

  function open(el){
    active = el;
    if (!drawer || drawer.__cfgOwner !== el.cfgKey) { buildDrawer(el.cfg); drawer.__cfgOwner = el.cfgKey; }
    draft = {1: state[1], 2: state[2]};
    renderDrawer();
    overlay.hidden = false;
    requestAnimationFrame(function(){ overlay.classList.add('is-open'); drawer.classList.add('is-open'); });
    drawer.setAttribute('aria-hidden', 'false');
    document.documentElement.classList.add('lf-pz-lock');
    var first = drawer.querySelector('.lf-pz-tile'); if (first) setTimeout(function(){ first.focus({preventScroll: true}); }, 350);
  }
  function close(){
    if (!drawer) return;
    overlay.classList.remove('is-open'); drawer.classList.remove('is-open');
    drawer.setAttribute('aria-hidden', 'true');
    document.documentElement.classList.remove('lf-pz-lock');
    setTimeout(function(){ overlay.hidden = true; }, 300);
    if (active) { var b = active.querySelector('[data-pz-open]'); if (b) b.focus({preventScroll: true}); }
  }
  function confirm(){
    if (count(draft) < 2) {
      var miss = !draft[1] ? 1 : 2;
      drawer.querySelector('[data-err="'+miss+'"]').hidden = false;
      var sec = drawer.querySelector('[data-sec="'+miss+'"]'), body = drawer.querySelector('.lf-pz-drawer__body');
      body.scrollTo({top: sec.offsetTop - body.offsetTop - 4, behavior: 'smooth'});
      var btn = drawer.querySelector('.lf-pz-drawer__confirm');
      btn.classList.remove('shake'); void btn.offsetWidth; btn.classList.add('shake');
      return;
    }
    state[1] = draft[1]; state[2] = draft[2];
    document.querySelectorAll('lf-piedras').forEach(function(el){ el.sync(); });
    close();
  }
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && drawer && drawer.classList.contains('is-open')) close(); });

  class LfPiedras extends HTMLElement {
    connectedCallback(){
      this.cfg = cfgOf(this);
      this.cfgKey = this.querySelector('[data-pz-config]').textContent;
      if (!this.__bound) {
        this.__bound = true;
        this.addEventListener('click', function(e){ if (e.target.closest('[data-pz-open]')) open(this); });
      }
      this.sync();
    }
    complete(){ return !!(state[1] && state[2]); }
    sync(){
      var cfg = this.cfg, self = this;
      this.querySelector('[data-pz-count]').textContent = count(state) + '/2';
      this.querySelector('[data-pz-chips]').innerHTML = [1, 2].map(function(n){
        var st = stoneBy(cfg, state[n]); return st ? gemSVG(st.color, 'c' + n) : '';
      }).join('');
      if (this.complete()) { this.classList.remove('is-error'); this.querySelector('[data-pz-need]').hidden = true; }
      // Propiedades del artículo, asociadas al formulario de compra mediante el atributo form=
      [[1, this.dataset.prop1], [2, this.dataset.prop2]].forEach(function(p){
        var st = stoneBy(cfg, state[p[0]]);
        var input = self.querySelector('input[data-pz-prop="'+p[0]+'"]');
        if (!input) {
          input = document.createElement('input'); input.type = 'hidden';
          input.setAttribute('data-pz-prop', p[0]); input.setAttribute('form', self.dataset.formId);
          self.appendChild(input);
        }
        input.name = 'properties[' + p[1] + ']';
        input.value = st ? label(st) : '';
        input.disabled = !st;
      });
    }
  }
  customElements.define('lf-piedras', LfPiedras);

  // Re-sincronizar después de que el tema vuelva a pintar la sección (cambio Oro/Plata)
  document.addEventListener('change', function(e){
    if (!e.target.closest || !e.target.closest('variant-picker')) return;
    [80, 500, 1200].forEach(function(ms){ setTimeout(function(){ document.querySelectorAll('lf-piedras').forEach(function(el){ el.sync(); }); }, ms); });
  });

  // Sin las 2 piedras no se puede añadir al carrito ni comprar directamente
  function pickerFor(target){
    var els = document.querySelectorAll('lf-piedras');
    for (var i = 0; i < els.length; i++) {
      var el = els[i], form = document.getElementById(el.dataset.formId);
      if (!form) continue;
      var host = form.closest('product-form-component') || form;
      if (target === form || host.contains(target)) return el;
      if (target.closest && target.closest('sticky-add-to-cart [ref="addToCartButton"]')) return el;
    }
    return null;
  }
  function isBuy(target){
    if (!target.closest) return false;
    return !!target.closest('button[type="submit"], [name="add"], [ref="addToCartButton"], shopify-accelerated-checkout, shopify-buy-it-now-button, .shopify-payment-button');
  }
  function block(el, e){
    e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
    el.classList.add('is-error'); el.querySelector('[data-pz-need]').hidden = false;
    open(el);
  }
  ['click', 'keydown'].forEach(function(type){
    document.addEventListener(type, function(e){
      if (type === 'keydown' && e.key !== 'Enter' && e.key !== ' ') return;
      if (!isBuy(e.target)) return;
      var el = pickerFor(e.target);
      if (el && !el.complete()) block(el, e);
    }, true);
  });
  document.addEventListener('submit', function(e){
    var el = pickerFor(e.target);
    if (el && !el.complete()) block(el, e);
  }, true);
})();
