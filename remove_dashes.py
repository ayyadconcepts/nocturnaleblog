import os
import glob

files = glob.glob("src/content/blog/*.md")

for filepath in files:
    with open(filepath, 'r') as file:
        content = file.read()
    
    # Replace em dash without spaces around it with space-hyphen-space
    # If it's already surrounded by spaces, just replace the dash
    new_content = content.replace(" — ", " - ")
    new_content = new_content.replace("—", " - ")
    
    with open(filepath, 'w') as file:
        file.write(new_content)

print("Em dashes removed from all articles!")
