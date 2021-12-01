FROM python:3.6
WORKDIR /py_script
COPY ./py_script/main.py ./py_script/requirements.txt ./py_script/app.py ./py_script/Dockerfile ./py_script/text.txt ./
# COPY . ../../
#RUN pip install --upgrade pip
# RUN apt-get update -y && apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev libsnmp-dev
RUN apt-get update -y
RUN apt-get install -y iputils-ping
RUN pip install -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]

EXPOSE 8080