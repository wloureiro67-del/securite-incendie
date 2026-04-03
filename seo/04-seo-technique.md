# 🔧 Audit SEO Technique — index.html
**Site :** https://securiteincendiepro.fr/
**Fichier analysé :** index.html (+ sitemap.xml, robots.txt)
**Date :** 30 mars 2026

---

## 📊 Tableau de Bord — Score Global

| Catégorie | Score | Statut |
|---|---|---|
| Balises fondamentales (title, meta, canonical) | 9/10 | ✅ Excellent |
| Données structurées Schema.org | 10/10 | ✅ Excellent |
| Performance / Poids de page | 5/10 | ⚠️ À améliorer |
| Contenu & structure HTML | 7/10 | 🟡 Bon |
| Sitemap & robots.txt | 8/10 | ✅ Bon |
| Maillage interne | 3/10 | 🔴 Insuffisant |
| Signaux E-E-A-T | 6/10 | 🟡 À renforcer |

**Score global estimé : 7/10** — Base solide, des améliorations ciblées peuvent avoir un impact rapide.

---

## ✅ CE QUI EST BIEN FAIT

### 1. Balises fondamentales — Excellentes
```
<title> : "Devis Sécurité Incendie Gratuit | Installateur Certifié APSAD Près de Chez Vous"
```
- ✅ Mot-clé principal dès le début ("Devis Sécurité Incendie Gratuit")
- ✅ Argument de différenciation ("APSAD Certifié")
- ✅ Longueur correcte (~67 caractères)

```
<meta name="description" : "Obtenez jusqu'à 3 devis gratuits pour votre sécurité incendie en 60 secondes..."
```
- ✅ Bonne longueur (158 caractères)
- ✅ Contient le mot-clé principal
- ✅ Chiffres concrets ("3 devis", "60 secondes")
- ✅ CTA implicite ("Sans engagement")

### 2. Données structurées Schema.org — Parfaites ⭐
Trois schémas implémentés correctement :
- ✅ **LocalBusiness + ProfessionalService** : nom, téléphone, areaServed France, catalogue de services
- ✅ **FAQPage** : 6 questions/réponses (potentiel Rich Snippets dans Google)
- ✅ **BreadcrumbList** : navigation structurée

Les avis Schema (aggregateRating: 4.9/5, 1 200 avis) sont un excellent signal social — ils peuvent apparaître comme Rich Snippets dans les SERP.

### 3. Balises Open Graph & Twitter Card — Complètes
- ✅ og:title, og:description, og:image, og:locale (fr_FR)
- ✅ twitter:card "summary_large_image"
- ✅ Images OG avec dimensions spécifiées (1200×630)

### 4. Balises techniques — Correctes
- ✅ `<meta charset="UTF-8">`
- ✅ `<meta name="viewport">` adaptatif mobile
- ✅ `<link rel="canonical">` présente
- ✅ `<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">`

### 5. robots.txt — Correct
```
User-agent: *
Allow: /
Sitemap: https://securiteincendiepro.fr/sitemap.xml
```
- ✅ Accès autorisé à tous les robots
- ✅ Référence correcte au sitemap

### 6. Sitemap.xml — Présent et structuré
5 URLs référencées avec `<lastmod>`, `<changefreq>` et `<priority>` :
- Page d'accueil (priority 1.0) ✅
- blog.html (priority 0.8) ✅
- 3 articles (priority 0.7) ✅

---

## ⚠️ CE QUI EST À AMÉLIORER

---

### 🔴 PRIORITÉ HAUTE — Poids de page (95 KB de HTML brut)

**Problème :** Le fichier index.html pèse **95 798 octets (~93 KB)** avec tout le CSS et les 40+ fonctions JavaScript intégrés directement dans le HTML. C'est 3 à 4× plus lourd qu'une page HTML bien optimisée.

**Impact :** Google intègre le Core Web Vitals dans son algorithme de classement. Un fichier HTML surchargé ralentit le Time to First Byte (TTFB) et le Largest Contentful Paint (LCP).

**Actions recommandées :**
1. Extraire le CSS dans un fichier séparé `styles.css` avec `<link rel="stylesheet">`
2. Extraire le JavaScript dans `script.js` avec l'attribut `defer`
3. Minifier le CSS et le JS (outils : cssnano, terser)
4. Activer la compression Gzip/Brotli sur Vercel (déjà actif par défaut — vérifier)

**Gain estimé :** Réduction du poids initial de 40-50%, amélioration du LCP de 0.5 à 1 seconde.

---

### 🔴 PRIORITÉ HAUTE — Maillage interne quasi inexistant

**Problème :** Votre site n'a qu'une seule page principale visible par Google. Il n'existe pas encore de vraies pages de contenu liées entre elles. Le sitemap référence des articles (installation-alarme-incendie.html, etc.) mais ceux-ci semblent absents ou non liés depuis l'accueil.

**Impact :** Sans maillage interne, Google ne peut pas "crawler" et indexer vos futures pages d'articles. Le jus SEO reste bloqué sur la page d'accueil au lieu de se distribuer sur l'ensemble du site.

