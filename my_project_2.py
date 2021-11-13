import os
import shutil

RootDir1 = r'D:\GB'
TargetFolder = r'D:\GB\my_project'
for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
    for name in files:
        if name.endswith('.jpg'):
            print "Found"
            SourceFolder = os.path.join(root,name)
            shutil.copy2(SourceFolder, TargetFolder) #copies file to target folder