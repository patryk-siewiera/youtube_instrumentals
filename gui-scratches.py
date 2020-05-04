import PySimpleGUI as sg

row1 = (40, 1)
row2 = (10, 1)
row3 = (50, 1)

how_much_combo = [0, 1, 2, 5, 10, 15, 20, 30, 50, 100]
stems_methods = ['1: Without Separation : Whole track',
                 '2: Stems: Vocal / Instrumental separation',
                 '4: Stems: Vocals / Drums / Bass / Other separation',
                 '5: Stems: Vocals / Drums / Bass / Piano / Other separation']

values = {10: '', 11: 0, 12: '1: Without Separation : Whole track'}

program_title = 'Youtube Instrumentals - v 0.1'
keep_on_top_bool = True
icon_path = "ico.ico"


# TODO now
def validation(value):
    # validation between pages
    print(len(value) // 3)
    for i in range(len(value) // 3):
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

    for j in range(len(value) // 3):
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


def gui_1line(value1):
    sg.theme('black')  # theme color
    layout_1line = [[sg.Text('Top line text', size=(10, 2))],
                    [sg.Text('Keywords or Link', size=(35, 1), key="11"), sg.Text('How much', size=(10, 1)),
                     sg.Text('Method 1/2/4/5')],
                    [sg.InputText(str(value1[10]), size=row1, key=10),
                     sg.Combo(how_much_combo,
                              default_value=value1[11], size=row2, key=11),
                     sg.Combo(stems_methods, size=row3, default_value=value1[12], key=12)],
                    [sg.Submit(button_text="  Download  "), sg.Cancel(button_text="   Close   "),
                     sg.Button(key="add5", button_text="  + 5 lanes  ")]]

    window = sg.Window(program_title, layout_1line, keep_on_top=keep_on_top_bool, icon=icon_path)
    event, value1 = window.read()
    window.close()

    value1 = validation(value1)

    if event == "add5":
        value1 = gui_5line(value1)

    if event == 'Cancel':
        print('if -> exit button')
        exit()

    print('\n_* def gui_1lane():  RETURN == ', value1, '\n')
    return value1


def gui_5line(values5):
    sg.theme('black')  # theme color
    layout_5lines = [[sg.Text('Top line text', size=(10, 2))],
                     [sg.Text('Keywords or Link', size=(35, 1), key="11"), sg.Text('How much', size=(10, 1)),
                      sg.Text('Method 1/2/4/5')],
                     [sg.InputText(str(values5[10]), size=row1, key=10),
                      sg.Combo(how_much_combo,
                               default_value=values5[11], size=row2, key=11),
                      sg.Combo(stems_methods, size=row3, default_value=values5[12], key=12)],
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
                     [sg.Submit(button_text="  Download  "), sg.Cancel(button_text="   Close   "),
                      sg.Button(key="add5", button_text=" + 5 lanes"),
                      sg.Button(key="remove5", button_text="  -  5 lanes  ")]]

    window5 = sg.Window(program_title, layout_5lines, keep_on_top=keep_on_top_bool, icon=icon_path)

    event, values5 = window5.read()
    window5.close()

    values5 = validation(values5)

    if event == "remove5":
        values5 = gui_1line(values5)

    if event == "add5":
        values5 = gui_10line(values5)

    if event == 'Cancel':
        print('if -> exit button')
        exit()

    print('\n_* def gui_5lane():  RETURN == ', values5, '\n')
    return values5


def gui_10line(values10):
    sg.theme('black')  # theme color
    layout_10lines = [[sg.Text('Top line text', size=(10, 2))],
                      [sg.Text('Keywords or Link', size=(35, 1), key="11"), sg.Text('How much', size=(10, 1)),
                       sg.Text('Method 1/2/4/5')],
                      [sg.InputText(str(values10[10]), size=row1, key=10),
                       sg.Combo(how_much_combo,
                                default_value=values10[11], size=row2, key=11),
                       sg.Combo(stems_methods, size=row3, default_value=values10[12], key=12)],
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
                                default_value=values10[11], size=row2, key=61),
                       sg.Combo(stems_methods, size=row3, default_value=values10[12], key=62)],
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
                       sg.Combo(stems_methods, size=row3, default_value=stems_methods[0], key=102)],

                      [sg.Submit(button_text="  Download  "), sg.Cancel(button_text="   Close   "),
                       sg.Button(key="remove5", button_text="  -  5 lanes  ")]]

    window10 = sg.Window(program_title, layout_10lines, keep_on_top=keep_on_top_bool, icon=icon_path)

    event, values10 = window10.read()
    window10.close()

    print('before validation:', values10)
    values10 = validation(values10)
    print('after:', values10)

    if event == "remove5":
        values10 = gui_5line(values10)

    if event == 'Cancel':
        print('if -> exit button')
        exit()

    print('\n_* def gui_10lane():  RETURN == ', values10, '\n')
    return values10


print(gui_1line(values))
# print(gui_5line(values))
# print(gui_10line(values))
#
