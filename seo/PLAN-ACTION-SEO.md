# PLAN D'ACTION SEO — SecuriteIncendiePro.fr
**Date :** 30 mars 2026
**Base :** Audit SEO Complet (AUDIT-SEO-COMPLET.md)
**Objectif :** Passer de 61/100 a 82/100 en 90 jours

---

## SYNTHESE EXECUTIF

Le site presente une base technique saine (Vercel, HTML statique, schemas implementes, mobile-first) mais souffre de trois problemes bloquants : une chaine de redirections incoherente avec un 307 temporaire, un mismatch canonique www/non-www, et un contenu trop mince pour rivaliser sur les requetes B2B cibles. Ces problemes doivent etre resolus en priorite absolue avant tout travail de contenu ou de netlinking.

---

## PRIORITE CRITIQUE — A corriger sous 72 heures

Ces problemes penalisent activement le site aujourd'hui. Chaque jour supplementaire = jus SEO perdu et signaux contradictoires envoyes a Google.

---

### C-1 : Corriger la chaine de redirections et le canonical www/non-www

**Probleme :** Le site redirige en 3 sauts (HTTP non-www → HTTPS non-www → HTTPS www), dont un 307 temporaire. Les canonicals disent "non-www" mais le contenu est servi sur "www". Google recoit des signaux contradictoires.

**Temps estime :** 1 heure

**Action :**

Etape 1 — Choisir la version canonique officielle. Recommandation : `https://www.securiteincendiepro.fr` (www) car c'est deja la version que le serveur sert.

Etape 2 — Modifier `vercel.json` pour unifier toutes les redirections en un seul 308 permanent :

```json
{
  "redirects": [
    {
      "source": "/:path*",
      "has": [{ "type": "host", "value": "securiteincendiepro.fr" }],
      "destination": "https://www.securiteincendiepro.fr/:path*",
      "permanent": true
    }
  ]
}
```

Etape 3 — Corriger TOUS les `<link rel="canonical">` dans TOUS les fichiers HTML :
```html
<!-- AVANT (incorrect) -->
<link rel="canonical" href="https://securiteincendiepro.fr/">

<!-- APRES (correct) -->
<link rel="canonical" href="https://www.securiteincendiepro.fr/">
```

Etape 4 — Corriger le sitemap.xml : remplacer toutes les URLs `https://securiteincendiepro.fr/...` par `https://www.securiteincendiepro.fr/...`

Etape 5 — Corriger robots.txt :
```
User-agent: *
Allow: /

Sitemap: https://www.securiteincendiepro.fr/sitemap.xml
```

Etape 6 — Corriger le schema LocalBusiness : le champ `"url"` doit pointer vers `https://www.securiteincendiepro.fr/`

Etape 7 — Corriger le schema FAQPage : verifier que `og:url` est aussi en www.

**Verification apres correction :**
```bash
curl -I "http://securiteincendiepro.fr/"
# Attendu : 301 ou 308 → https://www.securiteincendiepro.fr/

curl -I "https://securiteincendiepro.fr/"
# Attendu : 301 ou 308 → https://www.securiteincendiepro.fr/

curl -I "https://www.securiteincendiepro.fr/"
# Attendu : 200 OK
```

**Impact prevu :** Consolidation du PageRank, clarification des signaux d'indexation, elimination du 307 penalisant.

---

### C-2 : Corriger les dates futures dans le sitemap

**Probleme :** Plusieurs articles ont des `<lastmod>` dans le futur (07/04/2026, 14/04/2026, 21/04/2026) alors que nous sommes le 30/03/2026. Google detecte et ignore les dates incohérentes.

**Temps estime :** 15 minutes

**Action :** Mettre toutes les `<lastmod>` a la date de publication reelle ou a aujourd'hui.

```xml
<!-- AVANT -->
<lastmod>2026-04-07</lastmod>

<!-- APRES -->
<lastmod>2026-03-30</lastmod>
```

Si les articles ne sont pas encore publies, les retirer du sitemap jusqu'a leur publication effective.

---

### C-3 : Securiser le webhook Make.com expose

**Probleme :** L'URL complete du webhook Make.com est lisible dans `script.js`. N'importe qui peut envoyer des faux leads.

**Temps estime :** 2-4 heures

