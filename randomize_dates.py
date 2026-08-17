import os
import glob
import random
import re
from datetime import datetime, timedelta

def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

start_date = datetime(2026, 7, 1)
end_date = datetime(2026, 8, 17)

files = glob.glob("src/content/blog/*.md")

for filepath in files:
    with open(filepath, 'r') as file:
        content = file.read()
    
    new_date = random_date(start_date, end_date).strftime("%Y-%m-%d")
    
    # Replace pubDate
    new_content = re.sub(r'pubDate:\s*\d{4}-\d{2}-\d{2}', f'pubDate: {new_date}', content)
    
    with open(filepath, 'w') as file:
        file.write(new_content)

print("Dates randomized successfully!")
