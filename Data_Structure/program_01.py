# Slice list into 3 equal chunks and reverse each chunk

raw_list =  [11, 45, 8, 23, 14, 12, 78, 45, 89, 1, 2]
raw_list = [1,2,3,4,5,6,7,8,9]
new_raw_list = []
parts = 5
parts_of_rawdata = 3


for itr in range(parts):
    if itr != parts-1:
        sub_list = raw_list[0:parts_of_rawdata]
        sub_list = sub_list[-1::-1]
        new_raw_list.append(sub_list)
        raw_list = raw_list[parts_of_rawdata:]
    else:
        sub_list = raw_list[0:]
        sub_list = sub_list[-1::-1]
        print(sub_list)
        new_raw_list.append(sub_list)
    
print(new_raw_list)

#  ---------------------------------------------------------------------------

# chunks = int((len(raw_list)/parts))
# for itr in range(parts):
#     if itr != parts-1:
#         sub_list = raw_list[0:parts_of_rawdata]
#         sub_list.reverse()
#         new_raw_list.append(sub_list)
#         raw_list = raw_list[parts_of_rawdata:]
#     else:
#         sub_list = raw_list[0:]
#         sub_list.reverse()
#         new_raw_list.append(sub_list)
        
# print(new_raw_list)