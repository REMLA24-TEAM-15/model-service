FROM python:3.10.14
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt
RUN pip install -i https://test.pypi.org/simple/ libml-URLPhishing
EXPOSE 8081
ENTRYPOINT ["python"]
CMD["src/fetch_model.py"]
CMD ["src/serve_model.py"]
