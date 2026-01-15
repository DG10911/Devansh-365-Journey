import os

BASE = "9-Linux-Automation"

# Load Linux Automation Titles (must be EXACTLY 100)
with open("project_titles_linux_automation.txt", "r") as f:
    # Removes numbering like "1. Title"
    titles = [t.strip().lstrip("0123456789. ").strip()
              for t in f.readlines() if t.strip()]

if len(titles) != 100:
    raise ValueError(
        f"project_titles_linux_automation.txt must contain exactly 100 titles (found {len(titles)})"
    )

# README Template
TEMPLATE = """# Project-{num} — {title}

## 📌 Description
{title} — advanced Linux automation, system administration, scripting,
monitoring, or security-hardening project.

## 🐧 Skills Practiced
- Bash/Python automation
- System monitoring & logging
- Linux security hardening
- Performance tuning
- Backup & recovery scripting
- Process and resource management
- DevOps-style automation workflows

## 📝 Notes
(Add your notes here)
"""

# Create Projects 901–1000
for i in range(901, 1001):
    index = i - 901  # maps 901 → 0, 1000 → 99
    title = titles[index]

    folder_name = f"Project-{i:04d}"
    folder_path = os.path.join(BASE, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(TEMPLATE.format(num=f"{i:04d}", title=title))

print("🔥 DONE! Linux Automation Projects 901–1000 created successfully!")