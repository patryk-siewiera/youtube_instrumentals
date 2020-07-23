import youtube_dl
import validators

# playlistend -> to get name of creator of playlist - you need only to parse first element
YDL_SIMULATE_OPTS = {
    # options for youtube_dl
    # simulate: true -> this will only gather information
    'min_views': 10000,
    'max_views': 10000000000000,
    'ignoreerrors': True,
    'simulate': True,
    'playlistend': 1
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

        # skip empty queries
        if name == "" or name is None or how_much == 0:
            continue
        elif validators.url(name):
            print("Searching more details about URL...\t\t", name)
            youtube_dl_info_parser = youtube_dl.YoutubeDL(YDL_SIMULATE_OPTS).extract_info(name)
            uploader = youtube_dl_info_parser['uploader']
            parsed_list.append([uploader, name])
        elif not validators.url(name):
            # remove chars that aren't letters or numbers
            alphanumeric = [character for character in name if (character.isalnum() or character.isspace())]
            name = "".join(alphanumeric)
            # query generator
            query = f'ytsearch{how_much}:{name}'
            output = [name, query]
            parsed_list.append(output)

    return parsed_list
