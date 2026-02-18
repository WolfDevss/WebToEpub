FROM python:3.11-slim

WORKDIR /app

# Install git (required for pip to clone GitHub repos)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy your project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 10000

# Start the app
CMD ["bash", "start.sh"]