**Action A (simple) — Ajouter un champ honeypot :**
```html
<!-- Dans chaque formulaire, champ invisible pour les bots -->
<input type="text" name="website" style="display:none" tabindex="-1" autocomplete="off">
```
```javascript
// Dans le handler de soumission, rejeter si honeypot rempli
if (data.website && data.website.trim() !== '') return;
```

**Action B (recommandee) — Passer par une Vercel Edge Function :**
```javascript
// /api/submit.js (Vercel serverless function)
export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).end();
  const { prenom, telephone, email, ville, type_local } = req.body;
  // Validation cote serveur
  if (!prenom || !telephone || !email) return res.status(400).json({ error: 'Champs manquants' });
  // Appel vers Make.com cote serveur (non expose au client)
  await fetch(process.env.MAKE_WEBHOOK_URL, { method: 'POST', body: JSON.stringify(req.body) });
  return res.status(200).json({ success: true });
}
```
```javascript
// Dans script.js, appeler /api/submit au lieu de Make directement
fetch('/api/submit', { method: 'POST', body: JSON.stringify(data) })
```

---

## PRIORITE HAUTE — A realiser dans les 2 semaines

---

### H-1 : Ajouter og:image et twitter:image

**Probleme :** Les partages sur LinkedIn, Facebook, et Twitter affichent une vignette vide.

