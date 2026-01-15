import os

BASE = "11-LinkedIn-Posts"
os.makedirs(BASE, exist_ok=True)

TEMPLATE = """🚀 Day {day} of #Devansh365Journey

🎯 Today’s Focus:
{project}

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

📂 GitHub Project:
🔗 https://github.com/DG10911/Devansh-365-Journey/tree/main/{path}

🔥 Small progress every day → Massive progress in a year.

#cybersecurity #cloudsecurity #python #linux #devops #redteam #blueteam #osint #tryhackme #100DaysOfCode #ai #cloud #learningeveryday #infosec #hacking
"""

for i in range(1, 366):
    file_name = f"Day-{i:03d}.md"
    file_path = os.path.join(BASE, file_name)

    with open(file_path, "w") as f:
        f.write(
            TEMPLATE.format(
                day=i,
                project="{project_name}",
                task1="{task_1}",
                task2="{task_2}",
                task3="{task_3}",
                tools="{tools_used}",
                learn1="{learning_1}",
                learn2="{learning_2}",
                learn3="{learning_3}",
                path="{folder_path}"
            )
        )

print("🔥 DONE! 365 LinkedIn post templates generated successfully!")