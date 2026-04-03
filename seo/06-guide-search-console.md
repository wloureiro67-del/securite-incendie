# 📊 Guide Google Search Console — SecuriteIncendiePro.fr
**Site :** https://securiteincendiepro.fr/
**Date :** 30 mars 2026

---

## Qu'est-ce que Google Search Console ?

Google Search Console (GSC) est un outil **gratuit** fourni par Google qui vous permet de surveiller, maintenir et améliorer la présence de votre site dans les résultats de recherche Google. C'est votre tableau de bord officiel pour comprendre comment Google voit et indexe votre site.

**Ce que GSC vous permet de faire :**
- Voir quels mots-clés génèrent des clics vers votre site
- Connaître exactement quelles pages sont indexées par Google
- Détecter et corriger les erreurs d'exploration (404, pages bloquées)
- Soumettre votre sitemap manuellement
- Identifier les opportunités d'amélioration SEO
- Recevoir des alertes en cas de pénalité manuelle ou de problème de sécurité

---

## ÉTAPE 1 — Créer un compte et vérifier votre site

### 1.1 Accéder à Search Console
1. Rendez-vous sur **https://search.google.com/search-console/**
2. Connectez-vous avec votre compte Google (créez-en un si nécessaire)
3. Cliquez sur **"Commencer maintenant"**

### 1.2 Ajouter votre propriété
Google vous propose deux types de propriétés :

**Option A — Domaine (recommandée si vous achetez un domaine personnalisé)**
```
Format : example.com
Avantage : couvre toutes les variantes (http, https, www, sous-domaines)
Vérification : modification du DNS chez votre registrar
```

**Option B — Préfixe d'URL (recommandée pour votre URL Vercel actuelle)**
```
Format : https://securiteincendiepro.fr/
Avantage : vérification plus simple
Vérification : balise HTML, fichier HTML, ou Google Analytics
```

**👉 Pour votre site actuel, choisissez "Préfixe d'URL" et entrez :**
```
https://securiteincendiepro.fr/
```

### 1.3 Vérifier votre propriété via balise HTML
C'est la méthode la plus simple pour Vercel :

1. Dans GSC, sélectionnez **"Balise HTML"** comme méthode de vérification
2. Google vous donne un code du type :
```html
<meta name="google-site-verification" content="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" />
```
3. Copiez ce code et ajoutez-le dans le `<head>` de votre `index.html`, juste après la balise `<meta charset>` :
```html
<head>
  <meta charset="UTF-8">
  <meta name="google-site-verification" content="VOTRE_CODE_ICI" />
  ...
```
4. Déployez votre fichier sur Vercel
5. Retournez dans GSC et cliquez **"Vérifier"**

✅ Votre propriété est vérifiée ! GSC commence à collecter des données.

---

## ÉTAPE 2 — Soumettre votre Sitemap

Soumettre votre sitemap accélère l'indexation de toutes vos pages par Google.

1. Dans le menu gauche de GSC, cliquez sur **"Sitemaps"**
2. Dans le champ "Ajouter un nouveau sitemap", entrez :
```
sitemap.xml
```
3. Cliquez sur **"Envoyer"**

Google confirmera la réception. Les premières données d'exploration apparaissent sous 24 à 72 heures.

**Important :** À chaque fois que vous publiez un nouvel article, mettez à jour votre `sitemap.xml` et resoumettez-le dans GSC (ou attendez que Google le découvre seul via le crawl régulier).

---

## ÉTAPE 3 — Demander l'indexation de votre page d'accueil

Ne pas attendre que Google trouve votre site seul — demandez-lui dès maintenant :

1. Dans GSC, cliquez sur la barre de recherche en haut **"Inspecter n'importe quelle URL"**
2. Entrez : `https://securiteincendiepro.fr/`
3. Cliquez sur **"Demander l'indexation"**
4. Répétez pour chaque URL présente dans votre sitemap :
   - `https://securiteincendiepro.fr/blog.html`
   - `https://securiteincendiepro.fr/articles/installation-alarme-incendie.html`
   - `https://securiteincendiepro.fr/articles/mise-en-conformite-erp.html`
   - `https://securiteincendiepro.fr/articles/extincteurs-entreprise.html`

⏱️ L'indexation prend généralement 24h à 2 semaines selon la fréquence de crawl de Google sur votre domaine.

---

## ÉTAPE 4 — Les rapports clés à surveiller chaque semaine

### 4.1 Rapport "Performances" (le plus important)

**Où :** Menu gauche → "Performances" → "Résultats de la recherche"

Ce rapport montre :
- **Clics** : nombre de visiteurs venant de Google
- **Impressions** : nombre de fois où votre site est apparu dans les résultats
- **CTR** (Click Through Rate) : % de personnes qui cliquent sur votre résultat
- **Position moyenne** : rang moyen de vos pages dans Google

