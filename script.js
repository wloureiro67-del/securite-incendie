/* =============================================
   SECURITEINCENDIEPRO.FR — Script global v2
   ============================================= */

const MAKE_WEBHOOK_URL = 'https://hook.eu1.make.com/n29seqs24j7elaqeg4hh44d3v9nx6hkn';
const LOGO_URL = 'https://www.securiteincendiepro.fr/logo.png';

/* ── Helpers validation ── */
function formatPhone(val) {
  return val.replace(/\D/g, '').slice(0, 10)
    .replace(/(\d{2})(?=\d)/g, '$1 ').trim();
}
function isValidPhone(val) {
  return /^\d{10}$/.test(val.replace(/\s/g, ''));
}
function isValidEmail(val) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val);
}

/* ── Soumission générique (formFinal, sidebar forms) ── */
let genericIsSubmitting = false;

function submitForm(formEl, btnEl, successEl) {
  if (genericIsSubmitting) return;
  const fields = formEl.querySelectorAll('[required]');
  let ok = true;

  fields.forEach(el => {
    const fieldWrap = el.closest('.field');
    const isValid =
      el.name === 'telephone' ? isValidPhone(el.value) :
      el.name === 'email'     ? isValidEmail(el.value) :
                                el.value.trim() !== '';
    el.classList.toggle('error', !isValid);
    if (fieldWrap) fieldWrap.classList.toggle('has-err', !isValid);
    if (!isValid) ok = false;
  });
  if (!ok) return;

  genericIsSubmitting = true;
  btnEl.classList.add('loading');
  btnEl.innerHTML = '<span class="spinner"></span> Envoi en cours…';

  const data = {};
  new FormData(formEl).forEach((v, k) => { data[k] = v; });
  data.date      = new Date().toLocaleString('fr-FR', { timeZone: 'Europe/Paris' });
  data.source    = window.location.pathname;
  data.logo_url  = LOGO_URL;
  if (!data.form_id) data.form_id = 'final';

  fetch(MAKE_WEBHOOK_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  .catch(err => console.error('Webhook error:', err))
  .finally(() => {
    genericIsSubmitting = false;
    localStorage.setItem('si_submitted', '1');
    formEl.style.display = 'none';
    if (successEl) successEl.style.display = 'block';
    launchConfetti();
  });
}

/* ══════════════════════════════════════════
   FORMULAIRE MULTI-ÉTAPES (Hero)
══════════════════════════════════════════ */
function initHeroForm() {
  const form = document.getElementById('formHero');
  if (!form) return;

  const successDiv  = document.querySelector('#form-hero .form-success-v2');
  let heroData = {};
  let heroIsSubmitting = false;

  /* ── Progress helper ── */
  function goToStep(step) {
    form.querySelectorAll('.form-step').forEach(s => s.classList.remove('active'));
    const target = form.querySelector('.form-step[data-step="' + step + '"]');
    if (target) target.classList.add('active');

    /* Progress indicators */
    document.querySelectorAll('#form-hero .prog-step').forEach((s, i) => {
      const idx = i + 1;
      s.classList.toggle('active', idx === step);
      s.classList.toggle('done',   idx < step);
      if (idx < step) s.textContent = '✓';
      else s.textContent = String(idx);
    });
    /* Progress lines */
    const lines = document.querySelectorAll('#form-hero .prog-line-fill');
    lines.forEach((l, i) => {
      l.style.width = (i < step - 1) ? '100%' : '0%';
    });
    /* Label */
    const lbl = document.querySelector('#form-hero .form-step-label');
    if (lbl) lbl.textContent = step === 1
      ? 'Étape 1/2 — Votre établissement'
      : 'Étape 2/2 — Vos coordonnées';
  }

  /* ── Étape 1 → 2 ── */
  const nextBtn = form.querySelector('.step-next-btn');
  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      const step1Fields = form.querySelectorAll('.form-step[data-step="1"] [required]');
      let ok = true;
      step1Fields.forEach(el => {
        const valid = el.value.trim() !== '';
        el.classList.toggle('error', !valid);
        el.closest('.field')?.classList.toggle('has-err', !valid);
        if (!valid) ok = false;
      });
      if (!ok) return;
      step1Fields.forEach(el => { heroData[el.name] = el.value; });
      goToStep(2);
    });
  }

  /* ── Retour ── */
  const backLink = form.querySelector('.step-back-link');
  if (backLink) {
    backLink.addEventListener('click', e => {
      e.preventDefault();
      goToStep(1);
    });
  }

  /* ── Formatage téléphone ── */
  const telInput = form.querySelector('[name="telephone"]');
  if (telInput) {
    telInput.addEventListener('input', function() {
      this.value = formatPhone(this.value);
    });
  }

  /* ── Sauvegarde localStorage ── */
  const emailInput = form.querySelector('[name="email"]');
  if (emailInput) {
    emailInput.addEventListener('input', function() {
      if (this.value) localStorage.setItem('si_email', this.value);
    });
  }
  const nomInput = form.querySelector('[name="nom"]');
  if (nomInput) {
    nomInput.addEventListener('input', function() {
      if (this.value) localStorage.setItem('si_nom', this.value);
    });
  }

  /* ── Soumission ── */
  form.addEventListener('submit', e => {
    e.preventDefault();
    if (heroIsSubmitting) return;

    const step2Fields = form.querySelectorAll('.form-step[data-step="2"] [required]');
    let ok = true;
    step2Fields.forEach(el => {
      const isValid =
        el.name === 'telephone'  ? isValidPhone(el.value) :
        el.name === 'email'      ? isValidEmail(el.value) :
        el.name === 'codepostal' ? /^[0-9]{5}$/.test(el.value.trim()) :
                                   el.value.trim() !== '';
      el.classList.toggle('error', !isValid);
      el.closest('.field')?.classList.toggle('has-err', !isValid);
      if (!isValid) ok = false;
    });
    if (!ok) return;

    step2Fields.forEach(el => { heroData[el.name] = el.value; });
    /* Champs optionnels step 2 (entreprise, description) */
    form.querySelectorAll('.form-step[data-step="2"] [name]:not([required])').forEach(el => {
      if (el.value.trim()) heroData[el.name] = el.value.trim();
    });

    const submitBtn = form.querySelector('[type="submit"]');
    heroIsSubmitting = true;
    submitBtn.classList.add('loading');
    submitBtn.innerHTML = '<span class="spinner"></span> Envoi en cours…';

    const data = {
      ...heroData,
      form_id:        'hero',
      step_completed: 3,
      date:           new Date().toLocaleString('fr-FR', { timeZone: 'Europe/Paris' }),
      source:         window.location.pathname,
      logo_url:       LOGO_URL
    };

    fetch(MAKE_WEBHOOK_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    })
    .catch(err => console.error('Webhook hero error:', err))
    .finally(() => {
      heroIsSubmitting = false;
      localStorage.setItem('si_submitted', '1');

      /* Personnalisation écran succès */
      const nom = heroData.nom || '';
      const tel    = (heroData.telephone || '').replace(/\s/g, '');
      const maskedTel = tel.length === 10
        ? tel.slice(0,2) + ' ** ** ** ' + tel.slice(8)
        : '';

      const titleEl  = successDiv?.querySelector('.success-title');
      const subEl    = successDiv?.querySelector('.success-sub');
      const shareEl  = successDiv?.querySelector('.success-share');

      if (titleEl) titleEl.textContent = (nom ? nom + ', votre' : 'Votre') + ' demande est envoyée !';
      if (subEl)   subEl.textContent   = 'Un expert vous rappelle sous 24h' + (maskedTel ? ' au ' + maskedTel : '') + '.';
      if (shareEl) {
        const sub  = encodeURIComponent('Diagnostic sécurité incendie gratuit — SecuriteIncendiePro.fr');
        const body = encodeURIComponent('Bonjour,\n\nJe viens d\'obtenir un diagnostic sécurité incendie gratuit sur SecuriteIncendiePro.fr.\nFaites-en autant en 60 secondes : https://securiteincendiepro.fr/\n\nCordialement');
        shareEl.href = 'mailto:?subject=' + sub + '&body=' + body;
      }

      /* Afficher succès */
      form.style.display = 'none';
      if (successDiv) successDiv.style.display = 'block';
      launchConfetti();
    });
  });
}

