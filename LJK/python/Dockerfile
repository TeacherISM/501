# Use the base image from Amazon Elastic Container Registry (ECR) for Python 3.10 Lambda functions
FROM public.ecr.aws/lambda/python:3.10

# Copy the requirements.txt file from the current directory to the Docker image
COPY requirements.txt ./

# Install the Python dependencies listed in requirements.txt into the Lambda task root directory
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy the source code file app.py to the Lambda task root directory
COPY src/app.py ${LAMBDA_TASK_ROOT}

# Set the command to execute when the Docker container starts running

# The command is specified as an array, where the first element is the executable (app.py) and the second element is the function (handler) to be called
# This command will be executed by the Lambda runtime environment
CMD ["app.handler"]
