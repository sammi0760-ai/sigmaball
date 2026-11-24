with open("scripts/build_site_v3.py", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("@media")
while idx != -1:
    print(text[idx:idx+350])
    print("=" * 40)
    idx = text.find("@media", idx+1)
