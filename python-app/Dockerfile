# syntax=docker/dockerfile:1
# ↑ Tells Docker to use the latest Dockerfile features (optional but nice)

# ================================================================
# STAGE 1: Builder – install Python packages in a clean environment
# ================================================================
FROM python:3.12-slim AS builder

# Set working directory inside the container
WORKDIR /app

# Upgrade pip once so we have the latest version
RUN pip install --upgrade pip

# Copy ONLY requirements.txt first → Docker can cache this layer!
# This makes rebuilds lightning-fast when only app.py changes
COPY requirements.txt .

# Install Flask + Gunicorn into the user's local bin (no system packages)
# --user     → installs to /root/.local (we'll copy this later)
# --no-cache-dir → keeps image small
RUN pip install --user --no-cache-dir -r requirements.txt


# ================================================================
# STAGE 2: Final tiny image – only what we really need to run the app
# ================================================================
FROM python:3.12-slim

# Create a normal non-root user (security best practice!)
# Recent python:slim images removed "adduser", so we use useradd + groupadd
RUN set -eux; \
    groupadd --gid 1000 appuser; \
    useradd --uid 1000 --gid appuser --shell /bin/bash --create-home appuser

# Set working directory for the app
WORKDIR /app

# Copy the installed Python packages from the builder stage
# This is the magic of multi-stage builds → final image stays tiny!
COPY --from=builder /root/.local /home/appuser/.local

# Copy your actual Flask application code
COPY app.py .

# Make sure gunicorn (and any pip binaries) are found when the container runs
ENV PATH="/home/appuser/.local/bin:${PATH}"

# Switch to the non-root user from now on (very important for security)
USER appuser

# Tell Docker which port your app listens on
EXPOSE 8080

# How to start the app when the container runs
# Gunicorn is production-ready (much better than Flask's debug server)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
