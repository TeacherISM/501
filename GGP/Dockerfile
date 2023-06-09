FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt /lam/requirements.txt
RUN pip3 install -r /lam/requirements.txt --target "${LAMBDA_TASK_ROOT}"
COPY . ${LAMBDA_TASK_ROOT}

CMD ["lambda_func.addNums"]
