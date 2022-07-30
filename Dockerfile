FROM seleniarm/standalone-chromium

RUN sudo apt update -y

RUN sudo apt install -y python3-venv python3-pip
RUN sudo python3 -m pip install --upgrade pip
RUN sudo python3 -m pip install awscli


# Install psycopg2
RUN sudo apt-get -y install libpq-dev gcc
RUN sudo python3 -m pip install psycopg2-binary

COPY . .

RUN sudo python3 setup.py install

CMD ["python3", "scraper_docker.py"]