import os

BASE = "2-Advanced-Projects"

# Load Advanced Titles (must be EXACTLY 100)
with open("project_titles_advanced.txt", "r") as f:
    titles = [t.strip() for t in f.readlines() if t.strip()]

if len(titles) != 100:
    raise ValueError(f"project_titles_advanced.txt must contain exactly 100 titles (found {len(titles)})")

# README Template
TEMPLATE = """# Project-{num} — {title}

## 📌 Description
{title} — advanced-level cybersecurity, cloud, AI-security, or DevSecOps project.

## 🛠 Skills Practiced
- Advanced security engineering
- Cloud security
- Red/Blue teaming
- DevSecOps workflows
- Automation & scripting

## 📝 Notes
(Add your notes here)
"""

# Create Projects 201–300
for i in range(201, 301):
    index = i - 201   # maps 201→0, 300→99
    title = titles[index]

    folder_name = f"Project-{i:04d}"
    folder_path = os.path.join(BASE, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(TEMPLATE.format(num=f"{i:04d}", title=title))

print("🔥 DONE! Advanced Projects 201–300 created successfully!")