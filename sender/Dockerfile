# python base image 
FROM python:3.12.3

# Set the working directory inside the container
WORKDIR /app

# Copy scripts and dependencies into container
COPY sender.py /app/
COPY requirements.txt /app/
COPY encryption_key.key file.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default executable
ENTRYPOINT ["python", "sender.py"]

# Default argument 
CMD ["file.txt"] 
