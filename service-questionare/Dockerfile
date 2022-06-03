# Pull base image
FROM python:3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install dependencies
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

# Copy local project files
COPY . /code/

# Run server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]