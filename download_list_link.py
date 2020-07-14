import youtube_dl
from datetime import datetime
import PySimpleGUI as sg
import pathlib

input_links = ['https://www.youtube.com/watch?v=mu32phZdlZo', 'https://www.youtube.com/watch?v=VofkCG33xFs']


def download(input_links):
    progress_bar_steps = len(input_links)

    # datetime object containing current date and time, to folder naming
    now = datetime.now()
    dt_string = now.strftime("%y_%m_%d__%H_%M_%S")

    layout = [[sg.ProgressBar(progress_bar_steps, orientation='h', size=(70, 20), key='progressbar')]]

    # create the window`
    window = sg.Window('Downloading selected files...', layout)
    progress_bar = window['progressbar']

    event, values = window.read(timeout=10)

    # ###### Downloader
    ydl_opts_wav = {
        'format': 'bestaudio/best',
        'outtmpl': '!audio/' + dt_string + '/%(uploader)s/%(title)s.%(ext)s',
        'max_length': 1000,
        'ignoreerrors': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '320',
        }],
    }

    for i in range(progress_bar_steps):
        print(str(input_links[i]))
        youtube_dl.YoutubeDL(ydl_opts_wav).download([str(input_links[i])])
        progress_bar.UpdateBar(i + 1)

    window.close()

    current_path = pathlib.Path().absolute()

    sg.popup("Files are downloaded in folder:\n", str(current_path) + "\!download\n\n\nProgram will exit end in 10s...",
             auto_close=True,
             auto_close_duration=10)

# download(input_links)
