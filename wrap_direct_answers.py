import os
import glob
import re

files = glob.glob("src/content/blog/*.md")

def replacer(match):
    text = match.group(0)
    # Remove the **Direct answer:** bold text because we might want to style it via CSS 
    # or keep it and just wrap the whole thing. The user wants the paragraph contrasted.
    # We will just wrap it.
    return f'<div class="direct-answer">\n\n{text}\n\n</div>'

for filepath in files:
    with open(filepath, 'r') as file:
        content = file.read()
    
    # We want to match the paragraph starting with **Direct answer:**
    # The regex looks for **Direct answer:** at the start of a line, 
    # followed by anything until it hits a double newline \n\n or end of file \Z.
    new_content = re.sub(r'^\*\*Direct answer:\*\*.*?(?=\n\n|\Z)', replacer, content, flags=re.MULTILINE | re.DOTALL)
    
    with open(filepath, 'w') as file:
        file.write(new_content)

print("Direct answers wrapped successfully!")
