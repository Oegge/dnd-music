# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

COPY requirements/dev.txt requirements.txt

RUN apt update && \
    apt install -y ffmpeg


RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port Django will run on
EXPOSE 8000
# Run Gunicorn server on IPv6
CMD ["gunicorn", "--bind", "[::]:8000", "dndmusic.wsgi:application"]

