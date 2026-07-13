// ProspectaIA — banner de consentimento de cookies (RGPD)
(function () {
  var KEY = 'pia-cookies';
  function el(tag, css, html) {
    var e = document.createElement(tag);
    if (css) e.style.cssText = css;
    if (html) e.innerHTML = html;
    return e;
  }
  function init() {
    try { if (localStorage.getItem(KEY)) return; } catch (e) { return; }
    var wrap = el('div',
      'position:fixed;left:24px;bottom:24px;z-index:400;max-width:420px;background:#0B2530;border:1px solid rgba(255,255,255,0.12);border-radius:16px;padding:22px 24px;box-shadow:0 20px 60px rgba(0,0,0,0.55);font-family:Manrope,sans-serif;color:#E8F0F2;opacity:0;transform:translateY(16px);transition:opacity .45s ease-out,transform .45s ease-out;');
    wrap.setAttribute('role', 'dialog');
    wrap.setAttribute('aria-label', 'Consentimento de cookies');

    var title = el('div', "font-family:Sora,sans-serif;font-weight:700;font-size:16px;margin-bottom:8px;color:#F2F7F8;", 'Este site usa cookies');
    var txt = el('p', 'font-size:13.5px;line-height:1.55;color:#B8CBD1;margin:0 0 16px;',
      'Usamos cookies essenciais para o funcionamento do site e, com o seu consentimento, cookies de análise para melhorar a sua experiência. Saiba mais na nossa <a href="legal.dc.html?s=cookies" style="color:#1FD2A5;text-decoration:none;">Política de Cookies</a>.');

    var prefs = el('div', 'display:none;margin:0 0 16px;border-top:1px solid rgba(255,255,255,0.08);padding-top:14px;');
    prefs.innerHTML =
      '<label style="display:flex;align-items:center;justify-content:space-between;gap:12px;font-size:13.5px;color:#B8CBD1;margin-bottom:10px;">Essenciais (obrigatórios)<input type="checkbox" checked disabled></label>' +
      '<label style="display:flex;align-items:center;justify-content:space-between;gap:12px;font-size:13.5px;color:#B8CBD1;cursor:pointer;">Análise e estatísticas<input id="pia-ck-analytics" type="checkbox" style="cursor:pointer;"></label>';

    var row = el('div', 'display:flex;flex-wrap:wrap;gap:10px;align-items:center;');
    var btn = function (label, primary) {
      var b = el('button', primary
        ? 'background:#1FD2A5;color:#04211A;border:none;border-radius:8px;padding:10px 18px;font-family:Sora,sans-serif;font-weight:700;font-size:13.5px;cursor:pointer;transition:background .3s ease-out;'
        : 'background:none;color:#B8CBD1;border:1px solid rgba(255,255,255,0.2);border-radius:8px;padding:10px 18px;font-family:Sora,sans-serif;font-weight:600;font-size:13.5px;cursor:pointer;transition:border-color .3s ease-out,color .3s ease-out;');
      b.textContent = label;
      b.onmouseenter = function () { primary ? b.style.background = '#3ADFB6' : (b.style.borderColor = 'rgba(31,210,165,0.5)', b.style.color = '#F2F7F8'); };
      b.onmouseleave = function () { primary ? b.style.background = '#1FD2A5' : (b.style.borderColor = 'rgba(255,255,255,0.2)', b.style.color = '#B8CBD1'); };
      return b;
    };
    var accept = btn('Aceitar', true);
    var reject = btn('Rejeitar', false);
    var pref = el('button', 'background:none;border:none;color:#7E97A0;font-family:Manrope,sans-serif;font-size:13px;font-weight:600;cursor:pointer;text-decoration:underline;padding:0;');
    pref.textContent = 'Preferências';
    var save = btn('Guardar preferências', true);
    save.style.display = 'none';

    function close(value) {
      try { localStorage.setItem(KEY, JSON.stringify(value)); } catch (e) {}
      wrap.style.opacity = '0';
      wrap.style.transform = 'translateY(16px)';
      setTimeout(function () { wrap.remove(); }, 450);
    }
    accept.onclick = function () { close({ essential: true, analytics: true, ts: Date.now() }); };
    reject.onclick = function () { close({ essential: true, analytics: false, ts: Date.now() }); };
    pref.onclick = function () {
      prefs.style.display = 'block';
      save.style.display = 'inline-block';
      accept.style.display = 'none';
      reject.style.display = 'none';
      pref.style.display = 'none';
    };
    save.onclick = function () {
      var c = document.getElementById('pia-ck-analytics');
      close({ essential: true, analytics: !!(c && c.checked), ts: Date.now() });
    };

    row.appendChild(accept); row.appendChild(reject); row.appendChild(save); row.appendChild(pref);
    wrap.appendChild(title); wrap.appendChild(txt); wrap.appendChild(prefs); wrap.appendChild(row);
    document.body.appendChild(wrap);
    requestAnimationFrame(function () { requestAnimationFrame(function () {
      wrap.style.opacity = '1'; wrap.style.transform = 'translateY(0)';
    }); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { setTimeout(init, 800); });
  else setTimeout(init, 800);
})();