**Temps estime :** 2 heures (creation de l'image + integration)

**Action :**

Creer une image OG 1200x630px avec :
- Fond : degrade sombre du site (`#1a252f` vers `#2d1010`)
- Titre en blanc : "Diagnostic Sécurité Incendie Gratuit"
- Sous-titre : "Conformité ERP 2026 — Installateurs APSAD certifiés"
- Logo SecuriteIncendiePro.fr en haut a droite
- Visuel : icone d'extincteur ou d'alarme incendie en rouge
- Sauvegarder en JPG optimise (< 200 KB) : `/og-image.jpg`

Integrer dans toutes les pages :
```html
<meta property="og:image" content="https://www.securiteincendiepro.fr/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Diagnostic sécurité incendie gratuit — SecuriteIncendiePro.fr">
<meta name="twitter:image" content="https://www.securiteincendiepro.fr/og-image.jpg">
```

---

### H-2 : Ajouter le favicon

**Probleme :** Aucun favicon — onglets navigateur sans icone, degrade la perception de marque.

**Temps estime :** 30 minutes

**Action :**
1. Creer un favicon SVG simple : flamme rouge sur fond sombre, ou ecusson avec les lettres "SI"
2. Generer les formats via https://realfavicongenerator.net
3. Integrer dans le `<head>` de toutes les pages :
```html
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16">
<link rel="apple-touch-icon" href="/apple-touch-icon.png" sizes="180x180">
<link rel="manifest" href="/site.webmanifest">
```

---

### H-3 : Corriger le Title de la homepage (trop long)

**Probleme :** 86 caracteres — tronque dans les SERPs Google.

**Temps estime :** 5 minutes

**Action :**
```html
<!-- AVANT -->
<title>Diagnostic Sécurité Incendie Gratuit | Conformité ERP 2026 — SecuriteIncendiePro.fr</title>

<!-- APRES -->
<title>Diagnostic Sécurité Incendie Gratuit — Conformité ERP 2026</title>
```
(59 caracteres — s'affiche en entier dans les SERPs)

Note : La marque n'est plus dans le title, mais Google l'affiche de toute facon depuis le favicon/nom de domaine. Priorite : mot-cle + promesse > marque dans le title.

---

### H-4 : Ajouter les headers de securite HTTP

**Probleme :** X-Frame-Options, X-Content-Type-Options, Content-Security-Policy manquants.

**Temps estime :** 1 heure

**Action — Ajouter dans vercel.json :**
```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Frame-Options", "value": "SAMEORIGIN" },
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()" }
      ]
    }
  ]
}
```

---

### H-5 : Enrichir le contenu de la homepage (+1 500 mots)

**Probleme :** 1 734 mots actuels — insuffisant pour les requetes B2B concurrentielles cibles.

**Temps estime :** 4-6 heures de redaction

**Sections a ajouter dans l'ordre d'insertion :**

**Section A — Apres le Hero, avant "Les risques" :**
```
TITRE : "Qui est concerné par la réglementation incendie ?"
CONTENU (~300 mots) :
Tout établissement recevant du public (ERP) et tout local de travail
employant au moins un salarié est soumis à des obligations légales strictes.

Les 5 catégories d'ERP selon l'effectif :
- 1re catégorie : > 1 500 personnes
- 2e catégorie : 701 à 1 500 personnes
- 3e catégorie : 301 à 700 personnes
- 4e catégorie : ≤ 300 personnes (hors 5e cat.)
- 5e catégorie : en dessous des seuils d'admission

Les types d'établissements (J, L, M, N, O, P, R, S, T, U, V, W, X, Y)
et leurs obligations spécifiques...

[Continuer avec le detail des obligations selon les types]
```

**Section B — Apres les "3 etapes", avant "Experts certifies" :**
```
TITRE : "Les certifications APSAD : garantie de qualité"
CONTENU (~250 mots) :
APSAD R1 : Extinction (extincteurs portatifs)
APSAD R4 : Détection automatique d'incendie (alarme SSI)
APSAD R7 : Systèmes sprinklers
APSAD R13 : Désenfumage
APSAD F1 : Maintenance extincteurs

Pourquoi exiger une certification APSAD de votre installateur...
```

**Section C — Avant le FAQ (ou apres les temoignages) :**
```
TITRE : "Nos zones d'intervention en France"
CONTENU (~200 mots + liste de villes avec liens) :
Notre réseau couvre l'ensemble du territoire français :
[Paris et Île-de-France] — [Lyon et Auvergne-Rhône-Alpes] —
[Marseille et PACA] — [Toulouse et Occitanie] — etc.
+ lien vers chaque page locale
```

---

### H-6 : Creer 10 pages locales (strategy geo-SEO)

**Probleme :** Une seule page locale (Strasbourg) — opportunite massive.

**Temps estime :** 2 jours (creation template + declinaison)

**Pages a creer (Priorite Haute) :**

```
/securite-incendie-paris.html
/securite-incendie-lyon.html
/securite-incendie-marseille.html
/securite-incendie-bordeaux.html
/securite-incendie-toulouse.html
/securite-incendie-nantes.html
/securite-incendie-lille.html
/securite-incendie-nice.html
/securite-incendie-rennes.html
/securite-incendie-montpellier.html
```

**Template de title pour chaque page :**
```
Sécurité Incendie [Ville] — Diagnostic Gratuit ERP | SecuriteIncendiePro.fr
```
Exemple Paris :
```
Sécurité Incendie Paris — Diagnostic Gratuit ERP | SecuriteIncendiePro.fr
```

**Template de meta description :**
```
Diagnostic sécurité incendie gratuit à [Ville]. Installateurs APSAD certifiés
dans [département]. Conformité ERP 2026, devis comparatifs sous 24h.
```

**Structure de chaque page locale (~1 200 mots) :**
```
H1 : Diagnostic Sécurité Incendie à [Ville] — Gratuit et Sans Engagement
H2 : Pourquoi faire appel à un installateur APSAD à [Ville] ?
H2 : Les ERP à [Ville] et leurs obligations légales
H2 : Notre réseau d'installateurs certifiés à [Ville] et en [Département]
H2 : Obtenez votre devis de mise en conformité à [Ville]
[Formulaire de lead]
H2 : FAQ — Sécurité incendie à [Ville]
```

**Canonical :** chaque page pointe sur elle-meme (pas de canonical vers homepage).

**Maillage :** Chaque page locale se lie a la homepage et aux 2-3 pages de services les plus pertinentes.

---

### H-7 : Ameliorer les H2 avec des mots-cles

**Probleme :** Les H2 actuelles ne contiennent aucun mot-cle secondaire cible.

**Temps estime :** 30 minutes

**Action — Remplacer les H2 generiques :**

| H2 Actuelle | H2 Recommandee |
|---|---|
| "Les risques d'un local non conforme" | "Risques juridiques et financiers d'un ERP non conforme à la réglementation incendie" |
| "Le coût de la non-conformité" | "Amende, fermeture administrative : le vrai coût de la non-conformité incendie" |
| "3 étapes pour être en conformité" | "Comment obtenir votre diagnostic de conformité incendie en 3 étapes" |
| "Des experts certifiés à votre service" | "Des installateurs certifiés APSAD R1, R4, R7 dans toute la France" |
| "Ce que disent nos clients" | "Gérants d'ERP, restaurants et hôtels : leurs retours sur notre service" |
| "Tout ce que vous devez savoir" | "FAQ — Diagnostic sécurité incendie gratuit pour entreprises et ERP" |

---

### H-8 : Renforcer le E-E-A-T

**Temps estime :** 3 heures

**Actions :**

1. Ajouter une page `/a-propos.html` :
```
Title : À Propos — SecuriteIncendiePro.fr | Notre Mission
Meta  : SecuriteIncendiePro.fr connecte les entreprises françaises avec des
        installateurs APSAD certifiés depuis [année]. Découvrez notre mission.
H1   : À propos de SecuriteIncendiePro.fr
H2   : Notre mission : rendre la conformité incendie accessible à tous
H2   : Notre réseau d'installateurs certifiés APSAD
H2   : Les fondateurs et l'equipe
H2   : Contactez-nous
```

2. Ajouter l'adresse physique dans le footer et dans le schema LocalBusiness :
```json
"address": {
  "@type": "PostalAddress",
  "streetAddress": "[votre adresse]",
  "postalCode": "[code postal]",
  "addressLocality": "[ville]",
  "addressCountry": "FR"
}
```

3. Afficher les logos APSAD / CNPP avec lien vers cnpp.asso.fr

4. Ajouter dans le schema LocalBusiness :
```json
"sameAs": [
  "https://www.linkedin.com/company/securiteincendiepro",
  "https://www.facebook.com/securiteincendiepro"
]
```

5. Lier les references reglementaires dans le contenu :
```html
<a href="https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000290033"
   rel="noopener" target="_blank">
   Arrêté du 25 juin 1980 (ERP)
</a>
```

---

## PRIORITE MOYENNE — A realiser en semaines 3-6

---

### M-1 : Implementer IndexNow

**Temps estime :** 30 minutes

```bash
# 1. Generer une cle sur https://www.bing.com/indexnow
# 2. Creer le fichier de verification (ex: abc123.txt avec "abc123" comme contenu)
# 3. Deposer a la racine du site : /abc123.txt

# 4. Notifier via API a chaque nouvelle publication
curl -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json" \
  -d '{
    "host": "www.securiteincendiepro.fr",
    "key": "abc123",
    "urlList": [
      "https://www.securiteincendiepro.fr/",
      "https://www.securiteincendiepro.fr/nouveau-article.html"
    ]
  }'
```

---

### M-2 : Ajouter le schema HowTo pour les "3 etapes"

**Temps estime :** 20 minutes

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Comment obtenir un diagnostic sécurité incendie gratuit",
  "description": "Obtenez un diagnostic de conformité ERP en 3 étapes simples",
  "totalTime": "PT2M",
  "tool": [{ "@type": "HowToTool", "name": "Formulaire en ligne (60 secondes)" }],
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "Remplissez le formulaire",
      "text": "Indiquez le type de local (restaurant, commerce, bureau…), votre surface et vos coordonnées. 60 secondes suffisent."
    },
    {
      "@type": "HowToStep",
      "position": 2,
      "name": "Recevez votre diagnostic",
      "text": "Un installateur certifié APSAD de notre réseau vous contacte sous 24h ouvrés pour planifier votre audit de conformité gratuit."
    },
    {
      "@type": "HowToStep",
      "position": 3,
      "name": "Comparez et choisissez",
      "text": "Recevez plusieurs devis comparatifs sans engagement. Vous choisissez librement l'installateur qui vous convient."
    }
  ]
}
```

---

### M-3 : Ajouter le schema WebSite avec SearchAction

**Temps estime :** 10 minutes

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "SecuriteIncendiePro.fr",
  "url": "https://www.securiteincendiepro.fr/",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://www.securiteincendiepro.fr/blog.html?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

---

### M-4 : Optimiser les meta descriptions des pages secondaires

**Temps estime :** 1 heure

Pages a corriger / optimiser :

**Page diagnostic :**
```
Title : Diagnostic Incendie Entreprise Gratuit — Audit ERP | SecuriteIncendiePro.fr
Meta  : Faites réaliser gratuitement votre diagnostic incendie par un expert APSAD.
        Audit complet de conformité ERP, rapport détaillé, devis sous 24h.
