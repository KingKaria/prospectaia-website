// ============ COOKIE CONSENT (Google Consent Mode v2) ============
(function () {
  const STORAGE_KEY = 'prospectaia_consent';
  const EXPIRY_MS = 60 * 60 * 1000; // re-ask 1h after the last choice
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

  function readStoredChoice() {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return null;
    try {
      const { value, timestamp } = JSON.parse(raw);
      if (Date.now() - timestamp > EXPIRY_MS) return null;
      return value;
    } catch {
      return null;
    }
  }

  function storeChoice(granted) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({
      value: granted ? 'granted' : 'denied',
      timestamp: Date.now()
    }));
  }

  const stored = readStoredChoice();
  if (stored === 'granted' || stored === 'denied') {
    updateConsent(stored === 'granted');
  } else if (banner) {
    banner.classList.add('visible');
  }

  if (acceptBtn) {
    acceptBtn.addEventListener('click', () => {
      storeChoice(true);
      updateConsent(true);
      banner.classList.remove('visible');
    });
  }

  if (rejectBtn) {
    rejectBtn.addEventListener('click', () => {
      storeChoice(false);
      updateConsent(false);
      banner.classList.remove('visible');
    });
  }
})();
