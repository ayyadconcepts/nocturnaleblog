import glob

files = glob.glob("src/content/blog/*.md")

for filepath in files:
    with open(filepath, 'r') as file:
        content = file.read()
    
    # Remove the literal text but keep the paragraph intact
    new_content = content.replace("**Direct answer:** ", "")
    
    with open(filepath, 'w') as file:
        file.write(new_content)

print("Removed literal 'Direct answer:' text from all files.")
