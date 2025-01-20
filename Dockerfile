FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy files from local folder into the working directory
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copies all files into /app
COPY . . 


# Expose the port Flask will run on
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
