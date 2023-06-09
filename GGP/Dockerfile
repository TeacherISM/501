FROM public.ecr.aws/lambda/python:3.8

# RUN mkdir /lam
#COPY requirements.txt /lam/requirements.txt
COPY requirements.txt /requirements.txt
#RUN pip3 install -r /lamb/requirements.txt --target "${LAMBDA_TASK_ROOT}"
RUN pip3 install -r /requirements.txt --target "${LAMBDA_TASK_ROOT}"
COPY . ${LAMBDA_TASK_ROOT}
CMD ["lambda_func.addNums"]
