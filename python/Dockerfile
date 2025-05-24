# Use the official Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependency files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the application code
COPY . .

# Optional: expose a port (if your app runs a web server)
EXPOSE 5000

# Default command to run the app
CMD ["python", "app.py"]

