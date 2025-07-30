# Use official Python base image
FROM python:3.14.0rc1-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for compiling some Python packages like mysql-connector)
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better for Docker cache)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose port for Uvicorn
EXPOSE 8000

# Command to run FastAPI server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
