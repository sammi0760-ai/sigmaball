with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if not style_match:
    print("NO <style> TAG FOUND!")
    exit(1)

css = style_match.group(1)
classes_to_check = [
    "sim-preview-grid",
    "sim-mockup-card",
    "card-topbar-flex",
    "card-title-group",
    "card-badge-group",
    "badge-tag",
    "balls-horizontal-row",
    "ball-badge",
    "ball-divider-symbol",
    "metric-summary-grid",
    "metric-chip",
    "chip-label",
    "chip-val",
    "hot-cold-container",
    "hot-cold-row",
    "mini-chips-group",
    "mini-ball-chip",
    "filter-pills-wrap",
    "filter-pill-tag",
    "shake-action-btn",
    "card-disclaimer-caption"
]

all_ok = True
for cls in classes_to_check:
    if f".{cls}" in css:
        print(f"  [OK] .{cls} found in CSS")
    else:
        print(f"  [MISSING] .{cls} NOT found in CSS")
        all_ok = False

if all_ok:
    print("ALL CSS CLASSES PRESENT AND ACCOUNTED FOR!")
