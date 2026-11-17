import argparse
import functools
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from sitegen.builder import build_site


def serve_directory(directory: Path, port: int) -> None:
    handler = functools.partial(SimpleHTTPRequestHandler, directory=str(directory))
    with ThreadingHTTPServer(("127.0.0.1", port), handler) as server:
        print(f"Serving generated site at http://127.0.0.1:{port} (Ctrl+C to stop)")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a folder of Markdown files into a static HTML site."
    )
    parser.add_argument("--content", type=Path, default=Path("content"), help="Markdown source directory")
    parser.add_argument("--templates", type=Path, default=Path("templates"), help="Jinja2 templates directory")
    parser.add_argument("--static", type=Path, default=Path("static"), help="Static assets directory")
    parser.add_argument("--output", type=Path, default=Path("dist"), help="Output build directory")
    parser.add_argument("--serve", action="store_true", help="Start a local HTTP server after building")
    parser.add_argument("--port", type=int, default=8000, help="Port for local preview server")

    args = parser.parse_args()
    pages = build_site(args.content, args.templates, args.static, args.output)
    print(f"Built {len(pages)} page(s) into '{args.output}/'")

    if args.serve:
        serve_directory(args.output, args.port)


if __name__ == "__main__":
    main()
