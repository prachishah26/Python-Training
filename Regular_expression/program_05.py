# Write a regular expression to get only the part of the email before the "@" sign and include the "@" sign
import re
str = "prachis.wot2022@gmail.com"
match = re.findall("[a-zA-Z0-9.]+@",str)
print(match)