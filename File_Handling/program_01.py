# You have two files named questions.txt and answer.txt. You need to create a file that contains questions and answers. But both input files contain random questions followed by a numeric value. You need to match both values and then copy the question-answer pair in a new file.
# -> Optimize code properly.
# Sample file: question.txt:
# 3. What is your Hobby?
# 1. What is your name?
# 2. Where are you from?
# Sample file: answer.txt:
# 2. India
# 1. Bob
# 3. Swimming
# Output file:
# 1. What is your name?
# Bob
# 2. Where are you from?
# India
# 3. What is your Hobby?
# Swimming


filenames = ["que.txt","ans.txt"]
lines = []
for f in filenames:
   with open(f) as infile:
        for line in infile:
            lines.append(line)

lines.sort(key = lambda x:int(x[0]) )
# print(lines)

for i in range(len(lines)):
    with open("que_ans.txt","w") as qs:
        qs.write(''.join(lines))
