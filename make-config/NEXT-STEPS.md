# NEXT STEPS — Activer les 3 scénarios Make.com

## ✅ Déjà fait
- Scénario "Integration Webhooks, Google Sheets" → actif ✓
- Google Sheets "Leads — Sécurité Incendie Pro" → configuré ✓
- Emails Brevo (confirmation prospect + notification) → actifs ✓

---

## 🔧 SCÉNARIO 1 — Publication Réseaux Sociaux (faire maintenant)

**Durée estimée : 20 min**

### Étape 1 — Connecter Buffer à Make.com
1. Va sur [make.com](https://make.com) → **Connections** → **Add connection**
2. Cherche "Buffer" → OAuth2
3. Autorise l'accès → Buffer connecté

### Étape 2 — Uploader content-bank.md dans Google Drive
1. Va sur [drive.google.com](https://drive.google.com)
2. Crée un dossier `securite-incendie-content/`
3. Upload `C:\Users\200VEN09\securite-incendie\seo\content-bank.md`

### Étape 3 — Créer le scénario dans Make.com
1. Make.com → **Scenarios** → **Create a new scenario**
2. Nom : "Publication Réseaux Sociaux Automatique"
3. Ajouter module : **Clock** (schedule)
   - Every : Days of week → Lun + Mer + Ven → 09:00
4. Ajouter module : **Google Drive → Download a File**
   - Chercher le fichier `content-bank.md` dans ton Drive
5. Ajouter module : **Tools → Set Variable**
   - Jour actuel : `{{formatDate(now; "EEE")}}`
6. Ajouter module : **Text Parser → Match Pattern**
   - Pattern Lundi : `POST_LUN_LK_\d+:\n([\s\S]+?)(?=\n---|\nPOST_|$)`
7. Ajouter module : **Buffer → Create an Update** (LinkedIn)
8. Ajouter module : **Buffer → Create an Update** (Facebook)
9. Ajouter module : **Gmail → Send an Email** (récap)
10. **Activer** le scénario (toggle bleu)

---

## 🔧 SCÉNARIO 2 — Publication Article Blog (faire après scénario 1)

**Durée estimée : 30 min**

### Étape 1 — Connecter GitHub
1. Make.com → Connections → Add → "GitHub"
2. Personal Access Token → [github.com/settings/tokens](https://github.com/settings/tokens)
3. Permissions : `repo` (lecture + écriture)

### Étape 2 — Créer le scénario
1. Nom : "Publication Article Blog Automatique"
2. Schedule : Lundi 10:00
3. Modules dans l'ordre :
   - Google Drive → Download File (chercher `semaine-*.html`)
   - GitHub → Create or Update File (repo : wloureiro67-del/securite-incendie)
   - Tools → Sleep (120 secondes)
   - HTTP → POST vers Search Console (voir config dans make-social-media-config.md)
   - Buffer → LinkedIn (ARTICLE_ANNONCE_LK)
   - Buffer → Facebook (ARTICLE_ANNONCE_FB)
   - Gmail → confirmation

---

## 🔧 SCÉNARIO 3 — Rapport Hebdomadaire (le plus simple)

**Durée estimée : 10 min**

1. Nouveau scénario : "Rapport Hebdomadaire"
2. Schedule : Vendredi 17:00
3. Module 1 : **Google Sheets → Get Range Values**
   - Spreadsheet : "Leads — Sécurité Incendie Pro"
   - Range : A:N (toutes les colonnes)
4. Module 2 : **Gmail → Send an Email**
   - To : wloureiro67@gmail.com
   - Subject : `📊 Rapport semaine — {{count(1.values)}} leads`
   - Body (texte simple) :
     ```
     Leads cette semaine : {{count(1.values)}}

     Détail :
     {{join(map(1.values; "row"); "\n")}}
     ```

---

## 📋 ORDRE D'ACTIVATION RECOMMANDÉ

1. **Aujourd'hui** : Scénario 3 (rapport hebdo — le plus simple, 10 min)
2. **Cette semaine** : Scénario 1 (réseaux sociaux — connecter Buffer)
3. **Semaine prochaine** : Scénario 2 (articles — connecter GitHub + Search Console)

---

## 📁 Fichiers créés

| Fichier | Usage |
|---------|-------|
| `make-config/make-social-media-config.md` | Config détaillée des 3 scénarios |
| `seo/content-bank.md` | Banque de contenu (2 semaines pré-remplies) |
| `prompt-cowork-hebdo.md` | Prompt à coller chaque lundi dans Claude |
| `guide-systeme-complet.md` | Guide complet + checklists + troubleshooting |
| `make-config/NEXT-STEPS.md` | Ce fichier |
