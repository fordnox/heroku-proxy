import os
import requests

from flask import request
from flask import Flask
from flask import Response


app = Flask(__name__)


@app.route('/')
def root():
    
    url = request.args.get('url', '')
    usage = 'Pass a properly encoded url parameter e.g. /?url=https://www.google.com'

    if url:
        r = requests.get(url)
        rr = Response(response=r.content, status=r.status_code)
        rr.headers["Content-Type"] = r.headers['Content-Type']
        return rr
    else:
        return usage

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
