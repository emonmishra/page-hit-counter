from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host= "localhost", port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This page has been seen {0} times' . format (redis.get( 'hits' ))

if __name__ == "__main__":
    app.run(host= "0.0.0.0", debug=True)