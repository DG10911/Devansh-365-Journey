import os

BASE = "6-RedTeam"

# Load Red Team Titles (must be EXACTLY 100)
with open("project_titles_red_team.txt", "r") as f:
    titles = [t.strip().lstrip("0123456789. ").strip() for t in f.readlines() if t.strip()]

if len(titles) != 100:
    raise ValueError(f"project_titles_red_team.txt must contain exactly 100 titles (found {len(titles)})")

# README Template
TEMPLATE = """# Project-{num} — {title}

## 📌 Description
{title} — advanced red-team, offensive security, post-exploitation,
lateral movement, or adversary simulation project.

## 🛠 Skills Practiced
- AD & Kerberos attack chains
- C2 development & evasion
- Internal recon & lateral movement
- Credential theft & abuse
- Persistence & privilege escalation
- Red team automation

## 📝 Notes
(Add your notes here)
"""

# Create Projects 601–700
for i in range(601, 701):
    index = i - 601  # maps 601 → 0, 700 → 99
    title = titles[index]

    folder_name = f"Project-{i:04d}"
    folder_path = os.path.join(BASE, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(TEMPLATE.format(num=f"{i:04d}", title=title))

print("🔥 DONE! Red Team Projects 601–700 created successfully!")