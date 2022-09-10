FROM python:3

RUN mkdir /app
WORKDIR /app


EXPOSE 5555

# ENV FLASK_APP=app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD [ "uwsgi", "--ini", "app.ini" ]