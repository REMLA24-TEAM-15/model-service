FROM python:3.10.14
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt
RUN pip install -i https://test.pypi.org/simple/libml-URLPhishing
RUN mkdir /src/model
RUN wget https://github.com/REMLA24-TEAM-15/model-training/blob/main/release.joblib -P /src/model/
EXPOSE 8081
ENTRYPOINT ["python"]
CMD ["src/serve_model.py"]
