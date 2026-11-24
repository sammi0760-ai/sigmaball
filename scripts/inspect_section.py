with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

import re
m = re.search(r'(<section class="section" id="preview">.*?</section>)', c, re.DOTALL)
if m:
    print(m.group(1))
else:
    print("NOT FOUND")
