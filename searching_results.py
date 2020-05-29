import datetime
import pprint

import sample_data
import PySimpleGUI as sg
from youtube_dl import YoutubeDL

import backend_ydl

ydl_opts = {
    "ignoreerrors": False,
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
    filename = "!output.txt"
    open(filename, "w", encoding="utf-8").write(output)
    print("PPrint write to file: \t\t ", filename)
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
    YoutubeDL(ydl_opts).cache.remove()
    output = []
    for i in range(len(video)):
        title_ = video[i][0]
        print(title_)
        output.insert(i, [title_])
        output[i][0] = title_
        for j in range(len(video[i])):
            if j > 0:
                link_current_iteration = video[i][j]
                ydl_info_current = ydl_info_one_link(link_current_iteration)
                output[i].insert(j, ydl_info_current)
    save_to_file(output)
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

    return inside(video, i)


def create_window(data_input):
    # pretty_print_results(get_info(video))
    def frame(title, inside_text):
        output = []

        def one_frame(title, inside_text):
            return [sg.Frame(title=title, layout=[[sg.Text(inside_text)]])]

        for i in range(len(title)):
            output.append(one_frame(title[i], inside_text[i]))
        print("\n\n\n\n\n", inside_text)
        return output

    output = []
    # add tags
    title = []
    inside_text = []
    for j in range(len(data_input)):
        data = (data_input[j])
        try:
            title.append(data["artist"])
            current_average = float(data["average_rating"]) / 5 * 100
            inside_text.append("\ntitle:\t\t" + data["title"] \
                               + "\nuploader_id:\t" + str(data["uploader_id"]) \
                               + "\naverage rating:\t" + str("{:.2f}").format(current_average) + " %" \
                               + "\nview_count:\t" + str(data["view_count"]) \
                               + "\n")
        except:
            pass

    def tab(title, layout):
        return sg.Tab(title=title, layout=layout)

    tab1 = [[sg.T('This is inside tab 1')]]

    layout_content = frame(title, inside_text)

    layout = [
        [sg.TabGroup([[sg.Tab('Tab 1', tab1, tooltip='tip'), sg.Tab('Tab 2', layout_content)]])],
        [sg.Button('Read')]]

    # activate frame here in layout =
    window = sg.Window('Frame with buttons', layout=layout,
                       font=("Arial", 8))
    event, values = window.read()
    window.close()


# TODO:
# function save output searching to file -> for easier copying
# do 5 sample data links -> from 1 to 10
# do 5 sample already parsed information

# backend_ydl.remove_ydl_cache()
get_info_all_list(sample_data.nested_link_sample_data11_21_35)
# create_window((get_info(sample_data.link_sample_data4)))
# save_to_file(sample_data.searching_sample_values3)
