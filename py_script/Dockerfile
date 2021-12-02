FROM python:latest
WORKDIR /py_script
COPY ./py_script/requirements.txt ./
RUN pip install -r requirements.txt
COPY ./py_script/main.py ./py_script/app.py ./py_script/Dockerfile ./py_script/text.txt ./
# COPY . ../../
#RUN pip install --upgrade pip
# RUN apt-get update -y && apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev libsnmp-dev
# RUN apt-get update -y
# RUN apt-get install -y iputils-ping
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]

EXPOSE 8080