FROM public.ecr.aws/lambda/python:3.10

WORKDIR /app/

COPY requirements.txt  .
RUN  pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY ./src/ ./src/ ${LAMBDA_TASK_ROOT}

CMD [ "app.handler" ]

