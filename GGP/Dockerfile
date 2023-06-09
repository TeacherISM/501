FROM public.ecr.aws/lambda/python:3.8

RUN mkdir /lambda_f
COPY requirements.txt /lambda_f/requirements.txt
RUN pip3 install -r /lambda_f/requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY . ${LAMBDA_TASK_ROOT}
CMD ["lambda_f.add"]


