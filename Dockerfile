FROM python:3.14-slim

WORKDIR /app

COPY app.py .

ENV PORT=8085

EXPOSE 8085

CMD ["python", "app.py"]
