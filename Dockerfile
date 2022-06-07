FROM python:3.10

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
# ENV FLASK_APP=app.py
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]