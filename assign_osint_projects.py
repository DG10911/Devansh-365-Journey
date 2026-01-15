import os

BASE = "8-OSINT"

# Load OSINT Titles (must be EXACTLY 100)
with open("project_titles_osint.txt", "r") as f:
    # Remove numbering like "1. Title"
    titles = [t.strip().lstrip("0123456789. ").strip() 
              for t in f.readlines() if t.strip()]

if len(titles) != 100:
    raise ValueError(
        f"project_titles_osint.txt must contain exactly 100 titles (found {len(titles)})"
    )

# README Template
TEMPLATE = """# Project-{num} — {title}

## 📌 Description
{title} — expert-level OSINT project involving people, infrastructure,
geolocation, dark web OSINT, metadata analysis, threat intel, or social graph mapping.

## 🕵️ Skills Practiced
- People OSINT & social media footprint mapping
- GEOINT & image/video location analysis
- Dark web OSINT (safe metadata only)
- Corporate & infrastructure OSINT
- Threat intel enrichment & monitoring
- Metadata extraction, reverse lookup, search automation

## 📝 Notes
(Add your notes here)
"""

# Create Projects 801–900
for i in range(801, 901):
    index = i - 801  # maps 801 → 0, 900 → 99
    title = titles[index]

    folder_name = f"Project-{i:04d}"
    folder_path = os.path.join(BASE, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(TEMPLATE.format(num=f"{i:04d}", title=title))

print("🔥 DONE! OSINT Projects 801–900 created successfully!")