FROM public.ecr.aws/lambda/python:3.10 

WORKDIR /KVMR 
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

CMD [ "handler.handler" ]