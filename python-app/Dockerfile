# syntax-docker/dockerfile:1

# ----Build stage-----
FROM python:3.12-slim AS builder
WORKDIR /app

#Install build dependencies
RUN pip install --upgrade pip

# Copy only requirements first (leverages Docker cache)
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

#----Final Stage ----
FROM python:3.12-slim

#Create a non-root user
RUN adduser --disable-password --gecos '' appuser

WORKDIR /app
COPY --from=builder /root/.local /home/appuser/.local
COPY app.py .

# Make sure binaries are in PATH
ENV PATH=/home/appuser/.local/bin:$PATH

# Switch to non-root user
USER appuser

#Expose the port the app runs on
EXPOSE 8080

# Use gunicorn for production (adjust workers as needed)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
