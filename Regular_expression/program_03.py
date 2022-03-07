# Find the numbers starting with 212 from a string.
import re
raw_string = 'ggg2120000 house no. 21245'
match = re.findall(r"\b212\d+",raw_string)
print(match)
