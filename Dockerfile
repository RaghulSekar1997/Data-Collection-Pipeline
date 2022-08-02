FROM python:3.9
# FROM --platform=linux/amd64  python:3.9

COPY . . 

# install the needed packages
RUN apt-get -y update && apt-get install -y gnupg
RUN apt-get install -y wget
RUN apt-get install -y curl

# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -


# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'


# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Installing the most stable version of google chrome
RUN apt-get install -y google-chrome-stable

# Installing Unzip
RUN apt-get install -yqq unzip

# Download the Chrome Driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

# Unzip the Chrome Driver into /usr/local/bin directory
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

RUN pip install psycopg2

RUN pip install -U pandas

RUN pip install -U selenium

RUN pip install -U uuid

# RUN pip install -U sys

# RUN pip install -U time

# RUN pip install -U urllib

RUN pip install -U selenium

RUN pip install -U webdriver_manager

RUN pip install -r ./requirements.txt

ENV DISPLAY=:99

# RUN pip install -r ./requirements.txt

CMD [ "python", "scraper_docker.py"]
