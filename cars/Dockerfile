FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD python manage.py collectstatic
CMD python manage.py migrate
CMD python manage.py collectstatic
CMD python3 manage.py runserver 0.0.0.0:$PORT