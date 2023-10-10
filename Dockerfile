FROM python:3.11-slim AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy just the requirements file first to leverage Docker cache
COPY requirements.txt ./

# Install the required libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Whisper from PyPI instead of GitHub source
# RUN pip install git+https://github.com/openai/whisper.git

# Install FFmpeg and other required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the rest of the source code into the container
COPY . .

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /app/ /app/

EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]