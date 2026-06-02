"""
Soumet toutes les URLs du site à IndexNow (Bing/Yandex) en une seule requête.
À exécuter après chaque déploiement sur Vercel.
Prérequis : le fichier securiteincendiepro2026idx.txt doit être accessible sur le site.
"""
import urllib.request, json, sys

KEY = "securiteincendiepro2026idx"
HOST = "www.securiteincendiepro.fr"

# Modifiez cette liste au fur et à mesure des nouvelles publications
URLS = [
    "https://www.securiteincendiepro.fr/",
    "https://www.securiteincendiepro.fr/diagnostic-incendie-entreprise.html",
    "https://www.securiteincendiepro.fr/extincteur-obligatoire-entreprise.html",
    "https://www.securiteincendiepro.fr/normes-securite-incendie-erp.html",
    "https://www.securiteincendiepro.fr/mise-aux-normes-incendie.html",
    "https://www.securiteincendiepro.fr/blog.html",
    "https://www.securiteincendiepro.fr/a-propos.html",
    "https://www.securiteincendiepro.fr/securite-incendie-strasbourg.html",
    "https://www.securiteincendiepro.fr/securite-incendie-paris.html",
    "https://www.securiteincendiepro.fr/securite-incendie-lyon.html",
    "https://www.securiteincendiepro.fr/securite-incendie-marseille.html",
    "https://www.securiteincendiepro.fr/securite-incendie-bordeaux.html",
    "https://www.securiteincendiepro.fr/securite-incendie-toulouse.html",
    "https://www.securiteincendiepro.fr/securite-incendie-nantes.html",
    "https://www.securiteincendiepro.fr/securite-incendie-lille.html",
    "https://www.securiteincendiepro.fr/securite-incendie-nice.html",
    "https://www.securiteincendiepro.fr/securite-incendie-rennes.html",
    "https://www.securiteincendiepro.fr/securite-incendie-montpellier.html",
    "https://www.securiteincendiepro.fr/securite-incendie-nancy.html",
    "https://www.securiteincendiepro.fr/securite-incendie-metz.html",
    "https://www.securiteincendiepro.fr/securite-incendie-reims.html",
    "https://www.securiteincendiepro.fr/securite-incendie-mulhouse.html",
    "https://www.securiteincendiepro.fr/securite-incendie-colmar.html",
    "https://www.securiteincendiepro.fr/securite-incendie-metz.html",
    "https://www.securiteincendiepro.fr/articles/detecteur-fumee-obligatoire-entreprise-2026.html",
    "https://www.securiteincendiepro.fr/articles/securite-incendie-restaurant-obligations-2026.html",
    "https://www.securiteincendiepro.fr/articles/plan-evacuation-incendie-entreprise-obligations-2026.html",
    "https://www.securiteincendiepro.fr/articles/extincteur-obligatoire-entreprise-reglementation-2026.html",
    "https://www.securiteincendiepro.fr/articles/checklist-securite-incendie-restaurant-2026.html",
    "https://www.securiteincendiepro.fr/articles/commission-securite-erp-comment-se-preparer.html",
    "https://www.securiteincendiepro.fr/articles/installation-alarme-incendie.html",
    "https://www.securiteincendiepro.fr/articles/norme-incendie-erp-guide-complet-obligations-2026.html",
    "https://www.securiteincendiepro.fr/articles/plan-intervention-incendie-obligatoire-erp-2026.html",
    "https://www.securiteincendiepro.fr/articles/securite-incendie-entrepot-logistique-obligations-2026.html",
]

payload = json.dumps({
    "host": HOST,
    "key": KEY,
    "keyLocation": f"https://{HOST}/{KEY}.txt",
    "urlList": URLS
}).encode("utf-8")

req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=payload,
    headers={"Content-Type": "application/json; charset=utf-8"},
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        print(f"Réponse IndexNow : {resp.status} {resp.reason}")
        print(f"{len(URLS)} URLs soumises.")
except Exception as e:
    print(f"Erreur : {e}", file=sys.stderr)
    print("Vérifiez que le fichier {KEY}.txt est accessible sur le site déployé.")
