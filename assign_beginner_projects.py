import os

BASE = "0-Beginner-Projects"

# Load the 100 beginner titles
with open("project_titles_beginner.txt", "r") as f:
    titles = [t.strip() for t in f.readlines() if t.strip()]

if len(titles) != 100:
    raise ValueError(f"project_titles_beginner.txt must contain exactly 100 titles (found {len(titles)})")

# README template
TEMPLATE = """# Project-{num} — {title}

## 📌 Description
{title} — beginner level project for cybersecurity, automation, or programming.

## 🎯 Skills Practiced
- Basic scripting
- Problem solving
- Automation
- Debugging

## 📝 Notes
(Add your notes)
"""

# Create 100 project folders + README
for i in range(1, 101):
    num = f"{i:04d}"
    title = titles[i - 1]

    folder_name = f"Project-{num}"
    folder_path = os.path.join(BASE, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(TEMPLATE.format(num=num, title=title))

print("🔥 DONE! All 100 Beginner Projects created successfully!")