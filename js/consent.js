// ============ COOKIE CONSENT (Google Consent Mode v2) ============
(function () {
  const STORAGE_KEY = 'prospectaia_consent';
  const banner = document.getElementById('cookieBanner');
  const acceptBtn = document.getElementById('cookieAccept');
  const rejectBtn = document.getElementById('cookieReject');

  function updateConsent(granted) {
    const state = granted ? 'granted' : 'denied';
    gtag('consent', 'update', {
      'ad_storage': state,
      'ad_user_data': state,
      'ad_personalization': state,
      'analytics_storage': state
    });
  }

  const stored = localStorage.getItem(STORAGE_KEY);
  if (stored === 'granted' || stored === 'denied') {
    updateConsent(stored === 'granted');
  } else if (banner) {
    banner.classList.add('visible');
  }

  if (acceptBtn) {
    acceptBtn.addEventListener('click', () => {
      localStorage.setItem(STORAGE_KEY, 'granted');
      updateConsent(true);
      banner.classList.remove('visible');
    });
  }

  if (rejectBtn) {
    rejectBtn.addEventListener('click', () => {
      localStorage.setItem(STORAGE_KEY, 'denied');
      updateConsent(false);
      banner.classList.remove('visible');
    });
  }
})();
