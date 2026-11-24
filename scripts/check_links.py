import os
import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

links = re.findall(r'<a [^>]*href=["\'][^"\']*["\'][^>]*>', text)
print(f"Total <a> tags: {len(links)}")
for l in links:
    if "privacy" in l or "app-ads" in l:
        print("  Found link:", l)
