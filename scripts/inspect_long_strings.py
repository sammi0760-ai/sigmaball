with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
# Extract translations
match = re.search(r'const translations\s*=\s*(\{.*?\});\s*//\s*Language Switcher', html, re.DOTALL)
js_obj_str = match.group(1)

langs = ["en", "es", "ko"]
lang_data = {}
for lang in langs:
    pattern = rf'{lang}:\s*\{{(.*?)\n\s*\}}(?:,\s*|\s*}})'
    m = re.search(pattern, js_obj_str, re.DOTALL)
    block = m.group(1)
    lang_data[lang] = dict(re.findall(r'([a-zA-Z0-9_]+):\s*"((?:\\.|[^"\\])*)"', block))

# Check longest strings in each category
print("=== TOP 5 LONGEST HEADINGS & LABELS ===")
for k in sorted(lang_data["en"].keys()):
    if any(p in k for p in ["title", "tag", "lbl", "badge", "btn", "sublabel"]):
        lengths = {lang: len(lang_data[lang][k]) for lang in langs}
        max_l = max(lengths.values())
        if max_l > 25:
            print(f"Key: {k:20s} | Max: {max_l:2d} chars")
            for lang in langs:
                print(f"   [{lang}]: ({len(lang_data[lang][k]):2d}) {lang_data[lang][k]}")
