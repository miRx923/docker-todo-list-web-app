# File for creating "todo-web-app-web" image

# Use Python 3.8 Alpine base image
FROM python:3.8-alpine

# Set the working directory to /app
WORKDIR /app

# Install dependencies
RUN apk add --no-cache libpq-dev python3-dev g++ make

RUN pip install --upgrade pip \
    install flask \
    install flask-sqlalchemy \ 
    install psycopg2

# Copy the web source files
COPY ./web-src/ /app/web-src

# Set environment variable
ENV FLASK_APP=web-src/app.py

# Expose port 5000
EXPOSE 5000

# Run the flask app
ENTRYPOINT [ "flask" ]
# Command line arguments
CMD ["run", "--host", "0.0.0.0"]
