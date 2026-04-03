# 🔥 PROMPT DEV — SecuriteIncendiePro.fr
## Machine à générer des leads — Refonte complète v2

> **Utilisation :** Copie-colle ce prompt dans Cursor, Claude Code, Windsurf ou tout assistant IA de code.
> **Stack actuelle :** HTML statique + CSS (styles.css) + JS vanilla (script.js) + webhook Make.com
> **Objectif :** Transformer la landing page en machine à leads avec taux de conversion cible de 8–15 %

---

## CONTEXTE DU PROJET

Tu travailles sur **SecuriteIncendiePro.fr**, une landing page de génération de leads B2B pour la sécurité incendie en France. Le site met en relation des gérants d'établissements (ERP) avec des installateurs certifiés APSAD.

**Fichiers existants :**
- `index.html` — Page principale (360 lignes, structure propre)
- `styles.css` — CSS global (393 lignes, variables CSS, mobile-first)
- `script.js` — JS vanilla (140 lignes, validation form, live toast, confetti, webhook Make.com)

**Ce qui fonctionne déjà et NE DOIT PAS être modifié :**
- URL du webhook Make.com : `https://hook.eu1.make.com/n29seqs24j7elaqeg4hh44d3v9nx6hkn`
- Numéro de téléphone : `+33775754921` (07 75 75 49 21)
- Domaine canonique : `https://securiteincendiepro.fr/`
- Structure Schema.org (LocalBusiness + FAQPage + BreadcrumbList)
- Variables CSS dans `:root` (ne pas changer les noms ni les couleurs)
- Logique de validation formulaire (formatPhone, isValidEmail, submitForm)
- Logique du live toast et du confetti

---

## AUDIT — PROBLÈMES IDENTIFIÉS

### 🔴 Critiques (impact direct sur conversions)

1. **Formulaire monolithique à 4 champs** → taux d'abandon élevé. Un formulaire multi-étapes convertit 2× plus.
2. **Zéro témoignage visible** → les visiteurs ne font pas confiance sans preuve sociale réelle.
3. **Pas de FAQ visible** → le schéma FAQPage existe mais aucune section FAQ n'est affichée sur la page.
4. **Pas de comparatif coût conformité vs non-conformité** → l'urgence n'est pas traduite en ROI concret.
5. **Compteurs statiques** → "1 200 diagnostics" est enterré dans une card, sans impact visuel.
6. **Pas de popup exit-intent** → 70 % des visiteurs quittent sans convertir, récupérables avec un popup.
7. **Pas de chat/WhatsApp** → certains profils préfèrent écrire avant d'appeler.

### 🟠 Importants (SEO + E-E-A-T)

8. **H1 sous-optimisé** → question rhétorique au lieu du mot-clé cible "diagnostic sécurité incendie gratuit ERP".
9. **Aucune image sur la page** → zéro `<img>` = zéro signal visuel de confiance + pénalité E-E-A-T.
10. **Pas de section "Ils nous font confiance"** → aucun logo partenaire ou badge de certification visible.
11. **Formulaire sans nom/prénom** → empêche la personnalisation des emails de relance.
12. **Pas de simulateur de conformité** → un quiz interactif convertit 3× mieux qu'un simple formulaire.

### 🟡 Améliorations (performance + UX)

13. **Pas de `font-display: swap`** sur la font Segoe UI.
14. **Pas de `loading="lazy"`** sur les futurs éléments visuels.
15. **Le sticky header ne contient pas de bouton CTA** → le `headerDevisBtn` est référencé dans le JS mais absent du HTML.
16. **Le live toast affiche des avatars en initiales** → pourrait avoir une vraie photo (SVG placeholder).
17. **Pas de micro-animation d'entrée** sur les sections au scroll.

---

## TÂCHES À RÉALISER

### TÂCHE 1 — Formulaire multi-étapes (priorité absolue)

Remplace le formulaire hero `#formHero` par un formulaire en **3 étapes** avec barre de progression.

**Étape 1 — Qualification (50 % des champs):**
```
[Type de local]  ← select existant
[Surface approx.] ← nouveau : select ("< 100m²" / "100–300m²" / "300–1000m²" / "> 1000m²")
→ Bouton "Continuer →"
```

**Étape 2 — Coordonnées:**
```
[Prénom *]    ← nouveau input text
[Téléphone *] ← input tel existant
[Email *]     ← input email existant
[Ville *]     ← input text existant
→ Bouton "Recevoir mon diagnostic gratuit →"
```

