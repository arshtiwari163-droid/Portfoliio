import re
import os

file_path = 'hp.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the entire body::before block including the base64 string
new_content = re.sub(r'body::before\s*\{.*?\}', '', content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Block removed successfully.")
