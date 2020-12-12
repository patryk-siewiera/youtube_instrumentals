import logging
import os
import shutil
from pathlib import Path
import inspect

FILENAME_LOGS = "output/logs.txt"

logging.basicConfig(filename=FILENAME_LOGS, level=logging.DEBUG, format="%(asctime)s:  %(message)s")


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
        self.create_fld = str(create_new_folder)
        self.extensions = list(extensions_moved_to_new_folder)
        self.remove_fld = str(remove_folder_and_content_inside)

    def create_folder(self):
        logging.info("def {}():".format(inspect.stack()[0][3]))
        if not os.path.exists(self.create_fld):
            os.makedirs(self.create_fld)
            logging.info("\t" + self.create_fld + ' : Folder name -> Created')
        return self.create_fld

    def move_files(self):
        logging.info("def {}():".format(inspect.stack()[0][3]))
        sourcepath = Path().absolute()
        sourcefiles = os.listdir(sourcepath)
        destination = str(sourcepath.joinpath(self.create_fld))

        for file in sourcefiles:
            for ext_iterable in self.extensions:
                if file.endswith(ext_iterable):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(destination, file))
                    logging.info("\t {} was moved to {}".format(file, destination))

    def remove_delete_download(self):
        logging.info("def {}():".format(inspect.stack()[0][3]))
        try:
            shutil.rmtree(self.remove_fld)
            logging.info("\t" + self.remove_fld + ' : Folder name -> Deleted')
        except FileNotFoundError:
            logging.info("\t" + self.remove_fld + ' : Folder name -> Cannot be deleted')


# TODO: create logs via debbuging python?

# TODO: resume_here

if __name__ == '__main__':
    # removes all downloaded files + partly and undone
    organize = OrganizeDownloadedFiles('!delete', ['.part', '.ytdl', '.wav'], '!delete')
    # organize.create_folder()
    # organize.move_files()
    # organize.remove_delete_download()
    # OrganizeDownloadedFiles()
