with open("scripts/build_awwwards.py", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("Distribución equilibrada")
if idx != -1:
    print("Found in build_awwwards.py at", idx)
    print(text[max(0, idx-300):min(len(text), idx+500)])
else:
    print("NOT found in build_awwwards.py")