/* ══════════════════════════════════════════
   FAQ ACCORDION
══════════════════════════════════════════ */
function initFAQ() {
  const questions = document.querySelectorAll('.section-faq .faq-question');
  if (!questions.length) return;

  questions.forEach(btn => {
    btn.addEventListener('click', () => {
      const isOpen = btn.classList.contains('open');

      /* Fermer tout */
      questions.forEach(q => {
        q.classList.remove('open');
        q.setAttribute('aria-expanded', 'false');
        const ans = q.nextElementSibling;
        if (ans) ans.style.maxHeight = null;
      });

      /* Ouvrir si était fermé */
      if (!isOpen) {
        btn.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
        const ans = btn.nextElementSibling;
        if (ans) ans.style.maxHeight = ans.scrollHeight + 'px';
      }
    });
  });

  /* Première question ouverte par défaut */
  if (questions[0]) questions[0].click();
}

/* ══════════════════════════════════════════
   COMPTEURS ANIMÉS
══════════════════════════════════════════ */
function countUp(el, target, duration) {
  const start = performance.now();
  const suffix = el.dataset.suffix || '';
  function update(time) {
    const elapsed  = Math.min(time - start, duration);
    const progress = elapsed / duration;
    const eased    = 1 - Math.pow(1 - progress, 3); /* ease-out cubic */
    el.textContent = Math.round(eased * target).toLocaleString('fr-FR') + suffix;
    if (elapsed < duration) requestAnimationFrame(update);
  }
  requestAnimationFrame(update);
}

