FROM python:3.10

RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r /app/requirements.txt
EXPOSE 5000

CMD ["python3", "producer.py"]