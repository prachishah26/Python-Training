# Replace all special characters with space using regex

import re
name = "abc@def&ghi!" 
match = re.sub("[^a-zA-Z0-9]"," ",name)
print(match)