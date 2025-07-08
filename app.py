import re
import random
import random
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from flask import Flask, request, render_template

app = Flask(__name__)


def get_text(url: str, tag: str):

    user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
    ]

    headers = {
        'User-Agent': random.choice(user_agents) 
    }

    html = requests.get(url=url, headers=headers).content

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

    if url == '':
        art_h1 = 'Placeholder Header...'
        art_p = 'Placeholder Text...'
    else:
        art_h1 = = get_text(url=url, tag='h1'
        art_p = = get_text(url=url, tag='p'

    return render_template('index.html', text1=art_h1, text2=art_p)


if __name__ == '__main__':

    app.run(debug=True)
