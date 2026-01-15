import os

# -------------------------------
#  CONFIG
# -------------------------------
POSTS_FOLDER = "11-LinkedIn-Posts"
PROJECT_FOLDER_ORDER = [
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
TRYHACKME_FOLDER = "10-TryHackMe-Labs"

TOTAL_PROJECTS = 1000
TOTAL_THM_LABS = 200
TOTAL_DAYS = 365

# LinkedIn Post Template
TEMPLATE = """🚀 Day {day} of #Devansh365Journey

🎯 Today’s Focus:
{title}

🧠 What I Did Today:
• {task1}
• {task2}
• {task3}

🛠 Tools Used:
{tools}

📘 Key Learnings:
• {learn1}
• {learn2}
• {learn3}

📂 GitHub Project/Lab:
🔗 https://github.com/DG10911/Devansh-365-Journey/tree/main/{path}

🔥 Small progress every day → massive transformation in 365 days.

#cybersecurity #cloudsecurity #python #linux #redteam #blueteam #osint #tryhackme #infosec #devops #ai #learningeveryday
"""

# -------------------------------
#  LOAD ALL PROJECT TITLES
# -------------------------------
all_projects = []

for prefix, folder in zip(range(0, 1000, 100), PROJECT_FOLDER_ORDER):
    filename = f"project_titles_{folder.split('-')[1].lower().replace(' ', '_')}.txt"
    if not os.path.exists(filename):
        continue

    with open(filename, "r") as f:
        titles = [t.strip().lstrip("0123456789. ").strip() for t in f.readlines() if t.strip()]
        all_projects.extend(titles)

# Load THM labs
with open("tryhackme_labs.txt", "r") as f:
    thm_titles = [t.strip().lstrip("0123456789. ").strip() for t in f.readlines() if t.strip()]

# -------------------------------
#  BUILD DAILY MAPPING
# -------------------------------
mapped_titles = []
mapped_paths = []

# Add 1000 projects → FIRST
for i in range(min(1000, TOTAL_DAYS)):
    title = all_projects[i]
    proj_num = i + 1
    folder_index = (proj_num - 1) // 100
    folder_path = f"{PROJECT_FOLDER_ORDER[folder_index]}/Project-{proj_num:04d}"
    
    mapped_titles.append(title)
    mapped_paths.append(folder_path)

# Then TryHackMe labs until 365 days completed
day = len(mapped_titles) + 1
thm_index = 0

while day <= TOTAL_DAYS:
    title = thm_titles[thm_index]
    folder_path = f"{TRYHACKME_FOLDER}/THM-{(thm_index + 1):04d}"

    mapped_titles.append(title)
    mapped_paths.append(folder_path)

    day += 1
    thm_index += 1

# -------------------------------
#  GENERATE LINKEDIN POST FILES
# -------------------------------
os.makedirs(POSTS_FOLDER, exist_ok=True)

for i in range(1, TOTAL_DAYS + 1):
    file_path = os.path.join(POSTS_FOLDER, f"Day-{i:03d}.md")

    with open(file_path, "w") as f:
        f.write(
            TEMPLATE.format(
                day=i,
                title=mapped_titles[i-1],
                task1="{task_1}",
                task2="{task_2}",
                task3="{task_3}",
                tools="{tools_used}",
                learn1="{learning_1}",
                learn2="{learning_2}",
                learn3="{learning_3}",
                path=mapped_paths[i-1]
            )
        )

print("🔥 SUCCESS! Auto-generated 365 LinkedIn posts with proper title + folder mapping!")