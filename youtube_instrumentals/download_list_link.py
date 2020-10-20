import pathlib
import os
from datetime import datetime
from itertools import product

import PySimpleGUI as sg
import youtube_dl

# from spleeter.separator import Separator

input_links = (
    ['https://www.youtube.com/watch?v=mu32phZdlZo', 'https://www.youtube.com/watch?v=VofkCG33xFs'], "stem2")

input_links2 = (
    ['https://www.youtube.com/watch?v=VofkCG33xFs'], "stem2")

# max size of playlist
PLAYLIST_END_LIMIT = 99

# datetime object containing current date and time, to folder naming
NOW = datetime.now()
DT_STRING = NOW.strftime("%y_%m_%d__%H_%M_%S")
CURRENT_PATH = pathlib.Path().absolute()
NAME_DOWNLOAD_WILDCARD = "%(title)s.%(ext)s"
AUDIO_FOLDER_QUERY = CURRENT_PATH.joinpath("!audio", DT_STRING, NAME_DOWNLOAD_WILDCARD)
AUDIO_FOLDER = CURRENT_PATH.joinpath("!audio", DT_STRING)
AUDIO_FOLDER_SPLEETER = CURRENT_PATH.joinpath("!audio", DT_STRING, "separated")


def selector(input_links):
    if input_links[1] == "download_mp3" or input_links[1] == "download_wav" or input_links[1] == "download_webm":
        return download_only(input_links)
    elif input_links[1] == "stem2" or input_links[1] == "stem4" or input_links[1] == "stem5":
        return spleeter_module(input_links)


def spleeter_module(input_links):
    # remove this duplicate of code
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(AUDIO_FOLDER_QUERY),
        'max_length': 1000,
        'ignoreerrors': True,
        'playlistend': PLAYLIST_END_LIMIT,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '320',
        }],
    }
    progress_bar_steps = (len(input_links[0]))
    for i in range(progress_bar_steps):
        print("\n\tStep:\t", i + 1, "/", progress_bar_steps)
        youtube_dl.YoutubeDL(ydl_opts).download([str(input_links[0][i])])

    # list all files from that folder

    # push them into spleeter
    all_downloaded_files = (os.listdir(AUDIO_FOLDER))

    link_list = []
    for link in all_downloaded_files:
        # path_for_current_file = AUDIO_FOLDER.joinpath(link)
        path_for_current_file = os.path.join(AUDIO_FOLDER, link)
        link_list.append(path_for_current_file)

    print("\n\tList downloaded Files:\n", all_downloaded_files)
    print("\n\n", link_list)
    print(link_list)
    seapration(link_list)


mock_list = [
    'C:/!/git/youtube_instrumentals/youtube_instrumentals/!audio/20_07_25__17_33_13/king tubby - jah jah dub.wav',
    'C:/!/git/youtube_instrumentals/youtube_instrumentals/!audio/20_07_25__17_33_13/King Tubby - Sensation Version.wav']


def seapration(link_list):
    print(link_list)
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(
        audio_descriptor="C:/!/git/youtube_instrumentals/youtube_instrumentals/!audio/20_07_25__21_07_42/king tubby - jah jah dub.wav",
        destination="C:/!/git/youtube_instrumentals/youtube_instrumentals/!audio/separated",
        synchronous=True)
    exit()


# spleeter_2stems(mock_list)


def download_only(input_links):
    print("\n\tStart downloading...")
    progress_bar_steps = len(input_links[0])

    layout = [[sg.ProgressBar(progress_bar_steps, orientation='h', size=(70, 20), key='progressbar')]]

    # create the window`
    window = sg.Window('Downloading selected files...', layout)
    progress_bar = window['progressbar']

    event, values = window.read(timeout=10)

    # ###### Downloader
    if input_links[1] == "download_mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': str(AUDIO_FOLDER_QUERY),
            'max_length': 1000,
            'ignoreerrors': True,
            'playlistend': PLAYLIST_END_LIMIT,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }

    elif input_links[1] == "download_wav":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': str(AUDIO_FOLDER_QUERY),
            'max_length': 1000,
            'ignoreerrors': True,
            'playlistend': PLAYLIST_END_LIMIT,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '320',
            }],
        }
    elif input_links[1] == "download_webm":
        ydl_opts = {
            'format': 'bestaudio/best',
            'playlistend': PLAYLIST_END_LIMIT,
            'outtmpl': str(AUDIO_FOLDER_QUERY),
            'max_length': 1000,
            'ignoreerrors': True,
        }

    for i in range(progress_bar_steps):
        youtube_dl.YoutubeDL(ydl_opts).download([str(input_links[0][i])])
        progress_bar.UpdateBar(i + 1)

    window.close()
    print("\tDownloading Finished...\n")
    sg.popup("Files are downloaded in folder:\n",
             str(CURRENT_PATH.joinpath("!audio", DT_STRING)) + "\ \n\n\nProgram will exit end in 20s...",
             auto_close=True,
             auto_close_duration=20)

    print("\n\t\t Everything done, exit...")
    exit()

# selector(input_links2)
