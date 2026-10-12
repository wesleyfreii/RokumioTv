#!/usr/bin/env python3
"""Verificação estática do site Rokumio, sem dependências externas."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = sorted(ROOT.rglob("*.html"))
errors = []


class PageParser(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.links = []
        self.main_count = 0
        self.has_pt_lang = False
        self.has_skip = False
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.has_pt_lang = attrs.get("lang") == "pt-BR"
        if tag == "main":
            self.main_count += 1
        if "id" in attrs:
            if attrs["id"] in self.ids:
                errors.append(f"{self.path}: ID duplicado: {attrs['id']}")
            self.ids.add(attrs["id"])
        if tag == "a":
            href = attrs.get("href", "")
            if href.startswith("javascript:"):
                errors.append(f"{self.path}: link javascript: não permitido")
            if href == "#conteudo" and "skip-link" in attrs.get("class", "").split():
                self.has_skip = True
            if href:
                self.links.append(href)
        if tag == "img":
            self.images.append(attrs)


def resolve_target(source, href):
    url = urlsplit(href)
    if url.scheme or url.netloc or href.startswith("//"):
        return None, None
    if not url.path and not url.fragment:
        return None, None
    if url.path.startswith("/"):
        # A hospedagem usa um subcaminho no GitHub Pages; links devem ser relativos.
        errors.append(f"{source}: link absoluto não-portável: {href}")
        return None, None
    dest = (source.parent / unquote(url.path)).resolve() if url.path else source
    if not dest.is_relative_to(ROOT):
        errors.append(f"{source}: link sai da raiz do site: {href}")
        return None, None
    if dest.is_dir():
        dest /= "index.html"
    return dest, unquote(url.fragment)


def main():
    if not PAGES:
        errors.append("Nenhuma página HTML encontrada")
    pages = {}
    for path in PAGES:
        parser = PageParser(path.relative_to(ROOT))
        parser.feed(path.read_text(encoding="utf-8"))
        pages[path.resolve()] = parser
        if not parser.has_pt_lang:
            errors.append(f"{path}: html precisa de lang=pt-BR")
        if parser.main_count != 1:
            errors.append(f"{path}: esperado exatamente um elemento main")
        if not parser.has_skip or "conteudo" not in parser.ids:
            errors.append(f"{path}: faltam link de pular e alvo #conteudo")
        for img in parser.images:
            if not all(key in img for key in ("alt", "width", "height")):
                errors.append(f"{path}: imagem sem alt ou dimensões")
    for path, parser in pages.items():
        for href in parser.links:
            target, fragment = resolve_target(path, href)
            if target is None:
                continue
            if not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: link quebrado: {href}")
            elif fragment and target in pages and fragment not in pages[target].ids:
                errors.append(f"{path.relative_to(ROOT)}: âncora inexistente: {href}")
    if errors:
        for error in errors:
            print("ERRO:", error, file=sys.stderr)
        return 1
    print(f"OK: {len(pages)} páginas; links locais, imagens e estrutura básica verificados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
