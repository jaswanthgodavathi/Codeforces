import re

input_str = input().strip()
if not input_str:
    distinct_count = 0
else:
    elements = re.findall(r'\w+', input_str)
    distinct_count = len(set(elements))
print(distinct_count)
