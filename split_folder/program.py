# import splitfolders
# splitfolders.ratio('/home/woc/Downloads/images/', output="/home/woc/Downloads/output/", ratio=(.33, 0.33,0.34))

import csv
import os
import re
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)
root = '/home/woc/Prachi/Training/Python_Training/split_folder/prachi/TNR_LPR_cropped_images'
dirlist = sorted_alphanumeric(os.listdir(root))
# print(dirlist)
with open('lable_part_2.csv', 'w') as obj:
     for filename in dirlist:
         write = csv.writer(obj)
         write.writerow([filename])