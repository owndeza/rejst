import os
import re

pattern = re.compile(r'\b(18412|18,412|18\.412|18 412)\b')

script_name = os.path.basename(__file__)

for root, dirs, files in os.walk('.'):
    for file in files:
        if file == script_name:
            continue
        file_path = os.path.join(root, file)
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if pattern.search(content):
                    print(f"Найдено в: {file_path}")
        except PermissionError:
            continue