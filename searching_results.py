import pprint

# from . import sample_data
import PySimpleGUI as sg
import validators
from youtube_dl import YoutubeDL
from data import sample_links

ydl_opts = {
    "ignoreerrors": True,
    'sleep_interval': 5,
    'geo-bypass': False,
    'quiet': False
}


def save_to_file(input_data):
    """
    save input_data, in !output.txt file with pprint formatting
    """
    # if depth to small, returns (...) and cut important data
    pp = pprint.PrettyPrinter(depth=10)
    output = pp.pformat(input_data)
    filename = "data/!output__searching_results_PY.txt"
    open(filename, "w", encoding="utf-8").write(output)
    print("\nRaw youtube data in file (PPrint):\n", filename, "\n")
    return output


def get_info_all_list(video):
    """
    input:
    [
        [ query - tab name, url1, url2 ],
        [ query - tab name, url3, url4 ],
    ]


    :return:
    [
        [ query - unchanged, info_url1, info_url2],
        [ query - unchanged, info_url3, info_url4],
    ]
    """
    sg.theme('dark')
    progress_bar_steps = 0
    for _ in range(len(video)):
        for __ in range(len(video[_])):
            progress_bar_steps = progress_bar_steps + 1
    # print('progress bar steps: ', progress_bar_steps)

    layout = [[sg.ProgressBar(progress_bar_steps, orientation='h', size=(70, 20), key='progbar')]]

    # create the Window
    window = sg.Window('Searching for more details...', layout)

    YoutubeDL(ydl_opts).cache.remove()

    output = []

    progress_count = 0
    for i in range(len(video)):
        event, values = window.read(timeout=0)
        title_ = video[i][0]
        print("\nquery name: ", title_)
        output.insert(i, [title_])
        output[i][0] = title_

        for j in range(len(video[i])):
            if event == 'Cancel' or event == sg.WIN_CLOSED:
                break
            if j > 0:
                link_current_iteration = video[i][j]
                ydl_info_current = ydl_info_one_link(link_current_iteration)
                output[i].insert(j, ydl_info_current)
            window['progbar'].update_bar(progress_count)
            progress_count = progress_count + 1
    save_to_file(output)

    window.close()

    output = create_window(output)

    return output


def ydl_info_one_link(video):
    """
    take URL (str), and returns dict with information
    :param video: str url
    :return: dict
    """
    i = 0

    # retry 10 times before
    def inside(video, i):
        with YoutubeDL(ydl_opts) as ydl:
            try:
                info_dict = ydl.extract_info(video, download=False)
            except:
                i = i + 1
                print("Retry: ", i)
                if i >= 10:
                    return None
                inside(video, i)
        return info_dict

    try:
        output = inside(video, i)
    except:
        pass

    return output


def progress_bar():
    # TODO: continue here, merge two functions to one
    # layout the Window

    layout = [[sg.Text('A custom progress meter')],
              [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
              [sg.Output(size=(50, 10), key='-OUTPUT-')],
              [sg.Cancel()]]

    # create the Window
    window = sg.Window('Custom Progress Meter', layout)

    # loop that would normally do something useful
    for i in range(1000):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.read(timeout=0)
        print("output sample")
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
            # update bar with loop value +1 so that bar eventually reaches the maximum
        window['progbar'].update_bar(i + 1)
    # done with loop... need to destroy the window as it's still open
    window.close()


def tab_group_generator(title, layout):
    return sg.Tab(title=title, layout=[[sg.Frame("inside tabs frame", layout)]])


def layout_generator(data):
    tab_names = []
    unpack = []
    for tab_count in range(len(data)):
        tab_names.append(data[tab_count][0])

    # TODO: here change to vertical output in frames
    for j in range(len(data)):
        unpack.append(unpack_list(data[j]))

    inside_list = []

    def inside_layout(tab_names, unpack):
        """
        create layout for inside of every tab
        """
        for i in range(len(tab_names)):
            inside_list.append(tab_group_generator(tab_names[i], unpack[i]))
        return inside_list

    inside_list = inside_layout(tab_names, unpack)

    outside_layout = [
        [sg.TabGroup([inside_list])],
        [sg.Button('Download selected')]]

    # pprint.pprint(inside_list)

    return outside_layout


def create_window(data_input):
    """
    parse information window for selected links
    :param data_input:
    :return: selected links
    """

    sg.theme('dark')

    # unpack all of data
    layout = layout_generator(data_input)
    # activate frame here in layout =
    window = sg.Window('Download selected tracks', layout=layout,
                       font=("Calibri ", 8))

    # put output from window to variable, values
    event, values = window.read()

    # windows return what link to download, here take only with TRUE and returns it
    link_list = []
    for link, bool_checkbox_downloading in values.items():
        if bool_checkbox_downloading:
            if validators.url(str(link)):
                link_list.append(link)

    window.close()
    return link_list


def put_content_into_frame(content, key):
    return [[sg.Frame(title="title", key=key, layout=[[sg.Text(content)]])]]


def unpack_list(data):
    output = ""
    # for i in range(len(data)):
    #     output = str(output) + str(get_info_current_item(data[i]))
    # return get_info_current_item(data)
    return get_info_current_item(data)


def checkbox_per_track(data, key):
    """
    \n\n+\n\n -> don't need to click precise in checkbox - whole box is clickable
    :return: one checkbox element - track
    """
    return [sg.Checkbox("\n\n+\n\n", default=True, key=key, size=(1, 5)), sg.T(data, size=(60, 5))]


def get_info_current_item(data):
    '''
    format data for easier reading
    :param data: data parsed from get_info_all_list
    :return:
    '''
    output = ""
    output_list = []
    max_length = 50  # cut longer strings than, to make window smaller
    for i in range(len(data) - 1):
        i = i + 1
        title = str(data[i]['title'])[:max_length]
        uploader = str(data[i]['uploader'])[:max_length]
        current_average = str("{:.2f}").format(float(data[i]["average_rating"]) / 5 * 100)[:max_length]
        view_count = data[i]['view_count']
        view_count = f"{view_count:1,}"
        view_count = view_count.replace(",", " ")
        webpage_url_key = data[i]['webpage_url']
        output = str("title:\t\t" + title \
                     + "\nuploader:\t\t" + uploader \
                     + "\nlike / dislike ratio:\t" + current_average + " %" \
                     + "\nview_count:\t" + view_count + "\n")

        # modify this line to vertical
        output_list = output_list + [checkbox_per_track(output, webpage_url_key)]
        # output_list.append(create_layout(output, webpage_url_key))
    return output_list


print(get_info_all_list(sample_links.nested_link_sample_data12))
