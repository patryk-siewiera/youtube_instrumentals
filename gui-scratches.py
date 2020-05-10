import PySimpleGUI as sg

# size of each row
row1 = (40, 1)  # keywords
row2 = (10, 1)  # how much
row3 = (50, 1)  # method selection
output_row = (70, 1)  # folder output

# default values
how_much_combo = [0, 1, 2, 5, 10, 15, 20, 30, 50, 100]
stems_methods = ['1: Without Separation : Whole track',
                 '2: Stems: Vocal / Instrumental separation',
                 '4: Stems: Vocals / Drums / Bass / Other separation',
                 '5: Stems: Vocals / Drums / Bass / Piano / Other separation']
menu_layout = [['File', ['Settings', 'Exit']],
               ['Tools', ['Remove cache youtube-dl']],
               ["Help", ['Github Page', 'About']]]

# settings
keep_on_top_bool = True
sg.theme('purple')  # theme color
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


def gui_output():
    return [[sg.Text('')], [sg.Text('Output folder'), sg.InputText(size=output_row)], [sg.Text('')]]


def gui_buttons():
    return [[sg.Button(key="add5", button_text="            + + +           ")]]


def gui_download():
    return [[sg.Submit(button_text="         Download        ")]]


# TODO now
def validation(value):
    # validation between pages
    print(len(value) // 3)
    for i in range((len(value) // 3) - 1):
        i = i + 1
        # iterator for second table
        current = value[1 + 10 * i]
        try:
            if current == None:
                current = 0
            else:
                current = int(current)
            print("validation: INT for: value", current, 'number: ', i)
        except:
            value[1 + 10 * i] = 0
            print("NOT validation: INT for: value", current, 'number: ', i, "type", type(current),
                  "validation: change to == 0")

    for j in range((len(value) // 3) - 1):
        j = j + 1
        # iterator for third table
        stem_method_iteration = value[2 + 10 * j]
        print(stem_method_iteration)
        if stem_method_iteration in stems_methods:
            print('STEM METHOD')
        else:
            value[2 + 10 * j] = stems_methods[0]
            print("NOT validation: INT for: value", value[2 + 10 * j], 'number: ', j, "type",
                  type(value[2 + 10 * j]), "stem_method_iteration changed to", stems_methods[0])
    return value


def gui_1line(value):
    # gui 1 window details

    gui_input_row_1 = [[sg.InputText(str(value[10]), size=row1, key=10),
                        sg.Combo(how_much_combo,
                                 default_value=value[11], size=row2, key=11),
                        sg.Combo(stems_methods, size=row3, default_value=value[12], key=12)]]

    # initialize specific part
    window1 = sg.Window(title=program_title,
                        layout=(
                                gui_menu() + gui_info_row() + gui_input_row_1 + gui_output() + gui_buttons() + gui_download()),
                        keep_on_top=keep_on_top_bool,
                        icon=icon_path)

    event, value = window1.read()
    window1.close()

    if event == "add5":
        value = gui_10line(value)

    return value


def gui_10line(value):
    gui_input_row_10 = [[sg.InputText(str(value[10]), size=row1, key=10),
                         sg.Combo(how_much_combo,
                                  size=row2, key=11),
                         sg.Combo(stems_methods, size=row3, key=12)],
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
                        [sg.InputText(size=row1, key=10),
                         sg.Combo(how_much_combo,
                                  size=row2, key=11),
                         sg.Combo(stems_methods, size=row3, key=12)],
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
                         sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=52)]]

    window10 = sg.Window(title=program_title,
                         layout=(gui_menu() + gui_info_row() + gui_input_row_10 + gui_output() + gui_download()),
                         keep_on_top=keep_on_top_bool,
                         icon=icon_path)

    event, value = window10.read()
    window10.close()

    value = validation(value)

    return value


print(gui_1line(values_start))
