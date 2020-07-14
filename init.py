import gui
import searching_results
import backend_ydl
import clean_my_project
import download_list_link

# clean_my_project.main()

gui_output = gui.main()

link_list = backend_ydl.ydl(gui_output)

searching_output = searching_results.get_info_all_list(link_list)

download_list_link.download(searching_output)
