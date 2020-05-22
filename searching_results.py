import pprint

import PySimpleGUI as sg
from youtube_dl import YoutubeDL

import sample_data

ydl_opts = {
    'ignoreerrors': True,
    'quiet': False
}


def pretty_print_results(result):
    pp = pprint.PrettyPrinter(depth=2)
    return pp.pformat(result)


def get_info(video):
    output = []
    for i in range(len(video)):
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video[i], download=False)
            output.append(info_dict)
    return output


# pretty_print_results(get_info(video))
def frame(title, inside_text):
    output = []

    def one_frame(title, inside_text):
        return [sg.Frame(title=title, layout=[[sg.Text(inside_text)]])]

    for i in range(len(title)):
        output.append(one_frame(title[i], inside_text[i]))
    # print(title)
    print("\n\n\n\n\n", inside_text)
    return output


def create_window(data_input):
    output = []
    # add tags
    title = []
    inside_text = []
    for j in range(len(data_input)):
        data = (data_input[j])
        title.append(data["artist"])
        current_average = float(data["average_rating"]) / 5 * 100
        inside_text.append("\ntitle:\t\t" + data["title"] \
                           + "\nuploader_id:\t" + str(data["uploader_id"]) \
                           + "\naverage rating:\t" + str("{:.2f}").format(current_average) + " %" \
                           + "\nview_count:\t" + str(data["view_count"]) \
                           + "\n")

    # activate frame here in layout =
    window = sg.Window('Frame with buttons', layout=([[sg.Frame(layout=frame(title, inside_text), title="frame out")]]),
                       font=("Helvetica", 12))
    event, values = window.read()
    window.close()


title = ["title", "53544823658", 2, 3, 4, 5]

data = {
    "title": title[1],
    "inside_text": "inside_text xxx",
    "number_of_frames": 1,
}

print(sample_data.searching_sample_values1)
