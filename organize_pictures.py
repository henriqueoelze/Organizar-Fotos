from os import listdir
from os import mkdir
from os import path
from os import rename

basePath = '' #Insert path for organize here

lastFolderName = ''
for file in listdir(basePath):
    if('.jpg' in file or '.jpeg' in file or '.JPEG' in file or '.JPG' in file):
        if('(' in file):
            indexForSubstring = file.index('(')
            folderName = file[:indexForSubstring]
        else:
            indexForSubstring = file.index('.')
            folderName = file[:indexForSubstring]

        folderName = folderName.strip()
        newFolderPath = basePath + '\\' + folderName
        print('-> File "{}" will be moved to folder "{}".'.format(file, newFolderPath))

        if not (path.exists(newFolderPath)):
            mkdir(newFolderPath)
            print('---> Folder {} doesnt exists and was created!'.format(newFolderPath))

        oldPath = basePath + '\\' + file
        newPath = newFolderPath + '\\' + file

        rename(oldPath, newPath)

        lastFolderName = folderName
