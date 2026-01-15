import os

BASE = "10-TryHackMe-Labs"

# force create base folder
os.makedirs(BASE, exist_ok=True)

# Load titles file
try:
    with open("tryhackme_labs.txt", "r") as f:
        titles = [
            t.strip().lstrip("0123456789. ").strip()
            for t in f.readlines() if t.strip()
        ]
except FileNotFoundError:
    print("❌ ERROR: tryhackme_labs.txt NOT FOUND")
    exit()

# Validate count
if len(titles) != 200:
    print(f"❌ ERROR: Expected 200 labs, found {len(titles)}")
    exit()

# Load template file
try:
    with open("tryhackme_readme_template.md", "r") as f:
        TEMPLATE = f.read()
except FileNotFoundError:
    print("❌ ERROR: tryhackme_readme_template.md NOT FOUND")
    exit()

# Create 200 folders + README
for i in range(1, 201):
    title = titles[i - 1]
    folder_name = f"THM-{i:04d}"
    folder_path = os.path.join(BASE, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(
            TEMPLATE.replace("{num}", f"{i:04d}")
                    .replace("{title}", title)
        )

    print(f"✅ Created {folder_name} — {title}")

print("🔥 ALL 200 TryHackMe labs created successfully!")