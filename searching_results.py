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
    # layout_content_tab1 = [[sg.T('This is inside ab 1')]]
    layout_content_tab1 = unpack_list(data_input[0])
    # layout_content_tab2 = get_info_current_item(data_input[1]) + get_info_current_item(data_input[0])
    layout_content_tab2 = unpack_list(data_input[1])

    layout = [
        [sg.TabGroup(
            [[sg.Tab(title=data_input[0][0], layout=layout_content_tab1),
              sg.Tab(title=data_input[1][0], layout=layout_content_tab2)]])],
        [sg.Button('Ok')]]

    # activate frame here in layout =
    window = sg.Window('Frame with buttons', layout=layout,
                       font=("Calibri ", 8))

    # output values from window
    event, values = window.read()
    window.close()


def create_layout(data):
    # key for Checkbox -> url
    # download all keys
    return [[sg.CB('+', default=True), sg.T(data)]]


def put_content_into_frame(content):
    return [[sg.Frame(title="title", layout=[[sg.Text(content)]])]]


def unpack_list(data):
    output = ""
    print(data[1])
    # for i in range(len(data)):
    #     output = str(output) + str(get_info_current_item(data[i]))
    return get_info_current_item(data)


def get_info_current_item(data):
    '''
    format data for easier reading
    :param data: data parsed from get_info_all_list
    :return:
    '''
    output = ""
    for i in range(len(data) - 1):
        i = i + 1
        title = str(data[i]['title'])
        uploader = str(data[i]['uploader'])
        current_average = str("{:.2f}").format(float(data[1]["average_rating"]) / 5 * 100)
        view_count = data[i]['view_count']
        view_count = f"{view_count:1,}"
        view_count = view_count.replace(",", " ")
        webpage_url_key = data[i]['webpage_url']
        output = str(output) + str("\ntitle:\t\t" + title \
                                   + "\nuploader:\t\t" + uploader \
                                   + "\nlike / dislike ratio:\t" + current_average + " %" \
                                   + "\nview_count:\t" + view_count+"\n")

    output = create_layout(output)
    return output


# create_window(sample_data.output_13_22_32)
create_window(sample_data.output_14_23_24_skrillex_tameimpala_hole)
# get_info_all_list(sample_data.nested_link_sample_data14_23_24_skrillex_tameimpala_hole)
