import os

# Base directory (current repo folder)
base_dir = "."

# Coding folders
coding_folders = [
    "C",
    "DSA",
    "Python",
    "SQL"
]

# Project category folders
project_folders = [
    "0-Beginner-Projects",
    "1-Intermediate-Projects",
    "2-Advanced-Projects",
    "3-Expert-Projects",
    "4-AI-Security",
    "5-Cloud-Security",
    "6-RedTeam",
    "7-BlueTeam",
    "8-OSINT",
    "9-Linux-Automation"
]

# Other main folders
other_folders = [
    "TryHackMe-Labs",
    "LinkedIn-Posts",
    "Weekly-Content",
    "Google-Cloud",
    "Google-Cybersecurity",
    "Ethical-Hacking"
]

# Create all main folders
all_main = coding_folders + project_folders + other_folders
for folder in all_main:
    os.makedirs(folder, exist_ok=True)

# Create 1000 project folders
project_num = 1
for category in project_folders:
    for i in range(100):
        folder_name = f"Project-{project_num:04d}"
        os.makedirs(os.path.join(category, folder_name), exist_ok=True)
        project_num += 1

# Create 200 TryHackMe folders
for i in range(1, 201):
    thm_folder = f"THM-{i:03d}"
    os.makedirs(os.path.join("TryHackMe-Labs", thm_folder), exist_ok=True)

# Create 365 LinkedIn posts
for day in range(1, 366):
    post_file = f"Day-{day:03d}.md"
    open(os.path.join("LinkedIn-Posts", post_file), "w").close()

print("🔥 FULL MASTER STRUCTURE GENERATED SUCCESSFULLY!")