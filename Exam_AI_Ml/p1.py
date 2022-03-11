# ---------------------importing Libraries---------------
import names
import os
import gdown
from zipfile import ZipFile
import os, shutil

# --------------------------url--------------------------
url = "https://drive.google.com/file/d/1Aeh4GIjLwyiuWGd6AGxM8Q3WgiffLfIu/view"
output = "Exam.Zip"
# -------------------------gdown to download file from link---
gdown.download(url, output,quiet=False,fuzzy=True)


with ZipFile('Exam.Zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()


def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles 

# --------------------------------main function-------------------------------
def main():
    dirName = '/home/woc/Prachi/Training/Python_Training/Exam/'
    
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)
    
    # Print the files
    for elem in listOfFiles:
        print(elem)
        print("\n")
    print ("****************")
    
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    # print(listOfFiles)    
        
    # Print the files    
    with open("all_directories.txt","w") as ad:
        for elem in listOfFiles:
            ad.write(elem+"\n")
    
    for i in listOfFiles:
        with open(i,"w") as iw:
            iw.write(names.get_first_name())

    path1 = '/home/woc/Prachi/Training/Python_Training/Exam/'
    destination = '/home/woc/Prachi/Training/Python_Training/Output/'

    for root, dirs, files in os.walk(path1):
        for file in files:
            if file.endswith("txt"):
                # os.rename(file,root.replace("/","_")+file)
                new = root.replace("/ ","_")+file
                os.rename(os.path.join(root, file), os.path.join(destination, new))

    for root, dirs, files in os.walk(path1):
        for file in files:
            if file.endswith("txt"):
                shutil.copy(os.path.join(root,file),os.path.join(destination, file))
                  
if __name__ == '__main__':
    main()
    



