FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy only the necessary files first to leverage Docker caching
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the application port
EXPOSE 5000

# Specify the default command to run the application
CMD ["python", "app.py"]