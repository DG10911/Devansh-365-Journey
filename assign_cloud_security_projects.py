import os

BASE = "5-Cloud-Security"

# Load Cloud Security Titles (must be EXACTLY 100)
with open("project_titles_cloud_security.txt", "r") as f:
    titles = [t.strip().lstrip("0123456789. ").strip() for t in f.readlines() if t.strip()]

if len(titles) != 100:
    raise ValueError(f"project_titles_cloud_security.txt must contain exactly 100 titles (found {len(titles)})")

# README Template
TEMPLATE = """# Project-{num} — {title}

## 📌 Description
{title} — advanced cloud security engineering project covering AWS, Azure, GCP, Kubernetes, or multi-cloud.

## ☁️ Skills Practiced
- Cloud attack simulation
- Cloud IAM & privilege escalation
- Kubernetes security
- Cloud DFIR
- Serverless security
- Zero-trust architectures
- Cloud detection engineering

## 📝 Notes
(Add your notes here)
"""

# Create Projects 501–600
for i in range(501, 601):
    index = i - 501  # maps 501 → 0, 600 → 99
    title = titles[index]

    folder_name = f"Project-{i:04d}"
    folder_path = os.path.join(BASE, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(TEMPLATE.format(num=f"{i:04d}", title=title))

print("🔥 DONE! Cloud Security Projects 501–600 created successfully!")