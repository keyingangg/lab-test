FROM python:3.11-slim

# Create a non-root user
RUN useradd -m appuser

WORKDIR /app

# Copy files and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .
COPY common-passwords.txt .

# Change ownership and permissions (optional)
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

CMD ["python", "server.py"]
