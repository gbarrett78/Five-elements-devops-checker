import os
import sys

# List of required files
required_files = ["README.md", ".gitignore"]

missing_files = []

# Check if each required file exists
for file in required_files:
    if not os.path.isfile(file):
        missing_files.append(file)

# If missing, print them and exit with error
if missing_files:
    print("Missing required files:")
    for file in missing_files:
        print(f"- {file}")
    sys.exit(1)

# If everything exists, exit successfully
print("All required files are present.")
sys.exit(0)
