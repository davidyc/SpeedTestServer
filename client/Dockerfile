FROM python:3.6

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /client

COPY .  /client/

WORKDIR /client

CMD ["python3","app.py"]