# Python base image
FROM python:3.5.2

# Where the API server lives
WORKDIR /app/

# Install required dependencies
COPY requirements.txt /app/
RUN pip3 install -r ./requirements.txt

# API server
COPY server.py /app/
COPY models/svm.pckl /app/models/
# Container port on which the server will be listening
EXPOSE 5200
# Launch server app
ENTRYPOINT python3 ./server.py
