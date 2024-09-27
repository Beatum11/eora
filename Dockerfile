FROM python:3.12-slim

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

COPY . /app

RUN poetry install --no-interaction --no-ansi

CMD ["python", "main.py"]