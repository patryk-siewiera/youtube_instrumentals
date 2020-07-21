import pprint

import PySimpleGUI as sg
import validators
from youtube_dl import YoutubeDL

# TODO: separate gui and logic?

ydl_opts = {
    # options for youtube_dl
    # simulate: true -> this will only gather information
    'format': 'bestaudio/best',
    'outtmpl': '!download/%(uploader)s/%(title)s.%(ext)s',
    'min_views': 10000,
    'max_views': 10000000000000,
    'max_length': 1000,
    'ignoreerrors': True,
    'simulate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '320',
    }],
}


def parse(gui_output):
    parsed_list = []
    iterations = int(len(gui_output) / 3 - 1)
    for k in range(iterations):
        k = k + 1
        id_name = k * 10 + 0
        id_how_much = k * 10 + 1
        id_method = k * 10 + 2

        # parse for every iteration (line), corresponding value
        name = gui_output[id_name]
        how_much = gui_output[id_how_much]
        method = gui_output[id_method]

        # print(name)

        if validators.url(name):
            parsed_list.append(["SEARCH_FOR_TAB_NAME", name])

        # skip empty queries
        elif name == "" or name is None or how_much == 0:
            continue

        elif not validators.url(name):
            # remove chars that aren't letters or numbers
            alphanumeric = [character for character in name if (character.isalnum() or character.isspace())]
            name = "".join(alphanumeric)
            # query generator
            query = "ytsearch" + str(how_much) + ":" + str(name)
            output = [name, query]
            parsed_list.append(output)

    return parsed_list


def get_info_all_list(links_list):
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

    progress_count = 0
    progress_bar_steps = 0
    for _ in range(len(links_list)):
        for __ in range(len(links_list[_])):
            progress_bar_steps = progress_bar_steps + 1
    layout = [[sg.ProgressBar(progress_bar_steps, orientation='h', size=(70, 20), key='progbar')]]
    # create the Window
    window = sg.Window('Searching for more details...', layout)

    YoutubeDL(ydl_opts).cache.remove()

    output_info = []
    for i in range(len(links_list)):
        name_for_tab = False
        event, values = window.read(timeout=0)
        tab_title = links_list[i][0]

        if tab_title == "SEARCH_FOR_TAB_NAME":
            name_for_tab = True
            print("\n\n\nHERE FIND TAB NAME ")

        print("\n\ttab title: ", tab_title)
        output_info.insert(i, [tab_title])
        output_info[i][0] = tab_title

        for j in range(len(links_list[i])):
            if event == 'Cancel' or event == sg.WIN_CLOSED:
                break
            if j > 0:
                link_current_iteration = links_list[i][j]
                ydl_info_current = ydl_extract_info(link_current_iteration)
                output_info[i].insert(j, ydl_info_current)
                if name_for_tab == True:
                    print("\n\n TRUE")
                    try:
                        uploader = ydl_info_current['uploader']
                    except:
                        uploader = "??"
                    print(ydl_info_current)
                    output_info[i][0] = uploader
                    print(uploader)
            window['progbar'].update_bar(progress_count)
            progress_count = progress_count + 1

    save_to_file(output_info)

    window.close()

    output_info = create_window(output_info)

    return output_info


def ydl_extract_info(video):
    """
    take URL (str),
    and returns dict with information
    ydl.extract_info
    """

    # retry 10 times before
    i = 0

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


def info_current_item(data):
    '''
    format data for easier reading
    :param data: data parsed from get_info_all_list
    :return:
    '''
    output_list = []
    max_length = 50  # cut longer strings than, to make window smaller

    for i in range(len(data) - 1):
        i = i + 1

        # ytsearchX: is nested list so need to be iterated, single links don't
        try:
            range_of_list = len(data[i]['entries'])
            nested = True
        except:
            range_of_list = 1
            nested = False

        for j in range(range_of_list):
            # nested / not nested (signle links) need different queries
            if nested:
                query_search_or_link = data[i]['entries'][j]
            elif not nested:
                query_search_or_link = data[i]

            try:
                # sometimes current_average rating (like / dislike) == 0
                current_average = str("{:.2f}").format(float(query_search_or_link["average_rating"]) / 5 * 100)[
                                  :max_length]
            except:
                current_average = str('without any votes')

            try:
                title = str(query_search_or_link['title'])[:max_length]
                uploader = str(query_search_or_link['uploader'])[:max_length]

                # format view_count for ever 1000, example: 1,000,000,000
                view_count = query_search_or_link['view_count']
                view_count = f"{view_count:1,}"
                view_count = view_count.replace(",", " ")
                webpage_url_key = query_search_or_link['webpage_url']

                # format all parsed information to one string
                output = str("title:\t\t" + title \
                             + "\nuploader:\t\t" + uploader \
                             + "\nlike / dislike ratio:\t" + current_average + " %" \
                             + "\nview_count:\t" + view_count + "\n")

                # TODO: modify this line to vertical
                output_list = output_list + [checkbox_per_track(output, webpage_url_key)]

            except:
                # if there is premiere - you cannot download it
                # will just skip it
                pass

    return output_list


