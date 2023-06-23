# Base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY ./requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app .

EXPOSE 8000
VOLUME /app/data
VOLUME /.dizzy

# Run the server application
CMD ["python", "compute.py"]
