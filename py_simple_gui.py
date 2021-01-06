import PySimpleGUI as sg

# sg.preview_all_look_and_feel_themes()
layout = [
    [sg.Text("Enter text here"), sg.InputText(key='-IN-')],
    [sg.Text("Your ouput goes here", key='-OUT-', size=(30, 1))],
    [sg.OK(), sg.Exit()]
]

# ,[sg.Button("NAMASET !!!")]])#, no_titlebar=True)
window = sg.Window(title="HELLO APP", layout=layout, no_titlebar=True)

while True:
    event, values = window.read()
    print(values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    window['-OUT-'].update(values['-IN-'])
    window['-IN-'].update("")

window.close()
