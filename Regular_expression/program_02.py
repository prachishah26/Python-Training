# Find the words with exactly 8 letters from paragraph using regex
import re
raw_string = 'helloooo , my name is prachi..'
match = re.findall(r"\b[a-zA-Z]{8}\b", raw_string)
print(match)