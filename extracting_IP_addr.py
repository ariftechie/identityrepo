import re

with open('C:/Repo/Documents/rad_log.txt') as fh:
    file = fh.readlines()

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

lst = []
for line in file:
    match = pattern.findall(line)
    if len(match) != 0:
        lst.extend(match)

unique_addr = str(set(lst))

with open("C:/Repo/Documents/rad_log.txt", "w") as f:
    f.write(unique_addr)