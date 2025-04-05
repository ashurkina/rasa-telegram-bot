#FROM python:3.11-alpine
#RUN mkdir /app
#COPY . /app
#RUN pip install --no-cache-dir -r /app/requirements.txt
#
#EXPOSE 5010
#
#CMD python /app/main.py

# Use minimal Python base image
FROM python:3.11-alpine

# Create app directory
RUN mkdir /app

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install build dependencies for Alpine (needed for some pip packages)
RUN apk add --no-cache build-base gcc libffi-dev

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
