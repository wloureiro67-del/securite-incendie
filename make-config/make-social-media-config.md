# Configuration Make.com — Publication Réseaux Sociaux

## SCÉNARIO 1 — "Publication Réseaux Sociaux Automatique"

### Déclencheur : Schedule
- Jours : Lundi, Mercredi, Vendredi
- Heure : 09:00 (Europe/Paris)
- Dans Make : module "Clock" → choisir "Days of week" → cocher L/ME/V → 09:00

### Module 1 — Google Drive : Lire le fichier posts-semaine
- Module : **Google Drive → Download a File**
- Connection : ton compte Google
- Enter a File ID : utilise "Search for files/folders"
- Filtre : name contains `posts-semaine-` → trier par date décroissante → limit 1
- Résultat : `{{1.data}}` = contenu du fichier Markdown

### Module 2 — Text Parser : Extraire le post du jour
- Module : **Text Parser → Match Pattern**
- Input : `{{1.data}}`
- Pattern selon le jour (utilise un Router ou une variable) :
  - Lundi → `POST_LUN_LK:\s*([\s\S]*?)(?=POST_|$)`
  - Mercredi → `POST_MER_LK:\s*([\s\S]*?)(?=POST_|$)`
  - Vendredi → `POST_VEN_LK:\s*([\s\S]*?)(?=POST_|$)`
- Utilise `formatDate(now; "E")` pour détecter le jour : Mon/Wed/Fri
- Variable `{{post_linkedin}}` = groupe capturé 1
- Même logique pour `{{post_facebook}}` avec POST_*_FB_*

### Module 3 — Buffer : Post LinkedIn
- Module : **Buffer → Create an Update**
- Connection : ton compte Buffer (OAuth)
- Profile IDs : sélectionne ton profil LinkedIn
- Text : `{{post_linkedin}}`
- Scheduled At : `{{formatDate(now; "X")}}` (immédiat) ou timestamp 09:00

### Module 4 — Buffer → Post Facebook
- Identique au module 3
- Profile IDs : sélectionne ton profil Facebook
- Text : `{{post_facebook}}`

### Module 5 — Gmail : Récap
- Module : **Gmail → Send an Email**
- To : wloureiro67@gmail.com
- Subject : `✅ Posts publiés — {{formatDate(now; "DD/MM/YYYY")}}`
- Body :
```
Posts publiés aujourd'hui ({{formatDate(now; "dddd DD/MM")}}) :

LINKEDIN :
{{post_linkedin}}

FACEBOOK :
{{post_facebook}}
```

---

## SCÉNARIO 2 — "Publication Article Blog Automatique"

### Déclencheur : Schedule
- Jour : Lundi
- Heure : 10:00 (Europe/Paris)

### Module 1 — Google Drive : Lire le dernier article HTML
- Module : **Google Drive → Download a File**
- Filtre : name contains `semaine-` AND extension = `.html` → tri date desc → limit 1

### Module 2 — GitHub : Commit et push
- Module : **GitHub → Create or Update a File**
- Connection : GitHub OAuth (repo wloureiro67-del/securite-incendie)
- Repository : securite-incendie
- File Path : `articles/{{nom_fichier}}.html`
- Content : `{{base64(1.data)}}`
- Message : `feat: article semaine {{formatDate(now; "YYYY-WW")}}`
- Branch : main

### Module 3 — Sleep 2 minutes
- Module : **Tools → Sleep**
- Delay : 120 secondes (Vercel déploie automatiquement via webhook GitHub)

### Module 4 — Google Search Console : Soumettre URL
- Module : **HTTP → Make a Request** (API REST)
- URL : `https://searchconsole.googleapis.com/v1/urlInspection/index:inspect`
- Method : POST
- Headers : `Authorization: Bearer {{gsc_token}}`
- Body : `{"inspectionUrl": "https://www.securiteincendiepro.fr/articles/{{slug}}.html", "siteUrl": "https://www.securiteincendiepro.fr/"}`

### Module 5 & 6 — Buffer LinkedIn + Facebook
- Même config que Scénario 1 modules 3 & 4
- Text : contenu des champs `ARTICLE_ANNONCE_LK` / `ARTICLE_ANNONCE_FB` du fichier

### Module 7 — Gmail : Confirmation
- Subject : `🚀 Article publié — {{titre_article}}`
- Body : URL de l'article + confirmation indexation

---

## SCÉNARIO 3 — "Rapport Hebdomadaire"

### Déclencheur : Schedule
- Jour : Vendredi
- Heure : 17:00 (Europe/Paris)

### Module 1 — Google Sheets : Leads de la semaine
- Module : **Google Sheets → Search Rows**
- Spreadsheet : "Leads — Sécurité Incendie Pro"
- Sheet : Leads
- Filtre : colonne A (Date) >= lundi de la semaine en cours
- `{{formatDate(addDays(now; -4); "YYYY-MM-DD")}}`

### Module 2 — Gmail : Rapport HTML
- To : wloureiro67@gmail.com
- Subject : `📊 Rapport semaine {{formatDate(now; "WW/YYYY")}} — {{count(1)}} leads`
- Body HTML : voir template dans `rapport-hebdo-template.html`
- Données : nombre leads, liste codes postaux, statuts, comparaison S-1

---

## Connexions nécessaires dans Make.com
| Service | Type | Notes |
|---------|------|-------|
| Google Drive | OAuth | même compte que Sheets |
| Google Sheets | OAuth | déjà configuré |
| Buffer | OAuth2 | app.buffer.com → Settings → Apps |
| GitHub | OAuth | github.com/settings/tokens |
| Gmail | OAuth | déjà configuré via Brevo ou Gmail direct |
| Google Search Console | OAuth | nécessite API activée dans GCP |
