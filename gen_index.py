import os
import pathspec

output_file = "index.md"
repo_root = "."

# Folders/files to always exclude (hardcoded, even if not in .gitignore)
force_exclude_dirs = {".git", ".vscode", "__pycache__", ".idea", ".github"}
force_exclude_files = {".DS_Store", output_file}

# Load .gitignore rules if available
spec = None
gitignore_path = os.path.join(repo_root, ".gitignore")
if os.path.exists(gitignore_path):
    with open(gitignore_path, "r") as f:
        spec = pathspec.PathSpec.from_lines("gitwildmatch", f)

def is_ignored(path):
    rel_path = os.path.relpath(path, repo_root).replace("\\", "/")
    # Ignore hidden folders like .git/ even if not in .gitignore
    if any(part in force_exclude_dirs for part in rel_path.split("/")):
        return True
    if spec and spec.match_file(rel_path):
        return True
    return False

print("🔍 Scanning repo and applying .gitignore and system filters...\n")

total_files = 0
with open(output_file, "w", encoding="utf-8") as f:
    f.write("# 📄 Tranglo Document Index\n\n")
    f.write("Welcome! Below are all publicly accessible documents organized by folder:\n\n")

    for root, dirs, files in os.walk(repo_root):
        # Filter dirs in-place to avoid descending into them
        dirs[:] = [d for d in dirs if not is_ignored(os.path.join(root, d))]

        visible_files = [
            file for file in files
            if not is_ignored(os.path.join(root, file))
            and file not in force_exclude_files
        ]

        if not visible_files:
            continue

        relative_root = os.path.relpath(root, repo_root).replace("\\", "/")
        f.write(f"\n## 📁 {relative_root}\n\n")

        for file in sorted(visible_files):
            rel_path = os.path.join(relative_root, file).replace("\\", "/")
            f.write(f"- [{file}](./{rel_path})\n")
            print(f"✅ Added file: {rel_path}")
            total_files += 1

print(f"\n✅ index.md generated with {total_files} files (excluding .git, .vscode, .DS_Store, and .gitignore-matched files).")
