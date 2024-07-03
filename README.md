# FastAPI Summarizer Application

This is a FastAPI application that provides summarization services.

## Setup
There are 2 possible ways to run an app: the standard one and the docker-compose one.
### Standard setup
1. Create a virtual environment:
   ```
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

### Docker Compose setup

1. Build and run using Docker Compose:
   ```bash
   docker-compose up --build
   ```
This command will build the Docker image and start the FastAPI application in a Docker container.

## Test the endpoint:
   - Send a POST request to `http://127.0.0.1:8000/summarize` with a JSON body containing the text to be summarized.
