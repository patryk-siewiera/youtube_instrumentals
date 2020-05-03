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


def gui_1line(value1):
    sg.theme('black')  # theme color
    layout_1line = [[sg.Text('Top line text', size=(10, 2))],
                    [sg.Text('Keywords or Link', size=(35, 1), key="11"), sg.Text('How much', size=(10, 1)),
                     sg.Text('Method 1/2/4/5')],
                    [sg.InputText(str(value1[10]), size=row1, key=10),
                     sg.Combo(how_much_combo,
                              default_value=value1[11], size=row2, key=11),
                     sg.Combo(stems_methods, size=row3, default_value=value1[12], key=12)],
                    [sg.Submit(), sg.Cancel(), sg.Button(key="add5", button_text="+ 5 lanes")]]

    window = sg.Window(program_title, layout_1line, keep_on_top=keep_on_top_bool, icon=icon_path)
    event, value1 = window.read()
    window.close()

    if event == "add5":
        gui_5line(value1)

    if event == 'Cancel':
        print('if -> exit')
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
                     [sg.Submit(), sg.Cancel(), sg.Button(key="remove5", button_text="- 5 lanes")]]

    window5 = sg.Window(program_title, layout_5lines, keep_on_top=keep_on_top_bool, icon=icon_path)

    event, values5 = window5.read()
    window5.close()

    if event == "remove5":
        gui_1line(values5)

    if event == 'Cancel':
        print('if -> exit')
        exit()

    print('\n_* def gui_5lane():  RETURN == ', values5, '\n')
    return values5


# print(gui_1line(values))
print(gui_5line(values))
