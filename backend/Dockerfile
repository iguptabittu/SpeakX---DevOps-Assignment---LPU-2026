# Use a base image with Python
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . /app

# Expose the port that the Flask app will run on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
