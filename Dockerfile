FROM python:3.10.14
WORKDIR /src
COPY . /src
RUN apt-get update
RUN apt-get install -y pkg-config libhdf5-dev
RUN pip install poetry
RUN poetry install --no-root
#RUN pip install -r requirements.txt
RUN poetry run pip install -i https://test.pypi.org/simple/ libml-URLPhishing==0.2.1
EXPOSE 8081
CMD ["poetry", "run", "python3", "src/serve_model.py"]