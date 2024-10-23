# Use Python as the base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the app files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
