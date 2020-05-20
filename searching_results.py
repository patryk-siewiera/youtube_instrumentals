import PySimpleGUI as sg
import pprint

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

from youtube_dl import YoutubeDL

video = "https://www.youtube.com/watch?v=MCRiUi28UpA"
with YoutubeDL(youtube_dl_opts) as ydl:
    info_dict = ydl.extract_info(video, download=False)
    video_url = info_dict.get("url", None)
    video_id = info_dict.get("id", None)
    video_title = info_dict.get('title', None)

pp = pprint.PrettyPrinter(depth=2)
pp.pprint(info_dict)
