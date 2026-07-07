"""
Build script for the ProspectaIA static site.

Regenerates every root .html page from:
  - pages/<name>.html   -> per-page <head> extras + body content
  - partials/nav.html   -> shared nav menu (single source of truth)
  - partials/footer.html -> shared footer (single source of truth)

Usage: python build.py
Run this after editing anything in pages/ or partials/.
"""
from pathlib import Path

ROOT = Path(__file__).parent
PAGES_DIR = ROOT / "pages"
PARTIALS_DIR = ROOT / "partials"

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
{meta}
</head>
<body>

<header class="navbar" id="navbar">
  <div class="container navbar-inner">
    <a href="index.html" class="logo"><span class="logo-mark">P</span>Prospecta<span>IA</span></a>

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


def main():
    nav = (PARTIALS_DIR / "nav.html").read_text(encoding="utf-8")
    footer = (PARTIALS_DIR / "footer.html").read_text(encoding="utf-8")

    fragments = sorted(PAGES_DIR.glob("*.html"))
    if not fragments:
        raise SystemExit("No page fragments found in pages/")

    for fragment_path in fragments:
        build_page(fragment_path, nav, footer)

    print(f"\nDone. Built {len(fragments)} pages.")


if __name__ == "__main__":
    main()
