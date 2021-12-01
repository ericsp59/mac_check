FROM python:3.11-rc-alpine
WORKDIR /py_script
COPY ./py_script/main.py ./py_script/requirements.txt ./py_script/index.py ./py_script/Dockerfile ./py_script/text.txt ./
RUN pip3 install -r requirements.txt
RUN python3 index.py

EXPOSE 8080