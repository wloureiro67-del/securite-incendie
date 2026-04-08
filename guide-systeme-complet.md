# Guide Système Complet — SecuriteIncendiePro.fr

## Comment fonctionne le système

```
LUNDI MATIN (10 min de travail humain)
│
├── 1. Tu colles prompt-cowork-hebdo.md dans Claude
├── 2. Claude génère le contenu de la semaine
├── 3. Tu copies le résultat dans content-bank.md
├── 4. Make.com fait TOUT le reste automatiquement
│
└── RÉSULTAT : 6 posts publiés + 1 article + rapport leads
    sans aucune intervention supplémentaire
```

### Architecture des 3 scénarios Make.com

| Scénario | Déclencheur | Action |
|----------|-------------|--------|
| Social Media | Lun/Mer/Ven 9h | Lit content-bank.md → publie LinkedIn + Facebook |
| Article Blog | Lun 10h | Commit GitHub → attend Vercel → Search Console → annonce |
| Rapport Hebdo | Ven 17h | Lit Google Sheets → email rapport leads |

---

## CHECKLIST LUNDI MATIN (10 étapes, ~10 min)

- [ ] 1. Ouvrir `prompt-cowork-hebdo.md` → remplacer [SEMAINE] par la date
- [ ] 2. Coller le prompt dans Claude → attendre la génération
- [ ] 3. Copier le contenu généré → l'ajouter à la fin de `seo/content-bank.md`
- [ ] 4. Vérifier que Make.com Scénario 1 est actif (toggle vert)
- [ ] 5. Vérifier que Make.com Scénario 2 est actif
- [ ] 6. Si un article a été rédigé la semaine passée → uploader le .html dans Google Drive (dossier `articles-queue/`)
- [ ] 7. Vérifier le rapport de vendredi précédent → traiter les leads en attente
- [ ] 8. Envoyer 5 messages prospection LinkedIn (PROSPECT_001 à 005)
- [ ] 9. Vérifier Google Search Console → nouvelles impressions sur mots-clés cibles
- [ ] 10. Mettre à jour le statut des leads dans Google Sheets (colonne J)

---

## CHECKLIST VENDREDI (5 étapes, ~15 min)

- [ ] 1. Lire le rapport hebdomadaire reçu à 17h (email wloureiro67@gmail.com)
- [ ] 2. Appeler ou relancer les leads "Nouveau" non traités depuis +48h
- [ ] 3. Vérifier les posts publiés cette semaine dans Buffer → noter les engagements
- [ ] 4. Si un post performe bien → prévoir de le réutiliser dans 4 semaines
- [ ] 5. Préparer éventuellement une note pour le prompt de lundi (thème prioritaire)

---

## Ajouter un nouveau réseau social

1. Connecter le réseau dans Buffer (Settings → Channels)
2. Dans Make.com Scénario 1 → dupliquer le module Buffer existant
3. Changer le Profile ID pour le nouveau réseau
4. Dans `content-bank.md` → ajouter une section `POST_LUN_[RÉSEAU]_001:`
5. Mettre à jour le prompt Cowork pour inclure le nouveau format

---

## Ajouter un partenaire installateur

1. Ouvrir Google Sheets "Leads — Sécurité Incendie Pro"
2. Onglet "Leads" → colonne L "Partenaire assigné" → la formule se met à jour auto
3. Pour ajouter une zone → modifier la formule en G2 et L2 :
   - Ajouter `IF(LEFT(F2,2)="XX","Partenaire Ville",...)` dans la formule L2
4. Informer le partenaire : les leads de son département lui sont assignés automatiquement
5. Créer un filtre dans Sheets pour qu'il ne voie que ses leads (partage avec filtre)

---

## Scaler vers Google Ads

Quand budget disponible (recommandé : 500 €/mois minimum) :

**Étape 1 — Tracking**
- Installer Google Tag Manager sur le site
- Créer une conversion "Formulaire soumis" dans Google Ads
- Lier Google Ads à Search Console

**Étape 2 — Campagnes prioritaires**
- Campagne 1 : mots-clés "extincteur vérification [ville]" → CPC estimé 0,80-2 €
- Campagne 2 : mots-clés "conformité ERP 2026" → CPC estimé 1,50-4 €
- Campagne 3 : remarketing visiteurs du formulaire non soumis

**Étape 3 — Make.com**
- Ajouter module Google Ads API dans Scénario 3 (rapport hebdo)
- Récupérer coût/lead automatiquement chaque semaine

---

## Résolution des problèmes courants

### Make.com — Scénario désactivé automatiquement
**Cause :** erreur dans un module (ex: fichier non trouvé, API timeout)
**Fix :** Aller dans HISTORY → lire l'erreur → corriger → cliquer le toggle pour réactiver

### Buffer — Post non publié
**Cause :** limite du plan gratuit atteinte (10 posts schedulés)
**Fix :** Publier manuellement les anciens posts en attente → libère des slots

### Google Sheets — Formule département vide
**Cause :** code postal absent ou non standard
**Fix :** Colonne G utilise `=SI(F2="";"";GAUCHE(F2;2))` → vérifier que F2 n'est pas vide

### Make.com — Erreur Brevo "duplicate_parameter"
**Cause :** email déjà dans la liste Brevo avec ce statut
**Fix :** Module CreateContact → activer "updateEnabled = true" (déjà corrigé)

### GitHub — Commit échoue
**Cause :** token expiré ou permissions insuffisantes
**Fix :** github.com/settings/tokens → regénérer token → mettre à jour dans Make.com Credentials

### Search Console — Erreur 401
**Cause :** OAuth expiré
**Fix :** Make.com → Connections → Google Search Console → Reauthorize
