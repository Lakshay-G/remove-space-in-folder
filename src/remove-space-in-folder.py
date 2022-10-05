import os
from tkinter import Tk
from tkinter.filedialog import askdirectory


def RemoveSpaceInFolder(mypath):
    '''os.walk() goes in the path mentioned as the argument and finds all the
    root, folder and file names. 
        [0] index => root name,
        [1] index => folder names,
        [2] index => file names
        We choose [1] to get all the folder names
        '''
    foldernames = next(os.walk(mypath), (None, None, []))[1]
    for foldername in foldernames:
        changedname = foldername.replace(" ", "_")
        os.rename(mypath+'/'+foldername, mypath+'/'+changedname)
    # print(foldernames)


if __name__ == "__main__":

    mypath = askdirectory(title='Select your folder: ')
    RemoveSpaceInFolder(mypath)
