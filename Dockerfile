# ── Stage 1: builder ──────────────────────────────────────
FROM python:3.12-slim AS builder

WORKDIR /app

# Install dependencies into a separate location
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# ── Stage 2: final image ──────────────────────────────────
FROM python:3.12-slim

WORKDIR /app

# Copy installed packages from builder (keeps image small)
COPY --from=builder /install /usr/local

# Copy only the app source
COPY app.py .

EXPOSE 3000

CMD ["python", "app.py"]