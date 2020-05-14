import os
from json import (load as jsonload, dump as jsondump)
import PySimpleGUI as sg

# current directory folder
cwd = "{0}\\!download".format(os.getcwd())

# size of each row
row1 = (40, 1)  # keywords
row2 = (10, 1)  # how much
row3 = (50, 1)  # method selection
output_row = (80, 1)  # folder output

# default values
how_much_combo = [0, 1, 2, 5, 10, 15, 20, 30, 50, 100]
stems_methods = ['1: Without Separation : Whole track',
                 '2: Stems: Vocal / Instrumental separation',
                 '4: Stems: Vocals / Drums / Bass / Other separation',
                 '5: Stems: Vocals / Drums / Bass / Piano / Other separation']
menu_layout = [['File', ['Settings', 'Exit']],
               ['Tools', ['Remove cache youtube-dl']],
               ["Help", ['Github Page', 'About']]]
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


# static parts of gui
def gui_menu():
    return [[sg.Menu(menu_layout)]]


def gui_info_row():
    return [[sg.Text('Keywords or Link', size=(35, 1), key="11"), sg.Text('How much', size=(10, 1)),
             sg.Text('Method 1/2/4/5')]]


def gui_output_folder():
    return [[sg.Text('')],
            [sg.Text('Output folder'), sg.InputText(default_text=cwd, size=output_row, key='cwd'),
             sg.FolderBrowse()],
            [sg.Text('')]]


def gui_change_settings():
    return [[sg.Button(key="Change Settings", button_text='Change Settings')]]


def gui_buttons():
    return [[sg.Button(key="add5", button_text="            + + +           ")]]


def gui_download():
    return [[sg.Submit(button_text="         Download        ")]]


def gui_theme_picker():
    return [[sg.Combo(theme_combo)]]


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
                                 'if_tunebat_using': 'IF_TUNEBAT_USING', 'geo-bypass': '-GEO-BYPASS-'}


##################### Load/Save Settings File #####################
def defaults_settings_def(settings_file, default_settings):
    settings = default_settings
    save_settings(settings_file, settings, None)
    return settings


def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        settings = defaults_settings_def(settings_file, default_settings)

    return settings


def save_settings(settings_file, settings, values):
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
    sg.theme(settings['theme'])

    def TextLabel(text):
        return sg.Text(text + ':', justification='r', size=(20, 1))

    inp_size = (15, 2)
    cmb_size = (13, 13)

    layout = [[sg.Text('Settings', font='Any 15')],
              [sg.CBox('Window Always On Top', key='-KEEP_ON_TOP_SETTING-')],
              [TextLabel('Theme'), sg.Combo(theme_combo, size=(13, 10), key='-THEME-')],
              [sg.Text()],
              [sg.Text('Tunebat Scraping Preferences', font='Any 15')],
              [sg.CBox('Use TuneBat to specify bpm and key', key='IF_TUNEBAT_USING')],
              [TextLabel('bpm'), sg.Combo(bpm_combo, key='-BPM-', size=cmb_size), TextLabel('bpm_range'),
               sg.Input(key='-BPM_RANGE-', size=inp_size)],
              [TextLabel('key'), sg.Combo(keys_combo, key='-KEY-', size=cmb_size),
               TextLabel('key_range - circle of fifth'),
               sg.Input(key='-KEY_RANGE-', size=inp_size)],
              [sg.Text()],
              [sg.Text('YouTube Download Preferences', font='Any 15')],
              [sg.CBox('geo-bypass', key='-GEO-BYPASS-', size=cmb_size)],
              [TextLabel('min_length'), sg.Input(key='-MIN_LENGTH-', size=inp_size), TextLabel('max_length'),
               sg.Input(key='-MAX_LENGTH-', size=inp_size)],
              [TextLabel('min_views'), sg.Input(key='-MIN_VIEWS-', size=inp_size), TextLabel('max_views'),
               sg.Input(key='-MAX_VIEWS-', size=inp_size)],
              [sg.Text()],
              [sg.Text('Spleeter Preferences (separation engine)', font='Any 15')],
              [sg.Button('Reset to Defaults')],
              [sg.Button('Save'), sg.Button('Exit')]]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  # update window with the values read from settings file
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window


def validation(value):
    # validation between pages
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


def change_settings(window, settings):
    event, values = create_settings_window(settings).read(close=True)
    if event == 'Save':
        window.close()
        window = None
        save_settings(SETTINGS_FILE, settings, values)
    if event == 'Reset to Defaults':
        print('Reset to Defaults')
        try:
            defaults_settings_def(SETTINGS_FILE, DEFAULT_SETTINGS)
        except:
            pass
        gui_1line(values_start, settings)
    if event in (None, 'Exit'):
        exit()


def gui_1line(value, settings):
    sg.theme(settings['theme'])
    gui_input_row_1 = [[sg.InputText(str(value[10]), size=row1, key=10),
                        sg.Combo(how_much_combo,
                                 default_value=value[11], size=row2, key=11),
                        sg.Combo(stems_methods, size=row3, default_value=value[12], key=12)]]
    # initialize specific part
    return sg.Window(title=program_title,
                     layout=(gui_menu() + gui_info_row() + gui_input_row_1 + gui_output_folder() + gui_buttons()
                             + gui_download() + gui_change_settings()),
                     keep_on_top=settings['keep_on_top_setting'],
                     icon=icon_path)


def gui_10line(value, settings):
    gui_input_row_10 = [[sg.InputText(str(value[10]), size=row1, key=10),
                         sg.Combo(how_much_combo,
                                  size=row2, key=11, default_value=value[11]),
                         sg.Combo(stems_methods, size=row3, key=12, default_value=value[12])],
                        [sg.InputText(size=row1, key=20),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=21),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=22)],
                        [sg.InputText(size=row1, key=30),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=31),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=32)],
                        [sg.InputText(size=row1, key=40),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=41),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=42)],
                        [sg.InputText(size=row1, key=50),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=51),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=52)],
                        [sg.InputText(size=row1, key=60),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=61),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=62)],
                        [sg.InputText(size=row1, key=70),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=71),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=72)],
                        [sg.InputText(size=row1, key=80),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=81),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=82)],
                        [sg.InputText(size=row1, key=90),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=91),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=92)],
                        [sg.InputText(size=row1, key=100),
                         sg.Combo(how_much_combo,
                                  default_value=how_much_combo[0], size=row2, key=101),
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=102)]]

    window10 = sg.Window(title=program_title,
                         layout=(
                                 gui_menu() + gui_info_row() + gui_input_row_10 + gui_output_folder() + gui_download() + gui_change_settings()),
                         keep_on_top=settings['keep_on_top_setting'],
                         icon=icon_path)

    event, value = window10.read()
    window10.close()

    value = validation(value)

    return value


def main():
    while True:  # Event Loop
        window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS)
        window = gui_1line(values_start, settings)

        event, value = window.read()
        window.close()

        if event == "add5":
            gui_10line(value)

        if event == 'Change Settings':
            change_settings(window, settings)

        if event in (None, 'Exit'):
            exit()


main()
