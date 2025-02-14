# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and its dependencies
RUN apt-get update && apt-get install -y \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    libxkbcommon0 \
    libgbm1 \
    libpango-1.0-0 \
    libxshmfence1 \
    libglu1-mesa \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libnspr4 \
    libxss1 \
    xdg-utils \
    libgstreamer1.0-0 \
    libgtk-4-1 \
    libgraphene-1.0-0 \
    libwoff1 \
    libvpx7 \
    libopus0 \
    libgstallocators-1.0-0 \
    libgstapp-1.0-0 \
    libgstbase-1.0-0 \
    libgstpbutils-1.0-0 \
    libgstaudio-1.0-0 \
    libgstgl-1.0-0 \
    libflite1 \
    libavif15 \
    libharfbuzz-icu0 \
    libenchant-2-2 \
    libsecret-1-0 \
    libhyphen0 \
    libmanette-0.2-0 \
    libx264-160

RUN pip install playwright
RUN playwright install

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME FastAPI_Scraper

# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]