function initCounters() {
  const statsSection = document.querySelector('.testimonials-stats');
  if (!statsSection) return;

  const observer = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) {
      observer.disconnect();
      statsSection.querySelectorAll('.stat-value[data-target]').forEach(el => {
        const target = parseInt(el.dataset.target, 10);
        if (!isNaN(target)) countUp(el, target, 1800);
      });
    }
  }, { threshold: 0.3 });

  observer.observe(statsSection);
}

/* ══════════════════════════════════════════
   ANIMATIONS SCROLL (data-animate)
══════════════════════════════════════════ */
function initScrollAnimations() {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (prefersReduced) {
    document.querySelectorAll('[data-animate]').forEach(el => el.classList.add('is-visible'));
    return;
  }

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el    = entry.target;
        const delay = parseInt(el.dataset.delay || 0, 10);
        el.style.transitionDelay = delay + 'ms';
        el.classList.add('is-visible');
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('[data-animate]').forEach(el => observer.observe(el));
}

/* ══════════════════════════════════════════
   EXIT INTENT POPUP
══════════════════════════════════════════ */
function initExitIntent() {
  if (localStorage.getItem('si_submitted')) return;
  if (sessionStorage.getItem('si_exit_shown')) return;

  const popup = document.getElementById('exitPopup');
  if (!popup) return;

  /* Pré-remplir email */
  const savedEmail = localStorage.getItem('si_email');
  const emailInput = popup.querySelector('[name="email"]');
  if (savedEmail && emailInput) emailInput.value = savedEmail;

  let shown = false;
  function showPopup() {
    if (shown) return;
    if (localStorage.getItem('si_submitted')) return;
    if (sessionStorage.getItem('si_exit_shown')) return;
    shown = true;
    sessionStorage.setItem('si_exit_shown', '1');
    popup.classList.add('show');
    /* Re-pré-remplir email au moment du déclenchement */
    const email = localStorage.getItem('si_email');
    if (email && emailInput && !emailInput.value) emailInput.value = email;
  }

  /* Desktop: souris sort par le haut */
  document.addEventListener('mouseleave', e => {
    if (e.clientY < 10) showPopup();
  });

  /* Mobile: 45s d'inactivité */
  if (window.innerWidth < 751) {
    setTimeout(showPopup, 45000);
  }

  /* Fermeture */
  function closePopup() { popup.classList.remove('show'); }
  const overlay  = popup.querySelector('.exit-overlay');
  const closeBtn = popup.querySelector('.exit-close');
  const decline  = popup.querySelector('.exit-decline');
  if (overlay)  overlay.addEventListener('click', closePopup);
  if (closeBtn) closeBtn.addEventListener('click', closePopup);
  if (decline)  decline.addEventListener('click', e => { e.preventDefault(); closePopup(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closePopup(); });

  /* Formatage tél exit */
  const exitTel = popup.querySelector('[name="telephone"]');
  if (exitTel) {
    exitTel.addEventListener('input', function() {
      this.value = formatPhone(this.value);
    });
  }

  /* Soumission exit form */
  const exitForm = popup.querySelector('#formExit');
  if (exitForm) {
    let exitSubmitting = false;
    exitForm.addEventListener('submit', e => {
      e.preventDefault();
      if (exitSubmitting) return;

      const emailEl = exitForm.querySelector('[name="email"]');
      const telEl   = exitForm.querySelector('[name="telephone"]');
      let ok = true;

      const emailOk = isValidEmail(emailEl?.value || '');
      const telOk   = isValidPhone(telEl?.value   || '');
      emailEl?.classList.toggle('error', !emailOk);
      emailEl?.closest('.field')?.classList.toggle('has-err', !emailOk);
      telEl?.classList.toggle('error', !telOk);
      telEl?.closest('.field')?.classList.toggle('has-err', !telOk);
      if (!emailOk || !telOk) return;

      exitSubmitting = true;
      const submitBtn = exitForm.querySelector('.btn-cta');
      submitBtn.classList.add('loading');
      submitBtn.innerHTML = '<span class="spinner"></span> Envoi…';

      const data = {
        email:     emailEl.value,
        telephone: telEl.value,
        form_id:   'exit_intent',
        source:    window.location.pathname,
        date:      new Date().toLocaleString('fr-FR', { timeZone: 'Europe/Paris' }),
        logo_url:  LOGO_URL
      };

      fetch(MAKE_WEBHOOK_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      })
      .catch(err => console.error('Exit webhook error:', err))
      .finally(() => {
        exitSubmitting = false;
        localStorage.setItem('si_submitted', '1');
        exitForm.style.display = 'none';
        const exitSuccess = popup.querySelector('.exit-success');
        if (exitSuccess) exitSuccess.style.display = 'block';
        launchConfetti();
        setTimeout(closePopup, 3000);
      });
    });
  }
}

