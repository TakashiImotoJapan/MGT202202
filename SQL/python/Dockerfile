FROM python:3.5.2

RUN groupadd web
RUN useradd -d /home/python -m python

WORKDIR /home/python

ADD requirements.txt /home/python

RUN apt-get update && apt-get -y install vim
RUN apt-get -y install net-tools
RUN apt-get -y install mysql-client
RUN apt install -y python3-pip                               \
    && pip3 install --no-cache-dir -r ./requirements.txt                            \
    && rm -rf /var/lib/apt/lists/* 

ADD cgiserver.py /home/python
ADD index.html /home/python
COPY cgi-bin/ /home/python/cgi-bin/
RUN chmod 755 /home/python/cgi-bin/*

EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/python", "/home/python/cgiserver.py"]
USER python
