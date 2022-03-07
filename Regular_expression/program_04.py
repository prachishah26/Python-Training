# Loop through the list and apply the regex to each element so that only items ending with a semicolon (;) are matched
import re
data = ["abc", "abcdef;", "prachi", "shah;"]
for i in data:
    if re.findall(";$",i):
        print(i)