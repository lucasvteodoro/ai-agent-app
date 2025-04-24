
FROM python:3.11-slim-bullseye

USER root
WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt
COPY app /code/app
WORKDIR /code/app

CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0"]
