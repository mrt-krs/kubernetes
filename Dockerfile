FROM python:3

WORKDIR /usr/src/app

ADD main.py .
ADD indeed.py .
ADD README.md .
ADD requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=main.py

CMD ["python", "./main.py"]

