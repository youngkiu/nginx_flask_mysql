FROM python:3.8.2

COPY . /opt/project/app/
WORKDIR /opt/project/app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
ADD ./wait-for-it.sh /
