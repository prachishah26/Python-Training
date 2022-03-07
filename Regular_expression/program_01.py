# Write a regular expression to search digits inside a string
import re
raw_string = "pra1chishah0123"
match = re.findall('[0-9]',raw_string)
print(match)                     #gives integers in lists seperated by comma

# ---------------other method-------------------------------

match = re.findall("\d+",raw_string)
print(match)                       #gives integers together 