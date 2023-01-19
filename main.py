import re
import requests
import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs


def get_text(x):
    html = requests.get(x).content

    unicode_str = html.decode('utf8')
    encoded_str = unicode_str.encode('ascii', 'ignore')
    soup = bs(encoded_str, 'html.parser')

    element = soup.find_all('p')
    text_list = [re.sub(r'<.+?>', r'', str(p)) for p in element]

    text = ''
    for line in text_list:
        text += '{}'.format(line, '\n')

    return text


if __name__ == '__main__':
    sg.theme('DarkGrey2')
    layout = [[sg.Button('Enter URL!'), sg.Button('Get Text!'), sg.Cancel()],
              [sg.Output(size=(120, 60), key='_LOADEDURL_')]]

    window = sg.Window('Get URL Text!', layout, finalize=True)
    window.Maximize()

    while True:
        event, values = window.Read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event == 'Enter URL!':
            urltext = sg.popup_get_text('Enter URL Here...', '...')
            sg.popup('Loaded URL:', urltext)
        if event == 'Get Text!':
            try:
                text = get_text(urltext)
                window.Element('_LOADEDURL_').Update(text)
            except:
                sg.popup('Insert URL First!')
