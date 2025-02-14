# Use an official Python runtime as a parent image
FROM python:3.12-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


RUN pip install playwright && \
    playwright install --with-deps

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME FastAPI_Scraper

# Run app.py when the container launches
CMD ["python" , "main.py"]