```

**Page extincteur :**
```
Title : Extincteur Obligatoire en Entreprise — Réglementation ERP 2026
Meta  : Quels extincteurs sont obligatoires dans votre entreprise ? Type, nombre,
        maintenance : tout ce que dit la réglementation incendie 2026.
```

**Page normes ERP :**
```
Title : Normes Sécurité Incendie ERP — Obligations Légales 2026
Meta  : Obligations de sécurité incendie en ERP : alarme SSI, extincteurs,
        désenfumage, signalétique. Guide complet par type et catégorie d'ERP.
```

**Page mise aux normes :**
```
Title : Mise aux Normes Incendie Entreprise — Devis Gratuit 2026
Meta  : Mettez votre entreprise aux normes incendie avec un installateur APSAD
        certifié. Devis gratuit, intervention sous 5 jours ouvrés.
```

---

### M-5 : Enrichir le maillage interne

**Temps estime :** 2 heures

**Regles de maillage a implementer :**

1. Depuis la homepage : ajouter des liens contextuels vers les articles de blog dans le corps du texte
```html
<!-- Exemple dans le texte de la section "Risques" -->
<p>...une amende pouvant atteindre 45 000 €.
<a href="/articles/mise-en-conformite-erp.html">Découvrez notre guide complet sur la mise en conformité ERP</a>...</p>
```

2. Depuis chaque article de blog : lien de retour vers la homepage et vers 2 pages de services :
```html
<!-- En bas de chaque article -->
<div class="article-cta">
  <h3>Besoin d'un diagnostic gratuit ?</h3>
  <a href="/">Obtenez votre diagnostic sécurité incendie</a>
  <a href="/diagnostic-incendie-entreprise.html">En savoir plus sur le diagnostic</a>
