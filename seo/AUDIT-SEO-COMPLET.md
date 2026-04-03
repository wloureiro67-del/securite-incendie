# AUDIT SEO COMPLET — SecuriteIncendiePro.fr
**Date d'audit :** 30 mars 2026
**Auditeur :** Analyse technique automatisée (Claude — Technical SEO Specialist)
**URL auditée :** https://securiteincendiepro.fr
**Secteur :** Génération de leads B2B — Sécurité incendie / Conformité ERP
**Hébergement :** Vercel (CDN global, datacenter CDG1 Paris)

---

## SCORE SEO GLOBAL : 61 / 100

| Categorie | Score | Statut |
|---|---|---|
| Crawlabilite & Indexation | 13/20 | Problemes critiques |
| SEO On-Page & Contenu | 14/20 | Bon avec lacunes |
| Schema.org / Donnees structurees | 8/10 | Bon |
| Securite & Headers HTTP | 5/10 | Insuffisant |
| Performance / Core Web Vitals | 10/15 | Estimations favorables |
| Mobile & UX | 7/10 | Bon |
| Maillage interne & Architecture | 4/15 | Critique |

---

## 1. CRAWLABILITE ET INDEXATION

### 1.1 Robots.txt

**Statut : PASS (partiel)**

```
User-agent: *
Allow: /

Sitemap: https://securiteincendiepro.fr/sitemap.xml
```

Points positifs :
- Fichier present et accessible sous 200
- Aucune directive de blocage abusive
- Reference au sitemap presente

Problemes identifies :
- Le sitemap reference dans robots.txt pointe vers `https://securiteincendiepro.fr/sitemap.xml` (sans www)
- Le domaine servi est `https://www.securiteincendiepro.fr` (avec www)
- Incohérence entre l'URL canonique servie et le sitemap declare
- Absence de blocage des pages a faible valeur SEO (ex: `/politique-confidentialite.html`, `/mentions-legales.html` pourraient etre en `noindex` plutot que bloquees en robots.txt)

Recommandation :
```
# Corriger robots.txt pour pointer sur la bonne version www
Sitemap: https://www.securiteincendiepro.fr/sitemap.xml

# Ou unifier le domaine canonical sur non-www et corriger le 307
```

---

### 1.2 Sitemap XML

**Statut : PASS (avec anomalies)**

Le sitemap XML est bien structure et contient 15 URLs. Analyse detail :

| URL | Priorite | Statut HTTP | Observation |
|---|---|---|---|
| / (homepage) | 1.0 | 200 | OK |
| /diagnostic-incendie-entreprise.html | 0.9 | 200 | OK |
| /extincteur-obligatoire-entreprise.html | 0.9 | 200 | OK |
| /normes-securite-incendie-erp.html | 0.9 | 200 | OK |
| /mise-aux-normes-incendie.html | 0.9 | 200 | OK |
| /securite-incendie-strasbourg.html | 0.8 | 200 | OK |
| /blog.html | 0.8 | 200 | OK |
| /articles/plan-intervention-incendie-obligatoire-erp-2026.html | 0.8 | 200 | OK |
| /articles/extincteur-obligatoire-entreprise-reglementation-2026.html | 0.8 | 200 | OK |
| /articles/norme-incendie-erp-guide-complet-obligations-2026.html | 0.8 | 200 | OK |
| /articles/installation-alarme-incendie.html | 0.7 | 200 | OK |
| /articles/mise-en-conformite-erp.html | 0.7 | 200 | OK |
| /articles/extincteurs-entreprise.html | 0.7 | 200 | OK |
| /mentions-legales.html | 0.3 | 200 | OK |
| /politique-confidentialite.html | 0.3 | 200 | OK |

Problemes identifies :
- Toutes les URLs du sitemap utilisent `https://securiteincendiepro.fr` (sans www)
- Mais le serveur redirige systematiquement vers `https://www.securiteincendiepro.fr`
- Les dates `lastmod` de certains articles (2026-04-07, 2026-04-14, 2026-04-21) sont **dans le futur** par rapport a l'audit (30 mars 2026) — dates fictives potentiellement penalisantes pour la credibilite
- Absence de sitemap image et sitemap de news
- Les URLs `.html` sont correctes mais il manque une version en extension courte (pages deja indexees, statu quo acceptable)

