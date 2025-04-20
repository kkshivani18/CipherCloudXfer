# using python as base image 
FROM python:3.12.3

# set working site 
WORKDIR /app

# COPY necessary files
COPY receiver.py /app/
COPY requirements.txt /app/
COPY encryption_key.key /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set dafault executable
ENTRYPOINT ["python", "receiver.py"]

# Default argument 
CMD ["file.txt.enc"]
