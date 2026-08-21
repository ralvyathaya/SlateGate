# ============================================================================
# SlateGate — Production Dockerfile for Google Cloud Run
# ============================================================================

FROM python:3.12-slim

# Prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080 \
    APP_HOST=0.0.0.0

WORKDIR /app

# Install system dependencies if required
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency definitions
COPY requirements.txt .
COPY requirements.lock .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code and SQL assets
COPY app/ app/
COPY sql/ sql/
COPY pyproject.toml .

# Expose Google Cloud Run default port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Start FastAPI application via Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
