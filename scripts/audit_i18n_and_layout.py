import re
import json

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Extract translations dictionary from JS
match = re.search(r'const translations\s*=\s*(\{.*?\});\s*//\s*Language Switcher', html, re.DOTALL)
if not match:
    print("ERROR: could not find translations object in index.html")
    exit(1)

js_obj_str = match.group(1)

# Find all data-i18n in HTML
html_i18n_keys = set(re.findall(r'data-i18n="([^"]+)"', html))
print(f"Total distinct data-i18n keys in HTML: {len(html_i18n_keys)}")

# Parse languages
langs = ["en", "es", "ko"]
lang_data = {}

for lang in langs:
    pattern = rf'{lang}:\s*\{{(.*?)\n\s*\}}(?:,\s*|\s*}})'
    m = re.search(pattern, js_obj_str, re.DOTALL)
    if not m:
        print(f"ERROR: could not find language block for {lang}")
        continue
    block = m.group(1)
    keys_values = re.findall(r'([a-zA-Z0-9_]+):\s*"((?:\\.|[^"\\])*)"', block)
    lang_data[lang] = dict(keys_values)
    print(f"Language [{lang}]: {len(lang_data[lang])} keys extracted")

# 2. Check for missing keys across languages
all_keys = set()
for lang in langs:
    all_keys.update(lang_data[lang].keys())

print(f"\nTotal unique translation keys across all languages: {len(all_keys)}")

missing_in_langs = {lang: [] for lang in langs}
for k in sorted(all_keys):
    for lang in langs:
        if k not in lang_data[lang]:
            missing_in_langs[lang].append(k)

for lang in langs:
    if missing_in_langs[lang]:
        print(f"WARNING: Missing keys in [{lang}]: {missing_in_langs[lang]}")
    else:
        print(f"[OK] No missing keys in [{lang}] (100% complete)")

# 3. Check for HTML data-i18n keys not in translations
untranslated_html_keys = [k for k in html_i18n_keys if k not in all_keys]
if untranslated_html_keys:
    print(f"WARNING: HTML has data-i18n keys missing from translations: {untranslated_html_keys}")
else:
    print("[OK] All data-i18n keys in HTML are defined in translations!")

# 4. Check for keys in translations not used in HTML
unused_trans_keys = [k for k in all_keys if k not in html_i18n_keys]
print(f"Info: {len(unused_trans_keys)} keys defined in translations not directly in HTML data-i18n (may be JS dynamic or secondary): {unused_trans_keys}")

# 5. Measure text lengths and identify potential overflow candidates
print("\n--- TEXT LENGTH ANALYSIS ---")
for k in sorted(all_keys):
    en_len = len(lang_data.get("en", {}).get(k, ""))
    es_len = len(lang_data.get("es", {}).get(k, ""))
    ko_len = len(lang_data.get("ko", {}).get(k, ""))
    # Flag if Spanish is more than 2x English or > 40 chars for small elements
    if any(prefix in k for prefix in ["chip_", "btn_", "badge", "nav_", "spec_", "lbl_"]):
        print(f"  {k:20s} | EN: {en_len:2d} | ES: {es_len:2d} | KO: {ko_len:2d} | '{lang_data['en'].get(k,'')}' / '{lang_data['es'].get(k,'')}' / '{lang_data['ko'].get(k,'')}'")
