import markdown
import re
import urllib.parse
import urllib.request
import base64
import ssl
import os
from sys import argv
from pathlib import Path
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

# 1. Pre-compile regexes for performance
FRONTMATTER_RE = re.compile(r'^---\n(.*?)\n---\n(.*)', re.MULTILINE | re.DOTALL)
BLOCK_MATH_RE = re.compile(r'\$\$(.*?)\$\$', re.DOTALL)
INLINE_MATH_RE = re.compile(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)')
OBSIDIAN_IMG_RE = re.compile(r'!\[\[(.*?)\]\]')
CALLOUT_RE = re.compile(r'^>\s*\[!(\w+)\](.*)')

# Global cache to prevent duplicate network calls across imports
IMAGE_CACHE = {}

def fetch_as_data_uri(url):
    if url in IMAGE_CACHE:
        return IMAGE_CACHE[url]
        
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; WeasyPrint)"})
        verify_env = os.getenv('WEASY_VERIFY_SSL', '0')
        cafile = os.getenv('WEASY_CA_BUNDLE', "/home/guilhem/lycee.crt")
        
        if verify_env in ('0', 'false', 'False'):
            context = ssl._create_unverified_context()
        elif cafile:
            context = ssl.create_default_context(cafile=cafile)
        else:
            try:
                import certifi
                context = ssl.create_default_context(cafile=certifi.where())
            except ImportError:
                context = ssl.create_default_context()

        with urllib.request.urlopen(req, timeout=20, context=context) as resp:
            data = resp.read()
            content_type = resp.getheader('Content-Type', 'image/svg+xml').split(';')[0].strip()
            b64 = base64.b64encode(data).decode('ascii')
            data_uri = f"data:{content_type};base64,{b64}"
            IMAGE_CACHE[url] = data_uri
            return data_uri
            
    except Exception as e:
        print(f"Warning: failed to fetch {url}: {e}")
        return url

def _math_repl(match, is_block=False):
    formula = match.group(1).strip()
    prefix = '\\displaystyle ' if is_block else '\\textstyle '
    
    if not formula.lstrip().startswith(('\\displaystyle', '\\textstyle')):
        formula = prefix + formula
        
    url = f"https://latex.codecogs.com/svg.image?{urllib.parse.quote(formula)}"
    data_uri = fetch_as_data_uri(url)
    
    if is_block:
        return f'<div class="math-block"><img class="math-block-img math-svg" src="{data_uri}" alt="math formula"></div>'
    return f'<img class="math-inline math-svg" src="{data_uri}" alt="math inline">'

def process_callouts(text):
    lines = text.split('\n')
    new_lines = []
    in_admonition = False
    
    for line in lines:
        admonition_match = CALLOUT_RE.match(line)
        if admonition_match:
            in_admonition = True
            atype = admonition_match.group(1).lower()
            title = admonition_match.group(2).strip()
            new_lines.append(f'!!! {atype} "{title}"' if title else f'!!! {atype}')
        elif in_admonition and line.startswith('>'):
            new_lines.append('    ' + line[1:].lstrip(' '))
        else:
            in_admonition = False
            new_lines.append(line)
            
    return '\n'.join(new_lines)

def parse_md_with_frontmatter(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Safely extract Frontmatter
    meta = {}
    match = FRONTMATTER_RE.match(text)
    if match:
        yaml_part, content = match.groups()
        for line in yaml_part.strip().split('\n'):
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip().lower()] = v.strip().strip('"\'')
    else:
        content = text

    # Support for Obsidian Image syntax: convert ![[img.png]] to ![img.png](img.png)
    content = OBSIDIAN_IMG_RE.sub(r'![\1](\1)', content)

    # Pre-process LaTeX Math to SVG
    content = BLOCK_MATH_RE.sub(lambda m: _math_repl(m, True), content)
    content = INLINE_MATH_RE.sub(lambda m: _math_repl(m, False), content)

    # Process Callouts
    content = process_callouts(content)

    # Convert Markdown to HTML
    html_body = markdown.markdown(content, extensions=['admonition', 'extra', 'toc'])
    return meta, html_body

def generate_pdf(md_file, css_file, output_file):
    font_config = FontConfiguration()
    meta, html_body = parse_md_with_frontmatter(md_file)

    # Construct the Header from Frontmatter
    meta_parts = [meta.get(k) for k in ('date', 'author') if meta.get(k)]
    meta_html = f'<div class="doc-meta">{" | ".join(meta_parts)}</div>' if meta_parts else ''

    header_html = f"""
    <header class="doc-header">
        <h1>{meta.get('title', 'Untitled Document')}</h1>
        {meta_html}
    </header>
    """

    full_html_string = f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="utf-8"></head>
    <body>
        {header_html}
        <main>{html_body}</main>
    </body>
    </html>
    """

    # Resolve the directory of the Markdown file to load local images correctly
    base_dir = Path(md_file).parent.resolve()
    base_url = base_dir.as_uri() + "/"

    # Initialize WeasyPrint using the localized base_url
    html = HTML(string=full_html_string, base_url=base_url)
    css = CSS(filename=css_file, font_config=font_config)

    # Write PDF
    html.write_pdf(output_file, stylesheets=[css], font_config=font_config)
    print(f"🚀 PDF generated: {output_file}")

if __name__ == "__main__":
    markdown_file = argv[1] if len(argv) > 1 else "CITATIONS.md"
    output_file = argv[2] if len(argv) > 2 else "output.pdf"
    generate_pdf(markdown_file, "style.css", output_file)
