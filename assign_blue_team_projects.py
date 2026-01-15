import os

BASE = "7-BlueTeam"

# Load Blue Team Titles (must be EXACTLY 100)
with open("project_titles_blue_team.txt", "r") as f:
    # Remove numbering like "1. Title"
    titles = [t.strip().lstrip("0123456789. ").strip() for t in f.readlines() if t.strip()]

if len(titles) != 100:
    raise ValueError(f"project_titles_blue_team.txt must contain exactly 100 titles (found {len(titles)})")

# README Template
TEMPLATE = """# Project-{num} — {title}

## 📌 Description
{title} — enterprise-grade Blue Team, SOC, DFIR, SIEM engineering,
threat hunting, or detection engineering project.

## 🛡 Skills Practiced
- Log analysis & threat hunting
- Detection engineering
- SIEM rule creation (Splunk, ELK, Sentinel)
- Incident response automation
- MITRE ATT&CK mapping
- Forensics & threat intelligence

## 📝 Notes
(Add your notes here)
"""

# Create Projects 701–800
for i in range(701, 801):
    index = i - 701  # maps 701 → 0, 800 → 99
    title = titles[index]

    folder_name = f"Project-{i:04d}"
    folder_path = os.path.join(BASE, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(TEMPLATE.format(num=f"{i:04d}", title=title))

print("🔥 DONE! Blue Team Projects 701–800 created successfully!")