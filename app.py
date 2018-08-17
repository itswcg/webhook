from flask import Flask
from flask import request
import os
import subprocess

app = Flask(__name__)


@app.route('/webhook/git', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data = request.get_json(force=True)
        project = data['repository']['name']
        dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), project)

        print('%s' % dir)

        res = subprocess.call('git add .', shell=True, cwd=dir)

        print(res)

        if res != 0:
            subprocess.call('git add .', shell=True, cwd=dir)

    return 'Hello, World'


if __name__ == '__main__':
    app.run(debug=True)
