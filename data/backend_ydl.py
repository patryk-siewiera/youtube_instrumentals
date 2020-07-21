import youtube_dl
import validators

# TODO rename file to: search_links.py

# mock input data -> don't need to run gui to check
mock_gui_output_1 = {0: None, 10: 'skrillex', 11: 2, 12: '1: Without Separation : Whole track',
                     '-DEFAULT_FOLDER-': 'C:\\!\\git\\youtube_instrumentals\\!download', 'Browse': ''}

# TODO: default how_much == 1, just skip if query is empty
mock_gui_output_flume_skrillex_tameimpala_10 = {0: None, 10: 'flume', 11: 2, 12: '1: Without Separation : Whole track',
                                                20: 'skril!!lex', 21: '3',
                                                22: '1: Without Separation : Whole track', 30: 'tame impala ', 31: '4',
                                                32: '1: Without Separation : Whole track',
                                                40: 'https://www.youtube.com/watch?v=tsK0EG1vpSw', 41: 0,
                                                42: '1: Without Separation : Whole track',
                                                50: 'C:/Users/workp/Downloads/guitest/guitest.py', 51: 0,
                                                52: '1: Without Separation : Whole track', 60: 'The Dø', 61: 2,
                                                62: '1: Without Separation : Whole track', 70: '', 71: 0,
                                                72: '1: Without Separation : Whole track',
                                                80: '', 81: 0, 82: '1: Without Separation : Whole track', 90: '', 91: 0,
                                                92: '1: Without Separation : Whole track', 100: '', 101: 0,
                                                102: '1: Without Separation : Whole track',
                                                '-DEFAULT_FOLDER-': 'C:\\!\\git\\youtube_instrumentals\\!download',
                                                'Browse': ''}

mock_gui_output_banks_audioslave_sonlux_jamesblake = {0: None, 10: 'banks', 11: 10,
                                                      12: '1: Without Separation : Whole track',
                                                      20: 'audioslave', 21: '3',
                                                      22: '1: Without Separation : Whole track', 30: 'son lux', 31: '4',
                                                      32: '1: Without Separation : Whole track', 40: 'james blake',
                                                      41: 5,
                                                      42: '1: Without Separation : Whole track',
                                                      50: '', 51: 0, 52: '1: Without Separation : Whole track', 60: '',
                                                      61: 0,
                                                      62: '1: Without Separation : Whole track', 70: '', 71: 0,
                                                      72: '1: Without Separation : Whole track',
                                                      80: '', 81: 0, 82: '1: Without Separation : Whole track', 90: '',
                                                      91: 0,
                                                      92: '1: Without Separation : Whole track', 100: '', 101: 0,
                                                      102: '1: Without Separation : Whole track',
                                                      '-DEFAULT_FOLDER-': 'C:\\!\\git\\youtube_instrumentals\\!download',
                                                      'Browse': ''}

ydl_opts_wav = {
    # options for youtube_dl
    # simulate: true -> this will only gather information
    'format': 'bestaudio/best',
    'outtmpl': '!download/%(uploader)s/%(title)s.%(ext)s',
    'min_views': 10000,
    'max_views': 10000000000000,
    'max_length': 1000,
    'ignoreerrors': True,
    'simulate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '320',
    }],
}


def parse(gui_output):
    parsed_list = []
    iterations = int(len(gui_output) / 3)
    for k in range(iterations):
        k = k + 1
        id_name = k * 10 + 0
        id_how_much = k * 10 + 1
        id_method = k * 10 + 2

        # parse for every iteration (line), corresponding value
        name = gui_output[id_name]
        how_much = gui_output[id_how_much]
        method = gui_output[id_method]

        # print(name)

        if validators.url(name):
            print("Searching more details about URL...\t\t", name)
            youtube_dl_info_parser = youtube_dl.YoutubeDL(ydl_opts_wav).extract_info(name)
            uploader = youtube_dl_info_parser['uploader']
            parsed_list.append([uploader, name])

        # skip empty queries
        elif name == "" or name is None or how_much == 0:
            continue

        elif not validators.url(name):
            # remove chars that aren't letters or numbers
            alphanumeric = [character for character in name if (character.isalnum() or character.isspace())]
            name = "".join(alphanumeric)
            # query generator
            query = "ytsearch" + str(how_much) + ":" + str(name)
            output = [name, query]
            parsed_list.append(output)

    return parsed_list

global_artists_name = []

# print("\n\t\tOUTPUT:\t", parse(mock_gui_output_flume_skrillex_tameimpala_10))
