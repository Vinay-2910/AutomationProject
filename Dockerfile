# Use official Python image
FROM python:3.13-slim

# Create working directory inside container
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run application
CMD ["python", "scripts/main.py"]