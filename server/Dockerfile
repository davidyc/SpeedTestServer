FROM python:3.6

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /server

COPY .  /server/

WORKDIR /server

CMD ["python3","app.py"]