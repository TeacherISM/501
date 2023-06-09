FROM python:3.10

RUN mkdir /app
COPY execute.sh /app/execute.sh
COPY requirements.txt /app/requirements.txt
RUN chmod 777 /app/execute.sh
RUN pip install -r /app/requirements.txt
COPY src/ /app/src/
EXPOSE 5000
WORKDIR /app/
ENTRYPOINT ["./execute.sh"]