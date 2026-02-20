import os
UPLOADIR = "/Upload"
COPYDIR = "/UploadCopy"
curDir = os.getcwd()
workDir = curDir + UPLOADIR
copyDir = curDir + COPYDIR




def getFileSize(filepath):
    #Returns size of file in BYTES
    return os.path.getsize(filepath)



if not os.path.exists(copyDir):
    os.mkdir(copyDir)
for root, dirs, files in os.walk(workDir):
    for fileName in files:
        lFilePath = os.path.join(root, fileName)
        rFilePath = os.path.join(copyDir, f"{fileName}-Copy.txt")

        print("Size of File %s: %s Bytes"% (fileName, getFileSize(os.path.join(root, fileName))))

        with open(lFilePath, mode='rb') as filetoCopy:
            with open(rFilePath, mode='wb') as filetoWrite:
                filetoWrite.write(filetoCopy.read())




testLoop = ['This', 'Is', 'A', 'Loop']
while getFileSize(os.path.join(copyDir, "test4-Copy.txt")) < 50000:
    absPath = os.path.join(copyDir, "test4-Copy.txt")
    with open(absPath, 'a+') as fileToWrite:
        for let in testLoop:
            fileToWrite.write(let)

print("New File size for test4-Copy.txt: \n")
print(f"{getFileSize(os.path.join(copyDir, "test4-Copy.txt"))}")