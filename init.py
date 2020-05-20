import gui
import searching_results
import backend_ydl
import clean_my_project



clean_my_project.main()

gui_output = gui.main()

ydl = backend_ydl.ydl(gui_output)