---

### 1.3 Chaines de Redirections — PROBLEME CRITIQUE

**Statut : FAIL**

La chaine de redirections documentee est la suivante :

```
Etape 1 : http://securiteincendiepro.fr/
          → 308 Permanent Redirect vers https://securiteincendiepro.fr/

Etape 2 : https://securiteincendiepro.fr/
          → 307 Temporary Redirect vers https://www.securiteincendiepro.fr/

Etape 3 : https://www.securiteincendiepro.fr/
          → 200 OK (page servie)
```

Problemes :
1. **Chaine a 3 sauts** depuis HTTP non-www — chaque saut consomme du budget crawl et ajoute de la latence
2. **Etape 2 utilise un 307 (temporaire)** au lieu d'un 308 (permanent) — Google ne transmet pas le PageRank sur un redirect temporaire de la meme facon qu'un permanent
3. **Incoherence canonique majeure** : la page servie sur `www.securiteincendiepro.fr` contient `<link rel="canonical" href="https://securiteincendiepro.fr/">` (sans www). Google recoit donc : "la version www est la vraie page MAIS le canonical pointe vers non-www qui redirige vers www". Signal contradictoire.
4. **Sitemap declare dans robots.txt** en non-www, alors que le contenu est sur www.

Solution immediate (Vercel) :
```javascript
// vercel.json — unifier sur www avec 301 permanent
{
  "redirects": [
    {
      "source": "/:path*",
      "destination": "https://www.securiteincendiepro.fr/:path*",
      "permanent": true
    }
  ]
}
```
Et corriger TOUS les canonicals pour pointer vers `https://www.securiteincendiepro.fr/`.

---

### 1.4 Meta Robots & Noindex

**Statut : PASS**

```html
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
```

- Directives correctes et completes
- `max-snippet:-1` : autorise Google a afficher des extraits longs (bon pour les rich snippets)
- `max-image-preview:large` : autorise les previews d'image dans les SERPs
- Aucune directive noindex involontaire detectee

---

## 2. SEO ON-PAGE ET QUALITE DU CONTENU

### 2.1 Balise Title

**Statut : PASS (optimisable)**

```
Diagnostic Sécurité Incendie Gratuit | Conformité ERP 2026 — SecuriteIncendiePro.fr
```

- Longueur : 86 caracteres — **TROP LONG** (Google tronque au-dela de ~60-65 caracteres soit ~580px)
- Mot-cle principal positionne en debut : correct
- Marque presente en fin : correct
- "2026" comme signal de fraicheur : correct
- Separateurs mixtes `|` et `—` : acceptable mais a uniformiser

Recommandation :
```
Diagnostic Sécurité Incendie Gratuit — Conformité ERP 2026
```
(59 caracteres — rentrera completement dans les SERPs)

---

### 2.2 Meta Description

**Statut : PASS**

```
Diagnostic sécurité incendie gratuit pour votre entreprise. Conformité ERP 2026 garantie
par des installateurs certifiés APSAD. Devis comparatifs sous 24h, sans engagement.
```

- Longueur : 172 caracteres — dans la plage recommandee (150-165 caracteres)
- Contient les mots-cles principaux
- Appel a l'action present ("devis comparatifs sous 24h")
- Differentiant present ("sans engagement")

Amelioration possible :
```
Obtenez un diagnostic sécurité incendie gratuit en 60 secondes. Installateurs APSAD
certifiés, devis comparatifs sous 24h. Conformité ERP 2026 garantie.
```

---

### 2.3 Balises H1 / H2 / H3

**Statut : PASS (structure a ameliorer)**

**H1 unique detecte :**
```
Diagnostic Sécurité Incendie Gratuit — Conformité ERP 2026 garantie
```
- Une seule H1 : correct
- Aligne avec le title : correct
- Inclut le mot-cle principal : correct

**H2 detectees (7) :**
```
1. Les risques d'un local non conforme
2. Le coût de la non-conformité
3. 3 étapes pour être en conformité
4. Des experts certifiés à votre service
5. Ce que disent nos clients
6. Protégez votre activité dès aujourd'hui
7. Tout ce que vous devez savoir
```

