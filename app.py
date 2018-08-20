from flask import Flask
from flask import request
import os, subprocess
from celery import Celery

app = Flask(__name__)

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def git_pull(cwd):
    subprocess.call('git pull origin develop', shell=True, cwd=cwd)
    subprocess.call('git pull origin master', shell=True, cwd=cwd)


@app.route('/webhook/git', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data = request.get_json(force=True)
        project = data['repository']['name']
        dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), project)
        git_pull.delay(dir)

        return 'Success'

    return 'Hello, World'


if __name__ == '__main__':
    app.run()
