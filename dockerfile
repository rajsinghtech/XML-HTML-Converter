FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir flask lxml
EXPOSE 8069
CMD ["python3", "app.py"]