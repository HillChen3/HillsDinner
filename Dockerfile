FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
COPY app.py /app/main.py
COPY models/db_server.py /app/models/db_local.py