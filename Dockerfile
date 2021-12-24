FROM python:3.8-alpine

# this updates packages then adds python3-dev package as well as gcc and libc-dev
RUN apk update && apk add python3-dev gcc libc-dev

# this is your working directory in docker. when you run command with RUN, it runs under this directory
WORKDIR /app

# copying req.txt for the docker image
COPY ./requirements.txt ./requirements.txt

RUN pip install -U pip

RUN python3 -m pip install -r ./requirements.txt

#Line below copies everything in the root directory to /app
COPY . /app 

# thic command runs your application. your application attaches to process and stays there
# that is why docker does not exits and stays.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 