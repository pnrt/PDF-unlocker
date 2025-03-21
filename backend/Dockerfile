# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run the server
CMD ["python", "server.py"]
