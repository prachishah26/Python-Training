# Replace the space character that occurs after a word ending with a or r with a newline character
# Sample input: area not a _a2_ roar took 22
# Sample output:
# area
# not a
# _a2_ roar
# took 22

import re
from typing import final
str = "area not a _a2_ roar took 22"
elements_of_str = str.split(" ")
final_string = ""
# print(elements_of_str)
match = re.findall(r"\b[a-zA-Z]*a\b | \b[a-zA-Z]*r\b ",str)
for i in range(len(match)):
    match[i] = match[i].lstrip()
    match[i] = match[i].rstrip()
print(match)

for elements in elements_of_str:
    final_string += elements + " "
    if elements in match:
        final_string += "\n"

print(final_string)