Problemes :
- Aucune H2 ne contient de mots-cles secondaires cibles comme "installation alarme incendie", "extincteur obligatoire", "SSI", "SSIAP"
- Certaines H2 sont trop generiques (n°5, n°6, n°7) — opportunites manquees
- La section FAQ n'utilise pas ses questions comme H3 interrogatives optimisees

**H3 detectees :**
```
Amende jusqu'à 45 000 € / Fermeture administrative / Responsabilité pénale
Remplissez le formulaire / Recevez votre diagnostic / Comparez et choisissez
```
- Pas de H3 contenant des mots-cles thematiques

Recommandations H2 optimisees :
```
"Qui est obligé d'avoir une installation SSI (alarme incendie) ?"
"Extincteurs obligatoires : que dit la réglementation pour les ERP ?"
"Comment choisir un installateur certifié APSAD ?"
"Témoignages de gérants de restaurants, commerces et hôtels conformes"
"FAQ — Diagnostic sécurité incendie gratuit pour entreprises"
```

---

### 2.4 Volume et Qualite du Contenu

**Statut : FAIL (pour une landing page B2B competitive)**

- **Nombre de mots : ~1 734** (HTML brut, JS exclu)
- Ce volume est insuffisant pour une page concurrencant des acteurs etablis sur des requetes comme "mise aux normes incendie entreprise" ou "diagnostic securite incendie gratuit"
- Les concurrents en premiere page (prestataires, institutions, editeurs de contenu) depassent generalement 2 500 a 4 500 mots sur ces requetes
- Le contenu est principalement oriente conversion (formulaires, CTA) au detriment de la substance informationnelle

Absence notable de :
- Texte expliquant les categories ERP (types J, L, M, N, O, P, R, S, T, U, V, W, X, Y) et leurs obligations specifiques
- Detail sur les normes NF S61-931, NF S61-932, NF S61-933 (SSI)
- Explication des certifications APSAD R1 (extincteurs), R4 (alarme), R7 (sprinklers), R13 (desenfumage)
- Tarification indicative des travaux de mise en conformite
- Zones geographiques couvertes (autres que Strasbourg)

---

### 2.5 Analyse E-E-A-T (Experience, Expertise, Autorite, Fiabilite)

**Statut : INSUFFISANT**

| Signal E-E-A-T | Present | Qualite |
|---|---|---|
| Expertise auteur / societe | Non | Aucune mention d'experts nommes |
| Experience concrete | Partiel | Temoignages presents mais sans details verifiables |
| Autorite externe | Non | Aucun lien externe entrant mentionne, pas de partenariats officiels |
| Fiabilite / Transparence | Partiel | Mentions legales presentes, RGPD mentionne |
| Numero de telephone | Oui | 07 75 75 49 21 |
| Adresse physique | Non | Absente (problematique pour un service B2B) |
| SIRET / Mentions legales completes | Non verifie | Page mentions-legales presente mais non analysee |
| Certifications affichees | Partiel | APSAD mentionne mais sans preuve (logo, lien CNPP) |

Recommandations E-E-A-T :
1. Ajouter une page "A propos" avec l'equipe, le responsable nomme, l'experience sectorielle
2. Afficher les logos des partenaires APSAD / certifications avec lien vers CNPP
3. Integrer un lien vers la liste officielle CNPP (cnpp.asso.fr) pour valider la demarche
4. Ajouter l'adresse physique du siege dans le footer et dans le schema LocalBusiness
5. Mentionner les references reglementaires exactes : Code du Travail Art. R4227-28 a R4227-57, Arrete du 25 juin 1980

---

### 2.6 Open Graph et Twitter Cards

**Statut : FAIL partiel**

```html
<!-- Present et correct -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="SecuriteIncendiePro.fr">
<meta property="og:title" content="Diagnostic Sécurité Incendie Gratuit | Conformité ERP 2026">
<meta property="og:description" content="...">
<meta property="og:url" content="https://securiteincendiepro.fr/">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="...">
<meta name="twitter:description" content="...">

<!-- MANQUANT — CRITIQUE pour les partages sociaux -->
<!-- og:image ABSENT -->
<!-- twitter:image ABSENT -->
```

L'absence d'`og:image` et de `twitter:image` signifie qu'un partage sur LinkedIn, Facebook ou Twitter affichera une vignette vide ou generique — impact direct sur le CTR des partages sociaux.