**Actions recommandées :**
1. Créer une vraie page `/blog/` ou `/guides/` listant tous les articles
2. Lier chaque article depuis cette page index
3. Ajouter dans le footer : liens vers les articles, pages de services, mentions légales
4. Dans chaque article : lien de retour vers l'accueil + 2-3 liens vers articles connexes
5. Mettre à jour le sitemap à chaque nouvel article publié

---

### 🟡 PRIORITÉ MOYENNE — H1 ne contient pas exactement le mot-clé cible

**Problème actuel :**
```html
<h1>
  Trouvez le bon spécialiste sécurité incendie —
  devis gratuit & comparatif
</h1>
```

Le H1 contient "sécurité incendie" et "devis gratuit" mais pas la formulation exacte **"devis sécurité incendie gratuit"** qui est votre mot-clé principal (1 000–2 000 recherches/mois).

**Action recommandée :** Reformuler légèrement le H1 pour inclure la séquence exacte, par exemple :
```
Obtenez votre devis sécurité incendie gratuit
en 60 secondes — Installateurs APSAD certifiés
```

---

### 🟡 PRIORITÉ MOYENNE — Pas d'images sur la page

**Problème :** La page n'utilise aucune balise `<img>` — tout est en CSS et SVG inline. Cela signifie :
- Aucune opportunité de référencement via Google Images
- Aucun attribut `alt` exploitable pour le SEO
- Contenu visuel moins riche aux yeux des crawlers

**Actions recommandées :**
1. Ajouter au moins 1 image pertinente avec `alt` optimisé (ex: photo d'un technicien APSAD)
2. Utiliser `loading="lazy"` sur les images non critiques
3. Ajouter `fetchpriority="high"` sur l'image principale (LCP)
4. Format WebP recommandé pour la performance

---

### 🟡 PRIORITÉ MOYENNE — URL Vercel vs domaine personnalisé

**Problème :** L'URL canonique pointe vers `https://securiteincendiepro.fr/`

Un domaine Vercel `.vercel.app` est fonctionnel mais présente deux désavantages SEO :
1. Moins de confiance de la part des utilisateurs (conversion)
2. Impossible de construire une autorité de domaine solide à long terme sur un sous-domaine gratuit

**Action recommandée :** Acheter le domaine `securiteincendiepro.fr` ou `securite-incendie.fr` (~12€/an) et le configurer sur Vercel. Mettre à jour la canonical, le sitemap et le Schema.org.

---

### 🟡 PRIORITÉ MOYENNE — Signaux E-E-A-T à renforcer

Google valorise de plus en plus l'**Expérience, Expertise, Autorité et Fiabilité (E-E-A-T)** surtout sur les sujets à enjeux légaux/sécuritaires comme la sécurité incendie.

**Ce qui manque actuellement :**
- Page "À propos" ou "Qui sommes-nous ?" absente
- Pas de mentions légales ni de politique de confidentialité (RGPD) visibles
- Pas de mentions de partenaires ou certifications officielles avec lien vérifiable

**Actions recommandées :**
1. Créer une page `/mentions-legales` et `/politique-confidentialite` (aussi obligatoire RGPD)
2. Ajouter une section "À propos de SecuriteIncendiePro.fr" sur l'accueil
3. Mentionner les certifications partenaires avec logos cliquables (APSAD, CNPP, Qualibat)
4. Ajouter les liens `sameAs` dans le Schema.org (LinkedIn, Pages Jaunes...)

---

### 🟢 PRIORITÉ FAIBLE — Script de vérification Search Console manquant

**Problème :** Aucun tag de vérification Google Search Console n'est visible dans le `<head>`.

**Action :** Ajouter la meta tag de vérification GSC dans le `<head>` :
```html
<meta name="google-site-verification" content="VOTRE_CODE_ICI" />
```
(Voir guide Search Console — fichier 06)

---

### 🟢 PRIORITÉ FAIBLE — Sitemap à enrichir au fur et à mesure

Le sitemap actuel ne liste que 5 URLs. Au fur et à mesure de la publication des 12 articles du calendrier éditorial, chaque nouvelle URL doit être ajoutée.

**Rappel du format :**
```xml
<url>
  <loc>https://securiteincendiepro.fr/articles/NOM-ARTICLE.html</loc>
  <lastmod>2026-04-07</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.7</priority>
</url>
```

---

## 📋 Plan d'Action Priorisé

| Priorité | Action | Difficulté | Impact SEO |
|---|---|---|---|
| 🔴 1 | Extraire CSS et JS dans des fichiers séparés (minifier) | Moyenne | Fort |
| 🔴 2 | Créer pages articles + maillage interne | Faible | Très fort |
| 🟡 3 | Reformuler le H1 avec le mot-clé exact | Très faible | Moyen |
| 🟡 4 | Ajouter 1 image principale avec alt optimisé | Faible | Moyen |
| 🟡 5 | Acheter un domaine personnalisé (securiteincendiepro.fr) | Faible | Fort (long terme) |
| 🟡 6 | Créer pages mentions légales + politique confidentialité | Faible | Moyen (RGPD + E-E-A-T) |
| 🟡 7 | Compléter les `sameAs` dans Schema.org | Très faible | Faible |
| 🟢 8 | Ajouter meta tag vérification Search Console | Très faible | Nécessaire |
| 🟢 9 | Mettre à jour sitemap à chaque publication | Très faible | Moyen |
