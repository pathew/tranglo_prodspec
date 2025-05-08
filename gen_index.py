import os

output_file = "index.md"
repo_root = "."  # You can change this if needed

with open(output_file, "w", encoding="utf-8") as f:
    f.write("# 📄 Tranglo Document Index\n\n")
    f.write("Welcome! Below are all publicly accessible documents organized by folder:\n\n")

    for root, dirs, files in os.walk(repo_root):
        # Skip hidden folders like .git or .github
        if any(part.startswith(".") for part in root.split(os.sep)):
            continue

        relative_root = os.path.relpath(root, repo_root)
        if relative_root == ".":
            relative_root = "Root"

        f.write(f"\n## 📁 {relative_root}\n\n")
        has_files = False

        for file in sorted(files):
            if file.startswith(".") or file == output_file:
                continue

            rel_path = os.path.relpath(os.path.join(root, file), repo_root).replace("\\", "/")
            f.write(f"- [{file}](./{rel_path})\n")
            has_files = True

        if not has_files:
            f.write("_(No files in this folder)_\n")

print(f"✅ '{output_file}' generated with full directory scan.")
