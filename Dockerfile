FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /code

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install requirements
COPY config/requirements/ config/requirements/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r config/requirements/local.txt

# Copy and install app
COPY . .

# Run entrypoint
COPY config/entrypoint.sh /config/entrypoint.sh
RUN chmod +x /config/entrypoint.sh
ENTRYPOINT ["/config/entrypoint.sh"]
