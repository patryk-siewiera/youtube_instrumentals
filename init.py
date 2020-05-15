from __future__ import unicode_literals
import youtube_dl
import validators
import PySimpleGUI as sg


# just proof if this even works

def gui():
    sg.theme('dark')  # theme color

    layout = [[sg.Text('Top line text')],
              [sg.InputText(), sg.Text('url'), ],
              [sg.InputText(), sg.Text('url2')],
              [sg.InputText(), sg.Text('keyword')],
              [sg.InputText(), sg.Text('keyword2')],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Window Title', layout, keep_on_top=True, icon="ico.ico")
    # TODO: keep on top flag

    # values -> text from text boxes -> dictionary
    # event -> what button was clicked
    event, values = window.read()
    window.close()

    if event == 'Cancel':
        print('if -> exit')
        exit()

    print('\n_* def gui():  RETURN == ', values, '\n')
    return values


def gui_second():
    layout2 = [[sg.Text('Second Window')],
               [sg.Ok()]]
    window2 = sg.Window('Answer', layout2)
    event2, values2 = window2.read()
    window2.close()


def validate(url):
    print('\n_* def validate():  INPUT == ', url, '\n')
    output = []
    url_list = []
    key_word_list = []

    for i in range(len(url)):
        if url[i] == '':
            continue
        check = validators.url(url[i])
        if not check:
            print('  --- wrong URL (False) --- ', url[i])
            output.append(False)
            key_word_list.append(url[i])
        if check:
            print('  +++ correct URL (True) +++ ', url[i])
            output.append(True)
            url_list.append(url[i])

    # return list of True / False
    end = [url_list, key_word_list]
    print('\n_* def validate():  RETURN == ', end, '\n')
    return end


def ydl(url_keyword):
    url = url_keyword[0]
    keyword = url_keyword[1]

    ydl_opts_wav = {
        'format': 'bestaudio/best',
        'outtmpl': '!download/%(uploader)s/%(title)s.%(ext)s',
        'min_views': 10000,
        'max_views': 10000000000000,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '320',
        }],
    }

    print('\n_* def ydl(): INPUT url== ', url)
    for i in range(len(url)):
        print('\ndownload: ', url[i])
        try:
            youtube_dl.YoutubeDL(ydl_opts_wav).download([url[i]])
        except:
            print('EXCEPT: youtube-dl unsupported URL')

    print('\n_* def ydl(): INPUT keywords== ', keyword)
    for i in range(len(keyword)):
        print('\ndownload: ', keyword[i])
        try:
            youtube_dl.YoutubeDL(ydl_opts_wav).extract_info("ytsearch:" + keyword[i])
        except:
            print('EXCEPT: youtube-dl unsupported keyword')

    # TODO: progress hooks

    # TODO: download links


mock_psg = {0: 'sdf][4]3212\[]\[',
            1: 'https://youtu.be/DfZPeUujmIk',
            2: 'https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_All_Widgets.py',
            3: 'tame impala',
            4: 'skrillex'}

input_values = gui()
links = validate(input_values)
ydl(links)
