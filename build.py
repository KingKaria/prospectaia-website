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

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{meta}
</head>
<body>

<header class="navbar" id="navbar">
  <div class="container navbar-inner">
    <a href="index.html" class="logo">Prospecta<span>IA</span></a>

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
