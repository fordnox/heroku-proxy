# Heroku Proxy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/fordnox/heroku-proxy/tree/master)

A free HTTP proxy that runs on Heroku.

## How to Use

To use this project, follow these steps:

1. Clone this project
2. `heroku create`
3. `heroku config:set PORT=80`
4. `git push heroku master`

Then visit {{your_heroku_url}}/https/wikipedia.com

## Development

    python3 -m venv hp-venv
    source hp-venv/bin/activate
    pip3 install -r requirements.txt
    python3 app.py
