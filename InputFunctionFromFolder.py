import os
import audio_metadata
import string

SpaceSimbols = ('/', '\'', '_', '-', ' ')
entries = os.listdir()

newList = []
for i in entries:
    if i[-4:] == '.wav' or i[-4:] == '.mp3':
        newList.append(i)

metadataList = []


def stringRefactoring(dirtyString):
    newString = ''
    for i in dirtyString:
        if i in SpaceSimbols:
            newString = newString + ' '
        elif i in string.ascii_lowercase or i in string.ascii_uppercase:
            newString = newString + i
    while newString[0] == ' ':
        newString = newString[1:]
    while newString[len(newString) - 1] == ' ':
        temp = len(newString) - 1
        newString = newString[:temp]
    newString = newString.lower()
    temp = newString.split()
    separator = ' '
    newString = separator.join(temp)
    return newString


def yearRefactoring(dirtyYear):
    findyear = False
    newString = ''
    for i in range(len(dirtyYear) - 4):
        if dirtyYear[i].isdigit() and dirtyYear[i + 1].isdigit() and dirtyYear[i + 2].isdigit() and dirtyYear[i + 3].isdigit():
            newYear = dirtyYear[i] + dirtyYear[i + 1] + \
                dirtyYear[i + 2] + dirtyYear[i + 3]
            break
    return newYear


for i in newList:
    metadata = audio_metadata.load(i)
    metadataListTemp = [0, 0, 0, 0]
    try:
        metadataListTemp[0] = stringRefactoring(str(metadata.tags.title))
    except AttributeError:
        metadataListTemp[0] = stringRefactoring(i[:-4])
    try:
        metadataListTemp[1] = stringRefactoring(str(metadata.tags.genre))
    except AttributeError:
        metadataListTemp[1] = None
    try:
        metadataListTemp[2] = stringRefactoring(str(metadata.tags.artist))
    except AttributeError:
        metadataListTemp[2] = None
    try:
        metadataListTemp[3] = yearRefactoring(str(metadata.tags.date))
    except AttributeError:
        metadataListTemp[3] = None
    metadataList.append(metadataListTemp)

print(metadataList)
