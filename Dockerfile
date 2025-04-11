FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir pyrogram tgcrypto
CMD ["python", "auto_forward_worker.py"]