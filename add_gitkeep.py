import os

for root, dirs, files in os.walk("."):
    if ".git" in root:  # skip .git folder
        continue

    # if folder is empty or has only subfolders
    if len(files) == 0:
        open(os.path.join(root, ".gitkeep"), "w").close()

print("🔥 Added .gitkeep to ALL empty folders!")