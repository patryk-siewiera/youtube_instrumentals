import datetime
import pprint

import sample_data
import PySimpleGUI as sg
from youtube_dl import YoutubeDL

import backend_ydl

ydl_opts = {
    "ignoreerrors": True,
    'sleep_interval': 5,
    'geo-bypass': True,
    'quiet': False
}


def pretty_print_results(result):
    pp = pprint.PrettyPrinter(depth=2)
    output = pp.pformat(result)
    with open('output.txt', 'wt') as out:
        pp.pprint(output, stream=out)
    return output


def get_info(video):
    output = []
    for i in range(len(video)):
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video[i], download=False)
            try:
                output.append(info_dict)
            except:
                pass
    return output


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

    layout = layout = [
        [sg.TabGroup([[sg.Tab('Tab 1', tab1, tooltip='tip'), sg.Tab('Tab 2', layout_content)]], tooltip='TIP2')],
        [sg.Button('Read')]]

    # activate frame here in layout =
    window = sg.Window('Frame with buttons', layout=layout,
                       font=("Arial", 8))
    event, values = window.read()
    window.close()


title = ["title", "53544823658", 2, 3, 4, 5]

data = {
    "title": title[1],
    "inside_text": "inside_text xxx",
    "number_of_frames": 1,
}


def output_to_file(output):
    now = datetime.datetime.now()
    print(output, file=open("!output.txt", "a"))

    return output


# TODO:
# function save output searching to file -> for easier copying
# do 5 sample data links -> from 1 to 10
# do 5 sample already parsed information

# backend_ydl.remove_ydl_cache()
create_window((get_info(sample_data.link_sample_data4)))
