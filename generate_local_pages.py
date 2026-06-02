"""
Génère les pages locales manquantes : Toulouse, Nantes, Nice, Rennes, Montpellier
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

cities = [
    {
        "slug": "toulouse",
        "name": "Toulouse",
        "dept": "31",
        "dept_name": "Haute-Garonne",
        "region": "Occitanie",
        "badge": "📍 Toulouse & Haute-Garonne (31)",
        "hero_sub": "Diagnostic gratuit et devis d'installateurs APSAD certifiés en Occitanie — Réponse sous 24h",
        "form_id": "formToulouse",
        "form_slug": "tlse",
        "form_placeholder": "Toulouse, Blagnac, Colomiers…",
        "btn_text": "Diagnostic gratuit Toulouse →",
        "success_msg": "Un installateur du 31 vous contacte sous <strong>24h</strong>.",
        "area_served": ["Toulouse", "Blagnac", "Colomiers", "Tournefeuille", "Ramonville-Saint-Agne", "Labège"],
        "h2_obligations": "Sécurité incendie à Toulouse : obligations 2026",
        "p1": "Toulouse, capitale de l'Occitanie, est la 4e ville de France par sa population. Avec une croissance démographique soutenue et un tissu économique dense — aéronautique, high-tech, enseignement supérieur — les ERP y sont nombreux et les contrôles de conformité incendie réguliers.",
        "p2": "Le SDIS 31 (Service Départemental d'Incendie et de Secours de Haute-Garonne) a renforcé ses inspections depuis 2026, notamment dans les zones à forte densité (hypercentre, quartier des Carmes, Capitole) et dans les locaux à risques industriels (Airbus, zones d'activités périphériques).",
        "h2_zone": "Zones d'intervention en Haute-Garonne",
        "zones": [
            "<strong>Toulouse</strong> (tous quartiers)",
            "Blagnac, Colomiers, Tournefeuille",
            "Labège, Ramonville, Castanet-Tolosan",
            "Muret, Saint-Gaudens",
            "Tarbes et Hautes-Pyrénées (65)",
            "Et toutes les communes du 31",
        ],
        "h2_sectors": "Secteurs d'activité spécifiques à Toulouse",
        "sectors": [
            ("Aéronautique et industrie", "La présence d'Airbus et de nombreux sous-traitants aéronautiques en périphérie de Toulouse génère des obligations incendie renforcées pour les entrepôts et ateliers : systèmes sprinklers, désenfumage, détection gaz."),
            ("Universités et grandes écoles", "Toulouse est l'une des premières villes universitaires de France. Les ERP de type R (enseignement) concentrent des milliers d'étudiants et sont soumis à des contrôles stricts de la commission de sécurité."),
            ("Commerce et restauration", "Du Capitole aux galeries marchandes périphériques, les commerces et restaurants toulousains doivent satisfaire aux obligations ERP type M et N, avec des délais d'intervention de 48h pour nos installateurs partenaires."),
        ],
        "faq": [
            ("Les obligations incendie sont-elles les mêmes à Toulouse qu'ailleurs en France ?", "Oui. La réglementation incendie (arrêté du 25 juin 1980 pour les ERP, Code du Travail pour les locaux de travail) est nationale et s'applique de manière identique à Toulouse. Seuls les délais de contrôle et la fréquence des inspections peuvent varier selon l'activité du SDIS 31."),
            ("Mon atelier industriel à Blagnac est-il concerné ?", "Oui. Tout local de travail employant au moins un salarié est soumis aux obligations d'extinction et d'alarme du Code du Travail. Les locaux industriels ont en outre des exigences spécifiques selon leur activité (ICPE). Un installateur APSAD certifié évaluera gratuitement votre situation."),
        ],
        "sidebar_city1": ("securite-incendie-bordeaux.html", "Sécurité incendie Bordeaux"),
        "sidebar_city2": ("securite-incendie-marseille.html", "Sécurité incendie Marseille"),
    },
    {
        "slug": "nantes",
        "name": "Nantes",
        "dept": "44",
        "dept_name": "Loire-Atlantique",
        "region": "Pays de la Loire",
        "badge": "📍 Nantes & Loire-Atlantique (44)",
        "hero_sub": "Diagnostic gratuit et devis d'installateurs APSAD certifiés en Pays de la Loire — Réponse sous 24h",
        "form_id": "formNantes",
        "form_slug": "nts",
        "form_placeholder": "Nantes, Saint-Herblain, Rezé…",
        "btn_text": "Diagnostic gratuit Nantes →",
        "success_msg": "Un installateur du 44 vous contacte sous <strong>24h</strong>.",
        "area_served": ["Nantes", "Saint-Herblain", "Rezé", "Saint-Nazaire", "La Baule", "Ancenis"],
        "h2_obligations": "Sécurité incendie à Nantes : obligations 2026",
        "p1": "Nantes, capitale des Pays de la Loire, est l'une des métropoles françaises à la croissance la plus rapide. Avec son port industriel de Saint-Nazaire, ses chantiers navals et son tissu tertiaire en pleine expansion, la ville concentre de nombreux ERP et locaux de travail soumis aux obligations de sécurité incendie.",
        "p2": "Le SDIS 44 a intensifié ses contrôles sur les établissements recevant du public depuis le renforcement de la réglementation de janvier 2026. Les zones de forte densité (île de Nantes, Erdre, Rezé) et les zones industrielles de Saint-Herblain font l'objet d'une attention particulière.",
        "h2_zone": "Zones d'intervention en Loire-Atlantique",
        "zones": [
            "<strong>Nantes</strong> (tous quartiers)",
            "Saint-Herblain, Rezé, Orvault, La Chapelle-sur-Erdre",
            "Saint-Nazaire, Pornic, La Baule",
            "Ancenis, Châteaubriant",
            "Et toutes les communes du 44",
        ],
        "h2_sectors": "Secteurs d'activité spécifiques à Nantes",
        "sectors": [
            ("Industrie navale et portuaire", "Les chantiers de l'Atlantique à Saint-Nazaire et les zones portuaires de Nantes sont des ICPE soumises à des réglementations incendie strictes : systèmes sprinklers, mousse haute expansion, détection gaz."),
            ("Bureaux et locaux tertiaires", "Le quartier d'affaires Euronantes et l'île de Nantes concentrent de nombreux ERP de type W (bureaux). Ces établissements doivent disposer d'une alarme incendie adaptée à leur effectif et d'extincteurs vérifiés annuellement."),
            ("Commerce et grande distribution", "Les centres commerciaux Atlantis, Beaulieu et les zones commerciales périphériques regroupent des ERP de type M aux obligations les plus contraignantes."),
        ],
        "faq": [
            ("Quels risques spécifiques à Nantes en matière de sécurité incendie ?", "Nantes est une ville à forte densité de bâti ancien (centre historique, quartier Bouffay). Ces bâtiments présentent souvent des configurations d'évacuation complexes nécessitant une adaptation des équipements. Un diagnostic gratuit permet d'identifier les mises en conformité nécessaires."),
            ("Mon entrepôt de la zone industrielle de Saint-Herblain est-il concerné par ICPE ?", "Cela dépend de la nature et du volume de produits stockés. Les entrepôts de plus de 500 m² ou stockant des produits inflammables relèvent généralement de la réglementation ICPE avec des obligations renforcées. Nos installateurs APSAD maîtrisent parfaitement ces réglementations."),
        ],
        "sidebar_city1": ("securite-incendie-paris.html", "Sécurité incendie Paris"),
        "sidebar_city2": ("securite-incendie-lyon.html", "Sécurité incendie Lyon"),
    },
    {
        "slug": "nice",
        "name": "Nice",
        "dept": "06",
        "dept_name": "Alpes-Maritimes",
        "region": "Provence-Alpes-Côte d'Azur",
        "badge": "📍 Nice & Alpes-Maritimes (06)",
        "hero_sub": "Diagnostic gratuit et devis d'installateurs APSAD certifiés sur la Côte d'Azur — Réponse sous 24h",
        "form_id": "formNice",
        "form_slug": "nice",
        "form_placeholder": "Nice, Cannes, Antibes…",
        "btn_text": "Diagnostic gratuit Nice →",
        "success_msg": "Un installateur du 06 vous contacte sous <strong>24h</strong>.",
        "area_served": ["Nice", "Cannes", "Antibes", "Cagnes-sur-Mer", "Menton", "Grasse"],
        "h2_obligations": "Sécurité incendie à Nice : obligations 2026",
        "p1": "Nice, capitale de la Riviera française et 5e ville de France, est une destination touristique mondiale. Avec ses hôtels, ses restaurants gastronomiques, ses musées et ses lieux de spectacle, la ville concentre une densité exceptionnelle d'ERP soumis aux obligations les plus strictes.",
        "p2": "Le SDIS 06 et la Direction Départementale des Territoires et de la Mer (DDTM) des Alpes-Maritimes ont renforcé leurs contrôles depuis le 1er janvier 2026. La saison touristique (juin-septembre) est une période critique : les établissements non conformes peuvent être fermés à la veille de leur période de plus forte activité.",
        "h2_zone": "Zones d'intervention dans les Alpes-Maritimes",
        "zones": [
            "<strong>Nice</strong> (tous quartiers)",
            "Cannes, Antibes, Juan-les-Pins",
            "Cagnes-sur-Mer, Vence, Saint-Paul-de-Vence",
            "Menton, Monaco (Principauté)",
            "Grasse, Mougins",
            "Et toutes les communes du 06",
        ],
        "h2_sectors": "Secteurs d'activité spécifiques à Nice",
        "sectors": [
            ("Hôtellerie et tourisme de luxe", "La Côte d'Azur concentre les hôtels de luxe parmi les plus contrôlés de France. Ces ERP de type O sont soumis à des exigences maximales : SSI catégorie A, détection automatique dans les chambres, compartimentage coupe-feu. Nos installateurs connaissent les contraintes des immeubles haussmanniens et des villas de prestige."),
            ("Restaurants et établissements de nuit", "La promenade des Anglais, le Vieux-Nice et les plages privées concentrent une densité remarquable de restaurants et bars. Les établissements avec terrasse ou cuisine de plein air ont des obligations spécifiques en désenfumage et extinction."),
            ("Commerces et galeries d'art", "Nice Étoile, Carré d'Or et les nombreuses galeries d'art de la ville sont des ERP dont les exigences incendie s'appliquent aussi bien au bâtiment qu'aux œuvres de grande valeur. Les systèmes de suppression automatique d'incendie adaptés aux espaces culturels sont notre spécialité."),
        ],
        "faq": [
            ("La réglementation incendie est-elle différente sur la Côte d'Azur ?", "Non, la réglementation nationale s'applique identiquement. En revanche, le profil très touristique des établissements niçois (hôtels, restaurants, discothèques) implique souvent des catégories ERP élevées avec des niveaux d'exigence maximaux."),
            ("Mon restaurant dispose d'une terrasse extérieure. Suis-je concerné ?", "Oui. Les terrasses exploitées commercialement sont considérées comme faisant partie de l'ERP dès lors qu'elles sont couvertes ou semi-couvertes. Les obligations en extincteurs et en signalétique s'appliquent également aux espaces extérieurs."),
        ],
        "sidebar_city1": ("securite-incendie-marseille.html", "Sécurité incendie Marseille"),
        "sidebar_city2": ("securite-incendie-lyon.html", "Sécurité incendie Lyon"),
    },
    {
        "slug": "rennes",
        "name": "Rennes",
        "dept": "35",
        "dept_name": "Ille-et-Vilaine",
        "region": "Bretagne",
        "badge": "📍 Rennes & Ille-et-Vilaine (35)",
        "hero_sub": "Diagnostic gratuit et devis d'installateurs APSAD certifiés en Bretagne — Réponse sous 24h",
        "form_id": "formRennes",
        "form_slug": "rns",
        "form_placeholder": "Rennes, Saint-Malo, Bruz…",
        "btn_text": "Diagnostic gratuit Rennes →",
        "success_msg": "Un installateur du 35 vous contacte sous <strong>24h</strong>.",
        "area_served": ["Rennes", "Saint-Malo", "Fougères", "Vitré", "Bruz", "Cesson-Sévigné"],
        "h2_obligations": "Sécurité incendie à Rennes : obligations 2026",
        "p1": "Rennes, capitale de la Bretagne, est une métropole universitaire dynamique. Avec ses 70 000 étudiants, ses nombreux commerces, restaurants et établissements culturels, la ville dispose d'un tissu d'ERP varié. La Bretagne est également une région touristique avec un fort afflux estival en bord de mer.",
        "p2": "Le SDIS 35 effectue des contrôles réguliers, en particulier dans le centre historique de Rennes et dans les nouvelles zones d'activités périphériques (Rennes Atalante, ZAC de la Courrouze). La conformité incendie est une priorité pour les établissements accueillant du public dans la région.",
        "h2_zone": "Zones d'intervention en Ille-et-Vilaine",
        "zones": [
            "<strong>Rennes</strong> (tous quartiers)",
            "Cesson-Sévigné, Bruz, Pacé, Saint-Jacques-de-la-Lande",
            "Saint-Malo, Dinard",
            "Fougères, Vitré, Redon",
            "Et toutes les communes du 35",
        ],
        "h2_sectors": "Secteurs d'activité spécifiques à Rennes",
        "sectors": [
            ("Enseignement et campus universitaires", "Rennes est l'une des premières villes universitaires de France. Les ERP de type R (enseignement) — universités, grandes écoles, lycées — sont parmi les établissements les plus strictement contrôlés. Les obligations incluent un SSI adapté et des exercices d'évacuation semestriels."),
            ("Commerce et restauration du centre-ville", "La rue de la Monnaie, la place Sainte-Anne et les Lices concentrent restaurants et commerces de proximité. Ces ERP de types M et N bénéficient d'une densité d'installateurs APSAD partenaires pour des interventions rapides."),
            ("Zones industrielles et tertiaires", "Rennes Atalante (technopole), ZAC de la Courrouze et zone industrielle nord regroupent des locaux tertiaires et industriels avec des obligations spécifiques selon l'activité."),
        ],
        "faq": [
            ("Mon restaurant dans le centre historique de Rennes est-il soumis à des contraintes spécifiques ?", "Les bâtiments historiques présentent parfois des contraintes architecturales (murs porteurs, plafonds bas, escaliers étroits) qui nécessitent des solutions d'évacuation adaptées. Nos installateurs APSAD sont habitués à travailler dans ce type de bâti."),
            ("La proximité de la mer (Saint-Malo) change-t-elle les obligations ?", "Non directement. Cependant, l'humidité et le sel marin accélèrent la corrosion des équipements incendie. La vérification annuelle prend encore plus d'importance dans les établissements côtiers pour maintenir les équipements en parfait état de fonctionnement."),
        ],
        "sidebar_city1": ("securite-incendie-nantes.html", "Sécurité incendie Nantes") if False else ("securite-incendie-paris.html", "Sécurité incendie Paris"),
        "sidebar_city2": ("securite-incendie-lyon.html", "Sécurité incendie Lyon"),
    },
    {
        "slug": "montpellier",
        "name": "Montpellier",
        "dept": "34",
        "dept_name": "Hérault",
        "region": "Occitanie",
        "badge": "📍 Montpellier & Hérault (34)",
        "hero_sub": "Diagnostic gratuit et devis d'installateurs APSAD certifiés en Occitanie — Réponse sous 24h",
        "form_id": "formMontpellier",
        "form_slug": "mtp",
        "form_placeholder": "Montpellier, Castelnau, Lunel…",
        "btn_text": "Diagnostic gratuit Montpellier →",
        "success_msg": "Un installateur du 34 vous contacte sous <strong>24h</strong>.",
        "area_served": ["Montpellier", "Castelnau-le-Lez", "Lattes", "Palavas-les-Flots", "Sète", "Béziers"],
        "h2_obligations": "Sécurité incendie à Montpellier : obligations 2026",
        "p1": "Montpellier est la métropole française à la croissance la plus rapide depuis 20 ans. Ville étudiante, touristique et médicale (CHU, pôle santé), elle concentre une variété d'ERP particulièrement étendue. La chaleur estivale et la sécheresse du climat méditerranéen amplifient les risques incendie.",
        "p2": "Le SDIS 34 (Hérault) a renforcé ses contrôles sur les établissements touristiques du littoral et les zones commerciales en forte croissance. La conformité incendie est d'autant plus critique que le risque feu de forêt est élevé en périphérie, augmentant les exigences pour les bâtiments en zone d'interface.",
        "h2_zone": "Zones d'intervention dans l'Hérault",
        "zones": [
            "<strong>Montpellier</strong> (tous quartiers)",
            "Castelnau-le-Lez, Lattes, Palavas-les-Flots",
            "Lunel, Sète, Agde",
            "Béziers, Frontignan",
            "Et toutes les communes du 34",
        ],
        "h2_sectors": "Secteurs d'activité spécifiques à Montpellier",
        "sectors": [
            ("CHU et établissements de santé", "Montpellier abrite l'un des plus grands CHU de France. Les ERP de type U (établissements de soins) et J (hébergement de personnes âgées ou handicapées) sont soumis aux obligations les plus strictes du règlement de sécurité : SSI catégorie A, détection automatique complète, compartimentage renforcé."),
            ("Pôle universitaire et grandes écoles", "Avec plus de 80 000 étudiants, Montpellier est la 3e ville universitaire de France. Les campus concentrent de nombreux ERP de type R avec des exercices d'évacuation obligatoires deux fois par an."),
            ("Tourisme et littoral", "Palavas-les-Flots, La Grande-Motte et les stations balnéaires de l'Hérault voient leur population décupler en été. Les hôtels, campings et restaurants de plage doivent être conformes avant la saison touristique."),
        ],
        "faq": [
            ("Le risque de feu de forêt modifie-t-il les obligations incendie de mon entreprise ?", "Pas directement pour les ERP. Cependant, les bâtiments situés en Zone de Danger (ZD) ou Zone d'Alerte (ZA) dans les Plans de Prévention des Risques Incendie de Forêt (PPRIF) peuvent être soumis à des obligations complémentaires sur les débroussaillements et les distances de sécurité."),
            ("Mon hôtel de bord de mer est-il soumis à des contrôles plus fréquents l'été ?", "Oui. Les établissements touristiques à forte saisonnalité font l'objet de contrôles préventifs avant l'ouverture de la saison. Il est recommandé de faire réaliser un diagnostic de conformité chaque printemps pour éviter toute fermeture en pleine saison."),
        ],
        "sidebar_city1": ("securite-incendie-marseille.html", "Sécurité incendie Marseille"),
        "sidebar_city2": ("securite-incendie-toulouse.html", "Sécurité incendie Toulouse"),
    },
]


TEMPLATE = '''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sécurité Incendie {name} — Installateur APSAD Certifié | Devis Gratuit</title>
  <meta name="description" content="Sécurité incendie à {name} et dans le {dept_name} ({dept}) : diagnostic gratuit, devis d'installateurs APSAD certifiés. Mise en conformité ERP 2026, alarme incendie, extincteurs. Réponse sous 24h.">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <meta name="author" content="SecuriteIncendiePro.fr">
  <link rel="canonical" href="https://www.securiteincendiepro.fr/securite-incendie-{slug}.html">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="SecuriteIncendiePro.fr">
  <meta property="og:title" content="Sécurité Incendie {name} — Diagnostic Gratuit &amp; Installateur APSAD">
  <meta property="og:description" content="Diagnostic sécurité incendie gratuit à {name}. Installateurs APSAD certifiés dans le {dept_name} ({dept}). Conformité ERP 2026, devis sous 24h.">
  <meta property="og:url" content="https://www.securiteincendiepro.fr/securite-incendie-{slug}.html">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:image" content="https://www.securiteincendiepro.fr/og-image.svg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Diagnostic sécurité incendie gratuit — SecuriteIncendiePro.fr">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Sécurité Incendie {name} — Diagnostic Gratuit">
  <meta name="twitter:description" content="Diagnostic sécurité incendie gratuit à {name}. Installateurs APSAD certifiés dans le {dept_name}. Conformité ERP 2026.">
  <meta name="twitter:image" content="https://www.securiteincendiepro.fr/og-image.svg">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "LocalBusiness",
        "@id": "https://www.securiteincendiepro.fr/securite-incendie-{slug}.html#local",
        "name": "SecuriteIncendiePro.fr — {name}",
        "description": "Service de mise en relation avec des installateurs certifiés APSAD en sécurité incendie à {name} et dans le {dept_name}.",
        "url": "https://www.securiteincendiepro.fr/securite-incendie-{slug}.html",
        "logo": "https://www.securiteincendiepro.fr/logo.png",
        "telephone": "+33775754921",
        "priceRange": "Gratuit",
        "areaServed": {area_served_json},
        "parentOrganization": {{
          "@id": "https://www.securiteincendiepro.fr/#organization"
        }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://www.securiteincendiepro.fr/"}},
          {{"@type": "ListItem", "position": 2, "name": "Sécurité Incendie {name}", "item": "https://www.securiteincendiepro.fr/securite-incendie-{slug}.html"}}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": {faq_json}
      }}
    ]
  }}
  </script>
  <link rel="stylesheet" href="/styles.css">
  <style>
    .header-nav{{display:flex;gap:20px;align-items:center}}
    .header-nav a{{color:white;text-decoration:none;font-size:.85rem;font-weight:600;opacity:.9}}
    .header-nav a:hover{{opacity:1;text-decoration:underline}}
    @media(max-width:640px){{.header-nav{{display:none}}}}
  </style>
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="icon" type="image/png" href="/logo.png" sizes="32x32">
  <link rel="apple-touch-icon" href="/logo.png">
</head>
<body>

<header class="site-header">
  <a href="index.html" class="site-logo">
    <img src="logo.png" alt="Sécurité Incendie Pro" height="44" loading="lazy">
  </a>
  <a href="tel:+33775754921" class="header-phone">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
    07 75 75 49 21
  </a>
  <nav class="header-nav">
    <a href="/blog.html">Blog</a>
    <a href="/diagnostic-incendie-entreprise.html">Diagnostic</a>
    <a href="/extincteur-obligatoire-entreprise.html">Extincteurs</a>
    <a href="/normes-securite-incendie-erp.html">Normes ERP</a>
  </nav>
</header>

<div class="page-hero">
  <div class="page-hero-inner">
    <div class="page-hero-badge">{badge}</div>
    <h1>Sécurité Incendie à {name}</h1>
    <p>{hero_sub}</p>
  </div>
</div>

<div class="page-wrap">
  <div class="page-content">

    <div class="article-alert">
      <strong>&#128205; Service local :</strong> Notre réseau d'installateurs certifiés couvre {name} et tout le département du {dept_name} ({dept}) : {area_served_str} et toutes les communes alentour.
    </div>

    <h2>{h2_obligations}</h2>
    <p>{p1}</p>
    <p>{p2}</p>
    <p>Tout ERP non conforme s'expose à une amende pouvant atteindre <strong>45 000 €</strong> et une fermeture administrative immédiate. Consultez notre guide sur les <a href="/normes-securite-incendie-erp.html">normes de sécurité incendie ERP</a> et <a href="/articles/commission-securite-erp-comment-se-preparer.html">comment se préparer à la commission de sécurité</a>.</p>

    <h2>Nos installateurs APSAD certifiés à {name}</h2>
    <p>SecuriteIncendiePro.fr met en relation les entreprises du {dept_name} avec des installateurs certifiés APSAD, sélectionnés pour leur expertise et leur réactivité :</p>
    <ul>
      <li><strong>Certification APSAD R1</strong> — Systèmes de détection incendie (SDI/SSI)</li>
      <li><strong>Certification APSAD R4</strong> — Extincteurs et robinets d'incendie armés</li>
      <li><strong>Certification APSAD R7</strong> — Systèmes sprinklers</li>
      <li><strong>Certification APSAD R17</strong> — Systèmes de désenfumage</li>
    </ul>

    <h2>{h2_zone}</h2>
    <ul>
{zones_html}
    </ul>

    <h2>{h2_sectors}</h2>
{sectors_html}

    <h2>Comment obtenir votre diagnostic à {name} ?</h2>
    <p>Le processus est simple et entièrement gratuit :</p>
    <ol>
      <li>Remplissez le formulaire avec votre type de local et votre adresse à {name}</li>
      <li>Un installateur APSAD de votre secteur vous contacte sous 24h</li>
      <li>Il réalise un audit de conformité de votre établissement</li>
      <li>Vous recevez un plan de mise en conformité avec <a href="/diagnostic-incendie-entreprise.html">devis détaillé</a></li>
      <li>Vous choisissez librement — sans engagement</li>
    </ol>

    <h2>FAQ — Sécurité incendie à {name}</h2>
    <div class="faq-list">
{faq_html}
    </div>

  </div>

  <aside class="page-sidebar">
    <div class="sidebar-form">
      <div class="form-card-header">
        <span class="form-badge">&#128205; {name}</span>
        <strong>Diagnostic gratuit</strong>
        <p>Installateur APSAD dans le {dept}</p>
      </div>
      <div class="form-card-body">
        <form class="lead-form" id="{form_id}" novalidate>
          <div class="field">
            <label for="type_local_{form_slug}">Type de local *</label>
            <select name="type_local" id="type_local_{form_slug}" required>
              <option value="">-- Sélectionnez --</option>
              <option value="Restaurant / Bar">Restaurant / Bar</option>
              <option value="Commerce / Boutique">Commerce / Boutique</option>
              <option value="Bureau / Open space">Bureau / Open space</option>
              <option value="Entrepôt / Stockage">Entrepôt / Stockage</option>
              <option value="Hôtel / Hébergement">Hôtel / Hébergement</option>
              <option value="Établissement scolaire">Établissement scolaire</option>
              <option value="Salle de sport / Loisirs">Salle de sport / Loisirs</option>
              <option value="Industrie / Atelier">Industrie / Atelier</option>
              <option value="Autre ERP">Autre ERP</option>
            </select>
          </div>
          <div class="field">
            <label for="ville_{form_slug}">Commune *</label>
            <input type="text" name="ville" id="ville_{form_slug}" placeholder="{form_placeholder}" required>
          </div>
          <div class="field">
            <label for="telephone_{form_slug}">Téléphone *</label>
            <input type="tel" name="telephone" id="telephone_{form_slug}" placeholder="06 XX XX XX XX" required>
          </div>
          <div class="field">
            <label for="email_{form_slug}">Email *</label>
            <input type="email" name="email" id="email_{form_slug}" placeholder="vous@entreprise.fr" required>
          </div>
          <button type="submit" class="btn-cta">{btn_text}</button>
        </form>
        <div class="form-success" style="display:none">
          <div class="success-icon">&#9989;</div>
          <h3>Demande envoyée !</h3>
          <p>{success_msg}</p>
        </div>
      </div>
    </div>
    <div class="sidebar-links">
      <h4>Guides pratiques</h4>
      <a href="/normes-securite-incendie-erp.html">Normes ERP 2026</a>
      <a href="/extincteur-obligatoire-entreprise.html">Extincteurs obligatoires</a>
      <a href="/mise-aux-normes-incendie.html">Mise aux normes incendie</a>
      <a href="/diagnostic-incendie-entreprise.html">Diagnostic incendie</a>
      <h4 style="margin-top:16px">Articles</h4>
      <a href="/articles/commission-securite-erp-comment-se-preparer.html">Commission de sécurité ERP</a>
      <a href="/articles/extincteur-obligatoire-entreprise-reglementation-2026.html">Extincteurs 2026</a>
      <a href="/articles/detecteur-fumee-obligatoire-entreprise-2026.html">Détecteur de fumée</a>
      <h4 style="margin-top:16px">Autres villes</h4>
      <a href="/{sidebar_city1_url}">{sidebar_city1_name}</a>
      <a href="/{sidebar_city2_url}">{sidebar_city2_name}</a>
      <a href="/securite-incendie-strasbourg.html">Sécurité incendie Strasbourg</a>
    </div>
  </aside>
</div>

<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-logo">
      <strong>SecuriteIncendiePro.fr</strong>
      <small>Service gratuit de mise en relation avec des installateurs certifiés APSAD partout en France.</small>
    </div>
    <div class="footer-links">
      <a href="index.html">Accueil</a>
      <a href="blog.html">Blog</a>
      <a href="mentions-legales.html">Mentions légales</a>
      <a href="politique-confidentialite.html">Politique de confidentialité</a>
    </div>
    <p class="footer-copy">&copy; 2026 SecuriteIncendiePro.fr — Tous droits réservés</p>
  </div>
</footer>

<div class="sticky-mobile">
  <a href="#{form_id}" class="sticky-btn sticky-diag">Diagnostic gratuit</a>
  <a href="tel:+33775754921" class="sticky-btn sticky-call">&#128222; Appeler</a>
</div>

<script src="/script.js" defer></script>
</body>
</html>
'''

import json

for city in cities:
    slug = city["slug"]
    path = os.path.join(ROOT, f"securite-incendie-{slug}.html")
    if os.path.exists(path):
        print(f"  SKIP (exists) securite-incendie-{slug}.html")
        continue

    area_served_json = json.dumps(
        [{"@type": "City", "name": c} for c in city["area_served"]] +
        [{"@type": "AdministrativeArea", "name": city["dept_name"]}],
        ensure_ascii=False
    )

    faq_items = []
    for q, a in city["faq"]:
        faq_items.append(f'{{"@type": "Question", "name": "{q}", "acceptedAnswer": {{"@type": "Answer", "text": "{a}"}}}}')
    faq_json = "[\n          " + ",\n          ".join(faq_items) + "\n        ]"

    zones_html = "\n".join(f"      <li>{z}</li>" for z in city["zones"])

    sectors_html = ""
    for title, text in city["sectors"]:
        sectors_html += f"    <h3>{title}</h3>\n    <p>{text}</p>\n"

    faq_html = ""
    for q, a in city["faq"]:
        faq_html += f"""      <div class="faq-item">
        <h3>{q}</h3>
        <p>{a}</p>
      </div>\n"""

    area_served_str = ", ".join(city["area_served"])

    html = TEMPLATE.format(
        name=city["name"],
        slug=city["slug"],
        dept=city["dept"],
        dept_name=city["dept_name"],
        region=city["region"],
        badge=city["badge"],
        hero_sub=city["hero_sub"],
        form_id=city["form_id"],
        form_slug=city["form_slug"],
        form_placeholder=city["form_placeholder"],
        btn_text=city["btn_text"],
        success_msg=city["success_msg"],
        h2_obligations=city["h2_obligations"],
        p1=city["p1"],
        p2=city["p2"],
        h2_zone=city["h2_zone"],
        h2_sectors=city["h2_sectors"],
        area_served_json=area_served_json,
        faq_json=faq_json,
        zones_html=zones_html,
        sectors_html=sectors_html,
        faq_html=faq_html,
        area_served_str=area_served_str,
        sidebar_city1_url=city["sidebar_city1"][0],
        sidebar_city1_name=city["sidebar_city1"][1],
        sidebar_city2_url=city["sidebar_city2"][0],
        sidebar_city2_name=city["sidebar_city2"][1],
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  CREATED  securite-incendie-{slug}.html")

print("\nFait.")