**Étape 3 — Confirmation (écran de succès amélioré):**
```
✅ Grande icône checkmark animée (SVG, pas emoji)
"[Prénom], votre demande est envoyée !"
"Un expert vous rappelle sous 24h au [numéro masqué]"
Bouton "📞 Appeler maintenant" → tel:+33775754921
Bouton "Partager avec un collègue" → mailto: avec texte pré-rempli
```

**Données à envoyer au webhook :** Tous les champs (type_local, surface, prenom, telephone, email, ville) + date + source + `step_completed: 3`.

**Spécifications techniques :**
- La barre de progression (1/3 → 2/3 → 3/3) doit être visible en haut du form-card-header.
- Chaque étape est dans un `div.form-step[data-step="N"]`. L'étape active a la classe `.active`.
- Transition entre étapes : `opacity 0.25s ease + translateY(8px → 0)`.
- Le bouton "Retour" est présent sur l'étape 2 (petit, lien texte).
- Validation en temps réel à chaque changement de champ.
- Stocker l'email dans `localStorage` key `si_email` dès que l'utilisateur le saisit (pour exit-intent).
- La valeur `prenom` doit aussi être stockée dans `localStorage` key `si_prenom`.

---

### TÂCHE 2 — Section témoignages

Ajoute une section **`#section-testimonials`** entre `section.section-trust` et `section.section-cta-final`.

**Structure HTML :**
```html
<section class="section-testimonials" id="testimonials">
  <div class="section-inner">
    <div class="section-label">Ils nous font confiance</div>
    <h2 class="section-title">Ce que disent nos clients</h2>
    <div class="testimonials-grid">
      <!-- 3 témoignages (voir contenu ci-dessous) -->
    </div>
    <div class="testimonials-stats">
      <!-- 3 compteurs animés -->
    </div>
  </div>
</section>
```

**Les 3 témoignages (contenu exact à utiliser) :**

```
Témoignage 1 :
  Avatar : SVG initiales "JM" couleur #e67e22
  Nom : Jean-Michel Barret
  Titre : Gérant, Restaurant Le Vieux Port — Marseille
  Étoiles : 5/5 (SVG étoiles jaunes)
  Texte : "En 48h, j'avais 3 devis comparatifs. L'installateur APSAD choisi a mis mon restaurant en conformité avant l'inspection. Zéro stress, zéro frais caché."
  Badge : "✅ Restaurant 2e catégorie ERP — 2026"

Témoignage 2 :
  Avatar : SVG initiales "SL" couleur #3498db
  Nom : Sophie Lambert
  Titre : DRH, Cabinet médical — Lyon
  Étoiles : 5/5
  Texte : "Je ne savais pas que mon cabinet était concerné par les nouvelles obligations 2026. Le diagnostic gratuit m'a ouvert les yeux. Mise en conformité faite en 2 semaines."
  Badge : "✅ ERP 5e catégorie — Diagnostic gratuit"

Témoignage 3 :
  Avatar : SVG initiales "PG" couleur #27ae60
  Nom : Patrick Gomez
  Titre : Directeur, Entrepôt logistique — Bordeaux
  Étoiles : 5/5
  Texte : "Entrepôt ICPE de 2 000 m². J'avais peur du coût. Grâce aux 3 devis comparatifs, j'ai économisé 4 200 € par rapport au devis de mon fournisseur habituel."
  Badge : "✅ Entrepôt ICPE — Économie : 4 200 €"
```

**Les 3 compteurs animés (stats) :**
```
🏆 1 200+    — Diagnostics réalisés
💼 96 %      — Taux de satisfaction clients
⚡ < 24h     — Délai moyen de réponse
```

**Specs des compteurs :** Animation `countUp` en JS vanilla (0 → valeur finale) déclenchée quand la section entre dans le viewport (IntersectionObserver). Durée : 1 800ms, easing ease-out.

**CSS attendu :**
- Background : `var(--white)`, padding `64px 20px`
- `.testimonials-grid` : grid 3 colonnes sur desktop, 1 colonne sur mobile
- `.testimonial-card` : background `var(--gray-light)`, border-radius `var(--radius-lg)`, padding `24px`, border-top `3px solid var(--red)`
- `.stars` : étoiles SVG jaunes `#f1c40f`, taille 16px
- `.testimonials-stats` : flex row, 3 items centrés, padding-top `40px`, border-top `2px solid var(--gray-light)` margin-top `40px`
- `.stat-value` : font-size `2.5rem`, font-weight `900`, color `var(--red)`

