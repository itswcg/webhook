## Webhook
一个git webhook服务器端自动git pull的工具

## Usage
```bash
# python3.6 & flask & celery
$ git clone git@github.com:itswcg/webhook.git
$ cd webhook/ && python3 -m venv venv && pip install -r requirements.txt
$ flask run && clery -A app.celery worker --loglevel=info
```
