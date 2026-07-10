// ============ GOOGLE ADS CONVERSION ============
const ADS_CONVERSION_SEND_TO = 'AW-18214310940/6jAFCPrZ6M0cEJyooe1D';

function trackAdsConversion(userData) {
  if (typeof gtag === 'function') {
    if (userData && (userData.email || userData.phone_number)) {
      gtag('set', 'user_data', userData);
    }
    gtag('event', 'conversion', {
      'send_to': ADS_CONVERSION_SEND_TO,
      'value': 10.0,
      'currency': 'EUR'
    });
  }
}

// ============ NAVBAR: shadow/blur ao scroll ============
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 50);
});

// ============ HAMBURGER MENU ============
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('navMenu');
const navBackdrop = document.getElementById('navBackdrop');
const MOBILE_NAV_QUERY = '(max-width: 900px)';

let scrollLockY = 0;

function lockBodyScroll() {
  scrollLockY = window.scrollY;
  document.body.style.position = 'fixed';
  document.body.style.top = `-${scrollLockY}px`;
  document.body.style.left = '0';
  document.body.style.right = '0';
  document.body.classList.add('nav-open-lock');
}

function unlockBodyScroll() {
  document.body.classList.remove('nav-open-lock');
  document.body.style.position = '';
  document.body.style.top = '';
  document.body.style.left = '';
  document.body.style.right = '';
  window.scrollTo(0, scrollLockY);
}

function getFocusableMenuItems() {
  return Array.from(navMenu.querySelectorAll('a, summary')).filter(
    (el) => el.offsetParent !== null
  );
}

function openNavMenu() {
  navMenu.classList.add('open');
  navBackdrop.classList.add('visible');
  hamburger.setAttribute('aria-expanded', 'true');
  lockBodyScroll();
  const items = getFocusableMenuItems();
  if (items.length) items[0].focus();
}

function closeNavMenu({ returnFocus = false } = {}) {
  if (!navMenu.classList.contains('open')) return;
  navMenu.classList.remove('open');
  navBackdrop.classList.remove('visible');
  hamburger.setAttribute('aria-expanded', 'false');
  unlockBodyScroll();
  navMenu.querySelectorAll('details[open]').forEach((d) => d.removeAttribute('open'));
  if (returnFocus) hamburger.focus();
}

hamburger.addEventListener('click', () => {
  if (navMenu.classList.contains('open')) {
    closeNavMenu({ returnFocus: true });
  } else {
    openNavMenu();
  }
});

navBackdrop.addEventListener('click', () => closeNavMenu({ returnFocus: true }));

document.addEventListener('keydown', (event) => {
  if (!navMenu.classList.contains('open')) return;

  if (event.key === 'Escape') {
    closeNavMenu({ returnFocus: true });
    return;
  }

  if (event.key === 'Tab' && window.matchMedia(MOBILE_NAV_QUERY).matches) {
    const items = getFocusableMenuItems();
    if (!items.length) return;
    const first = items[0];
    const last = items[items.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }
});

navMenu.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => closeNavMenu());
});

window.addEventListener('resize', () => {
  if (!window.matchMedia(MOBILE_NAV_QUERY).matches) closeNavMenu();
});

// ============ ACTIVE NAV LINK ============
(function markActiveNavLink() {
  const normalize = (pathname) => {
    const cleaned = pathname.replace(/index\.html$/, '').replace(/\/$/, '');
    return cleaned === '' ? '/' : cleaned;
  };
  const current = normalize(location.pathname);

  navMenu.querySelectorAll('a[href]:not(.nav-menu-cta)').forEach((link) => {
    const linkPath = normalize(new URL(link.getAttribute('href'), location.href).pathname);
    if (linkPath !== current) return;
    link.classList.add('active');
    const parentDropdown = link.closest('.nav-dropdown');
    if (parentDropdown) parentDropdown.querySelector('summary').classList.add('active');
  });
})();

// ============ FAQ ACCORDION ============
document.querySelectorAll('.faq-item').forEach(item => {
  const question = item.querySelector('.faq-question');
  const answer = item.querySelector('.faq-answer');

  question.addEventListener('click', () => {
    const isOpen = item.classList.contains('open');

    document.querySelectorAll('.faq-item.open').forEach(openItem => {
      if (openItem !== item) {
        openItem.classList.remove('open');
        openItem.querySelector('.faq-answer').style.maxHeight = null;
        openItem.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
      }
    });

    item.classList.toggle('open', !isOpen);
    question.setAttribute('aria-expanded', String(!isOpen));
    answer.style.maxHeight = !isOpen ? answer.scrollHeight + 'px' : null;
  });
});

// ============ FADE-IN ON SCROLL ============
const fadeEls = document.querySelectorAll('.fade-in');
const fadeObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      fadeObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });

fadeEls.forEach(el => fadeObserver.observe(el));

// ============ ANIMATED COUNTERS ============
function animateCount(el) {
  const target = parseInt(el.dataset.count, 10);
  const suffix = el.dataset.suffix || '';
  const duration = 1500;
  const start = performance.now();

  function step(now) {
    const progress = Math.min((now - start) / duration, 1);
    const value = Math.floor(progress * target);
    el.textContent = value + suffix;
    if (progress < 1) {
      requestAnimationFrame(step);
    } else {
      el.textContent = target + suffix;
    }
  }
  requestAnimationFrame(step);
}

const counters = document.querySelectorAll('[data-count]');
const countObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      animateCount(entry.target);
      countObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

counters.forEach(el => countObserver.observe(el));

// ============ CONTACT FORM (Web3Forms) ============
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  const statusEl = document.getElementById('formStatus');
  const submitBtn = contactForm.querySelector('button[type="submit"]');

  contactForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const submittedEmail = document.getElementById('email').value;
    const submittedPhone = document.getElementById('phone').value;

    statusEl.className = 'form-status';
    statusEl.textContent = '';
    const originalBtnText = submitBtn.textContent;
    submitBtn.disabled = true;
    submitBtn.textContent = 'A enviar...';

    try {
      const response = await fetch(contactForm.action, {
        method: 'POST',
        headers: { 'Accept': 'application/json' },
        body: new FormData(contactForm),
      });
      const result = await response.json();

      if (response.status === 200 && result.success) {
        statusEl.className = 'form-status success';
        statusEl.textContent = 'Mensagem enviada com sucesso! Entraremos em contacto em breve.';
        contactForm.reset();
        if (typeof gtag === 'function') {
          gtag('event', 'generate_lead', { form_id: 'contactForm' });
        }
        trackAdsConversion({
          email: submittedEmail,
          phone_number: submittedPhone
        });
      } else {
        throw new Error(result.message || 'Falha no envio');
      }
    } catch (err) {
      statusEl.className = 'form-status error';
      statusEl.textContent = 'Não foi possível enviar a mensagem. Tente novamente ou use o WhatsApp acima.';
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = originalBtnText;
    }
  });
}

// ============ WHATSAPP CLICK TRACKING ============
document.querySelectorAll('a[href^="https://wa.me/"]').forEach(link => {
  link.addEventListener('click', () => {
    if (typeof gtag === 'function') {
      gtag('event', 'contact_whatsapp');
    }
    trackAdsConversion();
  });
});
