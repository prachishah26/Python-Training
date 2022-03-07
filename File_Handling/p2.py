# with open("test.txt",'r',encoding = 'utf-8') as f:
# #    f.
#    f.write("This file\n\n")
#    f.write("contains three lines\n")



f = open("/home/woc/Prachi/Training/Python Training/test.txt",'r',encoding = 'utf-8')
# f.read(4)
# print(f.read())
print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())


data = data2 = ""
  
# Reading data from file1
with open('que.txt') as fp:
    data = fp.read()
  
# Reading data from file2
with open('ans.txt') as fp:
    data2 = fp.read()
  
# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data2