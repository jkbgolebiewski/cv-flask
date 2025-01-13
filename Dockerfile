FROM python:3-alpine

ENV ENVIRONMENT="production"

ADD / app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "website:app"]