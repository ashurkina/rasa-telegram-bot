FROM python:3.11-alpine
RUN mkdir /app
COPY . /app
RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 5010

CMD python /app/main.py