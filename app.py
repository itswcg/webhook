from flask import Flask
from flask import request
import os

app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data = request.json
        project = data['repository']['name']
        dir = os.path.abspath(project)
        return '%s' % dir


if __name__ == '__main__':
    app.run()
