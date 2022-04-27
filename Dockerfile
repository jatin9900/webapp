FROM python:alpine3.10
WORKDIR /app
COPY . /app
RUN pip install -r dependencies.txt
EXPOSE 5000
CMD python ./webapp.py
