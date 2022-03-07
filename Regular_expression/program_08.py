# Split the given input string on one or more repeated sequences of cat using regex
# Sample input: firecatlioncatcatcatbearcatcatparrot
# Sample output: ['fire', 'lion', 'bear', 'parrot']
import re
str = "firecatlioncatcatcatbearcatcatparrot"
match = re.split(r'cat',str)
matched_list = list(filter(lambda x: x != "", match))

print(matched_list)
