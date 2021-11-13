import os

path = r'D:\GB'
project_name = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']


def create_Folder(path):
    if not os.path.exists(fullPath):
        os.mkdir(fullPath)


fullPath = os.path.join(path, project_name)
create_Folder(fullPath)

for f in folders:
    folder = os.path.join(fullPath, f)
    create_Folder(folder)

