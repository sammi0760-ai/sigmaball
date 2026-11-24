import os
import shutil

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PUBLIC_DIR = os.path.join(BASE_DIR, "public")

# 1. Ensure public dir exists
os.makedirs(PUBLIC_DIR, exist_ok=True)

# 2. Copy index.html to public/
shutil.copy2(os.path.join(BASE_DIR, "index.html"), os.path.join(PUBLIC_DIR, "index.html"))
print("Copied index.html -> public/index.html")

# 3. Copy app-ads.txt to public/
shutil.copy2(os.path.join(BASE_DIR, "app-ads.txt"), os.path.join(PUBLIC_DIR, "app-ads.txt"))
print("Copied app-ads.txt -> public/app-ads.txt")

# 4. Copy assets directory to public/assets
public_assets = os.path.join(PUBLIC_DIR, "assets")
if os.path.exists(public_assets):
    shutil.rmtree(public_assets)
shutil.copytree(os.path.join(BASE_DIR, "assets"), public_assets)
print("Copied assets/ -> public/assets/")

# 5. Copy privacy directory to public/privacy
public_privacy = os.path.join(PUBLIC_DIR, "privacy")
if os.path.exists(public_privacy):
    shutil.rmtree(public_privacy)
shutil.copytree(os.path.join(BASE_DIR, "privacy"), public_privacy)
print("Copied privacy/ -> public/privacy/")

print("\nSuccessfully synchronized all files into public/ folder!")
