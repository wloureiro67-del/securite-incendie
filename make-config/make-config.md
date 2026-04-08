# Configuration Make.com — SecuriteIncendiePro.fr
## Guide de reconfiguration complet

---

## ÉTAPE 1 — Préparer Google Sheets

### 1a. Créer le fichier

1. Ouvre [sheets.google.com](https://sheets.google.com)
2. Crée un nouveau fichier : "Leads — Sécurité Incendie Pro"
3. Renomme l'onglet `Sheet1` en **"Leads"**

### 1b. Importer les en-têtes

1. Fichier → Importer → Upload → sélectionne `leads.csv` (dans ce dossier)
2. Séparateur : virgule
3. Cela crée automatiquement les 14 colonnes dans le bon ordre

### 1c. Ajouter les formules automatiques

**Colonne G — Département (depuis code postal) :**
Colle cette formule en G2 (et tire vers le bas) :
```
=IF(F2="","",LEFT(F2,2))
```

**Colonne L — Partenaire assigné (depuis code postal) :**
Colle cette formule en L2 :
```
=IF(F2="","",IF(LEFT(F2,2)="67","Partenaire Strasbourg",IF(LEFT(F2,2)="68","Partenaire Mulhouse",IF(LEFT(F2,2)="69","Partenaire Lyon",IF(OR(LEFT(F2,2)="75",LEFT(F2,2)="77",LEFT(F2,2)="78",LEFT(F2,2)="91",LEFT(F2,2)="92",LEFT(F2,2)="93",LEFT(F2,2)="94",LEFT(F2,2)="95"),"Partenaire Paris IDF","Non assigné")))))
```

**Colonne J — Statut (valeur par défaut "Nouveau") :**
Make remplira cette colonne avec "Nouveau" automatiquement.

### 1d. Créer 2 onglets supplémentaires (optionnel)
- Onglet **"Exit Intent"** : même structure, pour les leads popup
- Onglet **"Formulaire Final"** : pour les leads du 2e formulaire en bas de page

### 1e. Protéger les colonnes formules
Sélectionne G:G et L:L → Clic droit → "Protéger la plage" → pour éviter que Make les écrase.

---

## ÉTAPE 2 — Configurer Make.com

### 2a. Ouvrir le scénario existant

1. Va sur [make.com](https://make.com) → Scénarios
2. Ouvre le scénario avec le webhook `n29seqs24j7elaqeg4hh44d3v9nx6hkn`

### 2b. Structure du scénario final

```
[Webhook] → [Router] → Route 1 : form_id = "hero" ou "final"
                     → Route 2 : form_id = "exit_intent"

Chaque route :
  → [Google Sheets: Search Rows] (vérifie si email existe déjà)
  → [Router 2] → Contact NOUVEAU : → [Sheets: Add Row] + [Email nouveau contact] + [Email notification]
              → Contact EXISTANT : → [Sheets: Add Row] + [Email contact existant] + [Email notification]
```

### 2c. Configuration du module Webhook

Le webhook est déjà configuré. Voici les variables disponibles dans Make :
- `{{nom}}` — Nom du prospect
- `{{entreprise}}` — Nom de l'entreprise (optionnel)
- `{{email}}` — Email
- `{{telephone}}` — Téléphone
- `{{codepostal}}` — Code postal (5 chiffres)
- `{{superficie}}` — Superficie sélectionnée
- `{{type_local}}` — Type de local ERP
- `{{description}}` — Description du projet (optionnel)
- `{{form_id}}` — Source : "hero", "final", ou "exit_intent"
- `{{date}}` — Date/heure de soumission
- `{{source}}` — Page source (ex: "/")
- `{{logo_url}}` — URL du logo pour les emails

---

## ÉTAPE 3 — Module Google Sheets "Search Rows" (détection doublon)

**Objectif :** détecter si l'email existe déjà dans la colonne D.

**Configuration :**
- Connection : ton compte Google
- Spreadsheet : "Leads — Sécurité Incendie Pro"
- Sheet : "Leads"
- Column : D (Email)
- Filter : `{{email}}` (variable du webhook)
- Limit : 1

**Résultat :** Si la recherche renvoie un résultat → contact existant. Sinon → nouveau contact.

---

## ÉTAPE 4 — Module Google Sheets "Add a Row"

**Mapping des colonnes :**

| Colonne | En-tête | Valeur Make |
|---------|---------|-------------|
| A | Date/Heure | `{{date}}` |
| B | Nom | `{{nom}}` |
| C | Entreprise | `{{entreprise}}` |
| D | Email | `{{email}}` |
| E | Téléphone | `{{telephone}}` |
| F | Code Postal | `{{codepostal}}` |
| G | Département | *(laisse vide — formule Google Sheets)* |
| H | Superficie | `{{superficie}}` |
| I | Description | `{{description}}` |
| J | Statut | `Nouveau` *(texte fixe)* |
| K | Contact existant | `Non` ou `Oui` *(selon le résultat de Search Rows)* |
| L | Partenaire assigné | *(laisse vide — formule Google Sheets)* |
| M | Date d'assignation | *(laisser vide — rempli manuellement)* |
| N | Notes | *(laisser vide)* |

---

## ÉTAPE 5 — Module Email "Notification interne"

**Configuration (Gmail ou SMTP) :**
- À : `wloureiro67@gmail.com`
- Objet : `🔥 Nouveau lead {{nom}} — {{codepostal}} — {{entreprise}}`
- Type de contenu : HTML
- Corps : colle le contenu de `email-notification.html`

**Remplacement des variables dans Make :**
Dans l'éditeur HTML de Make, les `{{variable}}` sont automatiquement remplacées si tu utilises les variables du webhook. Assure-toi que les noms correspondent exactement.

**Variables spéciales à calculer dans Make :**
- `{{departement}}` : utilise la fonction `substring({{codepostal}}; 1; 2)` dans Make
- `{{partenaire}}` : utilise un module "Set variable" avec une condition :
  ```
  IF(substring(codepostal;1;2) = "67"; "Partenaire Strasbourg";
  IF(substring(codepostal;1;2) = "68"; "Partenaire Mulhouse";
  IF(substring(codepostal;1;2) = "69"; "Partenaire Lyon";
  IF(OR(substring(codepostal;1;2) = "75"; ... = "92"; ... = "93"; ...); "Partenaire Paris IDF";
  "Non assigné"))))
  ```
- `{{badge_bg}}` : `#27AE60` si nouveau contact, `#E8591A` si existant
- `{{badge_text}}` : `NOUVEAU CONTACT` ou `CONTACT EXISTANT`

---

## ÉTAPE 6 — Module Email "Confirmation prospect"

**Configuration :**
- À : `{{email}}` (adresse du prospect)
- Objet : `✅ Votre demande a bien été reçue — Sécurité Incendie Pro`
- Type de contenu : HTML
- Corps :
  - Si **nouveau contact** → contenu de `email-nouveau-contact.html`
  - Si **contact existant** → contenu de `email-contact-existant.html`

**Important :** Dans les templates HTML, les `{{logo_url}}` sont déjà présents. Make remplacera automatiquement `{{logo_url}}` par la valeur envoyée dans le webhook (`https://www.securiteincendiepro.fr/logo.png`).

---

## ÉTAPE 7 — Activer et tester

1. Clique sur **"Run once"** dans Make
2. Soumets le formulaire sur [securiteincendiepro.fr](https://securiteincendiepro.fr)
3. Vérifie :
   - [ ] Une ligne apparaît dans Google Sheets
   - [ ] Tu reçois l'email de notification sur wloureiro67@gmail.com
   - [ ] Le prospect reçoit l'email de confirmation
   - [ ] Département et Partenaire sont calculés correctement
4. Si tout est OK → clique **"Activate scenario"** (toggle en haut à gauche)

---

## ÉTAPE 8 — Planification Make (optionnel)

Par défaut Make exécute le scénario à chaque webhook entrant (instantané).
Si tu veux réduire les opérations Make :
- Change le mode en **"Scheduled"** : toutes les 15 minutes
- Make traite alors les webhooks en lot

**Recommandation : garde le mode instantané** pour les notifications temps réel.

---

## Résumé du flux final

```
LEAD SOUMIS SUR LE SITE
        ↓
   WEBHOOK MAKE
        ↓
   ROUTER (form_id)
   ↙              ↘
hero/final      exit_intent
        ↓              ↓
  SEARCH ROWS    SEARCH ROWS
  (doublon ?)    (doublon ?)
  ↙       ↘
Nouveau  Existant
  ↓         ↓
ADD ROW  ADD ROW (K=Oui)
  ↓         ↓
Email    Email
nouveau  existant
  ↓         ↓
Email notification → wloureiro67@gmail.com
```

---

## Fichiers dans ce dossier

| Fichier | Description |
|---------|-------------|
| `leads.csv` | En-têtes Google Sheets à importer |
| `email-notification.html` | Email alerte interne (pour toi) |
| `email-nouveau-contact.html` | Email confirmation nouveau prospect |
| `email-contact-existant.html` | Email confirmation client fidèle |
| `make-config.md` | Ce guide |
