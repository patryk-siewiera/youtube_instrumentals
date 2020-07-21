import os
import webbrowser
from json import (load as jsonload, dump as jsondump)

import PySimpleGUI as sg

# current directory folder
cwd = "{0}\\!download".format(os.getcwd())

# size of each row
row1 = (50, 1)  # keywords
row2 = (10, 1)  # how much
row3 = (50, 1)  # method selection
output_row = (80, 1)  # folder output

# button colors
button_yes = ('White', 'Green')
button_no = ('White', 'Red')

# default values
how_much_combo = [0, 1, 2, 5, 10, 15, 20, 30, 50, 100]
stems_methods = ['1: Without Separation : Whole track',
                 '2: Stems: Vocal / Instrumental separation',
                 '4: Stems: Vocals / Drums / Bass / Other separation',
                 '5: Stems: Vocals / Drums / Bass / Piano / Other separation']

menu_layout = [["Help", ['GitHub Page', 'About']]]
bpm_combo = [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250,
             260, 270, 280, 290, 300, 310]

keys_combo = ['C / a',
              'G / e',
              'D / b',
              'A / f#',
              'E / c#',
              '(B/C#) / g#',
              '(Gb/F#) / (eb / d#)',
              '(Db/C#) / bb',
              'Ab / f',
              'Eb / c',
              'Bb / g',
              'F / d']

theme_combo = [
    'LightGrey3',
    'BrownBlue',
    'DarkGrey4',
    'Black']

# settings
program_title = 'Youtube Instrumentals - v 0.1'
icon_path = ""

# for testing
values_start = {
    10: '', 11: 0, 12: '1: Without Separation : Whole track',
}

SETTINGS_FILE = os.path.join(os.path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'theme': sg.theme(),
                    'keep_on_top_setting': False, 'min_length': 10, 'max_length': 1000,
                    'min_views': 1, 'max_views': 10000000000, 'key': keys_combo[0], 'key_range': 12,
                    'bpm': bpm_combo[8], 'bpm_range': 150, 'if_tunebat_using': False, 'geo-bypass': False}

# "Map" from the settings dictionary keys to the window's element keys
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'theme': '-THEME-',
                                 'keep_on_top_setting': '-KEEP_ON_TOP_SETTING-',
                                 'min_length': '-MIN_LENGTH-', 'max_length': '-MAX_LENGTH-',
                                 'min_views': '-MIN_VIEWS-', 'max_views': '-MAX_VIEWS-',
                                 'key': '-KEY-', 'key_range': '-KEY_RANGE-',
                                 'bpm': '-BPM-', 'bpm_range': '-BPM_RANGE-',
                                 'if_tunebat_using': '-IF_TUNEBAT_USING-', 'geo-bypass': '-GEO-BYPASS-', }


def gui_help(event_list):
    """open website (django)"""
    sg.popup("""
    --- THIS WILL OPEN HELP PAGE ---
    """)
    return event_list[:-1]


def gui_about(event_list):
    """open popup: about information and libraries"""
    sg.popup("""

PLEASE USE THIS ONLY WITH NOT  COPYRIGHTED 
MATERIAL ONLY EDUCATIONAL USE

Used Python Packages:
- PySimpleGui
- YouTubeDL
- Spleeter (Deezer)

""", title="About", keep_on_top=True)
    return event_list[:-1]


def gui_github_page(event_list):
    """open webpage github with project"""
    url_git = 'https://github.com/patryk-siewiera/youtube_instrumentals'
    sg.popup_timed("\nOpening webpage: \n\n" + url_git + "\n", auto_close_duration=2, title="info")
    webbrowser.open_new_tab(url=url_git)
    return event_list[:-1]


# static parts of gui
def gui_menu():
    """create top menu: file / about"""
    return [[sg.Menu(menu_layout)]]


def gui_info_row():
    """add information about every row """
    return [[sg.Text('Keywords, Link or Playlist YouTube', size=(44, 1), key="11"), sg.Text('How much', size=(10, 1))]]


def gui_output_folder():
    """gui part: default folder"""
    return [[sg.Text('')],
            [sg.Text('Output folder'), sg.InputText(default_text=cwd, size=output_row, key='-DEFAULT_FOLDER-'),
             sg.FolderBrowse()],
            [sg.Text('')]]


