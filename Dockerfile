FROM python:3.8-slim-buster

WORKDIR /code

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "python3", "write.py"]