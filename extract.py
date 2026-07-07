"""
One-time migration: split each existing root .html page into a content
fragment (pages/<name>.html) and pull the shared navbar/footer out into
partials/. Run once; after this, edit fragments + partials and use
build.py to regenerate the root pages.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
PAGES_SRC = [
    "index.html", "sobre.html", "servicos.html", "planos.html", "cases.html",
    "contacto.html", "blog.html", "blog-1.html", "blog-2.html", "blog-3.html",
    "blog-4.html", "blog-5.html", "blog-6.html", "diferenciais.html",
    "setor-restaurantes.html", "setor-hoteis.html", "setor-clinicas.html",
    "setor-spas.html", "setor-agencias.html", "setor-lojas.html",
    "setor-consultorios.html", "setor-outros.html",
]

VIEWPORT_LINE = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'


def extract_partials():
    html = (ROOT / "index.html").read_text(encoding="utf-8")

    nav_match = re.search(r'(<nav class="nav-menu" id="navMenu">.*?</nav>)', html, re.S)
    footer_match = re.search(r'(<footer class="footer">.*?</footer>)', html, re.S)
    if not nav_match or not footer_match:
        raise SystemExit("Could not locate nav or footer block in index.html")

    (ROOT / "partials" / "nav.html").write_text(nav_match.group(1) + "\n", encoding="utf-8", newline="\n")
    (ROOT / "partials" / "footer.html").write_text(footer_match.group(1) + "\n", encoding="utf-8", newline="\n")
    print("Wrote partials/nav.html and partials/footer.html")


def extract_page(name):
    html = (ROOT / name).read_text(encoding="utf-8")

    vp_idx = html.index(VIEWPORT_LINE) + len(VIEWPORT_LINE)
    head_end_idx = html.index("</head>")
    head_fragment = html[vp_idx:head_end_idx].strip("\n")

    header_end_idx = html.index("</header>") + len("</header>")
    footer_start_idx = html.index('<footer class="footer">')
    body_fragment = html[header_end_idx:footer_start_idx].strip("\n")

    fragment = (
        "<!--META-->\n"
        f"{head_fragment}\n"
        "<!--BODY-->\n"
        f"{body_fragment}\n"
    )
    (ROOT / "pages" / name).write_text(fragment, encoding="utf-8", newline="\n")
    print(f"Wrote pages/{name}")


def main():
    extract_partials()
    for name in PAGES_SRC:
        extract_page(name)


if __name__ == "__main__":
    main()