def gui_empty_lines():
    """ add 2 empty lines to gui"""
    return [[sg.Text('')]]


def gui_oneline():
    """go back to gui 1 line download"""
    return [[sg.Button(key="one_line", button_text="             - - -             "),
             sg.Button(key="Change Settings", button_text='  Change Settings  ')]]


def gui_add10():
    """gui buttons function"""
    return [[sg.Button(key="add10", button_text="            + + +           "),
             sg.Button(key="Change Settings", button_text='  Change Settings  ')]]


def gui_download_exit():
    """gui button download: returns all data to youtube-dl module
    #TODO: youtube-dl module """
    return [[sg.Submit(button_text="         Download        ", button_color=button_yes, key="Download"),
             sg.Button('           Exit           ', key='Exit', button_color=button_no)]]


def gui_theme_picker():
    """gui settings part theme picker"""
    return [[sg.Combo(theme_combo)]]


def current_data(data, default_data):
    """keep data during change of pages in gui"""
    pass


##################### Load/Save Settings File #####################
def load_settings(settings_file, default_settings):
    """try to load existing settings if not, create new file from defaults"""
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        settings = defaults_settings_def(settings_file, default_settings)
    return settings


def defaults_settings_def(settings_file, default_settings):
    """load defaults settings"""
    settings = default_settings.copy()
    save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    """"try to save values as settings_file.cfg (json)"""
    if values:  # if there are stuff specified by another window, fill in those values
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  # update window with the values read from settings file
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f, indent=4, sort_keys=True)


##################### Make a settings window #####################
def create_settings_window(settings):
    """gui for SETTINGS WINDOW create"""
    sg.theme(settings['theme'])

    def TextLabel(text):
        """to simplify variable layout, use this function for text label"""
        return sg.Text(text + ':', justification='r', size=(20, 1))

    inp_size = (15, 2)
    cmb_size = (13, 13)

    layout = [[sg.Text('Settings', font='Any 15')],
              [sg.CBox('Window Always On Top', key='-KEEP_ON_TOP_SETTING-')],
              [TextLabel('Theme'), sg.Combo(values=theme_combo, size=(13, 10), key='-THEME-')],
              [sg.Text()],
              [sg.Text('YouTube Download Preferences', font='Any 15')],
              [sg.CBox('geo-bypass', key='-GEO-BYPASS-', size=cmb_size)],
              [TextLabel('min_length'), sg.Input(key='-MIN_LENGTH-', size=inp_size), TextLabel('max_length'),
               sg.Input(key='-MAX_LENGTH-', size=inp_size)],
              [TextLabel('min_views'), sg.Input(key='-MIN_VIEWS-', size=inp_size), TextLabel('max_views'),
               sg.Input(key='-MAX_VIEWS-', size=inp_size)],
              [TextLabel("naming wildcards TODO")],
              [sg.Text()],
              [sg.Text('Tunebat Scraping Preferences', font='Any 15')],
              [sg.CBox('Use TuneBat to specify bpm and key', key='-IF_TUNEBAT_USING-')],
              [TextLabel('bpm'), sg.Combo(bpm_combo, key='-BPM-', size=cmb_size), TextLabel('bpm_range'),
               sg.Input(key='-BPM_RANGE-', size=inp_size)],
              [TextLabel('key'), sg.Combo(keys_combo, key='-KEY-', size=cmb_size),
               TextLabel('key_range - circle of fifth'),
               sg.Input(key='-KEY_RANGE-', size=inp_size)],
              [sg.Text()],
              [sg.Text('Spleeter Preferences (separation engine)', font='Any 15')],
              [sg.Button('  Reset to Defaults  ', key='Reset to Defaults')],
              [sg.Button('   Save   ', key='Save', button_color=button_yes),
               sg.Button('   Exit   ', key='Exit', button_color=button_no)]]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    # TODO: rewrite -THEME- map

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  # update window with the values read from settings file
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window


