import gui
import clean_my_project
import youtube_dl

mock_gui_output_1 = {0: None, 10: 'skrillex', 11: 2, 12: '1: Without Separation : Whole track',
                     '-DEFAULT_FOLDER-': 'C:\\!\\git\\youtube_instrumentals\\!download', 'Browse': ''}

mock_gui_output_10 = {0: None, 10: 'tame impala', 11: 2, 12: '1: Without Separation : Whole track', 20: 'skrillex',
                      21: 1, 22: '1: Without Separation : Whole track', 30: 'flume', 31: '3',
                      32: '1: Without Separation : Whole track', 40: 'bruno mars', 41: '4',
                      42: '1: Without Separation : Whole track', 50: '', 51: 0,
                      52: '1: Without Separation : Whole track', 60: '', 61: 0,
                      62: '1: Without Separation : Whole track', 70: '', 71: 0,
                      72: '1: Without Separation : Whole track', 80: '', 81: 0,
                      82: '1: Without Separation : Whole track', 90: '', 91: 0,
                      92: '1: Without Separation : Whole track', 100: '', 101: 0,
                      102: '1: Without Separation : Whole track',
                      '-DEFAULT_FOLDER-': 'C:\\!\\git\\youtube_instrumentals\\!download', 'Browse': ''}


def how_many_iterations(data):
    return int(len(data) / 3 - 1)


def ydl(gui_output):
    iterations = how_many_iterations(gui_output)

    ydl_opts_wav = {
        'format': 'bestaudio/best',
        'outtmpl': '!download/%(uploader)s/%(title)s.%(ext)s',
        'min_views': 10000,
        'max_views': 10000000000000,
        'max_length': 1000,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '320',
        }],
    }

    # remove cache
    youtube_dl.YoutubeDL(ydl_opts_wav).cache.remove()

    for i in range(iterations):
        i = i + 1
        id_name = i * 10 + 0
        id_how_much = i * 10 + 1
        id_method = i * 10 + 2

        name = gui_output[id_name]
        how_much = gui_output[id_how_much]
        method = gui_output[id_method]

        if name == "":
            break

        query = "ytsearch" + str(how_much) + ":" + name

        print(query)
        try:
            youtube_dl.YoutubeDL(ydl_opts_wav).extract_info(query)
        except:
            print('EXCEPT: youtube-dl unsupported keyword')

    # url = url_keyword[0]
    # keyword = url_keyword[1]

    # TODO: map out incoming data

    # print('\n_* def ydl(): INPUT url== ', url)
    # for i in range(len(url)):
    #     print('\ndownload: ', url[i])
    #     try:
    #         youtube_dl.YoutubeDL(ydl_opts_wav).download([url[i]])
    #     except:
    #         print('EXCEPT: youtube-dl unsupported URL')
