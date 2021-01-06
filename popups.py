import PySimpleGUI as sg

layout = [
    [sg.Text('POPUPS TEST !!!')],
    [sg.Button('EXECUTE: popup_get_text("NAMASTE !!!")', key='-get_text-')],
    [sg.Button('EXECUTE: popup_get_file("NAMASTE !!!")', key='-get_file-')],
    [sg.Button('EXECUTE: popup_get_folder("NAMASTE !!!")', key='-get_folder-')],
    [sg.Button('EXECUTE: popup_get_date("NAMASTE !!!")', key='-get_date-')],
]

window = sg.Window("Popups Test", layout=layout, finalize=True)
window.maximize()

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == None:
        break
    elif event == '-get_text-':
        print(sg.popup_get_text("Enter Some Text"))
    elif event == '-get_file-':
        print(sg.popup_get_file("Enter Some file"))
    elif event == '-get_folder-':
        print(sg.popup_get_folder("Enter Some folder"))
    elif event == '-get_date-':
        print(sg.popup_get_date())

window.close()
