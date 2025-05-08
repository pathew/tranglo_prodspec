import os

output_file = "index.md"
repo_root = "."

# List of truly hidden or system folders to skip
excluded_folders = {".git", ".vscode", "__pycache__"}

print("🔍 Scanning repo...\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("# 📄 Tranglo Document Index\n\n")
    f.write("Welcome! Below are all publicly accessible documents organized by folder:\n\n")

    total_files = 0

    for root, dirs, files in os.walk(repo_root):
        folder_name = os.path.basename(root)
        if folder_name in excluded_folders:
            print(f"⏭️ Skipping excluded folder: {root}")
            continue

        visible_files = [
            file for file in files
            if not file.startswith(".") and file != output_file
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

print(f"\n✅ index.md generated with {total_files} files.")
