# Use the official Python image with version 3.11.4 as the base image
# FROM python:3.11.4
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy just the requirements file first to leverage Docker cache
COPY requirements.txt /app/

# Install the required libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install FFmpeg and other required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Expose the port that Streamlit runs on (default: 8501)
EXPOSE 8501

# Copy the rest of the source code into the container
COPY . /app/

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]