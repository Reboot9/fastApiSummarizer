# Stage 1: builder
FROM python:3.10 AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1

# Set the working directory in the container
WORKDIR /builder

COPY /requirements.txt ./

# Install dependencies including uvicorn
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Stage 2: runtime
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1

WORKDIR /fastApiSummarizer

# Copy dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy the rest of the application
COPY . /fastApiSummarizer

EXPOSE 8000

# Start FastAPI app with uvicorn
CMD ["python3", "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