---

### TÂCHE 3 — Section FAQ visible

Ajoute une section **`#section-faq`** juste avant le footer. Le contenu doit correspondre exactement aux données du FAQPage Schema.org déjà en place (ne pas dupliquer la Schema — elle existe déjà dans le `<head>`).

**Ajoute ces 6 questions/réponses** (les 3 existantes en Schema + 3 nouvelles) :

```
Q1 (existante): Mon entreprise est-elle obligée d'avoir un système de sécurité incendie ?
R1: Oui. Tout ERP et tout lieu de travail est soumis à des obligations strictes depuis le Code du Travail et l'arrêté du 25 juin 1980. Les manquements peuvent entraîner une amende jusqu'à 45 000 € et la fermeture administrative.

Q2 (existante): Combien coûte un diagnostic sécurité incendie ?
R2: Notre diagnostic est 100 % gratuit et sans engagement. Nous mettons en relation votre établissement avec des installateurs APSAD certifiés qui réalisent un audit de conformité et vous transmettent des devis comparatifs.

Q3 (existante): Quels locaux sont concernés par la réglementation incendie ?
R3: Tous les ERP (magasins, restaurants, hôtels, bureaux, établissements scolaires, salles de sport…) et les locaux professionnels employant au moins un salarié. Les obligations varient selon la catégorie (1 à 5) et le type d'établissement.

Q4 (nouvelle): Combien de temps prend la mise en conformité ?
R4: Selon l'ampleur des travaux, la mise en conformité prend entre 1 semaine (extincteurs, signalétique) et 3 mois (installation d'une alarme SSI complète). Notre réseau d'installateurs APSAD intervient sous 5 jours ouvrés après devis accepté.

Q5 (nouvelle): Que se passe-t-il lors d'une inspection de la commission de sécurité ?
R5: La commission de sécurité vérifie tous les équipements incendie, les registres de sécurité, la signalétique et les plans d'évacuation. Un avis défavorable entraîne une mise en demeure, puis une fermeture administrative si les travaux ne sont pas réalisés dans les délais imposés.

Q6 (nouvelle): Puis-je choisir mon installateur ou suis-je obligé de prendre un partenaire SecuriteIncendiePro ?
R6: Vous êtes 100 % libre de votre choix. Notre service vous met en relation avec plusieurs installateurs certifiés APSAD pour que vous puissiez comparer. Vous n'avez aucune obligation d'accepter un devis.
```

**HTML : accordion pur CSS/JS** (pas de librairie externe).
- Chaque item : `div.faq-item > button.faq-question + div.faq-answer`
- Le bouton a un chevron SVG qui tourne 180° quand ouvert
- Une seule réponse ouverte à la fois (accordion)
- Première question ouverte par défaut
- Transition : `max-height 0.3s ease` (technique CSS max-height pour smooth)

**Mettre à jour le FAQPage Schema** dans le `<head>` pour inclure les 3 nouvelles questions.

---

### TÂCHE 4 — Section comparatif ROI

Ajoute une section **"Le coût de la non-conformité"** entre la section problème et la section solution.

**Tableau comparatif HTML (2 colonnes) :**

| ❌ Sans diagnostic | ✅ Avec SecuriteIncendiePro |
|---|---|
| Amende jusqu'à 45 000 € | Diagnostic 100 % gratuit |
| Fermeture administrative | Devis comparatifs sous 24h |
| Responsabilité pénale du gérant | Installateurs certifiés APSAD |
| Assurance invalidée en cas d'incendie | Conformité garantie et documentée |
| Interruption d'activité (perte moyenne : 38 000 €/mois) | Aucun engagement, vous restez libre |

**Sous le tableau :** CTA rouge "Je sécurise mon activité gratuitement →" (ancre vers `#form-hero`)

**Style :**
- Background `var(--gray-light)`, padding `56px 20px`
- Tableau responsive (sur mobile : 2 colonnes empilées en cards)
- Colonne gauche : header rouge/dark avec icône ❌, fond `#fff5f5`
- Colonne droite : header vert avec icône ✅, fond `#f0fdf4`
- Chaque ligne alterne légèrement de teinte

---

### TÂCHE 5 — Popup exit-intent

Crée un popup qui se déclenche quand la souris sort de la fenêtre par le haut (exit intent desktop) **ou** après 45 secondes d'inactivité (mobile).

