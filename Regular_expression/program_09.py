# Filter all elements that contain a sequence of lowercase alphabets followed by - followed by digits. They can be optionally surrounded by {{ and }}. Any partial match shouldn't be part of the output.
# Sample input: ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']
# Sample output: ['{{apple-150}}', 'grape-87']

import re
# from typing import final
data = ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']
final_list=[]
for index in range(len(data)):
    match = re.findall(r"{{[a-z]*-[0-9]*}}|\b[a-z]*-[0-9]*\b",data[index])
    if match:
        if len(match[0]) == len(data[index]):
            final_list.append(match[0])


print(final_list)
