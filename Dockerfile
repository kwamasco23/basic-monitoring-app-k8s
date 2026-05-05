FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy your app
COPY app.py .

# Expose the port your app runs on
EXPOSE 6001

# Run the app
CMD ["python", "app.py"]