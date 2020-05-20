from youtube_dl import YoutubeDL
import pprint
import PySimpleGUI as sg

# import youtube_dl

"""
This is second page 
after pressing 
DOWNLOAD button
-> show what could be downloaded
and use checkboxes to tick if interested in downloading """

ydl_opts = {
    'ignoreerrors': True,
    'quiet': True
}

youtube_dl_opts = {}

video = "https://www.youtube.com/watch?v=MCRiUi28UpA"


def pretty_print_results(result):
    pp = pprint.PrettyPrinter(depth=2)
    pp.pprint(result)


def get_info(video):
    with YoutubeDL(youtube_dl_opts) as ydl:
        info_dict = ydl.extract_info(video, download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)
    return info_dict


pretty_print_results(get_info(video))
