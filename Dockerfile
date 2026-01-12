FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no cache-dir -r requirements.txt

COPY health_reporter.py .

ENV DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/1460270340440850596/ANmcQgargW8c8TBMN0nGl3nmlh1MxGFJdspYvD7_1NKYzPvj2si9oCU0gzKZesY5zBFO"

CMD ["python", "health_reporter.py"]