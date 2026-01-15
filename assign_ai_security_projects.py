import os

BASE = "4-AI-Security"

# Load AI Security Titles (must be EXACTLY 100)
with open("project_titles_ai_security.txt", "r") as f:
    titles = [t.strip().lstrip("0123456789. ").strip() for t in f.readlines() if t.strip()]

if len(titles) != 100:
    raise ValueError(f"project_titles_ai_security.txt must contain exactly 100 titles (found {len(titles)})")

# README Template
TEMPLATE = """# Project-{num} — {title}

## 📌 Description
{title} — expert-level AI Security, LLM Red Teaming, adversarial ML, or model safety project.

## 🧠 Skills Practiced
- Prompt security & jailbreak detection
- Model extraction / inversion / poisoning
- Adversarial ML
- LLM red teaming & security automation
- AI risk, governance & compliance
- AI-powered SOC & detection engineering

## 📝 Notes
(Add your notes here)
"""

# Create Projects 401–500
for i in range(401, 501):
    index = i - 401  # maps 401 → 0, 500 → 99
    title = titles[index]

    folder_name = f"Project-{i:04d}"
    folder_path = os.path.join(BASE, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(TEMPLATE.format(num=f"{i:04d}", title=title))

print("🔥 DONE! AI-Security Projects 401–500 created successfully!")