**Ce qu'il faut surveiller :**

| Métrique | Objectif à 3 mois | Objectif à 6 mois |
|---|---|---|
| Clics / mois | 50–200 | 300–800 |
| Impressions / mois | 500–2 000 | 3 000–10 000 |
| CTR moyen | > 3% | > 5% |
| Position moyenne | < 30 | < 15 |

**Onglet "Pages" :** Identifie quelles pages reçoivent le plus de trafic. Vos articles doivent progressivement monter.

**Onglet "Requêtes" :** Montre les mots-clés exacts tapés par les utilisateurs. C'est une mine d'or pour ajuster vos contenus.

**Astuce :** Si une requête génère beaucoup d'impressions mais peu de clics → améliorez votre titre et meta description pour cette page.

### 4.2 Rapport "Couverture" (indexation)

**Où :** Menu gauche → "Indexation" → "Pages"

Ce rapport liste :
- **Pages indexées** : Google les a trouvées et les affiche dans ses résultats ✅
- **Pages non indexées** : Google les a trouvées mais refuse de les indexer ⚠️
- **Erreurs** : pages introuvables (404), erreurs serveur, etc. 🔴

**Actions :**
- Si une page importante n'est pas indexée → cliquer dessus pour voir la raison → corriger le problème → demander une nouvelle indexation
- Si vous voyez des erreurs 404 → c'est que des liens pointent vers des pages supprimées → rediriger vers la bonne URL

### 4.3 Rapport "Expérience" — Core Web Vitals

**Où :** Menu gauche → "Expérience" → "Signaux Web Essentiels"

Ce rapport évalue la performance technique de votre site selon 3 indicateurs clés que Google utilise pour le classement :

| Indicateur | Description | Cible |
|---|---|---|
| **LCP** (Largest Contentful Paint) | Temps d'affichage du plus grand élément visible | < 2,5 secondes |
| **INP** (Interaction to Next Paint) | Réactivité aux interactions utilisateur | < 200 ms |
| **CLS** (Cumulative Layout Shift) | Stabilité visuelle (les éléments ne bougent pas) | < 0,1 |

Si votre site est en "Rouge" ou "Orange" → appliquer les optimisations décrites dans le fichier `04-seo-technique.md`.

### 4.4 Rapport "Liens"

**Où :** Menu gauche → "Liens"

Montre :
- **Liens externes** : les sites qui pointent vers le vôtre (vos backlinks) → vous verrez progressivement apparaître les annuaires où vous vous êtes inscrit
- **Liens internes** : comment vos pages se relient entre elles

---

## ÉTAPE 5 — Actions hebdomadaires recommandées (30 min/semaine)

**Chaque lundi matin :**

1. Ouvrir GSC → Rapport Performances → vérifier l'évolution des clics et impressions vs semaine précédente
2. Regarder le rapport "Pages" → identifier les articles qui progressent en position
3. Onglet "Requêtes" → noter les nouveaux mots-clés sur lesquels vous apparaissez
4. Rapport "Couverture" → vérifier qu'aucune nouvelle erreur n'est apparue
5. Si vous venez de publier un nouvel article → l'inspecter et demander son indexation

**Temps total : 15 à 30 minutes par semaine.**

---

## ÉTAPE 6 — Connecter Google Analytics 4 (optionnel mais recommandé)

Google Search Console vous dit **d'où viennent vos visiteurs** (Google Search). Google Analytics 4 vous dit **ce qu'ils font sur votre site** (temps passé, pages visitées, formulaires remplis).

Les deux outils sont complémentaires et se connectent entre eux pour des données enrichies.

**Pour connecter GA4 à GSC :**
1. Créez un compte Google Analytics sur analytics.google.com
2. Créez une propriété GA4 pour votre site
3. Ajoutez le tag GA4 dans le `<head>` de votre index.html
4. Dans GSC → Paramètres → Associations → Associer à Google Analytics

---

## 📌 Récapitulatif des Premières Actions

| Action | Deadline | Difficulté |
|---|---|---|
| Créer le compte GSC et vérifier le site | Semaine 1 | ⭐ Très facile |
| Soumettre le sitemap.xml | Semaine 1 | ⭐ Très facile |
| Demander l'indexation de toutes les URLs | Semaine 1 | ⭐ Très facile |
| Vérifier le rapport Couverture | Semaine 2 | ⭐ Très facile |
| Analyser les premières requêtes (après 2 sem.) | Semaine 3-4 | ⭐⭐ Facile |
| Créer compte Google Analytics 4 + liaison GSC | Semaine 2-3 | ⭐⭐ Facile |
| Vérification hebdomadaire régulière | Chaque lundi | ⭐ Très facile |
