# CLAUDE.md — SecuriteIncendiePro.fr

# RÈGLES CODE — PRIORITÉ ABSOLUE

## MODIFICATIONS
- Ne réécris JAMAIS un fichier entier
- Donne UNIQUEMENT le bloc modifié avec repères précis :
  "// Remplace X par Y — fichier: nom.js, ligne ~50"
- Si plusieurs fichiers touchés : liste-les d'abord, attends ma validation

## FORMAT DU CODE
- Pas de commentaires évidents dans le code (ex: "// on appelle la fonction")
- Conserve mon style de code existant (indentation, nommage, structure)
- Pas d'imports déjà présents dans le fichier

## AVANT DE CODER
- Pour toute nouvelle fonctionnalité > 20 lignes : 
  propose une approche en 3 lignes max, j'approuve, puis tu codes
- Si ma demande est ambiguë : pose UNE seule question, pas plusieurs

## DÉBOGAGE
- Cause du bug en 1 phrase
- Correctif minimal uniquement
- Pas d'explication sur ce que fait le code existant

## CE QU'IL NE FAUT JAMAIS FAIRE
- Réécrire tout un composant pour changer 3 lignes
- Ajouter des fonctionnalités non demandées
- Expliquer ce que tu viens de faire après avoir codé
- Mettre des blocs de code "pour exemple" non demandés

## Projet
Site vitrine HTML statique de mise en relation B2B pour la sécurité incendie (diagnostics, conformité ERP 2026, installateurs APSAD certifiés).
- **Domaine cible :** `https://www.securiteincendiepro.fr` (www = version canonique officielle)
- **Hébergement :** Vercel (HTML statique, pas de framework)
- **Fichier de config Vercel :** `vercel.json` (à créer/modifier pour les redirections)

## Structure des fichiers
```
/                    → pages HTML à la racine (index, blog, pages locales, légales)
/articles/           → articles de blog HTML
/seo/                → rapports et plans SEO (ne pas modifier, référence uniquement)
styles.css           → feuille de styles principale
script.js            → JS principal
sitemap.xml          → sitemap (URLs toutes en www)
robots.txt           → pointe vers sitemap www
```

## Règles techniques impératives
1. **Canonical toujours en www** : `<link rel="canonical" href="https://www.securiteincendiepro.fr/...">` — jamais sans www
2. **og:url toujours en www**
3. **Schema JSON-LD `"url"`** : toujours `https://www.securiteincendiepro.fr/`
4. **Sitemap** : toutes les URLs en www
5. **robots.txt** : sitemap en www

## Contexte SEO actuel (avril 2026)
- Score SEO : ~61/100 (objectif 82/100 en 90 jours)
- Problème canonique www/non-www en cours de correction
- Redirections : unifier en 308 permanent via vercel.json
- Contenu : enrichissement en cours (articles longs B2B, pages locales)
- Mots-clés cibles : conformité ERP, sécurité incendie entreprise, extincteur obligatoire, alarme incendie ERP

## Conventions de code HTML
- Pas de framework, HTML vanilla + CSS vanilla
- Schemas JSON-LD dans le `<head>`
- Balises meta complètes (title, description, og:*, twitter:*, canonical)
- Mobile-first

## Ce qu'il ne faut PAS faire
- Ne pas modifier les fichiers dans `/seo/` (ce sont des rapports, pas du code)
- Ne pas changer la version non-www comme canonique
- Ne pas ajouter de dépendances JS ou npm
- Ne pas créer de fichiers inutiles
