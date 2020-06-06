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
    """
    parse information window for selected links
    :param data_input:
    :return: selected links
    """
    layout_content_tab1 = [[sg.T('This is inside ab 1')]]
    layout_content_tab2 = [[sg.CB(' '), sg.T(unpack_data(data_input[0]))]]

    layout = [
        [sg.TabGroup(
            [[sg.Tab(title=data_input[0][0], layout=layout_content_tab1),
              sg.Tab(title=data_input[1][0], layout=layout_content_tab2)]])],
        [sg.Button('Ok')]]

    # activate frame here in layout =
    window = sg.Window('Frame with buttons', layout=layout,
                       font=("Arial", 8))

    # output values from window
    event, values = window.read()
    window.close()


def put_content_into_frame(content):
    return [[sg.Frame(title="title", layout=[[sg.Text(content)]])]]


def unpack_data(data):
    '''
    format data for easier reading
    :param data: data parsed from get_info_all_list
    :return:
    '''
    title = data[0]
    inside_text = []
    title = str(data[1]['title'])
    uploader = str(data[1]['uploader'])
    current_average = str("{:.2f}").format(float(data[1]["average_rating"]) / 5 * 100)
    view_count = str(data[1]['view_count'])
    output = ("title:\t\t" + title \
              + "\nuploader:\t\t" + uploader \
              + "\naverage rating:\t" + current_average + " %" \
              + "\nview_count:\t" + view_count + "\n")

    # output = put_content_into_frame(output)
    return output


create_window(sample_data.output_11_22)
