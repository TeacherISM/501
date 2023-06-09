FROM public.ecr.aws/lambda/python:3.8
WORKDIR /FDSC
COPY FDSC/ ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["app.lambda_handler"]