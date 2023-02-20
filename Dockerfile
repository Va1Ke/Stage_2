FROM python:3.10
WORKDIR /hotel/
COPY ./requirements.txt /hotel/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /hotel/requirements.txt
COPY hotel /hotel/
COPY .env /
ENTRYPOINT ["python3"]
CMD ["app.py"]