Recommandation :
```html
<meta property="og:image" content="https://www.securiteincendiepro.fr/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Diagnostic sécurité incendie gratuit — SecuriteIncendiePro.fr">
<meta name="twitter:image" content="https://www.securiteincendiepro.fr/og-image.jpg">
```
Creer une image 1200x630px avec le titre, le logo et un visuel d'ambiance (extincteur, alarme incendie, ERP).

---

## 3. SCHEMA.ORG ET DONNEES STRUCTUREES

### 3.1 Schemas implementes

**Statut : BON — a enrichir**

**Schema 1 : LocalBusiness + ProfessionalService**
```json
{
  "@type": ["LocalBusiness", "ProfessionalService"],
  "name": "SecuriteIncendiePro.fr",
  "telephone": "+33775754921",
  "priceRange": "Gratuit",
  "areaServed": { "@type": "Country", "name": "France" },
  "aggregateRating": { "ratingValue": "4.9", "reviewCount": "284" },
  "openingHoursSpecification": { ... },
  "hasOfferCatalog": { ... }
}
```

**Schema 2 : FAQPage — 6 questions**
Bien structure, aligne avec le contenu visible de la page.

**Problemes identifies :**
- `address` absent dans le LocalBusiness — champ obligatoire pour l'affichage en Knowledge Panel
- `@id` absent — recommendé pour une entite durable
- `logo` absent dans le LocalBusiness
- `sameAs` absent (liens vers profils Google Business Profile, LinkedIn)
- `url` pointe vers `https://securiteincendiepro.fr/` (non-www) alors que la page est servie sur www
- L'`aggregateRating` de 4.9/5 sur 284 avis ne correspond a aucune source externe verifiable visible — risque de penalite algorithmique (Google verifie la coherence des ratings avec les avis visibles sur la page)
- Les temoignages HTML ne sont pas marques en schema `Review` individuel

**Schemas manquants :**
- `WebSite` avec `SearchAction` (Sitelinks Search Box)
- `Organization` avec logo officiel
- `BreadcrumbList` sur les pages secondaires
- `Article` sur les articles de blog
- `HowTo` pour la section "3 etapes pour etre en conformite"
- `Service` detaille pour chaque type de service

