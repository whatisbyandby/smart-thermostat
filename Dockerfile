FROM python:3.9.2-alpine

WORKDIR /usr/app
COPY . .
RUN python -m pip install -r requirements.txt

CMD [python -m pytest]
