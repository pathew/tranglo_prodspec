import os

repo_path = "."  # Adjust if running from another directory
output_file = "index.md"

with open(output_file, "w", encoding="utf-8") as f:
    f.write("# 📄 Tranglo Document Index\n\n")
    f.write("Welcome! Below are publicly accessible documents used by our AI chatbot:\n\n")
    for filename in sorted(os.listdir(repo_path)):
        if filename == output_file or filename.startswith("."):
            continue
        if os.path.isfile(filename):
            f.write(f"- [{filename}](./{filename})\n")

print(f"✅ '{output_file}' generated with links to all files.")
