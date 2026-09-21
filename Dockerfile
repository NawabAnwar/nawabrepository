FROM python:3.11-slim

# Set container working directory
WORKDIR /usr/src/app

# Define runtime environment variables
ENV PORT=5000
EXPOSE 5000

# Install dependencies separately to leverage Docker layer caching
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Bundle application source
COPY . .

# Launch application server
CMD ["python", "app.py"]
