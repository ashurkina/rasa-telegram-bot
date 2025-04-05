FROM python:3.11-alpine
RUN mkdir /app
COPY . /app
RUN pip install --no-cache-dir -r /app/requirements.txt

ENV OPENAI_KEY
ENV TELEGRAM_API

CMD python /app/main.py