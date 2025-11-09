FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir poetry==1.8.3
COPY pyproject.toml /app/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
COPY . /app
CMD ["celery", "-A", "worker.app", "worker", "--loglevel=INFO"]
