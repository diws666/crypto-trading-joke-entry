import os

# Verified count: 97 characters (97 UTF-8 bytes).
LINE = "I bought the dip. Then I bought the dip of the dip. I now own a very expensive lesson in gravity."

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8', newline='') as f:
    f.write(LINE)

print(len(LINE))
