import os
import requests

from flask import request
from flask import Flask
from flask import Response


app = Flask(__name__)


@app.route('/')
def home():
    usage = 'Pass a properly encoded url parameter e.g. /https/www.google.com'
    return usage

@app.route('/https/<url>')
def root(url):    
    url = 'https://' + url
    r = requests.get(url)
    rr = Response(response=r.content, status=r.status_code)
    rr.headers["Content-Type"] = r.headers['Content-Type']
    return rr

@app.route('/g/<keyword>')
def gkeyword(keyword):    
    url = 'https://www.google.com/search'
    payload = {'q':keyword, 'num':1, 'start':1, 'sourceid':'chrome', 'ie':'UTF-8', 'cr':'cr=countryUS'}
    r = requests.get(url, params=payload)
    rr = Response(response=r.content, status=r.status_code)
    rr.headers["Content-Type"] = r.headers['Content-Type']
    return rr

@app.route('/r/<subreddit>')
def gsubreddit(subreddit):
    url = 'https://subredditstats.com/r/' + subreddit
    r = requests.get(url)
    rr = Response(response=r.content, status=r.status_code)
    rr.headers["Content-Type"] = r.headers['Content-Type']
    return rr

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