**Schema HowTo recommande pour la section "3 etapes" :**
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Comment obtenir un diagnostic sécurité incendie gratuit",
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "Remplissez le formulaire",
      "text": "Indiquez le type de local et votre surface en 60 secondes."
    },
    {
      "@type": "HowToStep",
      "position": 2,
      "name": "Recevez votre diagnostic",
      "text": "Un installateur certifié APSAD vous contacte sous 24h."
    },
    {
      "@type": "HowToStep",
      "position": 3,
      "name": "Comparez et choisissez",
      "text": "Recevez plusieurs devis comparatifs sans engagement."
    }
  ]
}
```

---

## 4. SECURITE ET HEADERS HTTP

### 4.1 HTTPS

**Statut : PASS**
- HSTS present : `Strict-Transport-Security: max-age=63072000` (2 ans) — correct
- Redirect HTTP → HTTPS present (308 permanent) — correct

### 4.2 Headers de Securite Manquants

**Statut : FAIL — vulnerabilites importantes**

Headers presents :
```
Strict-Transport-Security: max-age=63072000   [OK]
Cache-Control: public, max-age=0, must-revalidate   [OK]
```

Headers ABSENTS (critiques pour la securite et la confiance SEO) :
```
X-Frame-Options                  → ABSENT  (risque de clickjacking)
X-Content-Type-Options           → ABSENT  (risque MIME sniffing)
Content-Security-Policy          → ABSENT  (risque XSS)
Referrer-Policy                  → ABSENT
Permissions-Policy               → ABSENT
X-XSS-Protection                 → ABSENT
```

Impact SEO : Google prend en compte la securite du site comme signal de confiance (Core Web Signals). Ces headers manquants n'affectent pas directement le classement mais nuisent a la note de securite et peuvent etre signales dans Search Console.

**Configuration Vercel recommandee (vercel.json) :**
```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Frame-Options", "value": "SAMEORIGIN" },
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()" },
        { "key": "Content-Security-Policy", "value": "default-src 'self'; script-src 'self' 'unsafe-inline' hook.eu1.make.com; connect-src 'self' hook.eu1.make.com;" }
      ]
    }
  ]
}
```

### 4.3 Exposition du Webhook Make.com

**Statut : ALERTE**

Le fichier `script.js` contient en clair :
```javascript
const MAKE_WEBHOOK_URL = 'https://hook.eu1.make.com/n29seqs24j7elaqeg4hh44d3v9nx6hkn';
```

Ce webhook est public, visible dans le source. N'importe qui peut envoyer des donnees fictives vers Make.com et generer des faux leads. Recommandations :
1. Ajouter une validation cote serveur (Vercel Edge Function ou API route)
2. Implementer un honeypot field dans les formulaires
3. Ajouter un token CSRF ou une validation reCAPTCHA v3

---

## 5. PERFORMANCE ET CORE WEB VITALS (ESTIMATION)

### 5.1 Analyse des signaux de performance

**Infrastructure :** Vercel CDN (datacenter CDG1 Paris) — excellente base technique

**Poids des ressources (mesure reelle) :**
```
HTML  :  41.2 KB (non compresse)
CSS   :  31.0 KB (non compresse, 1 fichier)
JS    :  18.9 KB (non compresse, 1 fichier)
Total :  91.1 KB (HTML + CSS + JS uniquement)
```

Note : aucune image reelle detectee dans le HTML (l'unique `<img>` est un SVG inline 1x1px). Cela signifie que le site n'a pas d'images hero — poids tres faible, mais impact negatif sur le LCP et la qualite E-E-A-T.

### 5.2 Estimation LCP (Largest Contentful Paint)

**Score estime : BON (<2.5s)**

Facteurs positifs :
- Aucune image de grande taille a charger
- CSS charge en `<head>` (render-blocking mais leger : 31 KB)
- JS charge avec `defer` : ne bloque pas le rendu initial
- Vercel CDN avec cache HIT (Age: 5-59s) — TTFB excellent
- Contenu SSR/statique — pas de rendu cote client requis

Facteurs de risque :
- Le CSS de 31 KB est render-blocking (pas de `<link rel="preload">`)
- L'element LCP probable est le texte du H1 — acceptable
- L'utilisation d'un `<img>` 1x1px en `loading="eager"` comme "placeholder LCP" est une technique douteuse qui pourrait signaler au navigateur un LCP element invisible

**Recommandation :**
```html
<!-- Dans <head> : precharger le CSS critique -->
<link rel="preload" href="styles.css" as="style">
<!-- Splitter le CSS : critical CSS inline + CSS non-critique en async -->
```

### 5.3 Estimation INP (Interaction to Next Paint)

**Score estime : BON (<200ms)**

- JavaScript de 18.9 KB — legers evenements (formulaires, FAQ accordion, animations scroll)
- Pas de framework lourd (React, Vue, Angular)
- Animations CSS via `transition: opacity 0.55s ease` — GPU-accelere
- Pas de librairies tierces lourdes detectees (pas de jQuery, pas de Bootstrap JS)

Risques potentiels :
- L'exit intent popup utilise des evenements `mouseleave` et `scroll` — si mal debounce, peut generer des repaints frequents
- Le confetti au submit (launchConfetti) peut etre couteux si non optimise

### 5.4 Estimation CLS (Cumulative Layout Shift)

**Score estime : RISQUE MODERE (0.05 - 0.15)**

Facteurs de risque :
- Les animations `[data-animate]` utilisent `opacity: 0; transform: translateY(24px)` — les elements demarrent invisibles et se deplacent a l'apparition. Si le contenu au-dessus se reajuste, cela peut provoquer des shifts.
- Le header sticky (`position: sticky; top: 0`) peut causer des CLS sur certains navigateurs mobiles si la hauteur n'est pas reservee
- Aucune dimension `width/height` definie sur les elements qui se chargent dynamiquement (formulaire multi-etapes)
- L'absence d'images avec dimensions explicites est un facteur neutre ici (pas d'images = pas de CLS d'image)

Recommandations :
```css
/* Reserver l'espace pour les elements animes pour eviter le CLS */
[data-animate] {
  opacity: 0;
  transform: translateY(24px);
  /* Ajouter : */
  will-change: opacity, transform;
  contain: layout style;
}

