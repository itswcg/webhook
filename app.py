from flask import Flask
from flask import request
import os

app = Flask(__name__)


@app.route('/webhook/git', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data = request.get_json(force=True)
        project = data['repository']['name']
        dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), project)

        print('%s' % dir)

        os.chdir(dir)
        os.system('git pull origin develop')
        os.system('git pull origin master')

        return 'Hello, World'


if __name__ == '__main__':
    app.run()
