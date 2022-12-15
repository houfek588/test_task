FROM python:3.10

WORKDIR /flask_app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["flask_app.py"]