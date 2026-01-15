import os

BASE = "1-Intermediate-Projects"

# Load Intermediate Titles (should be EXACTLY 100 lines)
with open("project_titles_intermediate.txt", "r") as f:
    titles = [t.strip() for t in f.readlines() if t.strip()]

if len(titles) != 100:
    raise ValueError(f"project_titles_intermediate.txt must contain exactly 100 titles (found {len(titles)})")

# README Template
TEMPLATE = """# Project-{num} — {title}

## 📌 Description
{title} — intermediate-level cybersecurity or automation project.

## 🛠 Skills Practiced
- Scripting
- Pentesting
- Automation
- Security Testing
- Tool Development

## 📝 Notes
(Add your notes)
"""

# Create Projects 101–200
for i in range(101, 201):
    index = i - 101  # maps 101 → 0, 200 → 99
    title = titles[index]

    folder_name = f"Project-{i:04d}"
    folder_path = os.path.join(BASE, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(TEMPLATE.format(num=f"{i:04d}", title=title))

print("🔥 DONE! Intermediate Projects 101–200 created successfully!")