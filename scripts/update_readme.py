import html
import json
import os
import pathlib
import re
import urllib.error
import urllib.request
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
README_PATH = ROOT / "README.md"
ACTIVITY_SVG_PATH = ROOT / "assets" / "bento" / "activity-panel.svg"
USERNAME = os.environ.get("GITHUB_REPOSITORY_OWNER") or os.environ.get("GH_USER") or "JGustavoCN"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""

LANG_COLORS = {
    "Go": "#00ADD8",
    "Java": "#ED8B00",
    "JavaScript": "#F7DF1E",
    "TypeScript": "#3178C6",
    "Python": "#3776AB",
    "Dart": "#0175C2",
    "C#": "#512BD4",
    "TeX": "#3D6117",
}


def gh_get(url: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "JGustavoCN-Profile-Updater",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def replace_chunk(content: str, marker: str, chunk: str, inline: bool = False) -> str:
    pattern = re.compile(
        rf"<!-- {re.escape(marker)} starts -->.*?<!-- {re.escape(marker)} ends -->",
        re.DOTALL,
    )
    body = chunk if inline else f"\n{chunk}\n"
    replacement = f"<!-- {re.escape(marker)} starts -->".replace("\\", "") + body + f"<!-- {marker} ends -->"
    return pattern.sub(lambda _: replacement, content)


def fetch_profile_data():
    user = gh_get(f"https://api.github.com/users/{USERNAME}")
    repos = gh_get(
        f"https://api.github.com/users/{USERNAME}/repos?type=owner&sort=pushed&per_page=100"
    )

    own_repos = [r for r in repos if not r.get("fork")]
    total_stars = sum(r.get("stargazers_count", 0) for r in own_repos)
    total_forks = sum(r.get("forks_count", 0) for r in own_repos)

    updates = []
    for r in own_repos:
        name = r.get("name", "")
        if name.lower() == USERNAME.lower():
            continue
        updates.append({
            "name": name,
            "lang": r.get("language") or "Docs",
            "date": (r.get("pushed_at") or "")[:10],
            "url": r.get("html_url"),
        })
        if len(updates) >= 4:
            break

    releases = []
    for r in own_repos[:12]:
        if r.get("name", "").lower() == USERNAME.lower():
            continue
        try:
            rel_list = gh_get(f"https://api.github.com/repos/{USERNAME}/{r['name']}/releases?per_page=3")
            for rel in rel_list:
                if rel.get("prerelease") or rel.get("draft"):
                    continue
                releases.append({
                    "repo": r["name"],
                    "tag": rel.get("tag_name") or rel.get("name") or "release",
                    "url": rel.get("html_url"),
                    "date": (rel.get("published_at") or "")[:10],
                })
                break
        except urllib.error.HTTPError:
            continue

    releases.sort(key=lambda x: x["date"], reverse=True)
    releases = releases[:4]

    stats = {
        "public_repos": user.get("public_repos", len(own_repos)),
        "stars": total_stars,
        "forks": total_forks,
        "followers": user.get("followers", 0),
    }
    return stats, updates, releases


def build_activity_svg(stats: dict, updates: list, releases: list) -> str:
    today = datetime.now().strftime("%d/%m/%Y")

    updates_rows = []
    for idx, u in enumerate(updates):
        y = 92 + idx * 32
        dot_color = LANG_COLORS.get(u["lang"], "#8b949e")
        name_esc = html.escape(u["name"][:28])
        meta_esc = html.escape(f"{u['lang']} • {u['date']}")
        updates_rows.append(
            f'<rect x="26" y="{y - 16}" width="378" height="26" rx="6" class="row-bg" />'
            f'<circle cx="40" cy="{y - 3}" r="4.5" fill="{dot_color}" />'
            f'<text x="53" y="{y + 1}" class="repo-name">{name_esc}</text>'
            f'<text x="392" y="{y + 1}" text-anchor="end" class="meta">{meta_esc}</text>'
        )

    releases_rows = []
    for idx, rel in enumerate(releases):
        y = 92 + idx * 32
        repo_esc = html.escape(rel["repo"][:22])
        tag_esc = html.escape(rel["tag"][:12])
        date_esc = html.escape(rel["date"])
        releases_rows.append(
            f'<rect x="436" y="{y - 16}" width="378" height="26" rx="6" class="row-bg" />'
            f'<circle cx="450" cy="{y - 3}" r="4" fill="#3fb950" />'
            f'<text x="462" y="{y + 1}" class="repo-name">{repo_esc}</text>'
            f'<rect x="652" y="{y - 13}" width="78" height="20" rx="5" class="tag-pill" />'
            f'<text x="691" y="{y + 1}" text-anchor="middle" class="tag-txt">{tag_esc}</text>'
            f'<text x="802" y="{y + 1}" text-anchor="end" class="meta">{date_esc}</text>'
        )

    if not releases_rows:
        releases_rows.append('<text x="436" y="102" class="meta">Nenhum release público encontrado.</text>')

    return f'''<svg viewBox="0 0 840 225" width="100%" xmlns="http://www.w3.org/2000/svg">
  <style>
    .card {{ fill: #0d1117; stroke: #30363d; stroke-width: 1.5; }}
    .hdr {{ fill: #161b22; }}
    .hdr-txt {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 11px; font-weight: 700; fill: #00bfbf; letter-spacing: 0.5px; }}
    .stats-txt {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12px; font-weight: 600; fill: #c9d1d9; }}
    .col-title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 13px; font-weight: 700; fill: #f0f6fc; }}
    .row-bg {{ fill: #161b22; stroke: #21262d; stroke-width: 1; }}
    .repo-name {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12.5px; font-weight: 600; fill: #f0f6fc; }}
    .meta {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 10.5px; fill: #8b949e; }}
    .tag-pill {{ fill: rgba(0, 191, 191, 0.12); stroke: #00bfbf; stroke-width: 0.9; }}
    .tag-txt {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 10px; font-weight: 600; fill: #00bfbf; }}
  </style>

  <rect x="1" y="1" width="838" height="223" rx="14" class="card" />
  <path d="M 1 15 A 14 14 0 0 1 15 1 L 825 1 A 14 14 0 0 1 839 15 L 839 40 L 1 40 Z" class="hdr" />
  <line x1="1" y1="40" x2="839" y2="40" stroke="#21262d" stroke-width="1" />

  <text x="26" y="25" class="hdr-txt">ATIVIDADE AUTOMATIZADA VIA GITHUB ACTIONS • {today}</text>
  <text x="814" y="25" text-anchor="end" class="stats-txt">{stats['public_repos']} Repos • {stats['stars']} Stars • {stats['followers']} Seguidores</text>

  <text x="26" y="64" class="col-title">Últimos Repositórios Atualizados</text>
  {''.join(updates_rows)}

  <text x="436" y="64" class="col-title">Últimos Releases Publicados</text>
  {''.join(releases_rows)}
</svg>
'''


def main():
    stats, updates, releases = fetch_profile_data()

    ACTIVITY_SVG_PATH.parent.mkdir(parents=True, exist_ok=True)
    ACTIVITY_SVG_PATH.write_text(build_activity_svg(stats, updates, releases), encoding="utf-8")

    updates_md = "<br>".join(
        f'• <a href="{u["url"]}"><b>{u["name"]}</b></a> <sub>({u["lang"]} • {u["date"]})</sub>'
        for u in updates
    )
    releases_md = "<br>".join(
        f'• <a href="{r["url"]}"><b>{r["repo"]}</b> <code>{r["tag"]}</code></a> <sub>({r["date"]})</sub>'
        for r in releases
    )

    content = README_PATH.read_text(encoding="utf-8")
    if updates_md:
        content = replace_chunk(content, "recent_updates", updates_md)
    if releases_md:
        content = replace_chunk(content, "recent_releases", releases_md)
    README_PATH.write_text(content, encoding="utf-8")
    print("SVG de atividade e README.md atualizados com sucesso.")


if __name__ == "__main__":
    main()
