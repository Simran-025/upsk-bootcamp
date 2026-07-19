FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt ./
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# Only copy the app source
COPY app/ ./app/

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=builder /app/app /app/app

RUN groupadd -r appgroup && useradd -r -g appgroup -s /bin/false appuser
USER appuser
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
