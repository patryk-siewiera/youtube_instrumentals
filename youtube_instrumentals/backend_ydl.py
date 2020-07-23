import youtube_dl
import validators

ydl_opts_wav = {
    # options for youtube_dl
    # simulate: true -> this will only gather information
    'min_views': 10000,
    'max_views': 10000000000000,
    'ignoreerrors': True,
    'simulate': True,
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
