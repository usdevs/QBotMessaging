FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY . .

RUN pip install uv && uv sync

CMD ["python", "main.py"]
