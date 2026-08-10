from pathlib import Path
import re

root = Path('.')
updated = []

for path in root.glob('*.html'):
    if path.name == 'index.html':
        continue
    text = path.read_text(encoding='utf-8')
    title_match = re.search(r'<title>(.*?)</title>', text, re.IGNORECASE | re.DOTALL)
    if not title_match:
        continue
    page_title = title_match.group(1).strip()
    hero_title = page_title.split(' - ')[0].strip() if ' - ' in page_title else page_title

    h2_match = re.search(r'<h2>(.*?)</h2>', text, re.IGNORECASE | re.DOTALL)
    sub_text = h2_match.group(1).strip() if h2_match else ''
    if not sub_text or sub_text.lower() == hero_title.lower():
        sub_text = f'Informasi dan detail tentang {hero_title} di Kabupaten Bandung Barat.'

    def replace_hero(match):
        inner = match.group(1)
        if re.search(r'<h1>', inner, re.IGNORECASE):
            return match.group(0)
        eyebrow_match = re.search(r'<div class="eyebrow">.*?</div>', inner, re.IGNORECASE | re.DOTALL)
        if not eyebrow_match:
            return match.group(0)
        eyebrow = eyebrow_match.group(0).strip()
        new_block = (
            '<div class="hero-text">\n'
            f'    {eyebrow}\n'
            f'    <h1>{hero_title}</h1>\n'
            f'    <p class="sub">{sub_text}</p>\n'
            '  </div>'
        )
        return new_block

    new_text, count = re.subn(r'<div class="hero-text">(.*?)</div>', replace_hero, text, flags=re.DOTALL)
    if count > 0 and new_text != text:
        path.write_text(new_text, encoding='utf-8')
        updated.append(path.name)

print('updated:', updated)
