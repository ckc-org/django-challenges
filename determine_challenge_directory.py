import sys
from collections import defaultdict


BLACKLIST_DIRS = {
    '.github',
}

directories = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    if '/' not in line:
        continue
    directory = line.split('/')[0]
    if directory not in BLACKLIST_DIRS:
        directories[directory] += 1

max_dir = None
max_frequency = 0
for dir in directories:
    if directories[dir] > max_frequency:
        max_dir = dir
        max_frequency = directories[dir]

print(max_dir)
