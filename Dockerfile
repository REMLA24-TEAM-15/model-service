FROM python:3.10.14
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt
RUN pip install -i https://test.pypi.org/simple/ libml-URLPhishing
EXPOSE 8081
RUN chmod a+x run.sh
CMD ["./run.sh"]
