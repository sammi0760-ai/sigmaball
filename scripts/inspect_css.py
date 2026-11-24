with open("scripts/build_site_v3.py", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find(".sim-preview-grid")
print(text[idx:idx+2500])