/* ══════════════════════════════════════════
   DOMContentLoaded
══════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', () => {

  /* ── Multi-step hero form ── */
  initHeroForm();

  /* ── Formulaires génériques (.lead-form) ── */
  document.querySelectorAll('.lead-form').forEach(form => {
    const btn     = form.querySelector('.btn-cta');
    const wrapper = form.closest('.final-form-card, .form-card, .sidebar-form');
    const success = wrapper ? wrapper.querySelector('.form-success') : null;

    const telInput = form.querySelector('[name="telephone"]');
    if (telInput) {
      telInput.addEventListener('input', function() {
        this.value = formatPhone(this.value);
      });
    }

    form.addEventListener('submit', e => {
      e.preventDefault();
      submitForm(form, btn, success);
    });
  });

  /* ── FAQ ── */
  initFAQ();

  /* ── Compteurs ── */
  initCounters();

  /* ── Animations scroll ── */
  initScrollAnimations();

  /* ── Live toast ── */
  const toasts = [
    { av:'ML', name:'Marc L. — Lyon',        txt:'vient de recevoir son diagnostic',     t:'il y a 1 min'  },
    { av:'SF', name:'Sophie F. — Paris',     txt:'a été mise en conformité',             t:'il y a 3 min'  },
    { av:'TR', name:'Thomas R. — Bordeaux',  txt:'a reçu 3 devis comparatifs',           t:'il y a 5 min'  },
    { av:'AC', name:'Amélie C. — Marseille', txt:'vient de demander un diagnostic ERP',  t:'il y a 7 min'  },
    { av:'PB', name:'Pierre B. — Toulouse',  txt:'a choisi son installateur APSAD',      t:'il y a 9 min'  },
    { av:'LD', name:'Laura D. — Nantes',     txt:'a sécurisé son commerce aujourd\'hui', t:'il y a 12 min' },
  ];
  let tIdx = 0;
  const toast = document.getElementById('liveToast');
  if (toast) {
    function showToast() {
      const n = toasts[tIdx];
      const av   = toast.querySelector('.toast-av');
      const name = toast.querySelector('.toast-name');
      const txt  = toast.querySelector('.toast-txt');
      const time = toast.querySelector('.toast-time');
      if (av)   av.textContent   = n.av;
      if (name) name.textContent = n.name;
      if (txt)  txt.textContent  = n.txt;
      if (time) time.textContent = n.t;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 4500);
      tIdx = (tIdx + 1) % toasts.length;
    }
    setTimeout(() => { showToast(); setInterval(showToast, 13000); }, 4000);
  }

  /* ── Confetti ── */
  window.launchConfetti = function() {
    const colors = ['#c0392b','#e67e22','#27ae60','#3498db','#f1c40f'];
    for (let i = 0; i < 70; i++) {
      setTimeout(() => {
        const el = document.createElement('div');
        el.className = 'confetti-piece';
        el.style.cssText = [
          'left:'             + Math.random() * 100 + 'vw',
          'background:'       + colors[Math.floor(Math.random() * colors.length)],
          'width:'            + (6 + Math.random() * 8) + 'px',
          'height:'           + (6 + Math.random() * 8) + 'px',
          'border-radius:'    + (Math.random() > 0.5 ? '50%' : '2px'),
          'animation-duration:' + (1.5 + Math.random() * 2) + 's'
        ].join(';');
        document.body.appendChild(el);
        setTimeout(() => el.remove(), 3500);
      }, i * 30);
    }
  };

  /* ── Bouton CTA header (Tâche 7) ── */
  const headerDevisBtn = document.getElementById('headerDevisBtn');
  if (headerDevisBtn) {
    window.addEventListener('scroll', () => {
      headerDevisBtn.style.display = window.scrollY > 300 ? 'flex' : 'none';
    }, { passive: true });
  }

  /* ── Exit intent (après délai court) ── */
  setTimeout(initExitIntent, 3000);

});
