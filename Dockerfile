FROM python:3.9.4-alpine
WORKDIR /tmp
# prevents Python from copying pyc files to the container
ENV PYTHONDONTWRITEBYTECODE 1
# ensures that Python output is logged to the terminal, making it possible to monitor Django logs in realtime
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
RUN apk add zlib-dev jpeg-dev gcc musl-dev
COPY ./requirements.txt /tmp
RUN pip install -r requirements.txt

# copy project
COPY . /tmp

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
