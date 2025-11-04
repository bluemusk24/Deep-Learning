FROM python:3.13.1-slim-bookworm

# Simple, reproducible container that installs runtime deps via pip.
WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Install runtime Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
	pip install --no-cache-dir fastapi uvicorn[standard] onnxruntime keras-image-helper numpy

# Copy application code and model directory
COPY pyproject.toml ./
COPY main.py test.py ./

# copy the model directory explicitly into /app/model_onnx so test.py can load it
COPY model_onnx /app/model_onnx

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]