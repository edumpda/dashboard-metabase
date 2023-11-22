from flask import Flask, render_template
from dotenv import load_dotenv
import os
import jwt
import time

app = Flask(__name__)

load_dotenv()

METABASE_SITE_URL = os.getenv("METABASE_SITE_URL")
METABASE_SECRET_KEY = os.getenv("METABASE_SECRET_KEY")

@app.route('/')
def index():
    payload = {
        "resource": {"dashboard": 2},
        "params": {},
        "exp": round(time.time()) + (60 * 10)  # 10 minute expiration
    }
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

    iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token + "#bordered=true&titled=true"

    return render_template('index.html', iframeUrl=iframeUrl)

if __name__ == '__main__':
    app.run(debug=True)
