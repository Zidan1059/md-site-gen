import shutil
from pathlib import Path
import markdown
import yaml
from jinja2 import Environment, FileSystemLoader


def parse_markdown_file(file_path: Path) -> dict:
    """Extract YAML frontmatter and render Markdown body to HTML."""
    raw_text = file_path.read_text(encoding="utf-8")
    metadata = {"title": file_path.stem.replace("-", " ").title(), "date": ""}
    body = raw_text

    if raw_text.startswith("---"):
        parts = raw_text.split("---", 2)
        if len(parts) == 3:
            parsed_meta = yaml.safe_load(parts[1]) or {}
            metadata.update(parsed_meta)
            body = parts[2].strip()

    html_content = markdown.markdown(
        body, extensions=["fenced_code", "tables", "toc"]
    )
    return {
        "slug": file_path.stem,
        "url": f"{file_path.stem}.html",
        "metadata": metadata,
        "content": html_content,
    }


def build_site(
    content_dir: Path,
    templates_dir: Path,
    static_dir: Path,
    output_dir: Path,
) -> list[dict]:
    """Build static HTML pages and an index from a directory of Markdown files."""
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    if static_dir.exists():
        shutil.copytree(static_dir, output_dir / "static")

    env = Environment(loader=FileSystemLoader(str(templates_dir)))
    page_template = env.get_template("page.html")
    index_template = env.get_template("index.html")

    pages = []
    for md_file in sorted(content_dir.glob("*.md")):
        page_data = parse_markdown_file(md_file)
        pages.append(page_data)

    for page in pages:
        rendered = page_template.render(page=page, pages=pages)
        (output_dir / page["url"]).write_text(rendered, encoding="utf-8")

    index_html = index_template.render(pages=pages)
    (output_dir / "index.html").write_text(index_html, encoding="utf-8")

    return pages
