# Slice list into 3 equal chunks and reverse each chunk

raw_list =  [11, 45, 8, 23, 14, 12, 78, 45, 89, 1, 2]
new_raw_list = []
n = 5
parts_of_rawdata = 2
# chunks = int((len(raw_list)/n))
for i in range(n):
    if i != n-1:
        a = raw_list[0:parts_of_rawdata]
        a.reverse()
        new_raw_list.append(a)
        raw_list = raw_list[parts_of_rawdata:]
    else:
        a = raw_list[0:]
        a.reverse()
        new_raw_list.append(a)
        
print(new_raw_list)
