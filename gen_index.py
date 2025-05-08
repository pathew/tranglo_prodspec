import os

output_file = "index.md"
repo_root = "."  # Current directory

def is_visible_path(path):
    return not any(part.startswith('.') for part in path.split(os.sep))

with open(output_file, "w", encoding="utf-8") as f:
    f.write("# 📄 Tranglo Document Index\n\n")
    f.write("Welcome! Below are all publicly accessible documents organized by folder:\n\n")

    for root, dirs, files in os.walk(repo_root):
        # Skip hidden folders like .git, .github, .vscode
        if not is_visible_path(root):
            continue

        visible_files = [file for file in files if not file.startswith(".") and file != output_file]
        if not visible_files:
            continue

        relative_root = os.path.relpath(root, repo_root).replace("\\", "/")
        f.write(f"\n## 📁 {relative_root}\n\n")

        for file in sorted(visible_files):
            rel_path = os.path.join(relative_root, file).replace("\\", "/")
            f.write(f"- [{file}](./{rel_path})\n")

print(f"✅ index.md created with content from folders and subfolders.")
