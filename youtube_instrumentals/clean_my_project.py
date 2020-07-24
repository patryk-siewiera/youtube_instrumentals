import os
from pathlib import Path
import shutil
import time


def create_folder(folder_name):
    """create folders specified in argument"""
    print('\n_* def create_folder():  INPUT == ', folder_name, '\n')

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    return folder_name


def move_files(extension, folder):
    """move files with extension to specific folder"""
    print('\n_* def move_files():  INPUT ==  ext==', extension, " folder==", folder)
    sourcepath = Path().absolute()
    sourcefiles = os.listdir(sourcepath)
    destination = str(sourcepath.joinpath(folder))

    for file in sourcefiles:
        if file.endswith(extension):
            shutil.move(os.path.join(sourcepath, file), os.path.join(destination, file))


def remove_delete_download(folder):
    """delete folders with all content from:"""
    print('\n')
    try:
        shutil.rmtree(folder)
    except FileNotFoundError:
        print('Cannot delete: ', folder)


def main():
    """
    removes all downloaded files
    """
    move_files('.part', create_folder('!delete'))
    move_files('.ytdl', create_folder('!delete'))
    move_files('.wav', create_folder('!delete'))
    remove_delete_download("!delete")
    remove_delete_download("!audio")
