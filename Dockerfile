FROM python:3.10.4-bullseye

RUN apt update && apt search firefox && apt-get -y install curl firefox-esr

RUN pip install selenium

RUN curl -L https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz -o geckodriver.tar.gz && \
    tar xzvf geckodriver.tar.gz -C /usr/bin/

COPY ./main.py /

CMD ["python3", "/main.py"]