</div>
```

3. Depuis les pages de services : se lier entre elles :
```
diagnostic-incendie-entreprise.html → extincteur-obligatoire-entreprise.html
extincteur-obligatoire-entreprise.html → mise-aux-normes-incendie.html
normes-securite-incendie-erp.html → diagnostic-incendie-entreprise.html
```

4. Depuis les pages locales : se lier a la page correspondante de services :
```
securite-incendie-paris.html → diagnostic-incendie-entreprise.html
securite-incendie-paris.html → mise-aux-normes-incendie.html
```

---

### M-6 : Implementer le preload CSS et optimiser le cache

**Temps estime :** 30 minutes

```html
<!-- Dans <head>, avant la balise <link rel="stylesheet"> -->
<link rel="preload" href="styles.css" as="style">
<link rel="preconnect" href="https://hook.eu1.make.com">
```

```json
// vercel.json — longue duree de cache pour assets versiones
{
  "headers": [
    {
      "source": "/styles.css",
      "headers": [{ "key": "Cache-Control", "value": "public, max-age=86400, stale-while-revalidate=604800" }]
    },
    {
      "source": "/script.js",
      "headers": [{ "key": "Cache-Control", "value": "public, max-age=86400, stale-while-revalidate=604800" }]
    }
  ]
}
```

---

### M-7 : Schema Article sur les articles de blog

**Temps estime :** 1 heure (template a appliquer a tous les articles)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Titre de l'article]",
  "description": "[Meta description]",
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD]",
  "author": {
    "@type": "Organization",
    "name": "SecuriteIncendiePro.fr",
    "url": "https://www.securiteincendiepro.fr/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "SecuriteIncendiePro.fr",
    "logo": {
      "@type": "ImageObject",
      "url": "https://www.securiteincendiepro.fr/logo.png"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.securiteincendiepro.fr/articles/[slug].html"
  },
  "image": "https://www.securiteincendiepro.fr/articles/[slug]-og.jpg"
}
```

---

## PRIORITE BASSE — A realiser a partir de la semaine 7

---

### B-1 : Creer 5 nouveaux articles de blog

**Temps estime :** 3-5 jours

**Articles prioritaires avec leurs specifications :**

**Article 1 :**
```
Fichier  : /articles/registre-securite-incendie-obligatoire.html
Title    : Registre de Sécurité Incendie : Que Doit-il Contenir en 2026 ?
Meta     : Le registre de sécurité incendie est obligatoire pour tous les ERP.
           Découvrez ce qu'il doit contenir, comment le tenir et qui le contrôle.
Cible    : "registre securite incendie" (~400 rech/mois)
Longueur : 1 800 mots
H2       :
  - Qu'est-ce que le registre de sécurité incendie ?
  - Contenu obligatoire : les 8 rubriques indispensables
  - Qui doit tenir le registre et comment ?
  - Que risquez-vous en cas de registre absent ou incomplet ?
  - Registre papier ou numérique : que dit la réglementation ?
  - FAQ — Registre de sécurité incendie
CTA      : Formulaire de lead en bas de page
```

