from flask import Flask
from flask import request
import os, subprocess, asyncio

app = Flask(__name__)
loop = asyncio.get_event_loop()


async def git_pull(cwd):
    subprocess.call('git pull origin develop', shell=True, cwd=cwd)
    subprocess.call('git pull origin master', shell=True, cwd=cwd)


@app.route('/webhook/git', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data = request.get_json(force=True)
        project = data['repository']['name']
        dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), project)
        loop.run_until_complete(git_pull(dir))
        return 'Success'

    return 'Hello, World'


if __name__ == '__main__':
    app.run()
