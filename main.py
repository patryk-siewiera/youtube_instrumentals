from youtube_instrumentals import gui, download_list_link, backend_ydl, searching_results, clean_my_project

from youtube_instrumentals.test.scenarios import Testing

# clean_my_project.main()

if __name__ == '__main__':
    test = Testing()
    test.test_multiple_keywords_and_offline()
    return
    gui_output = gui.main(SAMPLE_INPUT)
    gui_output = gui.main()
    link_list = backend_ydl.parse(gui_output)
    searching_output = searching_results.get_info_all_list(link_list)
    download_list_link.download_only(searching_output)
