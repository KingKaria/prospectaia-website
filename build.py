"""
Build script for the ProspectaIA static site.

Regenerates every root .html page from:
  - pages/<name>.html   -> per-page <head> extras + body content
  - partials/nav.html   -> shared nav menu (single source of truth)
  - partials/footer.html -> shared footer (single source of truth)

Also regenerates sitemap.xml, listing every page in pages/ under the
domain declared in CNAME.

Usage: python build.py
Run this after editing anything in pages/ or partials/.
"""
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
PAGES_DIR = ROOT / "pages"
PARTIALS_DIR = ROOT / "partials"
SITE_URL = "https://" + (ROOT / "CNAME").read_text(encoding="utf-8").strip()

FAVICON = (
    "data:image/svg+xml,"
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>"
    "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
    "<stop offset='0' stop-color='%23667eea'/>"
    "<stop offset='1' stop-color='%2300d4ff'/>"
    "</linearGradient></defs>"
    "<rect width='100' height='100' rx='24' fill='url(%23g)'/>"
    "<text x='50' y='69' font-family='Segoe UI, Arial, sans-serif' "
    "font-size='58' font-weight='800' fill='white' text-anchor='middle'>P</text>"
    "</svg>"
)

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="{favicon}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{meta}
</head>
<body>

<header class="navbar" id="navbar">
  <div class="container navbar-inner">
    <a href="/" class="logo"><span class="logo-mark">P</span>Prospecta<span>IA</span></a>

    {nav}
    <a href="contacto.html" class="btn btn-cta">Iniciar Conversa</a>

    <button class="hamburger" id="hamburger" aria-label="Abrir menu de navegação">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

{body}

{footer}

<script src="js/script.js"></script>
<script data-goatcounter="https://prospectaia.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
"""


def build_page(fragment_path: Path, nav: str, footer: str):
    fragment = fragment_path.read_text(encoding="utf-8")
    if "<!--META-->" not in fragment or "<!--BODY-->" not in fragment:
        raise SystemExit(f"{fragment_path} is missing <!--META--> / <!--BODY--> markers")

    meta_part, body_part = fragment.split("<!--BODY-->", 1)
    meta = meta_part.replace("<!--META-->", "").strip("\n")
    body = body_part.strip("\n")

    html = PAGE_TEMPLATE.format(
        favicon=FAVICON,
        meta=meta,
        nav=nav.strip("\n"),
        body=body,
        footer=footer.strip("\n"),
    )

    out_path = ROOT / fragment_path.name
    out_path.write_text(html, encoding="utf-8", newline="\n")
    print(f"Built {out_path.name}")


def page_priority(name: str) -> tuple[str, str]:
    """Heuristic (changefreq, priority) for a root page filename."""
    if name == "index.html":
        return "weekly", "1.0"
    if name in {"sobre.html", "servicos.html", "diferenciais.html", "planos.html", "faq.html", "contacto.html"}:
        return "weekly", "0.8"
    if name.startswith(("setor-", "plataforma-", "metodologia")):
        return "monthly", "0.6"
    if name == "blog.html" or name.startswith("blog-"):
        return "monthly", "0.5"
    # legal/policy pages: privacidade, termos, cookies, disclaimer, reembolso
    return "yearly", "0.3"


def build_sitemap(fragments: list[Path]):
    today = date.today().isoformat()
    entries = []
    for fragment_path in fragments:
        name = fragment_path.name
        changefreq, priority = page_priority(name)
        entries.append(
            "  <url>\n"
            f"    <loc>{SITE_URL}/{name}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>{changefreq}</changefreq>\n"
            f"    <priority>{priority}</priority>\n"
            "  </url>"
        )

    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(entries) + "\n"
        "</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8", newline="\n")
    print(f"Built sitemap.xml ({len(fragments)} URLs)")


def main():
    nav = (PARTIALS_DIR / "nav.html").read_text(encoding="utf-8")
    footer = (PARTIALS_DIR / "footer.html").read_text(encoding="utf-8")

    fragments = sorted(PAGES_DIR.glob("*.html"))
    if not fragments:
        raise SystemExit("No page fragments found in pages/")

    for fragment_path in fragments:
        build_page(fragment_path, nav, footer)

    build_sitemap(fragments)

    print(f"\nDone. Built {len(fragments)} pages.")


if __name__ == "__main__":
    main()