**Article 2 :**
```
Fichier  : /articles/prix-installation-alarme-incendie.html
Title    : Prix d'une Installation d'Alarme Incendie en 2026 — Guide Complet
Meta     : Combien coûte une alarme incendie pour un ERP ou local professionnel ?
           Fourchettes de prix, facteurs de variation, aides disponibles.
Cible    : "cout installation alarme incendie" / "prix alarme incendie" (~600 rech/mois)
Longueur : 2 000 mots
H2       :
  - Les différents types de systèmes d'alarme incendie (SSI)
  - Fourchettes de prix selon la surface et le type d'ERP
  - Ce qui fait varier le prix : équipements, main d'œuvre, certification
  - Alarme incendie : obligation légale ou option ?
  - Comment obtenir plusieurs devis et les comparer ?
  - FAQ — Prix alarme incendie
```

**Article 3 :**
```
Fichier  : /articles/norme-incendie-restaurant.html
Title    : Norme Incendie Restaurant 2026 : Obligations par Catégorie ERP
Meta     : Restaurant, bar, brasserie : quelles sont vos obligations incendie ?
           ERP de type N — extincteurs, alarme, désenfumage, formation SSIAP.
Cible    : "norme incendie restaurant" / "securite incendie restaurant" (~500 rech/mois)
Longueur : 1 800 mots
H2       :
  - Les restaurants : ERP de type N, quelles obligations ?
  - Extincteurs obligatoires dans un restaurant
  - Alarme incendie : à partir de quand est-elle obligatoire ?
  - Désenfumage de cuisine : règles spécifiques
  - Formation du personnel : obligation SSIAP
  - Checklist avant la commission de sécurité
```

**Article 4 :**
```
Fichier  : /articles/inspection-commission-securite-erp.html
Title    : Commission de Sécurité ERP : Comment Se Préparer à l'Inspection ?
Meta     : Visite de la commission de sécurité : ce qu'elle vérifie, comment s'y
           préparer et éviter l'avis défavorable. Guide pratique 2026.
Cible    : "commission securite erp" / "inspection securite erp" (~400 rech/mois)
Longueur : 2 000 mots
```

**Article 5 :**
```
Fichier  : /articles/certifications-apsad-r1-r4-r7.html
Title    : Certifications APSAD R1, R4, R7 : Ce Que Garantissent-elles ?
Meta     : APSAD R1 (extincteurs), R4 (alarme), R7 (sprinklers) : signification
           et pourquoi choisir un installateur certifié APSAD pour votre ERP.
Cible    : "APSAD R4" / "certification APSAD installateur" (~300 rech/mois)
Longueur : 1 500 mots
```

---

### B-2 : Creer un Google Business Profile

**Temps estime :** 1 heure + 2 semaines de verification

**Actions :**
1. Aller sur https://business.google.com
2. Creer la fiche avec l'adresse physique du siege
3. Categorie principale : "Service d'installation de systèmes de sécurité"
4. Categories secondaires : "Service de protection incendie", "Installateur d'alarmes"
5. Ajouter les horaires, le telephone, le site web
6. Publier des photos du service, de l'equipe, des certifications
7. Synchroniser l'URL GBP avec le schema `sameAs` du LocalBusiness

---

### B-3 : Strategie de Netlinking (debuts)

**Temps estime :** 2-4 heures / mois (action continue)

**Sources de liens prioritaires (effort faible, impact reel) :**

1. **Annuaires professionnels gratuits :**
   - pagesjaunes.fr (profil gratuit)
   - societe.com (mention gratuite)
   - kompass.com
   - europages.fr

2. **Annuaires sectoriels :**
   - securite-incendie.com (si annuaire existant)
   - preventionincendie.fr
   - Les pages "partenaires" de federations (FFMI, UNCP, etc.)

3. **Presse et medias specialises :**
   - Rediger un communique de presse sur la plateforme gratuite de diagnostic
   - Proposer un article invité sur des blogs RH/juridique/conformite

4. **Contenu linkable a creer :**
   - Infographie "Les 10 obligations incendie a checker avant la commission de securite"
   - Checklist PDF telechargeables avec lien source vers le site
   - Statistiques sur les fermetures administratives (si accessibles)

---

### B-4 : Corriger les details mineurs du schema LocalBusiness

