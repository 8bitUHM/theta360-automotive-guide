# Use the official Python image from the Docker Hub
FROM python:3.12

# Project secret key define for build argument
ARG PROJECT_SECRET

# Set environment variables for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Set the working directory within the container
WORKDIR /app

# Install Node.js and npm
RUN apt-get update && apt-get install -y \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Copy app into image
COPY . /app/

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install node scripts
RUN npm install

# Change to the theme/static_src directory and install Node.js dependencies
WORKDIR /app/website
RUN npm install

# Change back to the app directory
WORKDIR /app

# Run Tailwind build and collect static files
RUN npm run build && python manage.py collectstatic --noinput

# Expose port 8000 for the Django application
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
