"""
Ajoute og:image, twitter:image et favicon.svg à toutes les pages HTML
qui ne les ont pas encore. À exécuter une seule fois.
"""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))

OG_IMAGE_TAGS = '''\n  <meta property="og:image" content="https://www.securiteincendiepro.fr/og-image.svg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Diagnostic sécurité incendie gratuit — SecuriteIncendiePro.fr">
  <meta name="twitter:image" content="https://www.securiteincendiepro.fr/og-image.svg">'''

FAVICON_TAGS = '''\n  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="icon" type="image/png" href="/logo.png" sizes="32x32">
  <link rel="apple-touch-icon" href="/logo.png">'''

files = (
    glob.glob(os.path.join(ROOT, "*.html")) +
    glob.glob(os.path.join(ROOT, "articles", "*.html"))
)

patched, skipped = 0, 0

for path in sorted(files):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False

    # og:image
    if 'og:image' not in content:
        # Insère juste avant </head>
        if 'og:url' in content:
            # Après la dernière balise og:url
            content = re.sub(
                r'(<meta property="og:url"[^>]*>)',
                lambda m: m.group(0) + OG_IMAGE_TAGS,
                content, count=1
            )
        else:
            content = content.replace('</head>', OG_IMAGE_TAGS + '\n</head>', 1)
        changed = True

    # favicon.svg
    if 'favicon.svg' not in content:
        # Remplace l'éventuel favicon logo.png existant ou insère avant </head>
        if '<link rel="icon"' in content:
            content = re.sub(
                r'<link rel="icon"[^>]*>',
                FAVICON_TAGS.strip(),
                content, count=1
            )
        else:
            content = content.replace('</head>', FAVICON_TAGS + '\n</head>', 1)
        changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  PATCHED  {os.path.relpath(path, ROOT)}")
        patched += 1
    else:
        print(f"  OK       {os.path.relpath(path, ROOT)}")
        skipped += 1

print(f"\n{patched} fichiers mis à jour, {skipped} déjà à jour.")
