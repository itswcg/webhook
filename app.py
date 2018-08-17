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

        res = subprocess.call('git pull origin master', shell=True, cwd=dir)

        if res != 0:
            res = subprocess.call('git pull origin develop', shell=True, cwd=dir)

        return '%s' % res


if __name__ == '__main__':
    app.run()