**Temps estime :** 30 minutes

```json
{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness", "ProfessionalService"],
  "@id": "https://www.securiteincendiepro.fr/#organization",
  "name": "SecuriteIncendiePro.fr",
  "url": "https://www.securiteincendiepro.fr/",
  "logo": "https://www.securiteincendiepro.fr/logo.png",
  "telephone": "+33775754921",
  "priceRange": "Gratuit",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[A REMPLIR]",
    "postalCode": "[A REMPLIR]",
    "addressLocality": "[A REMPLIR]",
    "addressCountry": "FR"
  },
  "areaServed": { "@type": "Country", "name": "France" },
  "sameAs": [
    "https://www.linkedin.com/company/securiteincendiepro",
    "https://www.facebook.com/securiteincendiepro",
    "https://www.google.com/maps/place/[ID_GBP]"
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "284",
    "bestRating": "5",
    "worstRating": "1"
  }
}
```

---

## CALENDRIER DE DEPLOIEMENT

```
SEMAINE 1 (31 mars - 6 avril 2026)
  [Lundi]    C-1 : Corriger redirections + canonical www/non-www
  [Lundi]    C-2 : Corriger dates sitemap
  [Mardi]    C-3 : Securiser webhook (honeypot minimum)
  [Mercredi] H-1 : Creer og:image + twitter:image
  [Jeudi]    H-2 : Ajouter favicon
  [Jeudi]    H-3 : Corriger title homepage
  [Vendredi] H-4 : Headers securite (vercel.json)

SEMAINE 2 (7 - 13 avril 2026)
  [Lundi-Mercredi]  H-5 : Enrichir contenu homepage (+1 500 mots)
  [Jeudi-Vendredi]  H-7 : Corriger H2 avec mots-cles

SEMAINES 3-4 (14 - 27 avril 2026)
  H-6 : Creer 10 pages locales (Paris, Lyon, Marseille, Bordeaux, Toulouse...)
  H-8 : Actions E-E-A-T (page A propos, adresse, logos APSAD)
  M-1 : Implementer IndexNow
  M-2 : Schema HowTo
  M-3 : Schema WebSite

SEMAINES 5-6 (28 avril - 11 mai 2026)
  M-4 : Corriger meta descriptions pages secondaires
  M-5 : Enrichir maillage interne
  M-6 : Preload CSS + optimisation cache
  M-7 : Schema Article sur articles de blog

SEMAINES 7-12 (mai - juin 2026)
  B-1 : Creer 5 nouveaux articles de blog (1 par semaine)
  B-2 : Creer Google Business Profile
  B-3 : Debuts de netlinking (annuaires, GBP)
  B-4 : Finaliser schema LocalBusiness
```

---

## KPIs A SUIVRE (Google Search Console + Analytics)

| KPI | Valeur Actuelle | Objectif J+30 | Objectif J+90 |
|---|---|---|---|
| Score SEO global | 61/100 | 72/100 | 82/100 |
| Impressions GSC / semaine | A mesurer | +40% | +150% |
| Clics organiques / semaine | A mesurer | +30% | +120% |
| Position moyenne | A mesurer | < 25 | < 15 |
| Pages indexees | ~15 | 25+ | 40+ |
| Core Web Vitals (LCP) | Estime bon | Confirme bon | Bon |
| Core Web Vitals (CLS) | Estime moyen | Ameliore | Bon |
| Taux de conversion leads | A mesurer | Base etablie | +20% |

---

## CHECKLIST FINALE DE VALIDATION

Avant de deployer chaque groupe d'actions, valider :

- [ ] Tester les redirections avec `curl -I [URL]`
- [ ] Valider le schema sur https://search.google.com/test/rich-results
- [ ] Tester l'og:image sur https://developers.facebook.com/tools/debug/
- [ ] Tester le title/meta dans https://seomofo.com/snippet-optimizer.html
- [ ] Verifier les canonicals avec `curl -s [URL] | grep canonical`
- [ ] Soumettre le sitemap dans Google Search Console
- [ ] Demander une reinspection dans GSC apres les corrections C-1 et C-2
- [ ] Activer IndexNow et notifier les nouvelles URLs
- [ ] Tester les Core Web Vitals avec PageSpeed Insights (mobile ET desktop)

---

*Document genere le 30 mars 2026 — a actualiser tous les 30 jours avec les donnees GSC.*
