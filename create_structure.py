import os

# Use the current directory (your cloned GitHub repo)
base_dir = "."

# Main folders already in your repo
main_folders = [
    "0-Beginner-Projects",
    "1-Intermediate-Projects",
    "2-Advanced-Projects",
    "3-Expert-Projects",
    "4-AI-Security",
    "5-Cloud-Security",
    "6-RedTeam",
    "7-BlueTeam",
    "8-OSINT",
    "9-Linux-Automation",
    "TryHackMe-Labs",
    "LinkedIn-Posts"
]

# Create main structure if not exists
for folder in main_folders:
    os.makedirs(folder, exist_ok=True)

# Create 1000 project folders
project_num = 1
for category in main_folders[:10]:  
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
    file_name = f"Day-{day:03d}.md"
    open(os.path.join("LinkedIn-Posts", file_name), "w").close()

print("🔥 ALL FOLDERS SUCCESSFULLY CREATED INSIDE YOUR REPO!")