/* Header : reserver la hauteur avec min-height */
.site-header { min-height: 58px; }
```

### 5.5 Cache et CDN

- `X-Vercel-Cache: HIT` confirme que le CDN fonctionne correctement
- `Cache-Control: public, max-age=0, must-revalidate` — la valeur `max-age=0` signifie que chaque ressource est revalidee a chaque requete. Pour des assets statiques (CSS, JS), envisager :

```json
// vercel.json
{
  "headers": [
    {
      "source": "/styles.css",
      "headers": [{ "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }]
    },
    {
      "source": "/script.js",
      "headers": [{ "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }]
    }
  ]
}
```

---

## 6. MOBILE ET UX

### 6.1 Balise Viewport

**Statut : PASS**
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
Configuration standard et correcte.

### 6.2 Responsive Design

**Statut : PASS**

Media queries detectees dans styles.css :
```css
@media (max-width: 750px)       /* Mobile */
@media (min-width: 751px) and (max-width: 960px)  /* Tablette */
@media (min-width: 961px)       /* Desktop */
```
Approche Mobile-First confirmee par la structure CSS.

### 6.3 Favicon

**Statut : FAIL**

Aucune balise `<link rel="icon">` ou `<link rel="apple-touch-icon">` detectee dans le `<head>`. Absence de favicon = icone generique dans les onglets, degrade la perception de marque.

```html
<!-- A ajouter dans <head> -->
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png" sizes="180x180">
```

### 6.4 Polices Web

**Statut : PASS (partiel)**

- Pile de polices systeme utilisee : `'Segoe UI', system-ui, -apple-system, Arial, sans-serif`
- Aucun chargement Google Fonts ou police externe — excellent pour la performance
- `font-display: swap` applique dans body (mais c'est une propriete CSS valide uniquement dans `@font-face`, pas dans `body`) — **erreur technique benignes**

---

## 7. MAILLAGE INTERNE ET ARCHITECTURE

### 7.1 Liens Internes (Homepage)

**Statut : INSUFFISANT**

Liens internes detectes sur la homepage :
```
/                                    (logo)
#form-hero                           (CTA)
tel:+33775754921                     (telephone)
politique-confidentialite.html       (x2)
#form-final                          (CTA)
blog.html
extincteur-obligatoire-entreprise.html
normes-securite-incendie-erp.html
mise-aux-normes-incendie.html
diagnostic-incendie-entreprise.html
securite-incendie-strasbourg.html
mentions-legales.html
```

Problemes :
- Seulement 5 liens vers des pages de contenu — tres faible pour une homepage destinee a pousser le jus SEO
- Aucun lien vers les articles de blog (installation-alarme-incendie, mise-en-conformite-erp, extincteurs-entreprise)
- Aucun lien vers les pages articles avec date 2026 pourtant references dans le sitemap
- Les liens n'ont pas de textes d'ancre descriptifs optimises (pas de balises `<a>` visibles avec texte cle)

### 7.2 Architecture du Site

```
Homepage (/)
├── blog.html
│   ├── articles/installation-alarme-incendie.html
│   ├── articles/mise-en-conformite-erp.html
│   ├── articles/extincteurs-entreprise.html
│   ├── articles/plan-intervention-incendie-obligatoire-erp-2026.html
│   ├── articles/extincteur-obligatoire-entreprise-reglementation-2026.html
│   └── articles/norme-incendie-erp-guide-complet-obligations-2026.html
├── diagnostic-incendie-entreprise.html
├── extincteur-obligatoire-entreprise.html
├── normes-securite-incendie-erp.html
├── mise-aux-normes-incendie.html
├── securite-incendie-strasbourg.html
├── mentions-legales.html
└── politique-confidentialite.html
```

Structure globalement plate (2 niveaux max) — bon pour le budget crawl.

Problemes :
- Une seule page locale (`securite-incendie-strasbourg.html`) — opportunite massive de pages geographiques manquee
- Les articles de blog sont accessibles depuis blog.html mais pas depuis la homepage
- Absence de categories dans le blog
- Les pages de services (`diagnostic`, `extincteur`, `normes`, `mise-aux-normes`) ne se maillent pas entre elles

---

## 8. INDEXNOW ET PROTOCOLES D'INDEXATION ACCELEREE

### 8.1 IndexNow

**Statut : ABSENT**

- Aucun fichier de cle IndexNow detecte (`/[cle].txt`)
- Aucune reference a IndexNow dans robots.txt ou sitemap
- IndexNow accelere l'indexation sur Bing et Yandex — sur un site recemment cree, c'est un avantage significatif

Implementation (30 minutes de travail) :
1. Generer une cle sur https://www.bing.com/indexnow
2. Deposer le fichier de cle a la racine : `https://www.securiteincendiepro.fr/[votre-cle].txt`
3. Notifier les mises a jour via API :
```bash
curl -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json" \
  -d '{
    "host": "www.securiteincendiepro.fr",
    "key": "votre-cle",
    "urlList": ["https://www.securiteincendiepro.fr/"]
  }'
```

---

## 9. ANALYSE DES URLS ET PAGES SECONDAIRES

### 9.1 Structure des URLs

**Statut : BON**

- Toutes les URLs sont lisibles et descriptives
- Mots-cles presents dans les URLs
- Extension `.html` explicite (acceptable, coherent)
- Pas de parametres d'URL dynamiques
- Pas de majuscules dans les URLs
- Pas d'underscores (tirets utilises) — conforme aux recommandations Google

Seul bémol : les URLs `.html` ne sont pas "propres" au sens CMS headless moderne (pas de trailing slash, pas d'extension). Pas critique, mais une migration vers des URLs sans extension (`/diagnostic-incendie-entreprise` au lieu de `/diagnostic-incendie-entreprise.html`) ameliorerait l'apparence.

### 9.2 Page Strasbourg — Analyse de la Page Locale

La page `securite-incendie-strasbourg.html` est presente et retourne 200. Cette page locale cible une ville specifique. L'initiative est excellente mais tres sous-exploitee avec une seule ville.

---

## 10. OPPORTUNITES DE MOTS-CLES

### 10.1 Mots-cles Prioritaires (Cibles Immediates)

| Mot-cle | Vol. mensuel estime | Difficulte | Intention | Page cible |
|---|---|---|---|---|
| diagnostic securite incendie gratuit | 400-700 | Moyenne | Commerciale | Homepage |
| mise aux normes incendie entreprise | 500-900 | Haute | Commerciale | /mise-aux-normes-incendie.html |
| securite incendie erp | 600-1200 | Haute | Informationnelle | /normes-securite-incendie-erp.html |
| extincteur obligatoire entreprise | 800-1500 | Moyenne | Informationnelle | /extincteur-obligatoire-entreprise.html |
| norme incendie erp | 400-800 | Haute | Informationnelle | /normes-securite-incendie-erp.html |
| installateur alarme incendie certifie | 200-400 | Moyenne | Commerciale | /diagnostic-incendie-entreprise.html |
| conformite incendie entreprise | 300-600 | Haute | Commerciale | Homepage |
| commission securite erp | 200-500 | Moyenne | Informationnelle | Article blog |
| ssi alarme incendie | 300-600 | Haute | Informationnelle | Article blog |
| registre securite incendie | 300-500 | Faible | Informationnelle | Article blog |

### 10.2 Mots-cles Locaux (Expansion Geographique)

| Mot-cle | Vol. estime | Priorite |
|---|---|---|
| securite incendie Paris | 200-400 | Haute |
| securite incendie Lyon | 150-300 | Haute |
| securite incendie Marseille | 150-300 | Haute |
| securite incendie Bordeaux | 100-200 | Moyenne |
| securite incendie Toulouse | 100-200 | Moyenne |
| securite incendie Nantes | 80-150 | Moyenne |
| installateur APSAD [ville] | 50-150 / ville | Haute ROI |
| mise aux normes incendie [ville] | 50-200 / ville | Haute ROI |

### 10.3 Mots-cles Longue Traine (Blog)

| Mot-cle | Opportunite | Article recommande |
|---|---|---|
| plan evacuation incendie obligatoire | Oui | /articles/plan-evacuation-incendie.html |
| registre securite incendie que mettre dedans | Oui | /articles/registre-securite-incendie.html |
| desenfumage obligatoire erp | Oui | /articles/desenfumage-obligatoire-erp.html |
| formation evacuation incendie obligatoire | Oui | /articles/formation-evacuation.html |
| cout installation alarme incendie | Oui | /articles/prix-installation-alarme-incendie.html |
| difference ssi ssiap | Oui | /articles/ssi-vs-ssiap-difference.html |
| apsad r1 r4 r7 explication | Oui | /articles/certifications-apsad-r1-r4-r7.html |
| inspection commission securite que verifier | Oui | /articles/inspection-commission-securite.html |
| restauration rapide norme incendie | Oui | /articles/norme-incendie-restauration.html |
| hotel norme incendie categorie | Oui | /articles/norme-incendie-hotel.html |

---

## 11. ANALYSE CONCURRENTIELLE (ESTIMEE)

### 11.1 Acteurs Positionnables sur les Requetes Cibles

**Sur "diagnostic securite incendie gratuit" :**
- Prestataires regionaux APSAD avec anciennete domaine > 5 ans
- Pages service d'entreprises comme Securitas, Verisure (B2C), Initial Securite
- Comparateurs / annuaires : habitatpresto.com, travaux.com sur certaines requetes adjacentes
- Sites institutionnels : inrs.fr, service-public.fr (pour les requetes informationnelles pures)

**Sur "mise aux normes incendie entreprise" :**
- Forte competition des installateurs locaux avec pages geographiques
- Contenu editorial de sites specialises securite (securiteincendie.com, etc.)
- Pages entreprises de formation SSIAP

**Sur "extincteur obligatoire entreprise" :**
- Distributeurs d'extincteurs (Sicli, Total Securite, etc.) avec des guides detailles
- Sites d'information reglementaire (MSA, INRS, gouvernement.fr)

### 11.2 Avantages Concurrentiels du Site

- Proposition de valeur claire (diagnostic 100% gratuit, sans engagement)
- Positionnement sur APSAD clairement mentionne (differenciateur de confiance)
- Architecture technique solide (Vercel, SSR statique, mobile-first)
- FAQ schema implementee (potentiel rich snippet eleve)
- Plusieurs pages de service existantes (maillage possible a construire)

### 11.3 Desavantages vs Concurrents

- Domaine probablement recent (pas d'age de domaine eleve, liens entrants non mesures)
- Aucun backlink externe visible ou mention de la presse
- Pas de Google Business Profile apparent
- Presence sociale non identifiee
- Adresse physique absente (E-E-A-T faible)

---

## 12. SYNTHESE — TABLEAU RECAPITULATIF

| Element | Statut | Impact SEO | Priorite |
|---|---|---|---|
| Chaine de redirections HTTP → www | FAIL | Tres eleve | Critique |
| Mismatch canonical www / non-www | FAIL | Tres eleve | Critique |
| 307 (temporaire) au lieu de 301/308 | FAIL | Eleve | Critique |
| og:image / twitter:image absents | FAIL | Moyen | Haute |
| Favicon absent | FAIL | Faible | Haute |
| Headers securite manquants | FAIL | Moyen | Haute |
| Title trop long (86 chars) | WARNING | Moyen | Haute |
| Contenu insuffisant (~1734 mots) | FAIL | Tres eleve | Haute |
| E-E-A-T insuffisant | FAIL | Tres eleve | Haute |
| Maillage interne faible | FAIL | Eleve | Haute |
| IndexNow absent | FAIL | Faible-Moyen | Moyenne |
| og:image absent | FAIL | Moyen | Haute |
| Pages locales insuffisantes (1 seule ville) | FAIL | Tres eleve | Haute |
| Schema address absent | WARNING | Moyen | Moyenne |
| Schema HowTo manquant | WARNING | Moyen | Moyenne |
| Preload CSS absent | WARNING | Faible | Moyenne |
| Cache-Control max-age=0 sur assets | WARNING | Faible | Basse |
| font-display mal placee | WARNING | Tres faible | Basse |
| Webhook Make.com expose | SECURITE | Hors SEO | Haute |
| robots.txt sitemap URL (non-www) | WARNING | Moyen | Haute |
| Contenu H2 sans mots-cles | WARNING | Moyen | Moyenne |
| Schema aggregateRating sans avis visibles | WARNING | Moyen | Moyenne |

---

*Audit realise le 30 mars 2026. Ce document est a actualiser apres chaque modification majeure du site.*
