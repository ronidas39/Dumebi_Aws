FROM python:3.9
WORKDIR /code
RUN pip install fastapi uvicorn
COPY main.py ./
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]