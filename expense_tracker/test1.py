import PySimpleGUI as sg
import requests
_base_url = 'http://104.236.44.234/'
create_url = _base_url+'expenses/create/'
list_url = _base_url+'expenses/'
unique_url = _base_url+'expenses/'

# sg.preview_all_look_and_feel_themes()
layout = [
    [sg.Text("Spent On"), sg.Input(key='-SPENT-')],
    [sg.Text("Amount"), sg.Input(key='-AMOUNT-')],
    [sg.Text("Message", key='-OUT-', size=(30, 20))],
    [sg.Button(button_text='Add'),sg.Button(button_text='View All'), sg.Exit()]
]

# ,[sg.Button("NAMASET !!!")]])#, no_titlebar=True)
window = sg.Window(title="HELLO APP", layout=layout, no_titlebar=True)

while True:
    event, values = window.read()
    print(values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Add':
        data = {'text':values['-SPENT-'], 'amount':int(values['-AMOUNT-'])}
        response = requests.post(data=data, url=create_url)
        window['-OUT-'].update(f'status={response.status_code}')
    if event == 'View All':
        response = requests.get(url=list_url)
        output_text = ''
        if response.status_code != 200:
            output_text = 'ERROR OCCURRED'
        else:
            output_text = '\n'.join([f'{res["text"]}\t{res["amount"]}' for res in response.json()])
        window['-OUT-'].update(output_text)
window.close()
