FROM python:3.6
WORKDIR /py_script
COPY ./py_script/main.py ./py_script/requirements.txt ./py_script/index.py ./py_script/Dockerfile ./py_script/text.txt ./
# COPY . ../../
#RUN pip install --upgrade pip
# RUN apt-get update -y && apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev libsnmp-dev
RUN pip install -r requirements.txt
RUN python index.py

# EXPOSE 8080