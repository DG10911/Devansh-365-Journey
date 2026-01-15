import os

BASE = "3-Expert-Projects"

# Load Expert Titles (must be EXACTLY 100)
with open("project_titles_expert.txt", "r") as f:
    titles = [t.strip() for t in f.readlines() if t.strip()]

if len(titles) != 100:
    raise ValueError(f"project_titles_expert.txt must contain exactly 100 titles (found {len(titles)})")

# README Template
TEMPLATE = """# Project-{num} — {title}

## 📌 Description
{title} — expert-level cybersecurity, red team, blue team, DFIR, AI-security, cloud, or adversary emulation project.

## 🛠 Skills Practiced
- Advanced exploitation & detection
- Threat hunting
- Adversary emulation
- Red/Blue/Purple teaming
- Malware analysis & DFIR
- Cloud & Kubernetes security

## 📝 Notes
(Add your notes here)
"""

# Create Projects 301–400
for i in range(301, 401):
    index = i - 301  # maps 301 → 0, 400 → 99
    title = titles[index]

    folder_name = f"Project-{i:04d}"
    folder_path = os.path.join(BASE, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(TEMPLATE.format(num=f"{i:04d}", title=title))

print("🔥 DONE! Expert Projects 301–400 created successfully!")