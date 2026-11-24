import json
import os
import pathlib
import re
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
README_PATH = ROOT / "README.md"
USERNAME = os.environ.get("GITHUB_REPOSITORY_OWNER") or os.environ.get("GH_USER") or "JGustavoCN"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""


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
    replacement = f"<!-- {marker} starts -->{body}<!-- {marker} ends -->"
    return pattern.sub(lambda _: replacement, content)


def fetch_profile_data():
    user = gh_get(f"https://api.github.com/users/{USERNAME}")
    repos = gh_get(
        f"https://api.github.com/users/{USERNAME}/repos?type=owner&sort=pushed&per_page=100"
    )

    own_repos = [r for r in repos if not r.get("fork")]
    total_stars = sum(r.get("stargazers_count", 0) for r in own_repos)
    total_forks = sum(r.get("forks_count", 0) for r in own_repos)

    recent_updates = []
    for r in own_repos[:5]:
        name = r.get("name", "")
        if name.lower() == USERNAME.lower():
            continue
        pushed = (r.get("pushed_at") or "")[:10]
        lang = r.get("language") or "Docs"
        url = r.get("html_url")
        recent_updates.append(f"• <a href=\"{url}\"><b>{name}</b></a> <sub>({lang} • {pushed})</sub>")
        if len(recent_updates) >= 4:
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
                pub = (rel.get("published_at") or "")[:10]
                tag = rel.get("tag_name") or rel.get("name") or "release"
                releases.append({
                    "repo": r["name"],
                    "tag": tag,
                    "url": rel.get("html_url"),
                    "date": pub,
                })
                break
        except urllib.error.HTTPError:
            continue

    releases.sort(key=lambda x: x["date"], reverse=True)
    release_lines = [
        f"• <a href=\"{rel['url']}\"><b>{rel['repo']}</b> <code>{rel['tag']}</code></a> <sub>({rel['date']})</sub>"
        for rel in releases[:4]
    ]

    summary = (
        f"<b>{user.get('public_repos', len(own_repos))}</b> repositórios públicos • "
        f"<b>{total_stars}</b> stars • "
        f"<b>{total_forks}</b> forks • "
        f"<b>{user.get('followers', 0)}</b> seguidores"
    )

    return summary, "<br>".join(recent_updates), "<br>".join(release_lines)


def main():
    content = README_PATH.read_text(encoding="utf-8")
    summary, updates_html, releases_html = fetch_profile_data()

    if updates_html:
        content = replace_chunk(content, "recent_updates", updates_html)
    if releases_html:
        content = replace_chunk(content, "recent_releases", releases_html)
    content = replace_chunk(content, "github_stats", summary, inline=True)

    README_PATH.write_text(content, encoding="utf-8")
    print("README.md atualizado com sucesso.")


if __name__ == "__main__":
    main()