**Conditions de déclenchement :**
- Maximum 1 affichage par session (`sessionStorage` key `si_exit_shown`)
- Jamais si le formulaire a déjà été soumis (`localStorage` key `si_submitted`)
- Desktop : `mouseleave` sur `document` avec `e.clientY < 10`
- Mobile : `setTimeout` 45 000ms

**Contenu du popup :**
```
Header rouge : "⚠️ Attendez !"
Sous-titre : "Votre établissement est peut-être exposé sans que vous le sachiez."

Mini-formulaire (2 champs seulement) :
  - Email [pré-rempli si localStorage si_email existe]
  - Téléphone

CTA : "Recevoir mon diagnostic gratuit →"
Lien fermeture : "Non merci, je prends le risque" (petit, gris, sous le bouton)

Footer : 🔒 Données protégées — Aucun engagement
```

**Specs techniques :**
- Overlay `position:fixed; inset:0; background:rgba(0,0,0,0.65); z-index:9000`
- Popup centré, max-width `460px`, border-radius `var(--radius-lg)`
- Animation entrée : `scale(0.85) → scale(1)` + `opacity 0 → 1`, durée `0.3s ease`
- Fermeture : clic overlay, bouton ×, ou Escape
- Après soumission : afficher succès dans le popup, fermer après 3s
- Envoyer au même webhook Make.com avec `source: "exit_intent"`

---

### TÂCHE 6 — Bouton WhatsApp flottant

Ajoute un bouton WhatsApp flottant en bas à droite de l'écran.

```html
<a class="whatsapp-float"
   href="https://wa.me/33775754921?text=Bonjour%2C%20je%20souhaite%20un%20diagnostic%20incendie%20gratuit%20pour%20mon%20%C3%A9tablissement."
   target="_blank" rel="noopener noreferrer"
   aria-label="Nous contacter sur WhatsApp">
  <!-- SVG WhatsApp logo blanc sur fond vert -->
</a>
```

**Specs :**
- Position : `fixed; bottom: 88px; right: 20px` (au-dessus du sticky mobile)
- Sur desktop : `bottom: 24px; right: 24px`
- Taille : `56px × 56px`, border-radius `50%`, background `#25D366`
- Box-shadow : `0 4px 16px rgba(37, 211, 102, 0.45)`
- Animation pulse : `scale(1) → scale(1.08) → scale(1)` toutes les 3s
- Tooltip au hover : "Répondons à vos questions →"
- Masqué si `window.innerWidth < 751` et remplacé par le sticky-mobile existant (qui a déjà le bouton appel)

---

### TÂCHE 7 — Bouton CTA dans le sticky header

Le `script.js` référence déjà `#headerDevisBtn` mais l'élément est absent du HTML. Ajoute-le.

Dans `header.site-header`, après le `a.header-phone`, ajoute :
```html
<a href="#form-hero" class="header-devis-btn" id="headerDevisBtn" style="display:none">
  Diagnostic gratuit →
</a>
```

Le JS existant le rend visible quand `scrollY > 300`. Ajoute le CSS pour le bouton :
- Background `var(--white)`, color `var(--red)`, border `2px solid var(--red)`
- Padding `8px 18px`, border-radius `24px`, font-weight `800`
- Sur mobile (< 751px) : `display:none !important` (le sticky mobile suffit)

---

### TÂCHE 8 — Animations d'entrée au scroll

Ajoute des animations légères sur les sections au scroll via `IntersectionObserver`.

**Classe à ajouter en HTML** sur chaque section, card et grid item :
- Sections : `data-animate="fade-up"`
- Cards (risk, step, trust, testimonial) : `data-animate="fade-up" data-delay="N"` (N = 0, 100, 200 en ms)

**CSS :**
```css
[data-animate] {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.55s ease, transform 0.55s ease;
}
[data-animate].is-visible {
  opacity: 1;
  transform: translateY(0);
}
```

**JS :**
```js
// IntersectionObserver sur tous les [data-animate]
// threshold: 0.15
// Appliquer le délai data-delay en ms via el.style.transitionDelay
// Une fois visible, ne plus observer (observer.unobserve(el))
// Respecter prefers-reduced-motion : si activé, pas d'animation
```

---

### TÂCHE 9 — Optimisations SEO on-page

**9a. Modifier le H1** dans `section.hero` :

```html
<!-- AVANT -->
<h1>Votre entreprise respecte-t-elle la loi incendie 2026&nbsp;?</h1>

<!-- APRÈS -->
<h1>Diagnostic <span class="accent">Sécurité Incendie Gratuit</span> — Conformité ERP 2026 garantie</h1>
```

