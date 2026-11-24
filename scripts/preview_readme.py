"""Gera preview.html usando a API oficial /markdown do GitHub (sem precisar dar git push)."""
import json
import os
import pathlib
import urllib.request
import webbrowser

ROOT = pathlib.Path(__file__).resolve().parent.parent
README_PATH = ROOT / "README.md"
OUT_PATH = ROOT / "preview.html"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""


def render_github_markdown(md_text: str) -> str:
    payload = json.dumps({
        "text": md_text,
        "mode": "gfm",
        "context": "JGustavoCN/JGustavoCN",
    }).encode("utf-8")
    headers = {
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "User-Agent": "JGustavoCN-Local-Preview",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request("https://api.github.com/markdown", data=payload, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8")


def main():
    md = README_PATH.read_text(encoding="utf-8")
    html_body = render_github_markdown(md)

    # Ajustar caminhos relativos ./assets/ para funcionarem localmente no preview.html
    html_body = html_body.replace('src="/JGustavoCN/JGustavoCN/raw/HEAD/', 'src="./')

    page = f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Preview GitHub Profile — JGustavoCN</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown-dark.min.css" />
  <style>
    body {{
      background: #0d1117;
      margin: 0;
      padding: 32px 16px;
    }}
    .markdown-body {{
      box-sizing: border-box;
      min-width: 200px;
      max-width: 920px;
      margin: 0 auto;
      padding: 32px;
      border: 1px solid #30363d;
      border-radius: 8px;
      background: #0d1117;
    }}
  </style>
</head>
<body>
  <article class="markdown-body">
    {html_body}
  </article>
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
    mermaid.initialize({{ startOnLoad: true, theme: 'dark' }});
  </script>
</body>
</html>"""
    OUT_PATH.write_text(page, encoding="utf-8")
    print(f"Preview gerado em: {OUT_PATH}")
    webbrowser.open(OUT_PATH.as_uri())


if __name__ == "__main__":
    main()
