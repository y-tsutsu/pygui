import PySimpleGUI as sg


def main():
    sg.ChangeLookAndFeel('LightBlue')
    layout = [[sg.Text('サンプルアプリ')],
              [sg.Text('入力してください'), sg.InputText(default_text='Hello!', key='input')],
              [sg.Button('OK'), sg.Button('Cancel')]]
    window = sg.Window('サンプル', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'OK':
            sg.popup(f'input: {values["input"]}')

    window.close()


if __name__ == '__main__':
    main()
