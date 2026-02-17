# Dockerfile
FROM python:3.9-slim

WORKDIR /code

# Copy requirements first to leverage Docker cache
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the app folder
COPY ./app /code/app

# Command to run the FastAPI app via Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]