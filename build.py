"""
Build a one-page site from templates/index.html + a config file.

Usage:  python build.py configs/textile.json
Output: docs/index.html, docs/sitemap.xml, docs/robots.txt, docs/static/
"""
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent
config_path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "configs" / "textile.json"
c = json.loads(config_path.read_text(encoding="utf-8"))


def latest_post(posts_dir: Path):
    """Read every .md file in posts/ and return the newest one (by its date line)."""
    posts = []
    for path in posts_dir.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        meta, body = {}, text
        match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        if match:
            for line in match.group(1).splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    meta[key.strip()] = value.strip()
            body = match.group(2)
        posts.append({
            "title": meta.get("title", path.stem),
            "date": meta.get("date", ""),
            "excerpt": meta.get("excerpt", ""),
            "html": markdown.markdown(body),
        })
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts[0] if posts else None


post = latest_post(ROOT / c.get("posts_dir", "posts"))

schema = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": c["business_name"],
    "description": c["meta_description"],
    "url": c["url"],
    "email": c.get("contact_email", ""),
    "address": {"@type": "PostalAddress", "addressLocality": c["location"]},
}

env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True)
html = env.get_template("index.html").render(c=c, post=post, schema=schema)

out = ROOT / "docs"
out.mkdir(exist_ok=True)
(out / "index.html").write_text(html, encoding="utf-8")
shutil.copytree(ROOT / "static", out / "static", dirs_exist_ok=True)
(out / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {c['url']}sitemap.xml\n", encoding="utf-8")
(out / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    f"  <url><loc>{c['url']}</loc><lastmod>{date.today().isoformat()}</lastmod></url>\n"
    "</urlset>\n",
    encoding="utf-8",
)
print(f"Built {out / 'index.html'} from {config_path.name}")
