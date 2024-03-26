FROM python:3.12.2-slim-bullseye

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080

ENV PYTHON_HOST=0.0.0.0
ENV PYTHON_PORT=8080

# Run app.py when the container launches
CMD ["python", "server.py"]
