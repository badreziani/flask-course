FROM python:3.11.4
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
CMD [ "docker", "run", "--port", "0.0.0.0"]