# From https://docs.docker.com/compose/gettingstarted/

# GET the Python3.8 image from dockerhub
FROM python:3.8-alpine

# This is the working directory for the project
WORKDIR /code/backend

# # These packages allows to compile in C for later flask-mysqldb installation
RUN apk add --no-cache gcc musl-dev linux-headers mariadb-dev

# Copy and run pip installation
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

# Now Copy all my code
COPY . .

# These are the the flask env variables
ENV FLASK_APP=src/app
ENV FLASK_RUN_HOST=0.0.0.0

#Finally run the app
CMD ["flask", "run"]