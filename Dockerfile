FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy just the requirements file first to leverage Docker cache
COPY requirements.txt /app/

# Install the required Python libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Clean up the package cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Expose the port that Streamlit runs on (default: 8501)
EXPOSE 8501

# Copy the rest of the source code into the container
COPY . /app/

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]