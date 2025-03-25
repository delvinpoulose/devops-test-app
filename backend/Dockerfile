# Use official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies (if needed by mysql-connector)
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    uvicorn\
 && rm -rf /var/lib/apt/lists/*

# Copy requirements (if you have one)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose port (Uvicorn default)
EXPOSE 8000

# Command to run FastAPI server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
