with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
for m in re.finditer(r'Distribuci', text):
    pos = m.start()
    print("--- MATCH AT", pos, "---")
    print(text[max(0, pos-150):min(len(text), pos+250)])
