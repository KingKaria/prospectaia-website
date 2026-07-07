// ============ NAVBAR: shadow/blur ao scroll ============
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 50);
});

// ============ HAMBURGER MENU ============
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('navMenu');

hamburger.addEventListener('click', () => {
  navMenu.classList.toggle('open');
});

navMenu.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => navMenu.classList.remove('open'));
});

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