def validation(value):
    """validate input values for youtube-dl, and between pages"""
    for i in range((len(value) // 3) - 1):
        i = i + 1
        # iterator for second table
        current = value[1 + 10 * i]
        try:
            if current == None:
                current = 0
            else:
                current = int(current)
        except:
            value[1 + 10 * i] = 0

    for j in range((len(value) // 3) - 1):
        j = j + 1
        # iterator for third table
        stem_method_iteration = value[2 + 10 * j]
        if stem_method_iteration in stems_methods:
            pass
        else:
            value[2 + 10 * j] = stems_methods[0]
    return value


def change_settings(window, settings, event):
    """backend:  for settings menu"""
    current_event, values = create_settings_window(settings).read(close=True)
    if current_event == 'Save':
        window = None
        save_settings(SETTINGS_FILE, settings, values)
        return event[:-1], settings
    if current_event == 'Reset to Defaults':
        try:
            settings = defaults_settings_def(SETTINGS_FILE, DEFAULT_SETTINGS)
        except:
            pass
        return event[:-1], settings
    if current_event in (None, 'Exit'):
        return event[:-1], settings


def gui_1line(value, settings, event_list):
    """initial menu, for one line downloader"""
    sg.theme(settings['theme'])
    gui_input_row_1 = [[sg.InputText(str(value[10]), size=row1, key=10),
                        sg.Combo(how_much_combo,
                                 default_value=1, size=row2, key=11),
                        sg.Combo(stems_methods, size=row3, default_value=value[12], key=12, visible=False)]]

    # initialize specific part
    window1 = sg.Window(title=program_title,
                        layout=(
                                gui_menu() + gui_info_row() + gui_input_row_1 + gui_empty_lines() + gui_add10() +
                                gui_download_exit()),
                        keep_on_top=settings['keep_on_top_setting'],
                        icon=icon_path)

    event, value = window1.read()
    window1.close()
    event_list.append(event)

    value = validation(value)

    return value, settings, event_list


def gui_10line(value, settings, event_list):
    """menu for 10 rows downloading"""
    gui_input_row_10 = [[sg.InputText(str(value[10]), size=row1, key=10),
                         sg.Combo(how_much_combo,
                                  size=row2, key=11, default_value=value[11]),
                         sg.Combo(stems_methods, size=row3, key=12, default_value=value[12], visible=False)],
                        [sg.InputText(size=row1, key=20),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=21),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=22, visible=False)],
                        [sg.InputText(size=row1, key=30),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=31),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=32, visible=False)],
                        [sg.InputText(size=row1, key=40),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=41),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=42, visible=False)],
                        [sg.InputText(size=row1, key=50),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=51),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=52, visible=False)],
                        [sg.InputText(size=row1, key=60),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=61),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=62, visible=False)],
                        [sg.InputText(size=row1, key=70),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=71),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=72, visible=False)],
                        [sg.InputText(size=row1, key=80),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=81),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=82, visible=False)],
                        [sg.InputText(size=row1, key=90),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=91),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=92, visible=False)],
                        [sg.InputText(size=row1, key=100),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=101),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=102, visible=False)]]

    window10 = sg.Window(title=program_title,
                         layout=(
                                 gui_menu() + gui_info_row() + gui_input_row_10 + gui_empty_lines() + gui_oneline() +
                                 gui_download_exit()),
                         keep_on_top=settings['keep_on_top_setting'],
                         icon=icon_path)

    event, value = window10.read()
    window10.close()
    event_list.append(event)

    value = validation(value)

    return value, settings, event_list


def main():
    event = [None, 'one_line']
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS)
    value, settings, event = gui_1line(values_start, settings, event)
    while True:  # Event Loop

        if event[-1] == "add10":
            value, settings, event = gui_10line(value, settings, event)

        if event[-1] == "one_line":
            value, settings, event = gui_1line(value, settings, event)

        if event[-1] == 'Change Settings':
            event, settings = change_settings(window, settings, event)

        if event[-1] == "About":
            event = gui_about(event)

        if event[-1] == "GitHub Page":
            event = gui_github_page(event)

        if event[-1] == "Help":
            event = gui_help(event)

        if event[-1] in (None, 'Exit'):
            exit()

        if event[-1] == "Download":
            return value
