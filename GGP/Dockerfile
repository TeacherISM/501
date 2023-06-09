FROM public.ecr.aws/lambda/python:3.8

RUN mkdir /lambda_func
COPY requirements.txt /lambda_func/requirements.txt
RUN pip3 install -r /lambda_func/requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY . ${LAMBDA_TASK_ROOT}
CMD ["lambda_func.add"]
