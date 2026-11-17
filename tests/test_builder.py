from pathlib import Path
from sitegen.builder import parse_markdown_file, build_site


def test_parse_markdown_with_frontmatter(tmp_path: Path):
    md_file = tmp_path / "hello-world.md"
    md_file.write_text(
        "---\ntitle: Custom Title\ndate: 2026-11-17\n---\n# Heading\nBody text.",
        encoding="utf-8",
    )

    result = parse_markdown_file(md_file)

    assert result["slug"] == "hello-world"
    assert result["metadata"]["title"] == "Custom Title"
    assert "<h1>Heading</h1>" in result["content"]


def test_build_site(tmp_path: Path):
    content_dir = tmp_path / "content"
    templates_dir = tmp_path / "templates"
    static_dir = tmp_path / "static"
    output_dir = tmp_path / "dist"

    content_dir.mkdir()
    templates_dir.mkdir()
    static_dir.mkdir()

    (content_dir / "post.md").write_text("---\ntitle: Test Post\n---\nHello!", encoding="utf-8")
    (templates_dir / "base.html").write_text("{% block content %}{% endblock %}", encoding="utf-8")
    (templates_dir / "page.html").write_text("{% extends 'base.html' %}{% block content %}{{ page.content }}{% endblock %}", encoding="utf-8")
    (templates_dir / "index.html").write_text("{% extends 'base.html' %}{% block content %}{{ pages|length }}{% endblock %}", encoding="utf-8")
    (static_dir / "style.css").write_text("body {}", encoding="utf-8")

    pages = build_site(content_dir, templates_dir, static_dir, output_dir)

    assert len(pages) == 1
    assert (output_dir / "index.html").exists()
    assert (output_dir / "post.html").exists()
    assert (output_dir / "static" / "style.css").exists()
