import re
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from flask import Flask, request, render_template

app = Flask(__name__)


def get_text(x):
    html = requests.get(x).content

    unicode_str = html.decode('utf8')
    encoded_str = unicode_str.encode('ascii', 'ignore')
    soup = bs(encoded_str, 'html.parser')

    element = soup.find_all('p')
    text_list = [re.sub(r'<.+?>', r'', str(p)) for p in element]

    text = '\n'.join(text_list)

    return text


@app.route('/')
def index():

    return render_template('index.html', text1='')


@app.route('/', methods=['POST'])
def get_art_text():

    url = request.form['flink']

    if url != '':
        art_text = get_text(url)
    else:
        art_text = ''

    return render_template('index.html', text1=art_text)


if __name__ == '__main__':

    app.run(debug=True)
