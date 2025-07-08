import re
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from flask import Flask, request, render_template

app = Flask(__name__)


def get_text(url: str, tag: str):
    html = requests.get(url).content

    unicode_str = html.decode('utf8')
    encoded_str = unicode_str.encode('ascii', 'ignore')
    soup = bs(encoded_str, 'html.parser')

    element = soup.find_all(tag)
    text_list = [re.sub(r'<.+?>', r'', str(p)) for p in element]

    text = '<br><br>'.join(text_list)

    return text


@app.route('/')
def index():

    return render_template('index.html', text1='')


@app.route('/', methods=['POST'])
def get_art_text():

    url = request.form['flink']

    if url != '':
        art_h1 = get_text(url=url, tag='h1')
        art_p = get_text(url=url, tag='p')
    else:
        art_h1 = 'Placeholder Heading....'
        art_p = 'Placeholder Text...'

    return render_template('index.html', text1=art_h1, text2=art_p)


if __name__ == '__main__':

    app.run(debug=True)
