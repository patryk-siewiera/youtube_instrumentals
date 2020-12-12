import logging
import os
import shutil
from pathlib import Path

logging.basicConfig(filename="output/logs.txt", level=logging.DEBUG, format="%(asctime)s:  %(message)s")


class OrganizeDownloadedFiles:
    """
    this is doctype for class -> ctrl + Q

    Parameters:
        create_new_folder (str) : this is test docstring
        extensions_moved_to_new_folder (list) : all of extensions that should be moved out
        remove_folder_and_content_inside (str) : remove this folder name
    Returns:
        action (str) : this is test returns
    """

    def __init__(self, create_new_folder, extensions_moved_to_new_folder, remove_folder_and_content_inside):
        self.create_fld = create_new_folder
        self.extensions = extensions_moved_to_new_folder
        self.remove_fld = remove_folder_and_content_inside

    def create_folder(self):
        """create folders specified in argument"""
        logging.info('\n_* def create_folder():  INPUT == ', self.create_fld, '\n')
        if not os.path.exists(self.create_fld):
            os.makedirs(self.create_fld)
        return self.create_fld

    def move_files(self):
        """move files with extension to specific folder"""
        print('\n_* def move_files():  INPUT ==  ext==', self.extensions, " folder==", self.create_fld)
        sourcepath = Path().absolute()
        sourcefiles = os.listdir(sourcepath)
        destination = str(sourcepath.joinpath(self.create_fld))

        for file in sourcefiles:
            for ext_iterable in self.extensions:
                if file.endswith(ext_iterable):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(destination, file))

    def remove_delete_download(self):
        """delete folders with all content from:"""
        print('\n')
        for fld_iterable in self.remove_fld:
            try:
                shutil.rmtree(fld_iterable)
            except FileNotFoundError:
                print('Cannot delete: ', fld_iterable)


# TODO: create logs via debbuging python?

# TODO: resume_here

if __name__ == '__main__':
    # removes all downloaded files + partly and undone
    organize = OrganizeDownloadedFiles('!delete', ['.part', '.ytdl', '.wav'], '!delete')
    # organize.create_folder()
    # organize.move_files()
    # organize.remove_delete_download()
    # OrganizeDownloadedFiles()
