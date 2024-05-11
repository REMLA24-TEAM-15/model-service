FROM python:3.10.14
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt
EXPOSE 8081
ENTRYPOINT ["python"]
CMD ["src/app.py"]