def tab_group_generator(title, layout):
    multiple = []
    horizontal_elements_size = 10
    print("len layout", len(layout))
    for i in range((len(layout) // horizontal_elements_size) + 1):
        print("inside")
        start_list = i * horizontal_elements_size
        end_list = (i + 1) * horizontal_elements_size
        print('range', start_list, end_list)
        multiple = multiple + [sg.Frame("inside tabs frame", layout[start_list:end_list])]

    return sg.Tab(title=title,
                  layout=[multiple])


def layout_generator(data):
    tab_names = []
    unpack = []
    for tab_count in range(len(data)):
        # parse tab names, and cut more than 15 chars
        tab_names.append(data[tab_count][0][:15])

    # TODO: here change to vertical output in frames
    for j in range(len(data)):
        unpack.append(info_current_item(data[j]))

    inside_list = []

    def inside_layout(tab_names, unpack):
        """
        create layout for inside of every tab
        """
        for i in range(len(tab_names)):
            inside_list.append(tab_group_generator(tab_names[i], unpack[i]))
            # every tab have objects - tracks - to calculate per tab - unpack[i]
            # print(unpack[i])

        return inside_list

    inside_list = inside_layout(tab_names, unpack)

    print(inside_list)
    button_size = (32, 1)
    outside_layout = [
        [sg.TabGroup([inside_list])],
        [sg.Button('Download and create stems', key="download_and_create_stems", size=button_size),
         sg.Button('Download only', key="download_only", size=button_size)]]

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
                       font=("Calibri ", 8), keep_on_top=True, resizable=True)

    # put output from window to variable, values
    event, values = window.read()

    pressed_button = event

    # windows return what link to download, here take only with TRUE and returns it
    link_list = []
    for link, bool_checkbox_downloading in values.items():
        if bool_checkbox_downloading:
            if validators.url(str(link)):
                link_list.append(link)

    window.close()
    return link_list, pressed_button


def put_content_into_frame(content, key):
    """
    this MAY BE used later as column generator
    when dealing with a lot of files to download
    rows x columns
    right now only one column
    """
    return [[sg.Frame(title="title", key=key, layout=[[sg.Text(content)]])]]


def checkbox_per_track(data, key):
    """
    \n\n+\n\n -> don't need to click precise in checkbox - whole box is clickable
    :return: one checkbox element - track
    """
    return [sg.Checkbox("\n\n+\n\n", default=True, key=key, size=(1, 5)), sg.T(data, size=(60, 5))]


def save_to_file(input_data):
    """
    save input_data, in output__searching_results_PY.py file with pprint formatting
    """
    # if depth to small, returns (...) and cut important data
    pp = pprint.PrettyPrinter(depth=10)
    output = pp.pformat(input_data)
    filename = "data/output/output__searching_results_PY.py"
    open(filename, "w", encoding="utf-8").write("output=" + output)
    print("\nRaw youtube data in file (PPrint):\n", filename, "\n")
    return output


# print(get_info_all_list(sample_links.nested_link_sample_data12))

mock_sample = [['q1', 'https://www.youtube.com/watch?v=WlosNFMCnE4'],
               ['q2', 'ytsearch2:test']]

mock_sample_only_search = [['q2', 'ytsearch10:ariana grande']]

mock_sample2 = [['q1', 'https://www.youtube.com/watch?v=WlosNFMCnE4', 'https://www.youtube.com/watch?v=q9fiSHCl5KQ'],
                ['q2', 'https://www.youtube.com/watch?v=yslkYSjAPh4', 'https://www.youtube.com/watch?v=qu577tNp1hA'],
                ['q3', 'QpyHrQYeoIE'],
                ['arianna grande', 'ytsearch10:ariana grande'],
                ['son lux', 'ytsearch12:son lux'],
                ['flume eeeeeee', 'ytsearch6:flume']]

tab_test = [['q3', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['long_tabtabtabtabtabname', 'QpyHrQYeoIE'],
            ['q3', 'QpyHrQYeoIE']]

mock_live_trans = [['flume', 'ytsearch3:flume']]

# print(get_info_all_list(tab_test))
# print(get_info_all_list(mock_live_trans))
# print(get_info_all_list(mock_sample2))
# get_info_all_list(sample_links.nested_link_sample_data14_23_24_skrillex_tameimpala_hole)
# print(get_info_all_list(parse(sample_gui.mock_gui_livestream_link_huge)))
# var = output__searching_results_PY
# create_window(output__searching_results_PY.output)
