import pathlib
import os
from datetime import datetime

import PySimpleGUI as sg
import youtube_dl

input_links = (['https://www.youtube.com/watch?v=mu32phZdlZo', 'https://www.youtube.com/watch?v=VofkCG33xFs'], "method")


def download(input_links):
    progress_bar_steps = len(input_links[0])

    # datetime object containing current date and time, to folder naming
    now = datetime.now()
    dt_string = now.strftime("%y_%m_%d__%H_%M_%S")

    layout = [[sg.ProgressBar(progress_bar_steps, orientation='h', size=(70, 20), key='progressbar')]]

    # create the window`
    window = sg.Window('Downloading selected files...', layout)
    progress_bar = window['progressbar']

    event, values = window.read(timeout=10)

    current_path = pathlib.Path().absolute()
    # path_one_level_up = pathlib.Path(current_path).parents[0]

    # ###### Downloader
    if input_links[1] == "download_mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': str(current_path) + "/!audio/" + dt_string + '/%(title)s.%(ext)s',
            'max_length': 1000,
            'ignoreerrors': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }

    elif input_links[1] == "download_wav":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': str(current_path) + "/!audio/" + dt_string + '/%(title)s.%(ext)s',
            'max_length': 1000,
            'ignoreerrors': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '320',
            }],
        }
    elif input_links[1] == "download_webm":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': str(current_path) + "/!audio/" + dt_string + '/%(title)s.%(ext)s',
            'max_length': 1000,
            'ignoreerrors': True,
        }

    for i in range(progress_bar_steps):
        youtube_dl.YoutubeDL(ydl_opts).download([str(input_links[0][i])])
        progress_bar.UpdateBar(i + 1)

    window.close()

    sg.popup("Files are downloaded in folder:\n",
             str(current_path) + "\ \n\ !audio \ " + dt_string + "\ \n\n\nProgram will exit end in 20s...",
             auto_close=True,
             auto_close_duration=20)

    print("\n\t\t Everything done, exit...")
    exit()
