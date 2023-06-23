# Base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY ./requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY django .

EXPOSE 8000
VOLUME /app/data

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=dazzlesite.settings

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
