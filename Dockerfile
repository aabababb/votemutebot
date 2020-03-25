FROM python:3

WORKDIR /usr/src/app

COPY * ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir python-telegram-bot
COPY . .

CMD [ "python", "./main.py" ]
