import os
import glob

files = glob.glob("src/content/blog/*.md")
for f in files:
    with open(f, "r") as file:
        lines = file.readlines()
    
    out_lines = []
    
    for line in lines:
        if "**Suggested internal links:**" in line:
            # Skip this line completely
            continue
        out_lines.append(line)
        
    with open(f, "w") as file:
        file.writelines(out_lines)

print("Cleanup of suggested links complete!")
