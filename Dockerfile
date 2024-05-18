FROM python:3.10.14
WORKDIR /src
COPY . /src
RUN apt-get update
RUN apt-get install -y pkg-config libhdf5-dev
RUN pip install -r requirements.txt
RUN pip install -i https://test.pypi.org/simple/ libml-URLPhishing
EXPOSE 8081
RUN chmod a+x run.sh
CMD ["python3", "src/serve_model.py"]