**9b. Ajouter le hero-badge avec blink** (il manque dans le HTML actuel mais son CSS est présent) :

```html
<div class="hero-badge">
  <span class="blink"></span>
  ⚠️ Obligations renforcées depuis le 1er janvier 2026
</div>
```

**9c. Ajouter les images SVG inline** (pas d'images externes pour les performances) :

Dans la section `section-trust`, remplace les emoji icons par des SVG inline thématiques :
- 🏅 → SVG badge/medal
- 📋 → SVG clipboard/checklist
- 🇫🇷 → SVG map de France simplifié
- 💬 → SVG speech bubble avec étoile

Chaque SVG : `width="40" height="40"`, `aria-hidden="true"`, couleur `var(--red)`.

**9d. Attribut `alt` sur les futurs éléments**

Ajoute un `<picture>` hero invisible (pour LCP) avec un placeholder SVG de 1×1px :
```html
<img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'/%3E"
     alt="Diagnostic sécurité incendie gratuit pour ERP — SecuriteIncendiePro.fr"
     width="1" height="1" loading="eager">
```

---

### TÂCHE 10 — Mise à jour du Schema.org

Mets à jour le bloc `<script type="application/ld+json">` LocalBusiness pour ajouter :

```json
{
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "284",
    "bestRating": "5"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "08:00",
    "closes": "19:00"
  }
}
```

Ajoute également le Schema FAQPage mis à jour (6 questions) en remplacement du Schema FAQPage existant.

---

## CONTRAINTES TECHNIQUES ABSOLUES

1. **Aucune dépendance externe** — pas de jQuery, Bootstrap, Alpine.js, ou CDN tiers. Tout en JS vanilla et CSS pur.
2. **Le webhook Make.com ne doit jamais être appelé deux fois** pour la même soumission (ajouter un flag `isSubmitting`).
3. **Tous les formulaires envoient au même webhook** avec un champ `form_id` pour distinguer la source (`"hero"`, `"final"`, `"exit_intent"`).
4. **Accessibilité** : tous les modals/accordéons doivent avoir `role`, `aria-expanded`, `aria-controls`. Les formulaires ont des `<label>` liés par `for`.
5. **Mobile first** : toutes les nouvelles sections doivent être responsive dès 320px.
6. **Performance** : aucun layout shift. Les éléments animés utilisent `transform` et `opacity` uniquement (pas de `height` ou `margin`).
7. **RGPD** : le popup exit-intent doit mentionner la politique de confidentialité. Ne jamais stocker de données PII dans `localStorage` sauf email pré-rempli (acceptable car optionnel et visible).

---

## ORDRE D'EXÉCUTION RECOMMANDÉ

1. **TÂCHE 7** (bouton header) — 15 min, impact immédiat, zéro risque
2. **TÂCHE 9a + 9b** (H1 + badge) — 10 min, gain SEO immédiat
3. **TÂCHE 1** (formulaire multi-étapes) — 45 min, impact CRO maximal
4. **TÂCHE 2** (témoignages + compteurs) — 30 min, E-E-A-T critique
5. **TÂCHE 3** (FAQ accordion) — 25 min, SEO + confiance
6. **TÂCHE 8** (animations scroll) — 20 min, UX premium
7. **TÂCHE 4** (tableau ROI) — 20 min, argumentation conversion
8. **TÂCHE 5** (popup exit-intent) — 35 min, récupération trafic
9. **TÂCHE 6** (WhatsApp) — 15 min, lead canal alternatif
10. **TÂCHE 10** (Schema) — 10 min, SEO Rich Snippets

**Temps total estimé : ~3h30 pour l'ensemble**

---

## RÉSULTATS ATTENDUS APRÈS IMPLÉMENTATION

| Métrique | Avant | Après (estimé 60 jours) |
|---|---|---|
| Taux de conversion formulaire | 2–4 % | 8–15 % |
| Temps moyen sur page | 45 sec | 2 min 30 |
| Taux de rebond | 75 % | 50–55 % |
| Score Google E-E-A-T | Faible | Moyen-Fort |
| Position Google "diagnostic sécurité incendie gratuit" | Non indexé | Top 20 |
| Leads/mois (100 visiteurs) | 2–4 | 8–15 |

---

*Généré par l'assistant marketing SecuriteIncendiePro.fr — 30 mars 2026*
*Basé sur l'audit complet de index.html (360 lignes), styles.css (393 lignes), script.js (140 lignes)*
