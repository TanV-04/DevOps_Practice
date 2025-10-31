# Use an official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Expose the Flask port
EXPOSE 5000

# Start Flask app
CMD ["python", "app.py"]