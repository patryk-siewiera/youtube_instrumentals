import os
import shutil
from pathlib import Path


class OrganizeDownloadedFiles:
    """
    this is doctype for class -> ctrl + Q
    """

    def __init__(self, create_new_folder, extensions_moved_to_new_folder, remove_folder_and_content_inside):
        self.create_fld = create_new_folder
        self.extensions = extensions_moved_to_new_folder
        self.remove_fld = remove_folder_and_content_inside

    def create_folder(self):
        """create folders specified in argument"""
        print('\n_* def create_folder():  INPUT == ', self.create_fld, '\n')
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

# removes all downloaded files + partly and undone
organize = OrganizeDownloadedFiles('!delete', ['.part', '.ytdl', '.wav'], ['!delete', 'audio'])
organize.create_folder()
organize.move_files()
organize.remove_delete_download()
# OrganizeDownloadedFiles.remove_delete_download('audio')
