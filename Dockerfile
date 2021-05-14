FROM python:3.9.1

WORKDIR /project-cloude

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

COPY entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/entrypoint.sh / # backwards compat
ENTRYPOINT ["entrypoint.sh"] 

#CMD [ "flask", "db", "init"]
#CMD [ "flask", "db", "migrate"]
#CMD [ "flask", "db", "upgrade"]
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


