#Dockerfile
FROM python:3.10.14
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN apt-get update
RUN apt-get install -y pkg-config libhdf5-dev
RUN pip install poetry
RUN poetry install --no-root
RUN poetry run pip install -i https://test.pypi.org/simple/ libml-URLPhishing
COPY . /app
ENV PYTHONPATH=/app
EXPOSE 8081
CMD ["poetry", "run", "python3", "src/serve_model.py"]