FROM python:3.11-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create a non-root user
RUN useradd -m appuser
USER appuser

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Command to run the application
ENTRYPOINT ["python", "dread_campaign_generator.py"] 