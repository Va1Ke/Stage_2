FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./department-app /code/
COPY . /code/
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]